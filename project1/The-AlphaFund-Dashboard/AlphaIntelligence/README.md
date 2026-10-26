# AlphaFund Terminal

AlphaFund Terminal is a Streamlit dashboard for asking questions about company financials and sample earnings-call transcript text. It combines SQL queries against an S&P 500 financials dataset with semantic search over bundled transcript excerpts, then uses an OpenRouter model to compose an answer.

## Features

- **Financial data:** Loads the S&P 500 financials CSV from GitHub into an in-memory SQLite database. If the download fails, the app uses fallback data for eight companies.
- **Transcript search:** Builds a local FAISS index from bundled Q4 2024 sample transcript text for MSFT, AAPL, GOOGL, NVDA, and AMZN. The `all-MiniLM-L6-v2` embedding model is downloaded on first launch.
- **AI answers:** A LangChain tool-calling agent chooses whether to query financials, search transcripts, or use both. OpenRouter provides the language model.
- **Interactive dashboard:** A Streamlit chat UI includes a routing log and sample queries.

## Requirements

- Python 3.10 or newer
- An OpenRouter API key
- Internet access on first launch to download Python packages, the financials CSV, and the embedding model

## Run locally

Run these commands from the repository root (the folder containing `requirements.txt`).

### 1. Clone the repository

```bash
git clone https://github.com/himanshuvidyarthi/The-AlphaFund-Dashboard.git
cd The-AlphaFund-Dashboard
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the app

```bash
streamlit run AlphaIntelligence/app.py
```

Open the local URL printed by Streamlit, usually <http://localhost:8501>. On first launch, the app downloads the embedding model and attempts to fetch the financials CSV.

### 5. Enter your OpenRouter API key

Create a key at <https://openrouter.ai/keys>, then enter it in the **OPENROUTER KEY** field in the app sidebar.

Alternatively, set `OPENROUTER_API_KEY` in your shell before launching Streamlit:

**Windows PowerShell**

```powershell
$env:OPENROUTER_API_KEY = "your-key"
streamlit run AlphaIntelligence/app.py
```

**macOS / Linux**

```bash
export OPENROUTER_API_KEY="your-key"
streamlit run AlphaIntelligence/app.py
```

The app does not automatically load `.env` files. Do not commit or share your API key.

## Models

Choose the routing model from the sidebar:

| Model | Notes |
|---|---|
| `google/gemini-2.0-flash-001` | Default |
| `anthropic/claude-3.5-haiku` | Alternative |
| `openai/gpt-4o-mini` | Alternative and automatic fallback |
| `mistralai/mistral-nemo` | Alternative |

If OpenRouter reports that the selected model has no endpoints (or returns a 404), the app retries with `openai/gpt-4o-mini`.

## Example questions

- What is Microsoft's market cap, and what does the bundled sample transcript say about AI infrastructure?
- Compare NVDA and AAPL market caps, then search for comments about revenue.
- Which sector has the highest average EBITDA?
- What does Amazon's bundled sample transcript say about capital expenditure?

The transcript content is bundled sample text, not a live transcript feed. Financial figures come from the downloaded dataset when available; otherwise, the app uses its built-in fallback values.

## Deploy with Streamlit Community Cloud

1. Push this repository to a GitHub account you control.
2. In Streamlit Community Cloud, create an app from that repository and branch.
3. Set **Main file path** to `AlphaIntelligence/app.py`.
4. Deploy, open the app, and enter your OpenRouter key in the sidebar.

The dependency file is at the repository root: `requirements.txt`. The current app reads the key from the sidebar or the `OPENROUTER_API_KEY` environment variable; it does not read Streamlit secrets directly.

## Project layout

```text
The-AlphaFund-Dashboard/
├── requirements.txt
└── AlphaIntelligence/
    ├── app.py
    ├── .env.example
    ├── .gitignore
    └── README.md
```

## Troubleshooting

| Issue | What to try |
|---|---|
| Authentication required | Enter a valid OpenRouter key in the sidebar or set `OPENROUTER_API_KEY` before launching. |
| Model endpoint or 404 error | The app retries with `openai/gpt-4o-mini`; check your OpenRouter account and model availability if it still fails. |
| First launch takes a while | The embedding model is downloaded and the FAISS index is built locally on startup. |
| Financial data does not load | Check internet access. If the CSV request fails, the app uses its eight-company fallback dataset. |
| A ticker is missing from fallback results | The fallback dataset contains MSFT, AAPL, GOOGL, NVDA, AMZN, META, TSLA, and JPM. |
| Deploy does not start | Confirm the main file is `AlphaIntelligence/app.py` and dependencies are installed from the root `requirements.txt`. |
