from multiprocessing import Event, Process, Value
from time import sleep

# Shared pulse interval variable
pulse_interval = Value('d', 0.5)  # 'd' for double (float) shared variable
stop_flag = Event()

def worker(delay, stop_flag):
    while not stop_flag.is_set():
        interval = delay.value
        sleep(interval)
        print(interval)

def run_ai_model():
    # Simulate a heavy AI computation
    for _ in range(10**8):
        pass
    pulse_interval.value = .2
    for _ in range(10**8):
        pass  # Replace with actual AI model computation

if __name__ == "__main__":
    # Start motor control in a separate process
    worker_process = Process(target=worker, args=(pulse_interval, stop_flag,))
    worker_process.start()

    try:
        # Run the AI model in the main process
        run_ai_model()
    finally:
        # Cleanup
        stop_flag.set()
        worker_process.join()
        print("done")
