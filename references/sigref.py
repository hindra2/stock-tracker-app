import queue
import threading
import time

a = True
lock = threading.Lock()
q = queue.Queue()

class asd:
    def __init__(self, a):
        self.a = a

        self.atrue()
    
    def atrue(self):
        while True:
            if self.a:
                print("TRUE")
            else:
                print("False")
            time.sleep(1)

def thread1():
    global a
    while True:
        with lock:
            if a:
                a = False
            else:
                a = True
            q.put(a)
        time.sleep(1)

def thread2():
    global a
    while True:
        with lock:
            try:
                a = q.get(block=False)
            except queue.Empty:
                pass
            print(a)
            time.sleep(1)


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()