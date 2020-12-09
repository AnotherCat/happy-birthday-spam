from main import send_happy


def test_send_happy():
    assert send_happy(5, 0.0005) == 0.07
    assert send_happy(5, 1) == 0.9
