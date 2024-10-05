import time
import sys

def schedule_tasks(task_hierarchy):
    def sort_tasks(tasks):
        return sorted(tasks, key=lambda x: x.get('priority', 0), reverse=True)

    if not task_hierarchy:
        return []

    scheduled_tasks = []
    sorted_tasks = sort_tasks(task_hierarchy)

    for task in sorted_tasks:
        scheduled_tasks.append(task['name'])
        
        if 'subtasks' in task and task['subtasks']:
            scheduled_tasks.extend(schedule_tasks(task['subtasks']))

    return scheduled_tasks

def calculate_memory_size(obj):
    if isinstance(obj, dict):
        return sys.getsizeof(obj) + sum(calculate_memory_size(v) for v in obj.values())
    elif isinstance(obj, list):
        return sys.getsizeof(obj) + sum(calculate_memory_size(i) for i in obj)
    else:
        return sys.getsizeof(obj)

task_hierarchy = [
    {
        "id": 1,
        "name": "cleaning the house",
        "subtasks": [
            {
                "id": 2,
                "name": "cleaning the bed room",
                "priority": 2,
                "subtasks": []
            },
            {
                "id": 3,
                "name": "cleaning the kitchen",
                "priority": 1,
                "subtasks": []
            }
        ],
        "priority": 3
    },
    {
        "id": 4,
        "name": "doctor appointment",
        "subtasks": [],
        "priority": 1
    }
]

start_time = time.time()

scheduled = schedule_tasks(task_hierarchy)

end_time = time.time()
execution_time = end_time - start_time

memory_size = calculate_memory_size(task_hierarchy)

print("Scheduled Tasks:")
for task in scheduled:
    print(task)

print(f"Execution Time: {execution_time:.6f} seconds")
print(f"Memory Size of Task Hierarchy: {memory_size} bytes")
