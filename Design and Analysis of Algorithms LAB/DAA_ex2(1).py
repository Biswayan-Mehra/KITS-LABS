def schedule_tasks(tasks, deadline):
    tasks = sorted(tasks, key=lambda x: (x[1], x[2]), reverse=True)
    schedule = []
    current_time = 0
    total_profit = 0
    for task in tasks:
        if current_time + task[1] <= deadline:
            schedule.append(task[0])
            current_time += task[1]
            total_profit += task[2]
    return schedule, total_profit

num = int(input("Enter the number of tasks: "))
tasks = []
for i in range(num):
    tasks.append(("Task"+str(i+1), int(input("Enter deadline: ")), int(input("Enter profit: "))))
deadline = 10
scheduled_tasks, total_profit = schedule_tasks(tasks, deadline)
print("Scheduled Tasks: ", scheduled_tasks)
print("Total Profit: ", total_profit)

#tasks = [("Task 1", 2, 50), ("Task 2", 1, 30), ("Task 3", 4, 80), ("Task 4", 3, 60), ("Task 5", 2, 40)]