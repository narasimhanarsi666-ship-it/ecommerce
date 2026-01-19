# Ecommerce Monorepo

A production-grade demo ecommerce system including:
- **Frontend**: Next.js + TypeScript
- **Backend**: FastAPI (Python)
- **Automation**: pytest (API/UI/E2E), Playwright (Python), Locust, ZAP
- **CI/CD**: GitHub Actions

## Quick Start (Dev)

```bash
# 1) Backend
cd ecommerce-backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload

# 2) Frontend
cd ../ecommerce-frontend
npm ci
npm run dev
# open http://localhost:3000
```

Or use Docker Compose from the repo root:

```bash
docker compose up --build
```

## Test Automation

```bash
cd ecommerce-test-automation
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## CI Pipelines
Workflows in `.github/workflows/` run smoke, regression and domain suites.
