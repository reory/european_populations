import pytest  # noqa
from hypothesis import given, strategies as st
from bar_chart import get_bar_chart


@given(n=st.integers(min_value=1, max_value=100))
def test_bar_chart_generation(n):

    # Verify the function creats a chart without crashing for valid ranges
    chart = get_bar_chart(n=n)
    assert chart is not None
