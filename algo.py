from abc import ABC, abstractmethod, abstractstaticmethod
from math import sqrt, gcd, floor, log, ceil, factorial
from typing import List, Tuple
import re


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


class Task178d(AlgoInterface):
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


class Task88a(AlgoInterface):

    def execute(self) -> None:
        n = input("Enter number n:")
        if type(n) == int and n > 0:
            if str(n * n).find("3") != -1:
                print("YES")
            else:
                print("NO")
            return None
        else:
            print("Wrong type of a number")

    @staticmethod
    def name() -> str:
        return "88a"


class Task178b(AlgoInterface):

    def execute(self) -> None:
        try:
            n = int(input('Enter the size of sequence:'))
        except ValueError:
            print("ValueError exception thrown")
            return None
        print('Enter the elements of sequence:')
        try:
            sequence = [int(input()) for i in range(n)]
        except ValueError:
            print("ValueError exception thrown")
            return None

        counter = 0
        for element in sequence:
            if element % 3 == 0 and element % 5 != 0:
                counter += 1

        print('Result:', counter)

        return None

    @staticmethod
    def name() -> str:
        return "178 б)"


class Task107(AlgoInterface):

    def execute(self) -> None:
        """
        Return  the largest integer k, at which 4 ^k < m

        :return: None
        """
        try:
            m = int(input("Enter m: "))
        except ValueError:
            print("M must be integer")
            raise

        if m < 0:
            raise ValueError("M can`t be negative")

        k = log(m, 4)

        k = int(k) if k != int(k) or k == 0 else int(k) - 1
        print("k =", k)
        print("4 ^", k, " < ", m)

        return None

    @staticmethod
    def name() -> str:
        return "107"


class Task243a(AlgoInterface):

    @staticmethod
    def check_squares_existence(n: int) -> tuple:
        """
        Check if there are two numbers (x, y) that x ^2 + y ^2 = n

        :param n: int
        :return: tuple
        """
        sq = sqrt(n)
        for y in range(1, int(sqrt(n)) + 1):
            # n = x^2 + y^2
            # x^2 = sqrt(n)^2 - y^2 = (sq + y) * (sq - y)
            x = sqrt((sq + y) * (sq - y))
            if int(x) == x:
                if int(x) >= y:
                    return int(x), y

            elif abs(round(x) - x) < 0.0000000001:  # prevention of calculation errors
                if round(x) >= y:
                    return round(x), y

        return ()

    def execute(self) -> None:
        """
        Processes user behavior and displays results

        :return: None
        """
        try:
            n = int(input("Enter n: "))
        except ValueError:
            raise ValueError("M must be integer")

        if n < 0:
            raise ValueError("M can`t be negative")

        exists = self.check_squares_existence(n)
        if exists:
            print("{x1} ^2 + {x2} ^2 = {N}".format(x1=exists[0], x2=exists[1], N=n))
        else:
            print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 а)"


class Task178c(AlgoInterface):

    def execute(self) -> None:
        try:
            n = int(input('Enter the size of array:'))
        except ValueError:
            print("ValueError exception thrown")
            return None
        print('Enter the elements of sequence:')
        try:
            sequence = [int(input()) for i in range(n)]
        except ValueError:
            print("ValueError exception thrown")
            return None

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


class Task86a(AlgoInterface):

    def execute(self) -> None:
        ''' input natural number N \n
        find amount of its digits '''

        if not (number := input("Enter number N: ")).isdigit():
            print("Wrong input!")
            return None
        # number must be natural
        print(len(number))
        return None

    @staticmethod
    def name() -> str:
        return "86 a)"


class Task554(AlgoInterface):

    def pythagorean(self, num):
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

    def execute(self) -> None:
        """
        Finds triples using Euclid's formula
        (Modified to print not only primitive triples)
        """
        try:
            num = int(input('Enter the number:')) + 1
        except ValueError:
            print("ValueError exception thrown")
            return None
        self.pythagorean(num)
        return None

    @staticmethod
    def name() -> str:
        return "554"


class Task87(AlgoInterface):

    def execute(self) -> None:
        print("Enter n and m:")
        try:
            n, m = input().split()
        except ValueError:
            print("Please enter the second value")
            return None
        if not n.isdigit() or not m.isdigit():
            print("You've entered not natural number")
            return None
        sum, quantity = 0, int(m)
        len_of_number = len(n)
        if quantity > len_of_number:
            print("m must be less than number of digits n")
        else:
            for i in range(quantity):
                sum += int(n[len_of_number - i - 1])
            print("The sum of the last {} digits of number {} is".format(quantity, n), sum)

        return None

    @staticmethod
    def name() -> str:
        return "87"


