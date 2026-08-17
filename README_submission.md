# Báo Cáo Thực Hành Lab 17: Multi-Layer Memory System

## 1. Phân tích Benchmark (Số liệu từ benchmark.json)

- **Layer có hit rate thấp nhất:** Ở baseline no-memory, toàn bộ `long_term`, `episodic`, `semantic` và `mixed` đều đạt hit rate 0% (thất bại E02–E09, E11) do thiếu bộ nhớ bền vững; chỉ `short_term` đạt 100% (E01, E10). Khi bật bộ nhớ (`student`), cả 4 layer đạt **100% (11/11 PASS)**.
- **Query retrieve nhiều token nhất:** Case **E08** (`long_term`: *Backend BLUEBIRD-42*) với **1368 tokens** (E03: 1367 tokens, E02: 1355 tokens).
- **Phân tích case E07 (Mixed):** Kết hợp **Long-term** (sở thích cá nhân) và **Semantic** (tài liệu domain). Hai evidence bắt buộc: `Python` (code preference) và `PAYMENT-RULE-3` (kèm `Idempotency-Key`).
- **Token Reduction vs Hit Rate:** Token reduction trung bình đạt **14.2%** (E06: 67.8%, E11: 74.2%). No-memory có reduction cao (81.8%) do không retrieve context (0 token), dẫn đến thiếu thông tin và hit rate chỉ đạt 18.2%.

## 2. Reflection Kiến Trúc & An Toàn Bộ Nhớ

- **Layer quan trọng nhất:** **Long-term memory** (chiếm 4/11 case: E02, E03, E08, E09 và hỗ trợ E07), cốt lõi cho cá nhân hóa xuyên phiên, quản lý open-loop/deadline (`LAB-REPORT-1600`) và cô lập dữ liệu giữa người dùng (`lan-lab17` vs `minh-lab17`).
- **Trade-off Zep Context Block vs Redis + Qdrant:** Zep tự động hóa temporal graph, entity resolution và sinh context block nhưng chịu độ trễ mạng (~947.8ms) và phụ thuộc SaaS. Tự làm Redis + Qdrant có độ trễ cực thấp, kiểm soát dữ liệu tại chỗ nhưng phức tạp khi tự xây pipeline quản lý graph, temporal decay và giải quyết xung đột.
- **Guardrail chống Memory Poisoning:** Dùng Consent Gate (`require_memory_consent`), lọc PII (`minimize_pii`), dùng `ignore_roles` khi eval để query không biến thành fact, theo dõi `valid_at`/`invalid_at` và kiểm duyệt chính sách trước khi ghi đè.
- **E08 Recency & E10 Compaction:** E08 xử lý xung đột theo phạm vi (scope-specific): cập nhật TypeScript/NestJS cho dự án `BLUEBIRD-42` mà vẫn giữ preference Python cho `ORCHID-27`. E10 dùng sliding compaction tự trích xuất ràng buộc bất biến (`REVIEW-DEADLINE-1600`) vào `<DURABLE_NOTES>`, bảo toàn thông tin cốt lõi dù raw message bị loại khỏi recent turns.
