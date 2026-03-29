# Python AI Starter Template

Minimal Streamlit app for quick prototypes.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e .
```

Optional: copy environment defaults and edit.

```bash
cp .env.example .env
```

## Run

```bash
streamlit run app.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

## Configuration

| Variable    | Description        | Default                        |
|------------|--------------------|--------------------------------|
| `APP_TITLE` | Browser/tab title and main heading | See `.env.example` |

Real secrets (API keys): use `.streamlit/secrets.toml` locally (see [Streamlit secrets](https://docs.streamlit.io/develop/concepts/connections/secrets-management)) or your host’s secret store in production.
