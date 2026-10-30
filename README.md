# train-or-call-api

For banking support questions, when does training a model beat calling an LLM API on accuracy, speed and cost?

**Status:** skeleton. `MajorityClass` is the floor every model must beat.

## Results

| Model | Accuracy | Response time | Cost per 1,000 |
|---|---|---|---|
| Majority class | not measured | not measured | none |
| TF-IDF + logistic regression | not measured | not measured | not measured |
| DistilBERT (PyTorch) | not measured | not measured | not measured |
| LLM API | not measured | not measured | not measured |

## Run

```
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev,notebooks]"
pytest
python evals/run.py
```

## Plan

- [ ] Score the majority baseline on Banking77
- [ ] Add TF-IDF + logistic regression
- [ ] Fine-tune DistilBERT in PyTorch and track runs with MLflow
- [ ] Call an LLM on the same test set
- [ ] Serve the winner with FastAPI and Docker

## Data

[Banking77](https://huggingface.co/datasets/PolyAI/banking77) (13,083 questions, 77 intents, CC BY 4.0). Download it into `data/`; it is not committed.

## Layout

- `src/`: the code
- `tests/`: unit tests
- `evals/`: measures quality on labelled cases
- `notebooks/`: exploration and results
- `docs/decisions/`: why each design choice was made
- `docs/failures.md`: what broke and how it was fixed

## AI use

Built with AI coding tools under the rules in [AGENTS.md](AGENTS.md).
