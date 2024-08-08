Features
--------------
Add Task: Allows you to add a task with a specific deadline. The task is stored in a heap, ensuring that the task with the highest deadline is given the highest priority.

Remove Most Urgent Task: Removes the task with the earliest or highest deadline from the heap.

Display Tasks: Shows the list of tasks currently in the heap, ordered by urgency, with the most urgent task displayed first.

Usage
------------
When you run the program, you'll be presented with a menu that offers four options:

Add task: Input a task name and deadline to add the task to the scheduler.

Remove most urgent task: Removes and displays the most urgent task.

Display tasks: Displays all tasks in order of urgency.

Exit: Exits the program.

How It Works
----------------
The task scheduler uses Python's heapq module to manage tasks in a priority queue (heap). 
By storing the negative of the deadlines, we simulate a max-heap in Python. This ensures that the task with the highest deadline (most urgent) is always at the top of the heap.

Requirements
--------------
Python 3.x

Running the Program
------------------------------
To run the program, simply execute the script. You will be prompted to interact with the task scheduler through a simple text-based menu.
