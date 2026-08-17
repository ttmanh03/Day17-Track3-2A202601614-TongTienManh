# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **836.7 ms**
- Average token reduction vs full source context: **19.0%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 861.3 | 56 | 87.8% |  |
| E09 | long_term | PASS | 1447.9 | 332 | 0.0% |  |
| E10 | short_term | PASS | 0.4 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1379.5 | 976 | 0.0% |  |
| E03 | long_term | PASS | 1565.0 | 814 | 0.0% |  |
| E04 | episodic | PASS | 286.8 | 233 | 0.0% |  |
| E05 | episodic | PASS | 324.2 | 221 | 0.0% |  |
| E07 | mixed | PASS | 1716.4 | 392 | 30.6% |  |
| E11 | semantic | PASS | 253.3 | 55 | 90.3% |  |
| E08 | long_term | PASS | 1369.2 | 825 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for backend. </USER_SUMMARY>  <ENTITIES>   - Name: LOTUS-88     Label: Organization     Attributes:       name: LOTUS-88     Summary: LOTUS-88 is a project of Lan Tran, who prioritizes Java and Spring Boot, and does not use Python for the backend.   - Name: Python     Label: Topic     Attributes:       name: Python     Summary: Python is not used for the backend of the LOTUS-88 project.   - Name: Spring Boot     Label: Topic     Attributes:       name: Spring Boot     Summary: Spring Boot is prioritized for the LOTUS-88 project.   - Name: Java     Label: Topic    `

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for personal demos suc`

### E03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for personal demos suc`

### E04 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurr`

### E05 - episodic

`EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection chu`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for person`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python for it. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python.  Minh prefers Python and dislikes Java. When explaining code, Minh wants the AI to use short examples. Minh is learning async/await and often confuses coroutines with Tasks. When this topic arises, Minh wants explanations to be presented as a timeline, stating: 'Toi se uu tien timeline khi giai thich coroutine va Task.' For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is not to be used for the backend of this project, but Python preference is still valid for personal demos suc`
