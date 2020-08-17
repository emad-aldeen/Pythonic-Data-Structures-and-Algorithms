# put your array_reverse challenge tests here
from challenges.array_reverse.array_reverse import (
    reverse_array,
)

# here's a test to get you started
def test_leave_as_is():
    actual = reverse_array([1])
    expected = [1]
    assert actual == expected
