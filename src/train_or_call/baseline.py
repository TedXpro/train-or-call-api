from collections import Counter


class MajorityClass:
    def fit(self, labels: list[str]) -> "MajorityClass":
        self.label = Counter(labels).most_common(1)[0][0]
        return self

    def predict(self, texts: list[str]) -> list[str]:
        return [self.label for _ in texts]
