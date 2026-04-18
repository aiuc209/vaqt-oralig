import pytest

def time_interval(minutes):
    days = minutes // 1440
    hours = (minutes % 1440) // 60
    return f"{days} kun {hours} soat"

def test_time_interval():
    assert time_interval(0) == "0 kun 0 soat"
    assert time_interval(60) == "0 kun 1 soat"
    assert time_interval(1440) == "1 kun 0 soat"
    assert time_interval(1500) == "1 kun 0 soat"
    assert time_interval(1800) == "1 kun 2 soat"

def test_time_interval_large():
    assert time_interval(10080) == "7 kun 0 soat"
    assert time_interval(20160) == "14 kun 0 soat"

def test_time_interval_zero():
    assert time_interval(0) == "0 kun 0 soat"

pytest.main([__file__])
