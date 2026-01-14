# Prooflayer

Prooflayer exists to make reasoning auditable. It provides a backend service where claims, evidence, and conclusions are handled as explicit, inspectable structures rather than opaque outputs.

## What It Does

Prooflayer is a backend service for verifiable reasoning workflows. It exposes a structured API for submitting claims, attaching evidence, and producing machine-checkable proof states. The system prioritizes traceability over abstraction and correctness over convenience.

## Core Properties

* Deterministic request handling
* Explicit linkage between claims, evidence, and results
* API-first architecture
* ASGI-compatible deployment

## Tech Stack

* Python 3.11
* FastAPI
* Uvicorn
* Pydantic

## Repository Structure

```
prooflayer/
├── main.py            # Application entrypoint (FastAPI app)
├── requirements.txt   # Runtime dependencies
├── runtime.txt        # Python version for deployment
├── README.md
```

`main.py` must expose:

```python
app = FastAPI()
```

## Local Development

Environment setup:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the server:

```
uvicorn main:app --reload
```

Service address:

```
http://127.0.0.1:8000
```

API documentation:

```
/docs
```


## Design Constraints

* No hidden global state
* No implicit imports
* No environment-dependent execution at import time

Failures are surfaced immediately and explicitly.

## Status

Early-stage prototype. Interfaces may change. Stability is not guaranteed.

## License

MIT
