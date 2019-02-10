import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

delay_print("HELLO!")
print(" ")
delay_print("WHO ARE YOU?")
print(" ")
name = input()
