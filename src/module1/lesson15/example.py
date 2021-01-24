import threading as thr
import time

memory = 0


def thr_1_handler(n, sleep_time):
    global memory
    for i in range(n):
        memory += 1
        time.sleep(sleep_time)


def thr_2_handler():
    global memory
    for i in range(100):
        memory += 1
        time.sleep(0.06)


thead1 = thr.Thread(target=thr_1_handler, args=(99, 0.05), daemon=True)
thead2 = thr.Thread(target=thr_2_handler, args=(), daemon=True)

thead1.start()
thead2.start()

thead1.join()
thead2.join()

print(memory)
