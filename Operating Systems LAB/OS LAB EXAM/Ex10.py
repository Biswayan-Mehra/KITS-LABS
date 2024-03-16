def fcfs(queue, head):
    diff = []
    mov = 0
    for req in queue:
        diff.append(abs(req-head))
        mov += abs(req-head)
        head = req
    return diff, mov

def sstf(queue, head):
    diff = []
    mov = 0
    while len(queue) > 0 :
        min_req = sorted(queue, key =lambda x: abs(x-head))[0]
        diff.append(abs(min_req-head))
        mov += abs(min_req-head)
        head = min_req
        queue.remove(min_req)
    return diff, mov

n = int(input("Enter the number of tracks: "))
queue = [int(x) for x in input().split()]
if not len(queue) == n:
    exit(0)
head = int(input("Enter the head start: "))
print(fcfs(queue,head))
print(sstf(queue,head))

#98 183 37 122 14 124 65 67