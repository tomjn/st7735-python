import sys
import mock


def _mock():
    sys.modules['numpy'] = mock.Mock()
    sys.modules['spidev'] = mock.Mock()
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi.GPIO'] = mock.Mock()


def test_128_64_0():
    _mock()
    import ST7735
    display = ST7735.ST7735(port=0, cs=0, dc=24, width=128, height=64, rotation=0)
    assert display.width == 128
    assert display.height == 64


def test_128_64_90():
    _mock()
    import ST7735
    display = ST7735.ST7735(port=0, cs=0, dc=24, width=128, height=64, rotation=90)
    assert display.width == 64
    assert display.height == 128
