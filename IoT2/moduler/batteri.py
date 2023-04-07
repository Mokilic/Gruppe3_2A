import smbus
#import RPi.GPIO as GPIO

i2c_bus_number = 1  # This depends on the specific Raspberry Pi model you're using
device_address = 0x49

#

i2c_bus = smbus.SMBus(i2c_bus_number)

def bat_funktion():
    adc_bytes = i2c_bus.read_i2c_block_data(device_address, 0x00, 2)
    
   
    lowByte = ((int(adc_bytes[0]) << 6) & 0xC0) + (int(adc_bytes[1]) >> 2)
    highByte = (int(adc_bytes[0]) >> 2)
    adc_val = (highByte << 8) + lowByte
 

    return adc_val