class Task86b(AlgoInterface):

    def execute(self) -> None:
        ''' input natural number N \n
         find sum of its digits '''
        if not (number := input("Enter number N: ")).isdigit():
            print("Wrong input!")
            return None

        sum_ = sum(map(int, list(number)))
        print(sum_)
        return None

    @staticmethod
    def name() -> str:
        return "86 б)"


class Task330(AlgoInterface):

    @staticmethod
    def _get_deviders(numb):
        # complexity O(sqrt(numb))

        # using set to avoid duplicates of deviders
        deviders = {1}
        # starting from 2 because 1 is always devider of natural number
        for i in range(2, int(numb ** 0.5) + 2):
            if numb % i == 0:
                deviders.add(numb / i)
                deviders.add(i)
        return deviders

    def execute(self) -> None:
        ''' input natural number N \n
            find all "ideal" numbers that is less than N \n

            "ideal" - number the sum of witch deviders(without the number itself)
            is equal to the number'''

        number = int(input("Enter number N: "))

        # general complixity of print all "ideal" numbers till number N
        # O(n*sqrt(n)) <==> O(n^(3/2))
        for i in range(2, number):
            if sum(self._get_deviders(i)) == i:
                print(i)

        # alternative form (cons: print all values after forloop ends)
        # print(*(i for i in range(2, number)  if sum(get_deviders(i)) == i ))

        return None

    @staticmethod
    def name() -> str:
        return "330"


class Task108(AlgoInterface):
    # input number n, we should find the least number, that is bigger than n and is degree of number 2
    # complexity - O(1)

    def execute(self) -> None:
        try:
            n = int(input('Input natural number: '))
            print('r = ', floor(log(n, 2)) + 1)
            print('Result (2^r) = ', 2 ** (floor(log(n, 2)) + 1))
        except ValueError:
            print("Wrong input!")
        return None

    @staticmethod
    def name() -> str:
        return "108"


class Task226(AlgoInterface):

    def execute(self) -> None:
        import math

        def lcm(a, b):
            return (a * b) // math.gcd(a, b)

        print("Enter n and m:")
        try:
            n, m = input().split()
        except ValueError:
            print("Please enter the second value")
        if not n.isdigit() or not m.isdigit():
            print("You've entered not natural number")
            return None

        n, m = int(n), int(m)
        lcm = lcm(n, m)
        result = [i for i in range(lcm, n * m, lcm)]
        if result:
            print("All common multiples less then {}: ".format(n * m), end='')
            for el in result:
                print(el, end=', ')
            print()
        else:
            print("There are no such values")

        return None

    @staticmethod
    def name() -> str:
        # Todo
        return "226"


class Task178_e(AlgoInterface):

    def execute(self) -> None:
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


class Task559(AlgoInterface):

    def execute(self) -> None:

        from math import log

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
            return set([2 ** i - 1 for i in range(2, int(log(n + 1, 2)) + 1)])

        print("Enter n:")
        n = input()
        if n.isdigit():
            n = int(n)
            result = list(eratosthenes(n).intersection(
                mersen_numbers(n)))  # Mersenne primes
            print("Mersenne primes less than {}:".format(n), sorted(result))
        else:
            print("You've entered not natural number")

        return None

    @staticmethod
    def name() -> str:
        return "559"


class Task243b(AlgoInterface):

    @staticmethod
    def find_all_squares(n: int) -> List[Tuple[int, int]]:
        """
        Find all of the two numbers (x, y) that x ^2 + y ^2 = n

        :param n: int
        :return:  list[tuple[int, int]]
        """

        sq = sqrt(n)
        squares_numbers = []

        for y in range(1, int(sqrt(n)) + 1):
            # n = x^2 + y^2
            # x^2 = sqrt(n)^2 - y^2 = (sq + y) * (sq - y)
            x = sqrt((sq + y) * (sq - y))
            if int(x) == x:
                if int(x) >= y:
                    squares_numbers.append((int(x), y))

            elif abs(round(x) - x) < 0.0000000001:  # prevention of calculation errors
                if round(x) >= y:
                    squares_numbers.append((round(x), y))

        return squares_numbers

    def execute(self) -> None:
        """
            Processes user behavior and displays results

            :return: None
        """
        try:
            n = int(input("Enter n: "))
        except ValueError:
            raise ValueError("M must be integer")

        if n < 0:
            raise ValueError("M can`t be negative")

        all_squares = self.find_all_squares(n)

        if all_squares:
            for pair in all_squares:
                print("{x1} ^2 + {x2} ^2 = {N}".format(x1=pair[0], x2=pair[1], N=n))
        else:
            print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 б)"


