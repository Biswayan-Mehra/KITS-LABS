def schedule_tasks():
    num_tasks = int(input("Enter the number of tasks: "))
    max_deadline = 0
    tasks = []
    deadlines = {}
    for i in range(num_tasks):
        profit = input("Enter the profit of task ")
        deadline = int(input("Enter deadline for task: "))
        if (deadline > max_deadline):
            max_deadline = deadline
        tasks.append(int(profit))
        deadlines[int(profit)] = deadline
    tasks.sort(reverse=True)
    timeline = [0] * (max_deadline)
    for x in tasks:
        varifier = deadlines[x]
        if (timeline[varifier - 1] == 0):
            timeline[varifier - 1] = x
        else:
            decoy_deadline = deadlines[x] - 2
            while (decoy_deadline >= 0):
                if (timeline[decoy_deadline] == 0):
                    timeline[decoy_deadline] = x
                else:
                    decoy_deadline -= 1
    print("the deadlinesof the corresponding jobs", deadlines)
    print("the jobs aranged based on the values ", timeline)
    print("the maximum profit which you can get by doing ",timeline," jobs is:")
    return sum(timeline)
schedule = schedule_tasks()
print(schedule)