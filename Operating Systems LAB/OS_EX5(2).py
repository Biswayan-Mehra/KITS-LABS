import threading
from random import choice 

def reader(cnt, wrt, mutex, readers, reader_count): 
        mutex.acquire()
        readers.release()
        if readers._value == 1: 
            wrt.acquire()
        print(f"Reader {reader_count}: reading value as {cnt[0]}") 
        wrt.release()
        readers.acquire() 
        mutex.release()
def writer(cnt, wrt, mutex, readers, val, writer_num): 
        mutex.acquire()
        wrt.acquire() 
        cnt[0] = val
        print(f"Writer {writer_num}: writing value as {cnt[0]}") 
        wrt.release()
        mutex.release() 
        
cnt = [0]
wrt = threading.Semaphore(1) 
mutex = threading.Semaphore(1) 
readers = threading.Semaphore(0) 
writer_num = 0
reader_count = 0 
for i in range(15):
    ftn = choice([0,1]) 
    if ftn == 0:
        reader_count += 1
        reader(cnt, wrt, mutex, readers, reader_count) 
    if ftn == 1:
        writer_num += 1
        val = choice(range(15))
        writer(cnt, wrt, mutex, readers, val, writer_num)