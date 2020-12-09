from main import send_happy

def test_send_happy():
    assert send_happy(5, 0.0005) is 0.07
    assert send_happy(5, 1) is 0.9