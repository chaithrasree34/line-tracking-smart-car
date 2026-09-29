# line-tracking-smart-car
# Python program for Line Tracking Smart Car
# 2 IR sensors: Left and Right
# Motor driver: L298N

import RPi.GPIO as GPIO
import time

# IR sensor pins
LEFT_SENSOR = 17
RIGHT_SENSOR = 18

# Motor pins
LEFT_MOTOR_FORWARD = 22
LEFT_MOTOR_BACKWARD = 23
RIGHT_MOTOR_FORWARD = 24
RIGHT_MOTOR_BACKWARD = 25

GPIO.setmode(GPIO.BCM)

GPIO.setup(LEFT_SENSOR, GPIO.IN)
GPIO.setup(RIGHT_SENSOR, GPIO.IN)

GPIO.setup(LEFT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_BACKWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_BACKWARD, GPIO.OUT)


def stop():
    GPIO.output(LEFT_MOTOR_FORWARD, 0)
    GPIO.output(LEFT_MOTOR_BACKWARD, 0)
    GPIO.output(RIGHT_MOTOR_FORWARD, 0)
    GPIO.output(RIGHT_MOTOR_BACKWARD, 0)


def forward():
    GPIO.output(LEFT_MOTOR_FORWARD, 1)
    GPIO.output(LEFT_MOTOR_BACKWARD, 0)
    GPIO.output(RIGHT_MOTOR_FORWARD, 1)
    GPIO.output(RIGHT_MOTOR_BACKWARD, 0)


def left():
    GPIO.output(LEFT_MOTOR_FORWARD, 0)
    GPIO.output(LEFT_MOTOR_BACKWARD, 0)
    GPIO.output(RIGHT_MOTOR_FORWARD, 1)
    GPIO.output(RIGHT_MOTOR_BACKWARD, 0)


def right():
    GPIO.output(LEFT_MOTOR_FORWARD, 1)
    GPIO.output(LEFT_MOTOR_BACKWARD, 0)
    GPIO.output(RIGHT_MOTOR_FORWARD, 0)
    GPIO.output(RIGHT_MOTOR_BACKWARD, 0)


try:
    while True:

        left_sensor = GPIO.input(LEFT_SENSOR)
        right_sensor = GPIO.input(RIGHT_SENSOR)

        # Both sensors detect the line
        if left_sensor == 1 and right_sensor == 1:
            forward()

        # Left sensor detects the line
        elif left_sensor == 1 and right_sensor == 0:
            left()

        # Right sensor detects the line
        elif left_sensor == 0 and right_sensor == 1:
            right()

        # No sensor detects the line
        else:
            stop()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Line tracking car stopped.")

finally:
    stop()
    GPIO.cleanup()

Working

Both sensors detect the line → Car moves forward.

Left sensor detects the line → Car turns left.

Right sensor detects the line → Car turns right.

Neither sensor detects the line → Car stops.

Note: The exact sensor logic (0/1) can be reversed depending on your IR sensor module. The GPIO pin numbers are examples and should be changed according to your circuit.

This version is suitable for a Raspberry Pi + IR sensors + L298N motor driver setup.
