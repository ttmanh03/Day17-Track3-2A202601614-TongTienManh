from __future__ import annotations

import re
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


def _clean_long_term_context(context_block: str, fact_text: str) -> str:
    """Format and prioritize long-term context components so salient facts
    and entity codes are preserved under tight budget limits.
    """
    parts: list[str] = []

    # 1. User profile summary (contains core preferences and project mappings)
    summary_match = re.search(r"(<USER_SUMMARY>.*?</USER_SUMMARY>)", context_block, re.DOTALL)
    if summary_match:
        parts.append(summary_match.group(1).strip())

    # 2. Entity summaries (contains literal task and project markers)
    entities_match = re.search(r"(<ENTITIES>.*?</ENTITIES>)", context_block, re.DOTALL)
    if entities_match:
        parts.append(entities_match.group(1).strip())

    # 3. Verified edge facts from search (with temporal validity ranges)
    if fact_text:
        parts.append(fact_text)

    # 4. Fallback: if no user summary or entities were parsed, use raw context block
    if not parts:
        return join_nonempty([fact_text, context_block], sep="\n\n")

    return join_nonempty(parts, sep="\n\n")


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # 1) Prime evaluation thread with current user and query
        prime_eval_thread(self.client, user_id, thread_id, query)

        # 2) Get Context Block for the evaluation thread
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""
        if not isinstance(context_block, str):
            context_block = str(context_block) if context_block is not None else ""

        # 3) Harden retrieval by searching user-scoped edges (facts with validity ranges)
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        return _clean_long_term_context(context_block, fact_text)

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # Search episodic graph scoped by user_id
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=20,
        )

        # Filter out evaluation probe messages and trivial echo acknowledgements
        episodes = []
        for ep in getattr(results, "episodes", []) or []:
            role = (getattr(ep, "role", "") or "").strip()
            if role == "Evaluation User":
                continue
            content = (getattr(ep, "content", "") or "").strip()
            if role == "Lab Assistant" and len(content) < 90 and any(content.startswith(p) for p in ("Da hieu", "Da tach", "Toi se uu tien", "Noted")):
                continue
            episodes.append(ep)

        class FilteredResult:
            pass

        res = FilteredResult()
        res.episodes = episodes
        for attr in ("context", "edges", "nodes", "observations", "thread_summaries"):
            setattr(res, attr, getattr(results, attr, None))

        return render_graph_search(res, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # Search the standalone semantic graph using graph_id
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=10,
            )
        except Exception:
            # Fallback to scope="nodes" if episodes scope fails or is unsupported
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=10,
            )

        # Deduplicate redundant JSON vs raw text representations of knowledge documents
        seen = set()
        clean_episodes = []
        for ep in getattr(results, "episodes", []) or []:
            content = (getattr(ep, "content", "") or "").strip()
            if content.startswith("{") and '"summary":' in content:
                continue
            if content and content not in seen:
                seen.add(content)
                clean_episodes.append(ep)

        class FilteredSemantic:
            pass

        res = FilteredSemantic()
        res.episodes = clean_episodes
        for attr in ("context", "edges", "nodes", "observations", "thread_summaries"):
            setattr(res, attr, getattr(results, attr, None))

        return render_graph_search(res)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        return self.budget.assemble(layers)
