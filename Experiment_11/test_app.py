from app import calculate_total


def test_calculate_total():
    prices = [100, 200, 300]
    expected = 600

    assert calculate_total(prices) == expected