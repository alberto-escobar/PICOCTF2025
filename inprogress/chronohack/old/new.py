import random
import time
import subprocess

def get_array(length):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    t = int(time.time() * 1000)
    output = []
    for i in range(-50,0):
        random.seed(t+i)  # seeding with current time 
        s = ""
        for i in range(length):
            s += random.choice(alphabet)
        output.append(s)
    return output

def main():
    host = "verbal-sleep.picoctf.net"
    port = 63127

    # Launch netcat as a subprocess with pipes for stdin and stdout
    # `text=True` (or `universal_newlines=True` in older Python) means we get strings rather than bytes
    proc = subprocess.Popen(
        ["nc", host, str(port)], 
        stdout=subprocess.PIPE,  # Explicitly capture stdout
        stderr=subprocess.PIPE,  # Capture stderr (optional)
        universal_newlines=True  # Same as `text=True`, but works in older versions
    )

    print("Captured Output:\n", proc.stdout.read())
    values = get_array(20)


    import os
    import fcntl

    # If on a system that supports fcntl (e.g., Linux / WSL),
    # set stdout to non-blocking for a moment:
    fd = proc.stdout.fileno()
    old_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, old_flags | os.O_NONBLOCK)

    try:
        output = proc.stdout.read()
    except:
        output = ""

    # restore flags
    fcntl.fcntl(fd, fcntl.F_SETFL, old_flags)
    return output

if __name__ == "__main__":
    main()
