from train_or_call.baseline import MajorityClass


def test_predicts_most_common_label():
    model = MajorityClass().fit(["card", "card", "refund"])
    assert model.predict(["any question"]) == ["card"]
