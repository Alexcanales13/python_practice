# ============================================================
#              STUDENT TO-DO LIST PROJECT
#                    COMPLETE SOLUTION
# ============================================================


# ------------------------------------------------------------
# STARTING DATA
# ------------------------------------------------------------

tasks = [
    "Math homework",
    "Walk the dog",
    "Study Python"
]

completed_tasks = []

print("=================================")
print("       WELCOME TO TO-DO LIST")
print("=================================")

student_name = input("What is your name? ")

print(f"\nWelcome, {student_name}!")


# ------------------------------------------------------------
# MAIN PROGRAM LOOP
# ------------------------------------------------------------

while True:

    print("\n=================================")
    print("          MY TO-DO LIST")
    print("=================================")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Complete a task")
    print("5. Search for a task")
    print("6. Count tasks")
    print("7. View completed tasks")
    print("8. Clear completed tasks")
    print("9. Quit")
    print("=================================")

    choice = input("Choose an option: ")


    # --------------------------------------------------------
    # OPTION 1 - ADD A TASK
    # --------------------------------------------------------

    if choice == "1":

        new_task = input("\nWhat task do you want to add? ")

        # Prevent blank tasks
        if new_task == "":
            print("You cannot add an empty task.")

        # Prevent duplicate tasks
        elif new_task in tasks:
            print("That task is already on your list.")

        else:
            tasks.append(new_task)

            print(f'"{new_task}" was added!')


    # --------------------------------------------------------
    # OPTION 2 - VIEW TASKS
    # --------------------------------------------------------

    elif choice == "2":

        print("\n=================================")
        print("             TASKS")
        print("=================================")

        if len(tasks) == 0:
            print("Your task list is empty!")

        else:

            task_number = 1

            for task in tasks:

                if task in completed_tasks:
                    print(f"{task_number}. {task} - DONE")

                else:
                    print(f"{task_number}. {task}")

                task_number += 1


    # --------------------------------------------------------
    # OPTION 3 - REMOVE A TASK
    # --------------------------------------------------------

    elif choice == "3":

        if len(tasks) == 0:
            print("\nThere are no tasks to remove.")

        else:

            print("\nWhich task do you want to remove?")

            for task in tasks:
                print("-", task)

            task_to_remove = input("\nEnter the task: ")

            if task_to_remove in tasks:

                tasks.remove(task_to_remove)

                # Also remove it from completed tasks
                if task_to_remove in completed_tasks:
                    completed_tasks.remove(task_to_remove)

                print("Task removed!")

            else:
                print("That task isn't on your list.")


    # --------------------------------------------------------
    # OPTION 4 - COMPLETE A TASK
    # --------------------------------------------------------

    elif choice == "4":

        if len(tasks) == 0:
            print("\nThere are no tasks to complete.")

        else:

            print("\nYour tasks:")

            for task in tasks:
                print("-", task)

            task_to_complete = input(
                "\nWhich task did you complete? "
            )

            if task_to_complete in tasks:

                if task_to_complete in completed_tasks:
                    print("That task is already completed.")

                else:
                    completed_tasks.append(task_to_complete)

                    print("Task marked as completed!")

            else:
                print("That task isn't on your list.")


    # --------------------------------------------------------
    # OPTION 5 - SEARCH FOR A TASK
    # --------------------------------------------------------

    elif choice == "5":

        search_task = input("\nWhat task are you looking for? ")

        found = False

        for task in tasks:

            if search_task.lower() == task.lower():

                found = True

                print(f'Task found: "{task}"')

        if found == False:
            print("Task not found.")


    # --------------------------------------------------------
    # OPTION 6 - COUNT TASKS
    # --------------------------------------------------------

    elif choice == "6":

        number_of_tasks = len(tasks)

        print(
            f"\nYou currently have "
            f"{number_of_tasks} tasks."
        )


    # --------------------------------------------------------
    # OPTION 7 - VIEW COMPLETED TASKS
    # --------------------------------------------------------

    elif choice == "7":

        print("\n=================================")
        print("       COMPLETED TASKS")
        print("=================================")

        if len(completed_tasks) == 0:

            print("You haven't completed any tasks yet.")

        else:

            for task in completed_tasks:
                print(f"✓ {task}")


    # --------------------------------------------------------
    # OPTION 8 - CLEAR COMPLETED TASKS
    # --------------------------------------------------------

    elif choice == "8":

        if len(completed_tasks) == 0:

            print("\nThere are no completed tasks to clear.")

        else:

            # Create a new list containing only tasks
            # that have NOT been completed.
            tasks = [
                task
                for task in tasks
                if task not in completed_tasks
            ]

            completed_tasks = []

            print("Completed tasks have been cleared!")


    # --------------------------------------------------------
    # OPTION 9 - QUIT
    # --------------------------------------------------------

    elif choice == "9":

        print("\n=================================")
        print("       THANK YOU FOR USING")
        print("          TO-DO LIST!")
        print("=================================")

        print(f"Goodbye, {student_name}!")

        break


    # --------------------------------------------------------
    # INVALID OPTION
    # --------------------------------------------------------

    else:

        print("\nInvalid option.")
        print("Please choose a number from the menu.")


# ============================================================
#                    PROGRAM FINISHED
# ============================================================

