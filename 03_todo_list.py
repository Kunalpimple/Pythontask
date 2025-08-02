# Initialize an empty list to store tasks
todo_list = []
# Display the menu and loop until user exits
while True:
    print("\n📋 To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append({"task": task, "done": False})
        print("✅ Task added!")

    elif choice == "2":
        if not todo_list:
            print("📭 No tasks to show.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(todo_list, start=1):
                status = "✔️ Done" if t["done"] else "❌ Not Done"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        if not todo_list:
            print("📭 No tasks to mark.")
        else:
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t['task']}")
            index = int(input("Enter the task number to mark as done: "))
            if 1 <= index <= len(todo_list):
                todo_list[index - 1]["done"] = True
                print("✔️ Task marked as done!")
            else:
                print("⚠️ Invalid task number.")

    elif choice == "4":
        if not todo_list:
            print("📭 No tasks to remove.")
        else:
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t['task']}")
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f"🗑️ Removed task: {removed['task']}")
            else:
                print("⚠️ Invalid task number.")

    elif choice == "5":
        print("👋 Exiting To-Do List. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number between 1 and 5.")
