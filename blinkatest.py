import board
import digitalio
import busio

print("Hello! This is a test program for blinka library")

# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print(pin)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print(i2c)
print("I2C ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print(spi)
print("SPI ok!")

print("done!")
