import threading
import RPi.GPIO as GPIO
import time

# Setup GPIO pins
PINS = [17, 18, 27]  # Replace with your actual GPIO pins

for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)

# Shared variables and threading controls
pulse_interval = 0.1
interval_lock = threading.Lock()
stop_event = threading.Event()

def pulse_motor():
    global pulse_interval
    while not stop_event.is_set():
        with interval_lock:
            interval = pulse_interval

        for pin in PINS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(interval)
            GPIO.output(pin, GPIO.LOW)

def main():
    global pulse_interval
    motor_thread = threading.Thread(target=pulse_motor)
    motor_thread.start()

    try:
        while True:
            new_interval = float(input("Enter new pulse interval in seconds: "))
            with interval_lock:
                pulse_interval = new_interval
    except KeyboardInterrupt:
        # Signal the child thread to stop and wait for it to finish
        stop_event.set()
        motor_thread.join()
        GPIO.cleanup()
        print("Program exited cleanly")

if __name__ == "__main__":
    main()
