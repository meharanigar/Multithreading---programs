#Two threads with diff task
import threading
def even():
    for i in range(0,10,2):
        print("Even:",i)
def odd():
    for i in range(1,10,2):
        print("odd",i)

t1 = threading.Thread(target=even)
t2 = threading.Thread(target=odd)
t1.start()
t2.start()

#OS sheduler decides:
#which thread to runs first
print(threading.current_thread())#if you want to know the current thread you should write this 

#Naming of threads:
import threading
def task():
    print(threading.current_thread().name)
t1 = threading.Thread(target=task,name="student_thraed")
t1.start()

#Pssing arguments
def square(n):
    print(n*n)

t= threading.Thread(target=square,args=(5,))
t.start()

#to delay the threads 
import time
print("start")
time.sleep(2)
print("end")

import threading
import time
def task():
    for i in range(5):
        print(i)
        time.sleep(2)
t = threading.Thread(target=task)
t.start()

#Retry mechanism
# while True:
#     try:
#         connect()
#     except:
#         time.sleep(5)