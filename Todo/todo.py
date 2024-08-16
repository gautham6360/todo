class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            print()

    def run(self):
        while True:
            print("\nOptions: ")
            print("1. Add a task")
            print("2. Delete a task")
            print("3. View all tasks")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
