"""
Entry point for algo_task program
"""
import re
from algo import TASKS

if __name__ == "__main__":

    # get all subclasses of AlgoInterface
    # and sort them as (int, str)

    tasks = sorted(
        TASKS,
        key=lambda x: (int(re.search("[0-9]+", x.name())[0]), x.name()),
    )

    # Console menu
    print("Choose task from:")
    print("\n".join("\t{}. {}".format(i, task.name()) for i, task in enumerate(tasks, 1)))

    while True:
        # handaling wrong input
        try:
            position = int(input("Execute task (index): ")) - 1
        except ValueError:
            print("Not a valid input")
            continue
        if not 0 <= position < len(tasks):
            print("Index out of range!")
            continue

        # executing algorithm

        Task_to_execute = tasks[position]()
        Task_to_execute.execute()

        # exit condition
        if input("Do you want to continue? (y-yes, ANY_KEY for exit) ").lower() != "y":
            break
