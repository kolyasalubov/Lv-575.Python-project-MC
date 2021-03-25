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

    @abstractstaticmethod
    def main_logic(*args, **kwargs):
        # return name of task
        # user representation
        pass

    @abstractstaticmethod
    def validate_data(*args, **kwargs):
        # return name of task
        # user representation
        pass


class TaskWithOneIntValidationParameter(AlgoInterface):
    @classmethod
    def validate_data(cls, *args, **kwargs):
        input_number, *_ = args
        string = str(input_number).strip()
        if not ((((string.startswith("-") or string.startswith("+")) and string[1:].isdigit())) or string.isdigit()):
            raise TypeError  # raises TypeError if not int

        number = int(input_number)

        if number <= 0:
            raise ValueError  # raises ValueError if not natural
        return number


class InvalidInput(Exception):
    """Custom extension"""


class TaskWithTwoIntValidationParameters(AlgoInterface):
    """Class for validation of two int parameters"""

    @classmethod
    def validate_data(cls, *args, **kwargs):
        input_data, *_ = args
        number, number2 = input_data.split()
        if not number.isdigit() or not number2.isdigit():
            raise TypeError

        return number, number2


class Task178d(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(sequence):
        result = 0
        for i in range(1, len(sequence) - 1):
            if sequence[i] < (sequence[i - 1] + sequence[i + 1]) / 2:
                result += 1
        return result

    def execute(self) -> None:
        print("-" * 60)
        print("Task - find amount of elements, which satisfy the condition\nAk < (Ak-1 + Ak+1) / 2.")
        print("-" * 60)
        n = input("Enter the size of sequence:")
        try:
            n = self.validate_data(n)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print("Enter sequence of integer numbers by one in row:")
        sequence = [int(input()) for i in range(n)]
        for i in range(len(sequence)):
            try:
                sequence[i] = self.validate_data(sequence[i])
            except ValueError:
                print("ValueError exception thrown")
                return None
        print("Result:", self.main_logic(sequence))

        return None

    @staticmethod
    def name() -> str:
        return "178 г)"


class Task88a(TaskWithOneIntValidationParameter):
    """A natural number n is given. Find out whether the digit 3 is included in the record of the number n^2."""

    @staticmethod
    def main_logic(n):
        if type(n) == int and n > 0:
            if str(n * n).find("3") != -1:
                return "YES"
            else:
                return "NO"

    def execute(self) -> None:
        print(self.__doc__)
        n = int(input("Input natural number: "))
        try:
            m = self.validate_data(n)
        except (ValueError, TypeError):
            print("Wrong input number")
            return None
        k = self.main_logic(n)
        print("Is 3 in n^2?", k)
        return None

    @staticmethod
    def name() -> str:
        return "88 a)"


class Task178b(TaskWithOneIntValidationParameter):
    """
    178) Natural numbers n, a1,…, an are given. Define
    number of members ak of the sequence a1,…, an:
    b) multiples of 3 and not multiples of 5;
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        """
        Given natural number n and a list of n elements.
        Find numbers which are multiples of 3 and not multiples of 5
        """
        sequence: list = args[0]
        counter = 0
        for element in sequence:
            if element % 3 == 0 and element % 5 != 0:
                counter += 1
        return counter

    def execute(self) -> None:
        print(self.__doc__)
        size = input("Enter the size of sequence:")
        try:
            size = self.validate_data(size)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print("Enter the elements of sequence:")
        sequence = [input() for _ in range(size)]
        for i in range(len(sequence)):
            try:
                sequence[i] = self.validate_data(sequence[i])
            except ValueError:
                print("ValueError exception thrown")
                return None

        print("Result:", self.main_logic(sequence))

        return None

    @staticmethod
    def name() -> str:
        return "178 б)"


class Task107(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(m: int) -> int:
        """
        Return  the largest integer k, at which 4 ^k < m
        :rtype: object
        """
        k: float = log(m, 4)
        k: int = int(k) if k != int(k) or k == 0 else int(k) - 1
        return k

    def execute(self) -> None:
        """
        Processes user behavior and displays results

        :return: None
        """

        input_data = input("Enter m: ")

        try:
            m = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        k = self.main_logic(m)
        print("k =", k)
        print("4 ^{} < {}".format(k, m))

        return None

    @staticmethod
    def name() -> str:
        return "107"


class Task243a(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(n: int) -> tuple:
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
        input_data = input("Enter n: ")

        try:
            n = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        exists = self.main_logic(n)
        if exists:
            print("{x1} ^2 + {x2} ^2 = {N}".format(x1=exists[0], x2=exists[1], N=n))
        else:
            print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 а)"


class Task178c(TaskWithOneIntValidationParameter):
    """
    178) Natural numbers n, a1,…, an are given. Define
    number of members ak of the sequence a1,…, an:
    c) which are squares of even numbers;
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        """
        Given natural number n and a list of n elements.
        Find numbers which are squares of even numbers.
        """
        sequence: list = args[0]
        counter = 0
        for element in sequence:
            root = sqrt(element)
            if root ** 2 == element and root % 2 == 0:
                counter += 1

        return counter

    def execute(self) -> None:
        print(self.__doc__)
        number = input("Enter the size of sequence:")
        try:
            number = self.validate_data(number)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print("Enter the elements of sequence:")
        sequence = [input() for i in range(number)]
        for i in range(len(sequence)):
            try:
                sequence[i] = self.validate_data(sequence[i])
            except ValueError:
                print("ValueError exception thrown")
                return None

        print("Result:", self.main_logic(sequence))
        return None

    @staticmethod
    def name() -> str:
        return "178 в)"


