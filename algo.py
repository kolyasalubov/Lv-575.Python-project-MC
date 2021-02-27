from abc import ABC, abstractmethod, abstractstaticmethod
from math import sqrt, gcd, ceil


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


class task_178b(AlgoInterface):

    def execute(self) -> None:
        n = int(input('Enter the size of sequence:'))
        print('Enter the elements of sequence:')
        sequence = [int(input()) for i in range(n)]

        counter = 0
        for element in sequence:
            if element % 3 == 0 and element % 5 != 0:
                counter += 1

        print('Result:', counter)
        return None

    @staticmethod
    def name() -> str:
        return "178 б)"


class task_178c(AlgoInterface):

    def execute(self) -> None:
        n = int(input('Enter the size of array:'))
        print('Enter the elements of sequence:')
        sequence = [int(input()) for i in range(n)]

        counter = 0
        for element in sequence:
            root = sqrt(element)
            if root ** 2 == element and root % 2 == 0:
                counter += 1

        print('Result:', counter)
        return None

    @staticmethod
    def name() -> str:
        return "178 в)"


class task_554(AlgoInterface):

    def execute(self) -> None:
        """
        Finds triples using Euclid's formula
        (Modified to print not only primitive triples)
        """
        num = int(input('Enter the number:')) + 1
        for m in range(2, ceil(sqrt(num))):
            for n in range(1, m):
                # m and n are coprime and not both odd
                if gcd(m, n) == 1 and (m - n) % 2 and (m ** 2 + n ** 2) < num:
                    a = m ** 2 - n ** 2
                    b = 2 * m * n
                    c = m ** 2 + n ** 2
                    if a > b:
                        a, b = b, a
                    k = 1
                    while k * c < num:
                        print(k * a, k * b, k * c)
                        k += 1
        return None

    @staticmethod
    def name() -> str:
        return "554"


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
