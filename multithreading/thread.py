'''
what is a program?
a program is set of instructions
stored on a disk

print("hello")

only stores the data

what is process?
when a program starts executing it becomes
a process
running?
python heloo.py
hello

OS-->Operating system

characteristics:
1.Independent
2.Separate memory
chrome:1.8GB, vs-code-500MB
3.Heavy weight:
memory allocations
resource allocation
cpu scheduling

what is a thread?
A thread is smallest unit of execution 
inside a process

^A thread a is a light weight process

Restaurant == process
workwes inside res = threads

worker 1 - Taking the orders
worker 2 - cleaning

Visually:
process:
chrome:
     +thread1
     +thread2
     +thread3

why threads are faster?
threads will share the memory
process needs separate memory allocation
'''
'''
------------------------------------------------------------|
process                             Thread                  |
------------------------------------------------------------|
1.Independent                      1.part of process        |
2.Heavy weight                     2.Light weight           |
3.separate memory                  3.sShred memory          |
4.Slow                             4.Fast                   |
5.Expensive                        5.cheap                  |
6.communication difficult          6.easy                   |
-------------------------------------------------------------
'''
'''--------------------------
Concuurency?
Teacher checking the notebook
student A
student B
student C

one at a time
rapidly switching
appears simultaneously
only one cpu
----------------------------------------
Parallelism:
truly simultaneous

CPU1--->TASK a
CPU2--->TASK b
CPU3--->TASK c
------------------------------
Example: concurency
one chef cooking
soup
chicken
noodles

Example: parallelism
one chef --> soup
second chef-->chicken
third chef--->noodles

pyhton threads will use--Concurency
due to GIL- Global intrepreter lock
'''
#creation of threads:
import threading
#function created(do's nothing)
def display():
    print("hello")
#thread object creation
t = threading.Thread(target=display)
t.start()#starts the created thread

#multiple threads:
import threading

def task():
    print("thread is running")
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t3 = threading.Thread(target=task)
t1.start()
t2.start()
t3.start()

'''
Main Thread 
    + t1
    + t2
    + t3
all execute independentily
'''
#Threads with loops:
def numbers():
    for i in range(5):
        print(i)
t = threading.Thread(target=numbers)
t.start()