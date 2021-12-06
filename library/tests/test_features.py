import mock


def test_display(GPIO, spidev, numpy, ST7735):
    display = ST7735.ST7735(port=0, cs=0, dc=24)
    image = mock.MagicMock()
    image.convert.return_value = [
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255]
    ]
    spidev.reset_mock()
    display.display(image)

    spidev.SpiDev().xfer3.assert_has_calls(
        (mock.call(b'\xf8\x00\x07\xe0\x00\x1f'),)
    )


def test_image_to_data_uint8(GPIO, spidev, numpy, ST7735):
    display = ST7735.ST7735(port=0, cs=0, dc=24)
    image = numpy.array([
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255]
    ])
    spidev.reset_mock()
    display.display(image)

    spidev.SpiDev().xfer3.assert_has_calls(
        (mock.call(b'\xf8\x00\x07\xe0\x00\x1f'),)
    )


def test_image_to_data_uint16(GPIO, spidev, numpy, ST7735):
    display = ST7735.ST7735(port=0, cs=0, dc=24)
    image = numpy.array([
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255]
    ], dtype='uint16')
    spidev.reset_mock()
    display.display(image)

    spidev.SpiDev().xfer3.assert_has_calls(
        (mock.call(b'\xf8\x00\x07\xe0\x00\x1f'),)
    )


def test_image_to_data(GPIO, spidev, numpy, ST7735):
    image = mock.MagicMock()
    image.convert.return_value = [255, 0, 255]
    assert ST7735.image_to_data(image) == b"\xf8\x1f"
