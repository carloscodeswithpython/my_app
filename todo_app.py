from functions import get_todos, write_todos
from datetime import datetime

date = datetime.now().strftime("%A %B %d, %Y %I:%M:%S %p")

print(f"It is {date}")

todo_items: list[str] = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todo_items = get_todos()

        todo_items.append(todo + '\n')

        write_todos(todo_items)

    #     | stands for or.
    elif user_action.startswith("show"):
        todo_items = get_todos()

        # stripped_todos = [todo.strip('\n') for todo in todo_items]

        for (index,item) in enumerate(todo_items, start=1):
            item = item.strip('\n')
            print(f"{index}-{item}")

    elif user_action.startswith("edit"):

        try:
            item_number = int((user_action[5:]))
            item_number = item_number - 1

            # showing the item to be edited
            print(todo_items[item_number].rstrip('\n'))

            todo_items = get_todos()


            new_todo = input("Enter the new todo item: ") + '\n'
            todo_items[item_number] = new_todo

            write_todos(todo_items)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        # TODO: Add the following todo_items line later.
        # todo_items = get_todos('todos.txt')
        try:
            completed_number = int((user_action[9:]))
            completed_number = completed_number - 1

            get_todos()
                # printing the list below
            # print(todo_items)

            removed_item  = todo_items[completed_number].rstrip('\n')
            todo_items.pop(completed_number)


            write_todos(todo_items)

            message = "Todo: {0} was removed".format(removed_item)
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue


    elif user_action.startswith("exit"):
        break

    else:
        print("Hey, you entered an unknown command")


print("Bye")