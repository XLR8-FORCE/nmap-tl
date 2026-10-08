# Vulnerability Dashboard (in progress)

A Python FastAPI/Jinja2 scaffold for a vulnerability dashboard, built with AI assistance and iterative prompting. The repository keeps its original `nmap-tl` name; it does not currently integrate Nmap.

## Current state
- Routes for home, search, statistics and watchlist pages.
- Basic home and search templates.
- A separate `temporary.py` script exploring NVD records and severity data.

Backend search, persistence and analytics modules are placeholders. Statistics/watchlist templates are empty. The search form is not yet connected to the backend.

## Run the scaffold
```sh
python -m venv .venv
# Activate .venv for your shell
python -m pip install -r requirements.txt
uvicorn app:app --reload
```
Open http://127.0.0.1:8000. Run from the project root so relative template paths resolve.

## Next steps
Connect the search form to validated query parameters, implement NVD pagination, add SQLite storage and write API tests. These are planned, not completed features.
