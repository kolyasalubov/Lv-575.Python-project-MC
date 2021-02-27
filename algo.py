from abc import ABC, abstractmethod, abstractstaticmethod
from math import floor, log, ceil, sqrt


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


class task_108 (AlgoInterface):

    def execute(self) -> None:
        n = int(input('Input: '))
        print('r = ', floor(log(n, 2)) + 1)
        print('Result (2^r) = ', 2 ** (floor(log(n, 2)) + 1))
        return None

    @staticmethod
    def name() -> str:
        return "108"

class task_331a (AlgoInterface):

    def execute(self) -> None:

        def check(number):
            for i in range(1, int(ceil(sqrt(number)))):
                for j in range(1, int(ceil(sqrt(number - i ** 2)))):
                    third = number - i ** 2 - j ** 2
                    if third > 0 and float(third ** (1 / 2)) % 1 == 0:
                        print(i, "^2 + ", j, "^2 + ", int(third ** (1 / 2)), "^2")
                        return True
            return False

        n = int(input('Input: '))
        if not check(n):
            print("It`s impossible!")
        return None

    @staticmethod
    def name() -> str:
        return "331 а)"


class task_331b(AlgoInterface):

    def execute(self) -> None:

        def check(number):
            exist = False
            for i in range(1, int(ceil(sqrt(number)))):
                for j in range(1, int(ceil(sqrt(number - i ** 2)))):
                    third = number - i ** 2 - j ** 2
                    if third > 0 and float(third ** (1 / 2)) % 1 == 0:
                        exist = True
                        print(i, "^2 + ", j, "^2 + ", int(third ** (1 / 2)), "^2")
            if not exist:
                return False
            else:
                return True

        n = int(input('Input: '))
        if not check(n):
            print("It`s impossible!")

    @staticmethod
    def name() -> str:
        return "331 б)"


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
