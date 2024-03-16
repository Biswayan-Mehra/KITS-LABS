profits = eval(input("Enter profits: "))
deadlines = eval(input("Enter deadlines: "))
jobs = [x for x in range(1, len(profits)+1)]

jobs, profits, deadlines = zip(*sorted(zip(jobs, profits, deadlines), key=lambda x:x[1], reverse =True))

timeline = [0]*max(deadlines)
maxProfit = 0

for i in range(len(profits)):
    if timeline[deadlines[i]-1] == 0:
        timeline[deadlines[i]-1] = jobs[i]
        maxProfit += profits[i]
    else:
        decoy = deadlines[i]-2
        while decoy >= 0:
            if timeline[decoy] == 0:
                timeline[decoy] = jobs[i]
                maxProfit += profits[i]
                break
            else:
                decoy -= 1
        

print(timeline)
print(maxProfit)

"""
[5,10,15,7,8,9,4]
[1,3,5,4,1,3,2]
"""