class Task555(AlgoInterface):

    @staticmethod
    def build_pascals_triangle(n: int):
        for i in range(n):
            for j in range(n - i + 1):
                print(end=" ")

            for j in range(i + 1):
                # C**k_n = n!/(k!*(n-r)!)
                print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
            print()

    def execute(self) -> None:
        print("-" * 60)
        print("Task - build first n rows of Pascal's triangle")
        print("-" * 60)
        print("Enter natural number:", end=" ")
        n = int(input())
        self.build_pascals_triangle(n)

        return None

    @staticmethod
    def name() -> str:
        return "555"


class Task88c(AlgoInterface):

    def execute(self) -> None:
        ''' switches first and last digits of the number '''
        n = input("Enter N to switch first and last digits of the number : ")
        print(n[-1] + n[1:-1] + n[0])
        return None

    @staticmethod
    def name() -> str:
        return "88в"


class Task88d(AlgoInterface):

    def execute(self) -> None:
        ''' inserts digit 1 on the start and last positions '''
        n = input("Enter N to insert digit 1 on the start and last positions of the number : ")
        print('1' + n + '1')
        return None

    @staticmethod
    def name() -> str:
        return "88г"


class Task332(AlgoInterface):

    def execute(self) -> None:
        ''' returns coeficients of distribution of a natural number into 4 squares '''

        n = int(input("Enter N to find Lagrange decomposition coefficients : "))
        res, tmp_res, counter = 0, 0, 0
        xs = [0, 0, 0, 0]
        for i in xs:
            counter += 1
            if tmp_res != n:
                while res < n:
                    res = tmp_res + i ** 2
                    i += 1
                if i == 0:
                    i = 0
                elif i == 2:
                    i = 1
                else:
                    i -= 2
                res = i ** 2
                print('x' + str(counter) + ' = ' + str(i))
                tmp_res += res
            else:
                print('x' + str(counter) + ' = 0')

        return None

    @staticmethod
    def name() -> str:
        return "332"


# for task 331. Checking whether we can represent given number as a sum of 3 number in power 2
# complexity ~ O(n)
def check(number, task):
    exist = False
    for i in range(1, int(ceil(sqrt(number)))):
        for j in range(1, int(ceil(sqrt(number - i ** 2)))):
            third = number - i ** 2 - j ** 2
            if third > 0 and float(third ** (1 / 2)) % 1 == 0:
                print(i, "^2 + ", j, "^2 + ", int(third ** (1 / 2)), "^2")
                exist = True
                if task == "331 a":
                    return True
    return exist


class Task331a(AlgoInterface):

    def execute(self) -> None:
        try:
            n = int(input('Input: '))
            if not check(n, "331 a"):
                print("It`s impossible!")
        except ValueError:
            print("Wrong input!")
        return None

    @staticmethod
    def name() -> str:
        return "331 а)"


class Task331b(AlgoInterface):

    def execute(self) -> None:
        try:
            n = int(input('Input: '))
            if not check(n, "331 b"):
                print("It`s impossible!")
        except ValueError:
            print("Wrong input!")
        return None

    @staticmethod
    def name() -> str:
        return "331 б)"


class Task88b(AlgoInterface):

    def execute(self) -> None:
        n = input("Enter number n:")
        print(n[::-1])
        return None

    @staticmethod
    def name() -> str:
        return "88b"


class Task322(AlgoInterface):

    def execute(self) -> None:
        def divisor(number):
            sum_of_divisors = 0
            for i in range(1, ceil(sqrt(number))):
                if i * i == number:
                    sum += i
                    break
                if number % i == 0:
                    sum_of_divisors += i
                    sum_of_divisors += number / i
            return sum_of_divisors

        maximal = 0
        number_with_maximal_sum = 0
        for i in range(1, 10001):
            if divisor(i) > maximal:
                maximal = divisor(i)
                number_with_maximal_sum = i
        print("Number with maximal sum of divisors is ", number_with_maximal_sum)
        return None

    @staticmethod
    def name() -> str:
        return "322"


if __name__ == "__main__":

    # get all subclasses of AlgoInterface
    tasks = sorted(AlgoInterface.__subclasses__(),
                   key=lambda x: int(re.search('[0-9]+', x.name())[0]))

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
        Taskto_execute = tasks[position]()
        Taskto_execute.execute()

        # exit condition
        if input("Do you want to continue? (y-yes, ANY_KEY for exit) ").lower() != 'y':
            break
