'''
Deadlock:
where the threads wait forever for locks
thread 1:
Lock A
waiting for Lock B
thread 2:
Lock B
waiting for Lock A

Tread 1--->waiting Lock A
Thread 2--->waitihng Lock B
deadlock

RLock:
Normal Lock
acquire once
release

if same thread acq
'''

# import threading

# lock = threading.Lock()
# def outer():
#     lock.acquire()
#     inner()
#     lock.release()
# def inner():
#     lock.acquire()
#     print("inner")
#     lock.release()
# outer()

'''
Outer() acquired the lock
inner() trying to  acquired the same lock
lock is already head  above
wait forver
'''
import threading
lock = threading.RLock
def inner():
    with lock:
        print("inner")
def outer():
    with lock:
        print("outer")
        inner()
outer()