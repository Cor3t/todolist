class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def complete_task(self, index):
        if len(self.tasks) == 0:
            print('No Task')
        else:
            self.completed.append(self.tasks[index])
             
    def display_task(self):
        if len(self.tasks) == 0:
            print('No task')
        else:
            for index, task in enumerate(self.tasks, 1):
                badge = '[]' if task in self.completed else '[x]'
                print(f"{index}. {badge} {task}")
                



def main():
    task_manager = ToDoList()

    while True:
        
        print('Welcome to the simple to do list')
        print('1. add a new task')
        print('2. mark a task as completed')
        print('3. display task')
        print('4. exist')
        

        response = input('Enter: ')

        if response == '1':
            task = input('Enter task: ')
            task_manager.add_task(task)
            print('task added successfully')
        elif response == '2':
            index = int(input('Enter index of task: '))
            task_manager.complete_task(index)
        elif response == '3':
            task_manager.display_task()
        elif response == '4':
            break

        print()
        print()

main()