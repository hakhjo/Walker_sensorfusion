import time
import os

import os

data_file = os.path.join(os.getcwd(), "data", "input.txt")
# data_file = os.path.abspath(data_file)  # Optional: Get the absolute path
i = 0

while True:
    try:
        with open(data_file, "w") as f:
            f.write("This is new data from Python " + str(i) + "\n")
        print(f"Python has written data to {data_file} with i={i}")
        i += 1
    except Exception as e:
        print(f"Error writing to {data_file}: {e}")
    time.sleep(5)
