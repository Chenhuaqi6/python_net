import os
from time import sleep

p = os.fork()

if p == 0:
    print("child PID",os.getpid())
    os._exit(1)
else:
    print("Parent process")
    sleep(20)