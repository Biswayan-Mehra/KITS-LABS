def fifo(n,pages):
    frame = []
    hits, miss = 0, 0
    for page in pages:
        if not page in frame:
            miss += 1
            frame.append(page)
        else:
            hits += 1
        while len(frame) > n:
            frame = frame[1:]
    return hits, miss

def opt(n,pages):
    #7 0 1 2 0 3 0 4 2 3 0 3 2 3
    frame = []
    count = dict((page, pages.count(page)) for page in pages)
    hits, miss = 0, 0
    for page in pages:
        if page in frame:
            hits += 1
        else:
            miss += 1
            while len(frame) >= n:
                rem = frame[0]
                for cache in frame[1:]:
                    if count[cache]< count[rem]:
                        rem = cache
                frame.remove(rem)
            frame.append(page) 
    return hits, miss

def lru(n,pages):
    frame = []
    hits, miss = 0, 0
    for page in pages:
        if page in frame:
            hits += 1
            frame.remove(page)
            frame.append(page)
        else:
            miss += 1
            while len(frame) >= n:
                frame = frame[1:]
            frame.append(page)
    return hits, miss

n = int(input("Number of Frames: "))
pages = [int(x) for x in input().split()]
print(fifo(n,pages))
print(opt(n,pages))
print(lru(n,pages))
