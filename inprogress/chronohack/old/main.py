import os
import sys
import time
import random
import subprocess

# Windows compatibility
import msvcrt

def get_array(length, epoch_time):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    output = []
    for i in range(-25, 25):
        random.seed(epoch_time + i)  # Use the fixed epoch_time
        s = "".join(random.choice(alphabet) for _ in range(length))
        output.append(s)
    return output

def read_all_nonblocking(proc):
    """Non-blocking read for Windows using `msvcrt`."""
    output = ""
    while True:
        if msvcrt.kbhit():  # Check if a character is available
            char = proc.stdout.read(1)
            if not char:
                break
            output += char
        else:
            break
    return output

def main():
    host = "verbal-sleep.picoctf.net"
    port = 51192

    # Capture a fixed timestamp at the start
    epoch_time = int(time.time() * 1000)

    # Generate the array using the fixed epoch_time
    values = get_array(20, epoch_time)

    # Launch netcat subprocess
    proc = subprocess.Popen(
        ["nc", host, str(port)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Read initial output (if any)
    time.sleep(0.5)
    init_output = read_all_nonblocking(proc)
    if init_output:
        print("Initial output:\n", init_output)

    # Send each value, read output, look for "picoCTF"
    for val in values:
        proc.stdin.write(val + "\n")
        proc.stdin.flush()
        time.sleep(0.2)

        response = read_all_nonblocking(proc)
        if response:
            print(val)
            print(response)
            if "picoCTF" in response:
                print("Found picoCTF in output!")
                break

    proc.stdin.close()
    proc.terminate()

if __name__ == "__main__":
    main()
