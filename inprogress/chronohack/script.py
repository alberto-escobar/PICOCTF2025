import random
import time
import string
import socket

HOST = "verbal-sleep.picoctf.net"
PORT = 56823

def get_random(length, seed):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed-1000)  # seeding with current time 
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

def connect_and_try_tokens(start_time):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        current_time = int(time.time() * 1000)
        data = s.recv(1024).decode()
        print(data)  # Welcome message
        token_length = 20

        for offset in range(start_time, start_time+50):  # Try a range of ~1 second
            seed = current_time + offset
            token_guess = get_random(token_length, seed)
            print(f"Trying token: {token_guess}")

            s.sendall((token_guess + "\n").encode())  # Send the guess
            response = s.recv(1024).decode()
            print(response)

            if "Congratulations" in response:
                print("FLAG FOUND! ")
                print(response)
                return 1
        return 0

def brute():
    for i in range(-1000, 1000, 46):
        print(i)
        if (connect_and_try_tokens(i) == 1):
            break


if __name__ == "__main__":
    brute()
