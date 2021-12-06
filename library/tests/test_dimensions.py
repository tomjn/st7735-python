def test_128_64_0(GPIO, spidev, numpy, ST7735):
    display = ST7735.ST7735(port=0, cs=0, dc=24, width=128, height=64, rotation=0)
    assert display.width == 128
    assert display.height == 64
    display.set_window(0, 0)


def test_128_64_90(GPIO, spidev, numpy, ST7735):
    display = ST7735.ST7735(port=0, cs=0, dc=24, width=128, height=64, rotation=90)
    assert display.width == 64
    assert display.height == 128
    display.set_window(0, 0)


def test_128_64_180(GPIO, spidev, numpy, ST7735):
    display = ST7735.ST7735(port=0, cs=0, dc=24, width=128, height=64, rotation=180)
    assert display.width == 128
    assert display.height == 64
    display.set_window(0, 0)
