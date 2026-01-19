def assert_in_range(value: float, low: float, high: float):
    assert low <= value <= high, f"{value} not in [{low},{high}]"
