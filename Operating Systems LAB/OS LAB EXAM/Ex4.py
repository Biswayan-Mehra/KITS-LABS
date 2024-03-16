n = int(input("Enter no. of process: "))
burst = eval(input("Enter burst time: "))
#1st
wait = [0]*n
tat = [0]*n
avg_wait = 0
avg_tat = 0

for p in range(1, n):
    wait[p] = wait[p-1] + burst[p-1]
    tat[p] = wait[p] + burst[p]
    avg_wait+=wait[p]
    avg_tat+=tat[p]

avg_tat+=burst[0]
print(wait)
print(tat)
print(avg_wait/n)
print(avg_tat/n)

#2nd
process= [int(x) for x in range(n)]
sorts = zip(process,burst)
newsort = sorted(sorts, key=lambda x: x[1], reverse=True)
process,burst = zip(*newsort)

wait = [0]*n
tat = [0]*n
avg_wait = 0
avg_tat = 0

for p in range(1, n):
    wait[p] = wait[p-1] + burst[p-1]
    tat[p] = wait[p] + burst[p]
    avg_wait+=wait[p]
    avg_tat+=tat[p]

avg_tat+=burst[0]
print(wait)
print(tat)
print(avg_wait/n)
print(avg_tat/n)

#[24,3,3]
#[3,6,7,8]