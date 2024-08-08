import heapq

class TaskScheduler:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_name, deadline):
        # Using negative deadline to simulate max-heap with heapq (which is a min-heap by default)
        heapq.heappush(self.tasks, (-deadline, task_name))
        print(f"Task '{task_name}' added with deadline {deadline}")
    
    def remove_task(self):
        if self.tasks:
            deadline, task_name = heapq.heappop(self.tasks)
            print(f"Task '{task_name}' with deadline {-deadline} removed")
        else:
            print("No tasks to remove")
    
    def display_tasks(self):
        if self.tasks:
            print("Tasks in order of urgency (most urgent first):")
            # Display tasks in max-heap order without sorting
            for deadline, task_name in self.tasks:
                print(f"Task: {task_name}, Deadline: {-deadline}")
        else:
            print("No tasks to display")

def main():
    scheduler = TaskScheduler()
    
    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add task")
        print("2. Remove most urgent task")
        print("3. Display tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task_name = input("Enter task name: ")
            deadline = int(input("Enter task deadline (as an integer): "))
            scheduler.add_task(task_name, deadline)
        elif choice == '2':
            scheduler.remove_task()
        elif choice == '3':
            scheduler.display_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
