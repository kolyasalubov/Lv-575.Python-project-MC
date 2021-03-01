from abc import ABC, abstractmethod, abstractstaticmethod
from math import sqrt, gcd, ceil
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
        return "87"


class task_108(AlgoInterface):

    def execute(self) -> None:
        n = int(input('Input: '))
        print('r = ', floor(log(n, 2)) + 1)
        print('Result (2^r) = ', 2 ** (floor(log(n, 2)) + 1))

        return None

    @staticmethod
    def name() -> str:
        return "108"


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
        # Todo
        return "555"


class task_88c(AlgoInterface):

    def execute(self) -> None:
        ''' switches first and last digit '''
        n = input()
        print(n[-1] + n[1:-1] + n[0])
        return None

    @staticmethod
    def name() -> str:
        return "88в"


class task_88d(AlgoInterface):

    def execute(self) -> None:
        ''' inserts digit 1 on the start and last positions '''
        n = input()
        print('1' + n + '1')
        return None

    @staticmethod
    def name() -> str:
        return "88г"

class task_332(AlgoInterface):

    def execute(self) -> None:
        ''' returns coeficients of distribution of a natural number into 4 squares '''
        n = int(input())
        res, tmp_res = 0, 0
        x, y, z, t = 0, 0, 0, 0
        while res < n :
            res = x ** 2
            x += 1
        if x == 0 : x = 0
        elif x == 2 : x = 1
        else : x -= 2
        res = x ** 2
        print('x = ' + str(x))
        tmp_res += res
        # print(tmp_res)
        # print()

        if tmp_res != n :
            while res < n :
                res = tmp_res + y ** 2
                y += 1
        if y == 0 : y = 0
        elif y == 2 : y = 1
        else : y -= 2
        res = y ** 2
        print('y = ' + str(y))
        tmp_res += res
        # print(tmp_res)
        # print()

        if tmp_res != n:
            while res < n :
                res = tmp_res + z ** 2
                z += 1

        if z == 0 : z = 0
        elif z == 2 : z = 1
        else : z -= 2
        res = z ** 2
        print('z = ' + str(z))
        tmp_res += res
        # print(tmp_res)
        # print()

        if tmp_res != n :
            while res < n :
                res = tmp_res + t ** 2
                t += 1

        if t == 0 : t = 0
        elif t == 2 : t = 1
        else : t -= 2
        res = t ** 2
        tmp_res += res
        print('t = ' + str(t))
        #print(tmp_res)
        return None

    @staticmethod
    def name() -> str:
        return "332"


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

        return None

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