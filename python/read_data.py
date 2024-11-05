import time
import os

data_file = "/data/input.txt"
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
