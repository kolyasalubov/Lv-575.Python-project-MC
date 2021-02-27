from abc import ABC, abstractmethod, abstractstaticmethod
from math import log, sqrt


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


class task_107(AlgoInterface):

    def execute(self) -> None:
        m = int(input("Enter m: "))
        k = log(m, 4)

        print("k =", int(k) if k != int(k) or k == 0 else int(k) - 1)

        return None

    @staticmethod
    def name() -> str:
        return "107"


class task_243a(AlgoInterface):

    def execute(self) -> None:
        n = int(input("Enter n: "))


        sq = sqrt(n)
        for y in range(1, int(sqrt(n)) + 1):
            # n = x^2 + y^2
            # x^2 = sqrt(n)^2 - y^2 = (sq + y) * (sq - y)
            x = sqrt((sq + y) * (sq - y))

            if int(x) == x:
                if int(x) >= y:
                    print(int(x), y)
                    return None

            elif abs(round(x) - x) < 0.0000000001:  # prevention of calculation errors
                if round(x) >= y:
                    print(round(x), y)
                    return None

        print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 а)"


class task_243b(AlgoInterface):

    def execute(self) -> None:
        n = int(input("Enter n: "))

        is_numbers = False
        sq = sqrt(n)
        for y in range(1, int(sqrt(n)) + 1):
            # n = x^2 + y^2
            # x^2 = sqrt(n)^2 - y^2 = (sq + y) * (sq - y)
            x = sqrt((sq + y) * (sq - y))

            if int(x) == x:
                if int(x) >= y:
                    print(int(x), y)
                    is_numbers = True

            elif abs(round(x) - x) < 0.0000000001:  # prevention of calculation errors
                if round(x) >= y:
                    print(round(x), y)
                    is_numbers = True

        if not is_numbers:
            print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 б)"


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
