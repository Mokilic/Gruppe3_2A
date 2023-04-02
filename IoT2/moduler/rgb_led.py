import RPi.GPIO as GPIO

# Funktion, der opsætter tre LED-pinde
def setup_led(red_pin, green_pin, blue_pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red_pin, GPIO.OUT)
    GPIO.setup(green_pin, GPIO.OUT)
    GPIO.setup(blue_pin, GPIO.OUT)

    # Variabler som laves til PWM objekter for hver farve
    red_pwm = GPIO.PWM(red_pin, 100)
    green_pwm = GPIO.PWM(green_pin, 100)
    blue_pwm = GPIO.PWM(blue_pin, 100)

    # Start PWM for hver farve
    red_pwm.start(0)
    green_pwm.start(0)
    blue_pwm.start(0)

    # Definerer en funktion til at sætte farven
    def set_color(red, green, blue):
        red_pwm.ChangeDutyCycle(red)
        green_pwm.ChangeDutyCycle(green)
        blue_pwm.ChangeDutyCycle(blue)
    
    return set_color