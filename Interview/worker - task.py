"""
Here at Scale, customers send us collections of data over the course of each week. Let’s call each unit of data a “task.” We send these tasks to our work force for labeling. When these tasks are labeled, we send them back to the customer.

Each task goes through three sequential stages:

L0 → L1 → L2

Workers are given task stages to work on.
A task is only “complete” when it reaches the L2 stage and work is finished on the L2 stage

Notes: 
- There is a 1:1 mapping between task stages and workers working on a task stage. (i.e  Task X L1 can only have 1 worker at one time, that worker cannot be working on anything else)
- A worker can only work on a task if the worker has never worked on that task before. 
- For now, assume each worker takes 1 min. We may change this later.
- Tasks should be greedily assigned to any free workers who can work on the task.

*Write a system that simulates the environment and runs until all tasks are completed. Do not worry about runtime, we are looking for correctness.
On every timestamp where activity happens:
Print out the timestamp, and all the activities that happened. (worker assignment/completion).*
*At the end, print out the total number of time taken to complete the simulation. *

*Sample input 1:* 
tasks = [Task('A')]
workers = [Worker('X'), Worker('Y'), Worker('Z')]

*Sample output 1:*
0
Assigning X to Task A for L0
1
Worker X finished Task A for L0
Assigning Y to Task A for L1
2
Worker Y finished Task A for L1
Assigning Z to Task A for L2
3
Worker Z finished Task A for L2
Total time taken: 3 min


*Sample input 2:* 
tasks = [Task('A'), Task('B')]
workers = [Worker('X'), Worker('Y'), Worker('Z')]

*Sample output 2 (one possible correct answer):* 
0
Assigning X to Task A for L0
Assigning Y to Task B for L0
1
Worker X finished Task A for L0
Worker Y finished Task B for L0 
Assigning Z to Task A for L1
Assigning X to Task B for L1
2
Worker Z finished Task A for L1
Worker X finished Task B for L1 
Assigning Y to Task A for L2
Assigning Z to Task B for L2
3
Worker Y finished Task A for L2
Worker Z finished Task B for L2
Total time taken: 3 min

*Sample output 2 (another possible correct answer):* 
0
Assigning X to Task A for L0
Assigning Y to Task B for L0
1
Worker X finished Task A for L0
Worker Y finished Task B for L0 
Assigning Y to Task A for L1
Assigning X to Task B for L1
2
Worker Y finished Task A for L1
Worker X finished Task B for L1 
Assigning Z to Task A for L2
3
Worker Z finished Task A for L2
Assigning Z to Task B for L2
4
Worker Z finished Task B for L2
Total time taken: 4 min

"""

class Task:
    def __init__(self, id, stage=0):
        self.id = id
        self.stage = stage
        self.worker = None
        
        
class Worker:
    def __init__(self, id, available_time=0):
        self.id = id
        self.available_time = available_time
        self.tasks = []
    
current_time = 0    
    
tasks = [Task('A'), Task('B')]
workers = [Worker('X'), Worker('Y'), Worker('Z')]

while tasks:
    print(current_time)
    current_task = list(tasks)
    for task in current_task:
        if task.worker:
            print(f'Worker {task.worker.id} finished Task {task.id} for L{task.stage - 1}')
            task.worker = None
        
        to_assign = None

        # while not to_assign:
        for worker in workers:
            # print(current_time, worker.id, worker.tasks, worker.available_time)
            if task not in worker.tasks and worker.available_time <= current_time:
                to_assign = worker
                break

        if to_assign: 
            print(f'Assining {to_assign.id} to Task {task.id} for L{task.stage}')
            to_assign.tasks.append(task)
            to_assign.available_time = current_time + 1
            task.worker = to_assign
            task.stage += 1
            
            

            if task.stage == 3:
                tasks.remove(task)
                
    current_time += 1

print(current_time)
