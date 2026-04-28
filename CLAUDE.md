# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GoIT Python Core V2 course repository containing code examples and exercises organized by module. Each module covers a distinct Python topic:

- **module01** — Data types (int, float, str, bool, list, dict, tuple, set)
- **module02** — Control flow (if/else, for, while, exceptions, functional basics)
- **module03–06** — Additional fundamentals
- **module07** — Generators, iterators, custom counter/decimal/IP aggregator examples
- **module08** — Functional programming (closures, decorators, comprehensions, map/filter/reduce)
- **module09–10** — OOP (classes, inheritance, polymorphism, composition, MRO, magic methods, ABCs)
- **module11** — Advanced OOP, FastAPI, SQLAlchemy; contains two sub-projects:
  - `module11/demo/` — design patterns demo with MongoDB/SQL db clients
  - `module11/fast_api_zoo/` — full FastAPI application (cats/owners/auth REST API)
- **module12** — Serialization (CSV, JSON, YAML, Pickle, Pydantic)

## Environment

The repo uses a local venv at `.env/` (Python 3.13.3 via pyenv). Activate with:

```bash
source .env/bin/activate
```

## Running Code

Most modules are standalone scripts. Run them directly:

```bash
python module07/gen/example.py
python module08/decorators/example.py
```

## FastAPI Zoo App (`module11/fast_api_zoo/`)

### Setup

Requires PostgreSQL and Redis. Start infrastructure with Docker Compose:

```bash
cd module11/fast_api_zoo
docker-compose up -d db redis
```

Configure the database in `src/settings/config.ini` (parsed by `src/settings/base.py`):

```ini
[DB]
USER=admin
PASSWORD=admin
DOMAIN=localhost
PORT=5432
DB_NAME=zoo

[AUTH]
SECRET_KEY=your_secret_key
```

### Run the server

```bash
cd module11/fast_api_zoo
uvicorn main:app --reload
```

API available at `http://localhost:8000`. Docs at `/docs`.

### Architecture

```
main.py               # FastAPI app, startup table creation, router registration
src/
  database/
    db.py             # SQLAlchemy engine, session factory, get_db dependency
    models.py         # ORM models
  repository/         # Data-access layer (cats.py, owners.py, users.py)
  routers/            # HTTP handlers (cats.py, owners.py, auth.py)
  schemas/            # Pydantic request/response schemas
  services/           # Business logic
  settings/           # Config parsing (config.ini → base.py)
```

The pattern is: **router → repository** (no service layer for simple CRUD; services used for auth/email).

### Tests

```bash
cd module11/fast_api_zoo
pytest
```

## Demo App (`module11/demo/`)

Demonstrates the Strategy/Repository pattern with interchangeable db clients (MongoDB vs SQL):

```
src/
  auth/               # login_user entry point
  db_client/          # base_client.py (ABC), mongodb_client.py, sql_client.py
  posts/              # post_controller.py, models/
  config.py
```

Run tests:

```bash
cd module11/demo
pytest
```
