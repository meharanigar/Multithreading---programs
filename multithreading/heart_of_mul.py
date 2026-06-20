'''
1.Race condition
2.Synchronization
3.Lock
4.Rlock

#why we need synchronization?

balance =1000

thread-1 ==withdraw 500
thraed-2 == withdraw 700

both are accessing the same variable
without proper control

Incorrect Balance
wrong transaction
data corruption

TO avoid the above we will use:
Synchronization:
This is a process of controlling access to shared
resources so that only one thraed modifies at a time

Lock:
hared
resources: any variable,file,database,object

Ex:
count = 0
if multiple threads modifies count simultaneously
---------------------------------------------------------

#Race Condition:
occurs when multiple threads access and modify
shared data simultaneously

#write in threading:
import threading 
count = 0 
def increments():
    global count
    count +=1

threads = []
for i in range(1000):
    t  = threading.Thread(target = increments)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(count)



Critical section:
code section where shared resources are
accessed is called critical section
count +=1-->critical section

to avoid thr tace condition?
one thread should enter critical section
solution :Lock



Whatt is lock?
that allows only one thread  to execute a critical section at a time 


Thread A acquires Lock
other Threads will Wait
Thread A releases lock
next thread gets lock 
   


import threading
 lock = threading,Lock()



 #TO apply Lock:
 lock.acqurie()


 # To release lock:
 lock.release()

 


 #Problem :
import threading
count = 0
lock= threading.Lock()
def increment():
    global count 
    for i in range(1000):
         with lock:
         #critical section
            count +=1
         #lock.release()
t1 = threading.Thread(target = increment)
t2 = threading.Thread(target = increment)
t1.start()
t2.start()
t1.join()
t2.join()
print(count)




#Bank example:(brute froce approach)
class Bank:
     def __init__(self):
         self.balance = 1000
     def withdraw(self,amount):
          if self.balance >= amount:
              self.balance -=amount

'''
import threading 
lock =threading.Lock()
class Bank:
     def __init__(self):
         self.balance = 1000
         self.lock = threading.Lock()
     def withdraw(self,amount):
        with lock:
           if self.balance >= amount:
              self.balance -=amount
              print(amount," withdrawn")
           else:
               print("Insufficient balance")
obj = Bank()
t1 = threading.Thread(target =obj.withdraw,args =(700,) )
t2 = threading.Thread(target =obj.withdraw,args =(500,) )
t1.start()
t2.start()
t1.join()
t2.join()
print(obj.balance)



