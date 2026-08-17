# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1140.9 ms**
- Average token reduction vs full source context: **15.4%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1533.0 | 344 | 0.0% |  |
| G09 | semantic | PASS | 254.5 | 155 | 66.2% |  |
| G10 | semantic | PASS | 365.6 | 100 | 78.2% |  |
| G14 | mixed | PASS | 1756.3 | 422 | 0.0% |  |
| G03 | long_term | PASS | 1308.0 | 975 | 0.0% |  |
| G04 | long_term | PASS | 1750.0 | 806 | 0.0% |  |
| G07 | episodic | PASS | 293.9 | 221 | 0.0% |  |
| G08 | episodic | PASS | 323.1 | 220 | 0.4% |  |
| G11 | mixed | PASS | 1827.1 | 444 | 21.4% |  |
| G13 | mixed | PASS | 511.9 | 376 | 33.5% |  |
| G15 | mixed | PASS | 2068.8 | 701 | 0.0% |  |
| G16 | mixed | PASS | 1635.0 | 492 | 12.9% |  |
| G17 | mixed | PASS | 1923.0 | 492 | 12.9% |  |
| G18 | mixed | PASS | 543.2 | 340 | 39.8% |  |
| G19 | mixed | PASS | 1689.5 | 557 | 1.4% |  |
| G05 | long_term | PASS | 1515.7 | 787 | 0.0% |  |
| G12 | mixed | PASS | 1824.5 | 390 | 38.3% |  |
| G20 | mixed | PASS | 1694.8 | 614 | 2.9% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for backend. </USER_SUMMARY>  <ENTITIES>   - Name: Lan Tran     Label: User     Attributes:       email:        first_name: Lan       last_name: Tran       name: Lan Tran       role_type: user       user_id: lan-lab17     Summary: The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for backend.   - Name: LOTUS-88     Label: Organization     Attributes:       name: LOTUS-88     Summary: LOTUS-88 is a project of Lan Tran, who prioritizes Java and Spring Boot, and does not use Python for the backend.   - `

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata=`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata=`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for backend. </USER_SUMMARY>  <ENTITIES>   - Name: LOTUS-88     Label: Organization     Attributes:       name: LOTUS-88     Summary: LOTUS-88 is a project of Lan Tran, who prioritizes Java and Spring Boot, and does not use Python for the backend.   - Name: Java + Spring Boot     Label: Topic     Attributes:       name: Java + Spring Boot     Summary: Java + Spring Boot is used for backend examples by Da hieu, a Lab Assistant.   - Name: Python     Label: Topic     Attributes:       name: Python     Summary: Python is not used for the backend of the LOT`

### G03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for personal demos suc`

### G04 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for personal demos suc`

### G07 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection chu`

### G08 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concu`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for person`

### G13 - mixed

`<EPISODIC> EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co `

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for person`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for person`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for person`

### G18 - mixed

`<EPISODIC> EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la con`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for person`

### G05 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for personal demos suc`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for person`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
