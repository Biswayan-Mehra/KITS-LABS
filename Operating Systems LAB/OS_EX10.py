def fcfs(requests, head):
    differences = []
    movements = 0
    for req in requests:
        differences.append(abs(req - head))
        movements += abs(req - head)
        head = req
    return differences, movements

def sstf(requests, head):
    differences = []
    movements = 0
    queue = list(requests)
    while len(queue) > 0:
        min_ = sorted(queue, key = lambda x: abs(x - head))[0]
        differences.append(abs(min_ - head))
        movements += differences[-1]
        head = min_
        queue.remove(min_)
    return differences, movements

head = int(input("Enter head value: "))
requests = [int(req) for req in input("Enter the requests: ").split()]
print("\nPerforming fcfs, movements taken are: ")
diff, mov = fcfs(requests, head)
print("\n".join(str(d) for d in diff))
print("Total movements taken:", mov)

print("\nPerforming sstf, movements taken are: ")
diff, mov = sstf(requests, head)
print("\n".join(str(d) for d in diff))
print("Total movements taken:", mov)
