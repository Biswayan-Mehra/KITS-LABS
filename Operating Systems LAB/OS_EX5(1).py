import threading
mutex = threading.Semaphore(1) 
full = threading.Semaphore(0) 
empty = threading.Semaphore(3) 
x = threading.Semaphore(0)
def producer(): 
    mutex.acquire() 
    full.release() 
    empty.acquire() 
    x.release()
    print(f"Producer produces the item number {x._value}") 
    mutex.release()
def consumer(): 
    mutex.acquire() 
    full.acquire() 
    empty.release()
    print(f"Consumer Consumed the item number {x._value}") 
    x.acquire()
    mutex.release() 
while(True):
    print("1)Producer 2)Consumer 3)Exit") 
    user_in = int(input())
    if (user_in == 1):
        if(mutex._value==1 and empty._value!=0): 
            print("this ran")
            producer() 
        else:
            print("Buffer is full") 
    elif (user_in == 2):
        if (mutex._value==1 and full._value !=0): 
            consumer()
        else:
            print("Buffer is empty")
    else:
        break