class Task86a(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(number):
        return len(str(number))

    def execute(self) -> None:
        """input natural number N \n
        find amount of its digits"""
        input_data = input("Enter number: ")

        try:
            number = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        # number must be natural
        print(self.main_logic(number))

        return None

    @staticmethod
    def name() -> str:
        return "86 a)"


class Task554(TaskWithOneIntValidationParameter):
    """
    A natural number n is given. Get all Pythagorean
    triples of natural numbers, each of which does not exceed n, i.e.
    all triples of natural numbers a, b, c such that
    a^2 + b^2 = c^2 (a ≤ b ≤ c ≤ n).
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> list:
        """
        Finds triples less than given natural number n using Euclid's formula
        (Modified to print not only primitive triples)
        """
        num: int = args[0]
        res = []
        for m_var in range(2, ceil(sqrt(num))):
            for n_var in range(1, m_var):
                # m and n are coprime and not both odd
                if gcd(m_var, n_var) == 1 and (m_var - n_var) % 2 and (m_var ** 2 + n_var ** 2) < num:
                    a_var = m_var ** 2 - n_var ** 2
                    b_var = 2 * m_var * n_var
                    c_var = m_var ** 2 + n_var ** 2
                    if a_var > b_var:
                        a_var, b_var = b_var, a_var
                    k_var = 1
                    while k_var * c_var < num:
                        res.append([k_var * a_var, k_var * b_var, k_var * c_var])
                        k_var += 1
        return res

    def execute(self) -> None:
        print(self.__doc__)
        number = input("Enter n: ")
        try:
            num = self.validate_data(number)
        except ValueError:
            print("ValueError exception thrown")
            return None
        res = self.main_logic(num + 1)
        for row in res:
            for el in row:
                print(el, end=' ')
            print()
        return None

    @staticmethod
    def name() -> str:
        return "554"


class Task87(TaskWithTwoIntValidationParameters):
    """Given natural n, m. Get the sum of the last m digits numbers n."""

    @staticmethod
    def main_logic(*args, **kwargs):
        number, quantity, *_ = args
        sum_, len_of_number = 0, len(number)
        for i in range(quantity):
            sum_ += int(number[len_of_number - i - 1])
        return sum_

    @classmethod
    def validate_data(cls, *args, **kwargs):
        input_data, *_ = args
        number, quantity_str = super().validate_data(input_data)
        quantity, len_of_number = int(quantity_str), len(number)
        if quantity > len_of_number:
            raise InvalidInput

        return number, quantity_str

    def execute(self) -> None:
        """Combine validation data + main logic"""
        print(self.__doc__)
        try:
            input_data = input("Enter number and m:")
            number, quantity_str = self.validate_data(input_data)
        except ValueError:
            print("Please enter the second value")
            return None
        except TypeError:
            print("You've entered not natural number")
            return None
        except InvalidInput:
            print("m must be less than number of digits number")
            return None
        # numbers must be natural
        result = self.main_logic(number, int(quantity_str))
        print(
            "The sum of the last {} digits of number {} is".format(int(quantity_str), number),
            result,
        )

        return None

    @staticmethod
    def name() -> str:
        return "87"


class Task86b(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(number):
        return sum(map(int, list(str(number))))

    def execute(self) -> None:
        """input natural number N \n
        find sum of its digits"""

        input_data = input("Enter number N: ")
        try:
            number = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        # number must be natural
        print(self.main_logic(number))
        return None

    @staticmethod
    def name() -> str:
        return "86 б)"


class Task330(TaskWithOneIntValidationParameter):
    @staticmethod
    def _get_dividers(numb):
        # complexity O(sqrt(numb))

        # using set to avoid duplicates of deviders
        deviders = {1}
        # starting from 2 because 1 is always devider of natural number
        for i in range(2, int(numb ** 0.5) + 2):
            if numb % i == 0:
                deviders.add(numb // i)
                deviders.add(i)
        return deviders

    @staticmethod
    def main_logic(number):
        for i in range(2, number):
            if sum(Task330._get_dividers(i)) == i:
                yield i

    def execute(self) -> None:
        """input natural number N \n
        find all "ideal" numbers that is less than N \n

        "ideal" - number the sum of witch deviders(without the number itself)
        is equal to the number"""

        number = input("Enter number N: ")
        try:
            number = self.validate_data(number)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        # general complixity of print all "ideal" numbers till number N
        # O(n*sqrt(n)) <==> O(n^(3/2))
        for n in self.main_logic(number):
            print(n)

        # alternative form (cons: print all values after forloop ends)
        # print(*(i for i in range(2, number)  if sum(get_deviders(i)) == i ))

        return None

    @staticmethod
    def name() -> str:
        return "330"


class Task108(TaskWithOneIntValidationParameter):
    # input number n, we should find the least number, that is bigger than n and is degree of number 2
    # complexity - O(1)

    @staticmethod
    def main_logic(n):
        return 2 ** (floor(log(n, 2)) + 1)

    def execute(self) -> None:
        n = int(input("Input natural number: "))
        try:
            m = self.validate_data(n)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None
        k = self.main_logic(n)
        print("r = ", floor(log(n, 2)) + 1)
        print("Result (2^r) = ", k)
        return None

    @staticmethod
    def name() -> str:
        return "108"


class Task226(TaskWithTwoIntValidationParameters):
    """Natural numbers m, n are given. Get all natural common multiples less than mn."""

    @staticmethod
    def main_logic(*args, **kwargs):
        value1, value2, *_ = args

        def lcm(var1, var2):
            return (var1 * var2) // gcd(var1, var2)

        lcm = lcm(value1, value2)
        return list(range(lcm, value1 * value2, lcm))

    def execute(self) -> None:
        """Combine validation data + main logic"""
        print(self.__doc__)
        try:
            input_data = input("Enter n and m:")
            number1, number2 = self.validate_data(input_data)
        except ValueError:
            print("Please enter the second value")
            return None
        except TypeError:
            print("You've entered not natural number")
            return None
        # numbers must be natural
        number1, number2 = int(number1), int(number2)
        result = self.main_logic(number1, number2)
        if result:
            print("All common multiples less then {}: ".format(number1 * number2), end="")
            for element in result:
                print(element, end=", ")
            print()
        else:
            print("There are no such values")

        return None

    @staticmethod
    def name() -> str:
        return "226"


class Task178e(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(sequence):
        result = 0
        for i in range(len(sequence)):
            if 2 ** i < sequence[i] and sequence[i] > factorial(i):
                result += 1
        return result

    def execute(self) -> None:
        print("-" * 60)
        print("Task - find amount of elements, which satisfy the condition\n2**k < Ak < k!")
        print("-" * 60)
        print("Enter sequence of integer numbers by ' ':")
        n = input("Enter the size of sequence:")
        try:
            n = self.validate_data(n)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print("Enter sequence of integer numbers by one in row:")
        sequence = [int(input()) for i in range(n)]
        for i in range(len(sequence)):
            try:
                sequence[i] = self.validate_data(sequence[i])
            except ValueError:
                print("ValueError exception thrown")
                return None
        print("Result:", self.main_logic(sequence))

        return None

    @staticmethod
    def name() -> str:
        return "178 д)"


class Task559(TaskWithOneIntValidationParameter):
    """A natural number n is given. Find all Mersen numbers less than n.
    (A prime number is called a Mersenne number if it can be represented as 2p - 1,\
    where p is also a prime number.)"""

    @staticmethod
    def eratosthenes(number):
        """Eratosthene's sieve to get primes"""
        sieve = list(range(number + 1))
        sieve[1] = 0
        for i in sieve:
            if i > 1:
                for j in range(i + i, len(sieve), i):
                    sieve[j] = 0
        sieve.pop(number)
        sieve_without_nulls = {x for x in sieve if x != 0}

        return sorted(set(sieve_without_nulls))

    @staticmethod
    def mersen_numbers(value):
        """Mersenne numbers"""
        return sorted({2 ** i - 1 for i in range(2, int(log(value + 1, 2)) + 1)})

    @staticmethod
    def main_logic(*args, **kwargs):
        number_str, *_ = args
        number = int(number_str)
        return sorted(
            set(Task559.eratosthenes(number)).intersection(set(Task559.mersen_numbers(number)))
        )  # Mersenne primes

    def execute(self) -> None:
        """Combine validation data + main logic"""
        print(self.__doc__)
        input_data = input("Enter n: ")

        try:
            number = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("You've entered not natural number")
            return None

        # number must be natural
        result = self.main_logic(number)
        print("Mersenne primes less than {}:".format(int(input_data)), sorted(result))

        return None

    @staticmethod
    def name() -> str:
        return "559"


class Task243b(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(n: int) -> List[Tuple[int, int]]:
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
        input_data = input("Enter n: ")

        try:
            n = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        all_squares = self.main_logic(n)

        if all_squares:
            for pair in all_squares:
                print("{x1} ^2 + {x2} ^2 = {N}".format(x1=pair[0], x2=pair[1], N=n))
        else:
            print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 б)"


class Task555(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(n: int):
        for i in range(n):
            for j in range(n - i + 1):
                print(end=" ")

            for j in range(i + 1):
                # C**k_n = n!/(k!*(n-r)!)
                yield factorial(i) // (factorial(j) * factorial(i - j))
            yield "\n"

    def execute(self) -> None:
        print("-" * 60)
        print("Task - build first n rows of Pascal's triangle")
        print("-" * 60)
        print("Enter natural number:", end=" ")
        n = int(input())
        try:
            n = self.validate_data(n)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print(" ", end="")
        for i in self.main_logic(n):
            print(i, end=" ")

        return None

    @staticmethod
    def name() -> str:
        return "555"


class Task88c(TaskWithOneIntValidationParameter):
    """
    A natural number n is given. Swap the first and last digits of n
    """

    @staticmethod
    def main_logic(n: int) -> int:
        """Switches first and last digits of the number"""

        n = str(n)
        return int(n) if len(n) == 1 else int(n[-1] + n[1:-1] + n[0])

    def execute(self) -> None:
        print(self.__doc__)

        input_data = input("Enter N to switch first and last digits of the number : ")
        try:
            n = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        print("Result: {}".format(self.main_logic(n)))

        return None

    @staticmethod
    def name() -> str:
        return "88 в)"


class Task88d(TaskWithOneIntValidationParameter):
    """
    A natural number n is given. Add the number 1 to the beginning and end of n
    """

    @staticmethod
    def main_logic(n: int) -> int:
        """Inserts digit 1 on the start and last positions"""

        n = str(n)
        return int("1" + n + "1")

    def execute(self) -> None:
        print(self.__doc__)

        input_data = input("Enter N to insert digit 1 on the start and last positions of the number : ")
        try:
            n = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        print("Result: {}".format(self.main_logic(n)))
        return None

    @staticmethod
    def name() -> str:
        return "88 г)"


class Task332(TaskWithOneIntValidationParameter):
    """
    A natural number n is given.
    Find non-negative x1, x2, x3, x4 such that x1^2 + x2^2 + x3^2 + x4^2 = n
    """

    @staticmethod
    def main_logic(n: int) -> List[int]:
        """Returns coefficients of distribution of a natural number into 4 squares"""

        res, tmp_res, counter = 0, 0, 0
        xs = [0, 0, 0, 0]
        for i in xs:
            counter += 1
            if tmp_res != n:
                while res <= n:
                    res = tmp_res + i ** 2
                    i += 1
                if i == 0:
                    i = 0
                elif i == 3 and counter == len(xs) and n == tmp_res + 4:
                    i = 2
                elif i == 2 and counter == len(xs) and n == tmp_res + 1:
                    i = 1
                else:
                    i -= 2
                res = i ** 2
                tmp_res += res
                xs[counter - 1] = i

        return xs

    def execute(self) -> None:
        print(self.__doc__)

        input_data = input("Enter N to find Lagrange decomposition coefficients : ")
        try:
            n = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        for i, x in enumerate(self.main_logic(n)):
            print("x" + str(i) + " = " + str(x))

        return None

    @staticmethod
    def name() -> str:
        return "332"


# for task 331. Checking whether we can represent given number as a sum of 3 number in power 2
# complexity ~ O(n)
def check(number, task):
    array = []
    for i in range(1, int(ceil(sqrt(number)))):
        for j in range(1, int(ceil(sqrt(number - i ** 2)))):
            third = number - i ** 2 - j ** 2
            if third > 0 and float(third ** (1 / 2)) % 1 == 0:
                array.append(str(i) + "^2 + " + str(j) + "^2 + " + str(int(third ** (1 / 2))) + "^2")
                if task == "331 a":
                    return array
    return array


class Task331a(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(n):
        result = check(n, "331 a")
        if not result:
            return False
        else:
            return result

    def execute(self) -> None:
        n = int(input("Input natural number: "))
        try:
            m = self.validate_data(n)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None
        k = self.main_logic(n)
        if not k:
            print("It`s impossible!")
        else:
            print(k)
        return None

    @staticmethod
    def name() -> str:
        return "331 а)"


class Task331b(TaskWithOneIntValidationParameter):
    @staticmethod
    def main_logic(n):
        result = check(n, "331 b")
        if not result:
            return False
        else:
            return result

    def execute(self) -> None:
        n = int(input("Input natural number: "))
        try:
            m = self.validate_data(n)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None
        k = self.main_logic(n)
        if not k:
            print("It`s impossible!")
        else:
            print(k)
        return None

    @staticmethod
    def name() -> str:
        return "331 б)"


class Task88b(TaskWithOneIntValidationParameter):
    """A natural number n is given. Reverse the order of the digits of the number n."""

    @staticmethod
    def main_logic(n):
        return int("".join(reversed(str(n))))

    def execute(self) -> None:
        print(self.__doc__)
        n = int(input("Input natural number: "))
        try:
            m = self.validate_data(n)
        except (ValueError, TypeError):
            print("Wrong input number")
            return None
        k = self.main_logic(n)
        print("Result = ", k)
        return None

    @staticmethod
    def name() -> str:
        return "88 б)"


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


class Task322(TaskWithOneIntValidationParameter):
    """Find a natural number from 1 to 10,000 with the maximum
    the sum of divisors."""

    def main_logic(self):
        maximal = 0
        number_with_maximal_sum = 0
        for i in range(1, 10001):
            if divisor(i) > maximal:
                maximal = divisor(i)
                number_with_maximal_sum = i
        return number_with_maximal_sum

    def execute(self) -> None:
        print(self.__doc__)
        k = self.main_logic()
        print("Result = ", k)
        return None

    @staticmethod
    def name() -> str:
        return "322"


# function for bfs search of endpoint classes
def get_classes(cls):
    stack = set(cls.__subclasses__())

    # array for all leaves
    endpoint_classes = []

    while stack:
        current = stack.pop()

        # checking if it is an rnd point class
        if classes := current.__subclasses__():
            stack |= {c for c in classes}
            continue

        endpoint_classes.append(current)

    return endpoint_classes


if __name__ == "__main__":

    # get all subclasses of AlgoInterface
    # and sort them as (int, str)
    tasks = sorted(
        get_classes(AlgoInterface),
        key=lambda x: (int(re.search("[0-9]+", x.name())[0]), x.name()),
    )

    # Console menu
    print("Choose task from:")
    print("\n".join("\t{}. {}".format(i, task.name()) for i, task in enumerate(tasks, 1)))

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

        Task_to_execute = tasks[position]()
        Task_to_execute.execute()

        # exit condition
        if input("Do you want to continue? (y-yes, ANY_KEY for exit) ").lower() != "y":
            break
