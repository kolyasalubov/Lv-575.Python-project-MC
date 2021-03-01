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

    @staticmethod
    def name() -> str:
        return "108"

class task_87(AlgoInterface):

    def execute(self) -> None:
        print("Enter n and m:")
        try:
            string_n, m = input().split()
            if string_n.isdigit() and m.isdigit():
                sum, quantity = 0, int(m)
                if len(string_n) > quantity:
                    for digit in list(string_n[:len(string_n) - int(quantity) - 1:-1]):
                        sum += int(digit)
                    print("The sum of the last {} digits of number {} is".format(quantity, string_n), sum)
                elif len(string_n) == quantity:
                    for digit in string_n:
                        sum += int(digit)
                    print("The sum of the last {} digits of number {} is".format(quantity, string_n), sum)
                else:
                    print("m must be less than number of digits n")
            else:
                print("You've entered not natural number")
        except ValueError:
            print("Please enter the second value")
        return None

    @staticmethod
    def name() -> str:
        # Todo
        return "87"


class task_226(AlgoInterface):

    def execute(self) -> None:
        import math

        def lcm(a, b):
            return (a * b) // math.gcd(a, b)

        result = []
        print("Enter n and m:")
        try:
            n, m = input().split()
            if n.isdigit() and m.isdigit():
                n, m = int(n), int(m)
                lcm = lcm(n, m)
                for i in range(lcm, n * m, lcm):
                    result.append(i)
                if not len(result):
                    print("There are no such values")
                else:
                    print("All common multiples less then {}: ".format(n * m), end='')
                    for el in result:
                        print(el, end=', ')
                    print()
            else:
                print("You've entered not natural number")
        except ValueError:
            print("Please enter the second value")
        return None

    @staticmethod
    def name() -> str:
        # Todo
        return "226"


class task_559(AlgoInterface):

    def execute(self) -> None:

        import math

        # Eratosthene's sieve to get primes
        def eratosthenes(n):
            sieve = list(range(n + 1))
            sieve[1] = 0
            for i in sieve:
                if i > 1:
                    for j in range(i + i, len(sieve), i):
                        sieve[j] = 0
            sieve_without_nulls = set([x for x in sieve if x != 0])
            return set(sieve_without_nulls)

        # Mersenne numbers
        def mersen_numbers(n):
            return set([2 ** i - 1 for i in range(2, int(math.log(n + 1, 2)) + 1)])

        print("Enter n:")
        n = input()
        if n.isdigit():
            n = int(n)
            result = list(eratosthenes(n).intersection(mersen_numbers(n)))  # Mersenne primes
            print("Mersenne primes less than {}:".format(n), sorted(result))
        else:
            print("You've entered not natural number")
        return None

    @staticmethod
    def name() -> str:
         return "559"


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
