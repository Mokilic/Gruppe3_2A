import smbus
#import RPi.GPIO as GPIO
import time

i2c_bus_number = 1  # This depends on the specific Raspberry Pi model you're using
device_address = 0x49

#

i2c_bus = smbus.SMBus(i2c_bus_number)

#findes ved at tage en måling på sit batteri, kaldet U
#U*1023/adc_val = u_num
u_num = 16.5

def bat_funktion():
    adc_bytes = i2c_bus.read_i2c_block_data(device_address, 0x00, 2)
    
    # # Here we print the individual ADC bytes
    # print("adc_byte 0          ", hex(adc_bytes[0]))
    # print("acd byte 0, bit 1-0 ", hex(adc_bytes[0] & 0x03))
    # print("acd byte 0, bit 3-2 ", hex((adc_bytes[0] >> 2) & 0x03))
    # print("adc_byte 1          ", hex(adc_bytes[1]))
    # print("adc_byte 1, bit 7-2 ", hex(adc_bytes[1] >> 2))

    # # Low_byte consists of adc_byte[0] 1-0 and adc_byte[1] 7-2
    lowByte = ((int(adc_bytes[0]) << 6) & 0xC0) + (int(adc_bytes[1]) >> 2)
    # print("Low byte:           ", hex(lowByte))
    highByte = (int(adc_bytes[0]) >> 2)
    # print("high byte:          ", hex(highByte))      
    adc_val = (highByte << 8) + lowByte
    # print("adc value  i hex     ", hex(adc_val))
    # print("adc value i int      ", int(adc_val))
    
    # Conversion of ADC value to voltage and print
    # voltage = (adc_val * u_num) / 1023.0
    # print("voltage             ", voltage)
    
    # print("  ")
    # time.sleep(2)

    return adc_val

# adc_value = bat_funktion()

# print(adc_value)