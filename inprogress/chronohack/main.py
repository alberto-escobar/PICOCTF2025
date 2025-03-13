import random
import time

def get_random(length):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(int(time.time() * 1000))  # seeding with current time 
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s


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

import subprocess

def main():
    host = "verbal-sleep.picoctf.net"
    port = 57177

    
    # Launch netcat as a subprocess with pipes for stdin and stdout
    # `text=True` (or `universal_newlines=True` in older Python) means we get strings rather than bytes
    proc = subprocess.Popen(
        ["nc", host, str(port)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    values = get_array(20)

    # Read a little bit of initial output (if any)
    # This is optional – you can see if the server prints a welcome message
    time.sleep(0.5)
    init_output = read_all_nonblocking(proc)
    if init_output:
        print("Initial output:")
        print(init_output)
    
    # Send each value, read output, look for "picoCTF"
    for val in values:
        # Write to nc
        proc.stdin.write(val + "\n")
        proc.stdin.flush()
        
        # Give the server a moment to respond
        time.sleep(0.2)
        
        # Read any new output
        response = read_all_nonblocking(proc)
        if response:
            print(val)
            print(response)
            if "picoCTF" in response:
                print("Found picoCTF in output!")
                break
    
    # Optionally, close the connection
    proc.stdin.close()
    proc.terminate()

def read_all_nonblocking(proc):
    """
    Attempt to read whatever is currently in stdout without blocking.
    By default, if you call proc.stdout.read(...) without blocking,
    you might wait until the subprocess closes the pipe or times out.
    
    We'll use .read() in a non-blocking manner by checking if there's data in the buffer.
    If you want simpler logic, you can do a small .read(1024) or so.
    """
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
