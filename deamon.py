# synchronization means callback q in js
# and u cannot run start before setting thread only after setting thread can you set thre
# ad

import threading
import time

# Define a function for the daemon thread
def background_task():
    while True:
        print("Daemon thread is running...")

        time.sleep(1)


daemon_thread = threading.Thread(target=background_task)
daemon_thread.daemon = True

# Start the daemon thread after setting main thread
daemon_thread.start()

# cannot use start after starting main thread

# Main thread doing some work
try:
    for i in range(5):
        print(f"Main thread is working... {i}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Main thread interrupted")

print("Main thread is done, exiting...")
