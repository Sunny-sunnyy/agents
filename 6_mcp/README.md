# 6_mcp

`6_mcp` là capstone project của Week 6 về MCP trong một khóa học AI Engineering. Dự án xây một `autonomous trading floor` mô phỏng với 4 trader agents và 1 researcher capability, dùng OpenAI Agents SDK cùng nhiều MCP servers để quản lý account state, market data, web research, memory, tracing và dashboard quan sát runtime.

Lưu ý quan trọng: đây là dự án học kiến trúc agent systems và MCP composition, không phải hệ thống trading thật. Một số phần setup/run bên dưới được suy luận từ notebooks, docs và code, chưa được chạy xác minh trong lượt exploration này.

## Mục tiêu dự án

- Minh họa cách dùng MCP servers trong agent workflows.
- Đi từ notebook demo sang Python modules có thể tái dùng.
- Kết hợp state, tools, resources, tracing và UI thành một hệ multi-agent hoàn chỉnh hơn.
- Cho phép trader agents tự nghiên cứu, trade và rebalance theo chu kỳ.

## Kiến trúc ngắn gọn

- `accounts.py` + `database.py`: domain state và SQLite persistence cho accounts, logs, market cache.
- `accounts_server.py`: expose account tools/resources qua FastMCP.
- `accounts_client.py`: handwritten MCP client bridge sang OpenAI `FunctionTool`.
- `market.py` + `market_server.py`: market data abstraction và MCP wrapper.
- `push_server.py`: MCP tool gửi push notification.
- `mcp_params.py`: tập trung cấu hình trader/researcher MCP servers.
- `templates.py`: prompt templates cho researcher và trader cycles.
- `traders.py`: orchestration của một trader agent.
- `trading_floor.py`: scheduler loop chạy cả team traders.
- `tracers.py`: trace processor ghi sự kiện xuống DB.
- `app.py`: Gradio dashboard hiển thị logs, holdings, transactions, PnL.

## Luồng hệ thống

1. `trading_floor.py` tạo 4 trader agents.
2. Mỗi trader spawn các MCP servers cần thiết qua `MCPServerStdio`.
3. Trader đọc `account` và `strategy` qua MCP resources.
4. Trader dùng researcher tool + market/account tools để ra quyết định.
5. Transactions, logs, portfolio snapshots và trace events được ghi vào SQLite.
6. `app.py` đọc cùng nguồn state đó để render dashboard.

## Thư mục và file quan trọng

### Root code

- `1_lab1.ipynb` đến `5_lab5.ipynb`: progression từ MCP basics đến capstone finale.
- `accounts.py`
- `accounts_client.py`
- `accounts_server.py`
- `app.py`
- `database.py`
- `market.py`
- `market_server.py`
- `mcp_params.py`
- `push_server.py`
- `reset.py`
- `templates.py`
- `tracers.py`
- `traders.py`
- `trading_floor.py`
- `util.py`

### Docs

- `tai_lieu/day1_study_guide.html`
- `tai_lieu/day2_study_guide.html`
- `tai_lieu/day3_study_guide.html`
- `tai_lieu/day4_study_guide.html`
- `tai_lieu/day5_study_guide.html`

Các study guides này mô tả rất rõ mental model của repo: Day 1 là MCP consumption, Day 2 là custom server/client, Day 3 là memory/search/market data, Day 4-5 là capstone productization.

## Cách chạy dự án

Đây là run guide suy luận từ code/docs:

1. Cài Python environment có `uv`.
2. Nếu dùng các Node-based MCP servers, cài thêm Node.js và `npx`.
3. Thiết lập `.env` với các biến cần thiết tùy capability:
   - `BRAVE_API_KEY`
   - `POLYGON_API_KEY`
   - `POLYGON_PLAN`
   - `PUSHOVER_USER`
   - `PUSHOVER_TOKEN`
   - `DEEPSEEK_API_KEY`
   - `GOOGLE_API_KEY`
   - `GROK_API_KEY`
   - `OPENROUTER_API_KEY`
4. Nếu muốn reset baseline cho 4 traders:

```bash
uv run reset.py
```

5. Chạy dashboard:

```bash
uv run app.py
```

6. Chạy trading loop ở terminal khác:

```bash
uv run trading_floor.py
```

## Runtime settings

Có thể cấu hình thêm qua `.env`:

- `RUN_EVERY_N_MINUTES=60`
- `RUN_EVEN_WHEN_MARKET_IS_CLOSED=false`
- `USE_MANY_MODELS=false`

Nếu `USE_MANY_MODELS=true`, code sẽ route sang DeepSeek, Gemini, Grok hoặc OpenRouter tùy trader/model name.

## Dependencies suy ra từ imports

Không thấy manifest dependency chính thức trong scope exploration, nhưng code hiện dùng:

- `openai-agents` / OpenAI Agents SDK
- `mcp`
- `pydantic`
- `python-dotenv`
- `requests`
- `polygon`
- `gradio`
- `pandas`
- `plotly`

Ngoài ra notebooks còn dùng:

- `uvx mcp-server-fetch`
- `@modelcontextprotocol/server-brave-search`
- `mcp-memory-libsql`
- official Polygon MCP server

## Testing và validation hiện tại

Repo không có test suite rõ ràng trong scope đã đọc. Cách validate chính hiện tại là:

- chạy notebook labs
- xem traces
- xem dashboard
- kiểm tra SQLite-backed state

Nếu mở rộng dự án, nên thêm:

- unit tests cho `accounts.py`, `database.py`, `market.py`
- MCP contract tests cho servers
- integration tests cho `Trader.run()`

## Lưu ý và rủi ro

- `market.py` có fallback random price khi Polygon lỗi hoặc thiếu key; tốt cho demo nhưng không đáng tin cho simulation nghiêm túc.
- `push_server.py` phụ thuộc network và credentials, nhưng error handling còn rất mỏng.
- Có subtree `hieu/` giống một bản copy của project; README này coi root `6_mcp` là canonical path.
- Day 1 docs có cảnh báo MCP trên Windows có thể cần WSL.

## Tài liệu bổ sung đã tạo

- `PROJECT_EXPLORATION.html`
- `project_exploration_state.json`

Nếu bạn muốn, bước tiếp theo mình có thể:

- rút tiếp README này xuống phiên bản cực ngắn cho public repo
- hoặc nâng nó thành README “chuẩn mở repo” với badges, prerequisites và troubleshooting section
