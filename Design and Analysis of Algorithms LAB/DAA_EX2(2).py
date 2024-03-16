def schedule_tasks():
    num_tasks = int(input("Enter no. of tasks: "))
    max_deadline = 0
    tasks = []
    deadlines = {}
    for i in range(num_tasks):
        profit = input("Enter profit: ")
        deadline = int(input("Enter deadline: "))
        if (deadline > max_deadline):
            max_deadline = deadline
        tasks.append(int(profit))
        deadlines[int(profit)] = deadline
    tasks.sort(reverse=True)
    timeline = [0] * (max_deadline)
    for x in tasks:
        if (timeline[deadlines[x] - 1] == 0):
            timeline[deadlines[x] - 1] = x
        else:
            decoy_deadline = deadlines[x] - 2
            while (decoy_deadline >= 0):
                if (timeline[decoy_deadline] == 0):
                    timeline[decoy_deadline] = x
                    break
                else:
                    decoy_deadline -= 1      
    print("{Jobs : Deadlines}: ", deadlines)
    print("Sorted Jobs: ", timeline)
    return sum(timeline)

schedule = schedule_tasks()
print("The maximum profit is:",schedule)