import json
from pathlib import Path

from train_or_call.baseline import MajorityClass

CASES = Path(__file__).parent / "cases.jsonl"


def main():
    cases = [json.loads(line) for line in CASES.read_text().splitlines()]
    labels = [case["label"] for case in cases]
    predictions = MajorityClass().fit(labels).predict([case["text"] for case in cases])
    correct = sum(p == label for p, label in zip(predictions, labels))
    print(f"accuracy {correct / len(cases):.2f}")


if __name__ == "__main__":
    main()
