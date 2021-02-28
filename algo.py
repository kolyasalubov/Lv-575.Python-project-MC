from abc import ABC, abstractmethod, abstractstaticmethod


class AlgoInterface(ABC):
    # interface for algo tasks
    # subclasees must be only algo tasks

    @abstractmethod
    def execute(self) -> None:
        # implement your algo task here
        pass

    @abstractstaticmethod
    def name() -> str:
        # return name of task
        # user representation
        pass


class task_178_d(AlgoInterface):

    def execute(self) -> None:
        print("-" * 60)
        print("Task - find amount of elements, which satisfy the condition\nAk < (Ak-1 + Ak+1) / 2.")
        print("-" * 60)
        print("Enter sequence of integer numbers by ' ':")
        sequence = [int(i) for i in input().split(' ')]
        result = 0
        for i in range(1, len(sequence) - 1):
            if sequence[i] < (sequence[i - 1] + sequence[i + 1]) / 2:
                result += 1
        print("Result:", result)
        return None

    @staticmethod
    def name() -> str:
        return "178 d)"


class task_178_e(AlgoInterface):

    def execute(self) -> None:
        import math
        print("-" * 60)
        print("Task - find amount of elements, which satisfy the condition\n2**k < Ak < k!")
        print("-" * 60)
        print("Enter sequence of integer numbers by ' ':")
        sequence = [int(i) for i in input().split(' ')]
        result = 0
        for i in range(len(sequence)):
            if 2 ** i < sequence[i] and sequence[i] > math.factorial(i):
                result += 1
        print("Result:", result)
        return None

    @staticmethod
    def name() -> str:
        return "178 e)"


class task_555(AlgoInterface):

    def execute(self) -> None:
        from math import factorial
        print("-" * 60)
        print("Task - build first n rows of Pascal's triangle")
        print("-" * 60)
        print("Enter natural number:", end=" ")
        n = int(input())
        for i in range(n):
            for j in range(n - i + 1):
                print(end=" ")

            for j in range(i + 1):
                # C**k_n = n!/(k!*(n-r)!)
                print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
            print()
        return None

    @staticmethod
    def name() -> str:
        return "555"


if __name__ == "__main__":

    # get all subclasses of AlgoInterface
    tasks = AlgoInterface.__subclasses__()

    # Console menu
    print("Choose task from:")
    print("\n".join('\t{}. {}'.format(i, task.name()) for i,
                    task in enumerate(tasks, 1)))

    while True:
        # handaling wrong input
        try:
            position = int(input("Execute task (index): ")) - 1
            if not (0 <= position < len(tasks)):
                raise IndexError
        except (IndexError, ValueError):
            print("Wrong index!")
            continue

        # executing algorithm
        task_to_execute = tasks[position]()
        task_to_execute.execute()

        # exit condition
        if input("Do you want to continue? (y-yes, ANY_KEY for exit) ").lower() != 'y':
            break
