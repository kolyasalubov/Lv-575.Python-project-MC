"""
Algo tasks realisation
"""
from abc import ABC, abstractmethod, abstractstaticmethod
from math import sqrt, gcd, floor, log, ceil, factorial
from typing import List, Tuple

# List of algo tasks
TASKS = []


def register(cls):
    """
    Decorator/funtion for class-task registration (added to list TASKS)
    """
    TASKS.append(cls)
    return cls


class AlgoInterface(ABC):
    """interface for algo tasks
    subclasees must be only algo tasks"""

    @abstractmethod
    def execute(self) -> None:
        """implement your algo task here"""

    @abstractstaticmethod
    def name() -> str:
        """return name of task
        user representation"""

    @abstractstaticmethod
    def main_logic(*args, **kwargs):
        """return task's answer"""

    @abstractstaticmethod
    def validate_data(*args, **kwargs):
        """Validation of input data"""


class TaskWithOneIntValidationParameter(AlgoInterface):
    """Abstract class for validation data with one parameter"""
    @classmethod
    def validate_data(cls, *args, **kwargs):
        """Validation of data with one parameter
        Input number must be an natural"""
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
        """Validation of data with 2 parameters
        Input numbers must be integers"""
        input_data, *_ = args
        number, number2 = input_data.split()
        if not number.isdigit() or not number2.isdigit():
            raise TypeError

        return number, number2


@register
class Task178d(TaskWithOneIntValidationParameter):
    """
    178) Natural numbers n, a1,…, an are given.
    Define number of members ak of the sequence a1,…, an:
    d) which satisfy the condition: Ak < (Ak-1 + Ak+1) / 2.
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        sequence: list = args[0]
        result = 0
        for i in range(1, len(sequence) - 1):
            if sequence[i] < (sequence[i - 1] + sequence[i + 1]) / 2:
                result += 1
        return result

    def execute(self) -> None:
        print(self.__doc__)
        size = input("Enter the size of sequence:")
        try:
            size = self.validate_data(size)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print("Enter sequence of integer numbers by one in row:")
        sequence = [int(input()) for i in range(size)]
        for i in sequence:
            try:
                i = self.validate_data(i)
            except ValueError:
                print("ValueError exception thrown")
                return None
        print("Result:", self.main_logic(sequence))

        return None

    @staticmethod
    def name() -> str:
        return "178 г)"


@register
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


@register
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
        except TypeError:
            print("TypeError exception thrown")
            return None
        print("Enter the elements of sequence:")
        sequence = [int(input()) for _ in range(size)]
        for i in sequence:
            try:
                i = self.validate_data(i)
            except ValueError:
                print("ValueError exception thrown")
                return None

        print("Result:", self.main_logic(sequence))

        return None

    @staticmethod
    def name() -> str:
        return "178 б)"


@register
class Task107(TaskWithOneIntValidationParameter):
    """
    A natural number n is given.
    Find the largest integer k such that 4 ^k < m
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        """Return  the largest integer k, at which 4 ^k < m"""
        m_number: int = args[0]
        k: float = log(m_number, 4)
        k: int = int(k) if k != int(k) or k == 0 else int(k) - 1
        return k

    def execute(self) -> None:
        print(self.__doc__)

        input_data = input("Enter m: ")

        try:
            m_number = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        k = self.main_logic(m_number)
        print("k =", k)
        print("4 ^{} < {}".format(k, m_number))

        return None

    @staticmethod
    def name() -> str:
        return "107"


@register
class Task243a(TaskWithOneIntValidationParameter):
    """
    A natural number n is given.
    Can you imagine it as a sum of two squares of natural numbers?
    If yes, find a pair x, y of such natural numbers that n = x ^2 + y ^2
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> tuple:
        """Check if there are two numbers (x, y) that x ^2 + y ^2 = n"""
        n_number: int = args[0]
        n_number_square: float = sqrt(n_number)

        for y_number in range(1, int(sqrt(n_number)) + 1):
            # n = x^2 + y^2
            # x^2 = sqrt(n)^2 - y^2 = (sq + y) * (sq - y)
            x_number = sqrt((n_number_square + y_number) * (n_number_square - y_number))
            if int(x_number) == x_number:
                if int(x_number) >= y_number:
                    return int(x_number), y_number

            elif abs(round(x_number) - x_number) < 0.0000000001:  # prevention of calculation errors
                if round(x_number) >= y_number:
                    return round(x_number), y_number

        return ()

    def execute(self) -> None:
        print(self.__doc__)

        input_data = input("Enter n: ")

        try:
            n_number = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        exists = self.main_logic(n_number)
        if exists:
            print("{x1} ^2 + {x2} ^2 = {N}".format(x1=exists[0], x2=exists[1], N=n_number))
        else:
            print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 а)"


@register
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
        sequence = [int(input()) for i in range(number)]
        for i in sequence:
            try:
                i = self.validate_data(i)
            except ValueError:
                print("ValueError exception thrown")
                return None
            except TypeError:
                print("TypeError exception thrown")
                return None

        print("Result:", self.main_logic(sequence))
        return None

    @staticmethod
    def name() -> str:
        return "178 в)"


@register
class Task86a(TaskWithOneIntValidationParameter):
    """
    86. A natural number n is given.
    a) How many digits are in the number n.
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        """
        Count amount of digits in number
        :param number: int
        :return: int
        """
        number: int = args[0]
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
        """Returns name of a class in user representation"""
        return "86 a)"


@register
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
        except TypeError:
            print("TypeError exception thrown")
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


@register
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
            "The sum of the last {} digits of number {} is".format(
                int(quantity_str), number),
            result,
        )

        return None

    @staticmethod
    def name() -> str:
        return "87"


@register
class Task86b(TaskWithOneIntValidationParameter):
    """
    86. A natural number n is given.
    b) What is the sum of its numbers?
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        """
        Count sum of digits in the number
        :param number: int
        :return: int
        """
        number: int = args[0]
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


@register
class Task330(TaskWithOneIntValidationParameter):
    """
    330. A natural number is called perfect if it is equal
    to the sum of all its divisors, except for itself.
    The number 6 is perfect, since 6 = 1 + 2 + 3.
    The number 8 is not perfect, since 8 ≠ 1 + 2 + 4.
    Given a natural number n. Get all perfect numbers less than n.
    """

    @staticmethod
    def get_dividers(numb: int) -> set[int]:
        """
        Finds all deviders of an integer except the number itself
        :param number: int
        :return: set[int]

        complexity O(sqrt(numb))
        """

        # using set to avoid duplicates of deviders
        deviders = {1}
        # starting from 2 because 1 is always devider of natural number
        for i in range(2, int(numb ** 0.5) + 2):
            if numb % i == 0:
                deviders.add(numb // i)
                deviders.add(i)
        return deviders

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        """
        Its a generator that find all numbers that is ideal
        :param number: int
        :return: int
        """
        number: int = args[0]
        for i in range(2, number):
            if sum(Task330.get_dividers(i)) == i:
                yield i

    def execute(self) -> None:
        """input natural number N \n
        find all "ideal" numbers that is less than N \n

        "ideal" - number the sum of witch deviders(without the number itself)
        is equal to the number"""
        print(self.__doc__)

        number = input("Enter number N: ")
        try:
            number = self.validate_data(number)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        # general complixity of print all "ideal" numbers till number N
        # O(n*sqrt(n)) <==> O(n^(3/2))
        for numb in self.main_logic(number):
            print(numb)

        # alternative form (cons: print all values after forloop ends)
        # print(*(i for i in range(2, number)  if sum(get_deviders(i)) == i ))

        return None

    @staticmethod
    def name() -> str:
        return "330"


@register
class Task108(TaskWithOneIntValidationParameter):
    """\n108. You should enter the number\nThe aim is to find the least number,
    that is bigger than n and is degree of number 2\n"""

    # complexity - O(1)

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        """Return the least number, that is bigger than n and is degree of number 2"""
        number: int = args[0]
        return int(2 ** (floor(log(number, 2)) + 1))

    def execute(self) -> None:
        """Input data"""
        print(self.__doc__)
        number = int(input("Input natural number: "))
        try:
            number = self.validate_data(number)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None
        result = self.main_logic(number)
        print("r = ", floor(log(number, 2)) + 1)
        print("Result (2^r) = ", result)
        return None

    @staticmethod
    def name() -> str:
        return "108"


@register
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
            print("All common multiples less then {}: ".format(
                number1 * number2), end="")
            for element in result:
                print(element, end=", ")
            print()
        else:
            print("There are no such values")

        return None

    @staticmethod
    def name() -> str:
        return "226"


@register
class Task178e(TaskWithOneIntValidationParameter):
    """
    178) Natural numbers n, a1,…, an are given.
    Define number of members ak of the sequence a1,…, an:
    e) which satisfy the condition: 2**k < Ak < k!"
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:
        sequence: list = args[0]
        result = 0
        for i in sequence:
            if 2 ** (sequence.index(i) + 1) < i and i < factorial((sequence.index(i) + 1)):
                result += 1
        return result

    def execute(self) -> None:
        print(self.__doc__)
        size = input("Enter the size of sequence: ")
        try:
            size = self.validate_data(size)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print("Enter sequence of integer numbers by one in row:")
        sequence = [int(input()) for i in range(size)]
        for i in sequence:
            try:
                i = self.validate_data(i)
            except ValueError:
                print("ValueError exception thrown")
                return None
        print("Result:", self.main_logic(sequence))

        return None

    @staticmethod
    def name() -> str:
        return "178 д)"


@register
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
            set(Task559.eratosthenes(number)).intersection(
                set(Task559.mersen_numbers(number)))
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
        print("Mersenne primes less than {}:".format(
            int(input_data)), sorted(result))

        return None

    @staticmethod
    def name() -> str:
        return "559"


@register
class Task243b(TaskWithOneIntValidationParameter):
    """
    A natural number n is given.
    Can you imagine it as a sum of two squares of natural numbers?
    If yes, find all of the pairs x, y of such natural numbers that n = x ^2 + y ^2
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> List[Tuple[int, int]]:
        """Find all of the two numbers (x, y) that x ^2 + y ^2 = n"""
        n_number: int = args[0]
        n_number_square: float = sqrt(n_number)

        squares_numbers = []

        for y_number in range(1, int(sqrt(n_number)) + 1):
            # n = x^2 + y^2
            # x^2 = sqrt(n)^2 - y^2 = (sq + y) * (sq - y)
            x_number = sqrt((n_number_square + y_number) * (n_number_square - y_number))
            if int(x_number) == x_number:
                if int(x_number) >= y_number:
                    squares_numbers.append((int(x_number), y_number))

            elif abs(round(x_number) - x_number) < 0.0000000001:  # prevention of calculation errors
                if round(x_number) >= y_number:
                    squares_numbers.append((round(x_number), y_number))

        return squares_numbers

    def execute(self) -> None:
        print(self.__doc__)

        input_data = input("Enter n: ")

        try:
            n_number = self.validate_data(input_data)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None

        all_squares = self.main_logic(n_number)

        if all_squares:
            for pair in all_squares:
                print("{x1} ^2 + {x2} ^2 = {N}".format(x1=pair[0], x2=pair[1], N=n_number))
        else:
            print("This number cannot be represented as the sum of two squares")

        return None

    @staticmethod
    def name() -> str:
        return "243 б)"


@register
class Task555(TaskWithOneIntValidationParameter):
    """
    Pascal's triangle is a numerical triangle in which there are ones
    at the edges, and each number inside is equal to the sum of the
    two above it in the nearest line above.
    Given natural n. Get first n rows of a triangle Pascal.
    """

    @staticmethod
    def main_logic(*args, **kwargs) -> int:

        number: int = args[0]
        for i in range(number):
            for j in range(number - i + 1):
                print(end=' ')

            for j in range(i + 1):
                # C**k_n = n!/(k!*(n-r)!)
                yield factorial(i) // (factorial(j) * factorial(i - j))
            # for j in range(n - i + 1):
            #     print(end=" ")
            yield "\n"

    def execute(self) -> None:
        print(self.__doc__)
        print("Enter natural number: ", end=" ")
        number = int(input())
        try:
            number = self.validate_data(number)
        except ValueError:
            print("ValueError exception thrown")
            return None
        print(" ", end="")
        for i in self.main_logic(number):
            print(i, end=" ")

        return None

    @staticmethod
    def name() -> str:
        return "555"


@register
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

        input_data = input(
            "Enter N to switch first and last digits of the number : ")

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


@register
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

        input_data = input(
            "Enter N to insert digit 1 on the start and last positions of the number : ")
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


@register
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

        input_data = input(
            "Enter N to find Lagrange decomposition coefficients : ")
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
    """Function to check in tasks 331a and 331b"""
    array = []
    for i in range(1, int(ceil(sqrt(number)))):
        for j in range(1, int(ceil(sqrt(number - i ** 2)))):
            third = number - i ** 2 - j ** 2
            if third > 0 and float(third ** (1 / 2)) % 1 == 0:
                array.append(str(i) + "^2 + " + str(j) + "^2 + " +
                             str(int(third ** (1 / 2))) + "^2")
                if task == "331 a":
                    return array
    return array


@register
class Task331a(TaskWithOneIntValidationParameter):
    """\n331 a. You should enter the number.\n
    The aim is to check whether we can represent given number as a sum of 3 number in power 2.
    And if yes, show the sum\n"""

    @staticmethod
    def main_logic(*args, **kwargs) -> List[str]:
        number: int = args[0]
        result = check(number, "331 a")
        return result

    def execute(self) -> None:
        print(self.__doc__)
        number = int(input("Input natural number: "))
        try:
            number = self.validate_data(number)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None
        result = self.main_logic(number)
        if not result:
            print("It`s impossible!")
        else:
            print(result)
        return None

    @staticmethod
    def name() -> str:
        return "331 а)"


@register
class Task331b(TaskWithOneIntValidationParameter):
    """\n331 b. You should enter the number.\n
    The aim is to check whether we can represent given number as a sum of 3 number in power 2.
    And if yes, show all possible sums\n"""

    @staticmethod
    def main_logic(*args, **kwargs) -> List[str]:
        number: int = args[0]
        result = check(number, "331 b")
        return result

    def execute(self) -> None:
        print(self.__doc__)
        number = int(input("Input natural number: "))
        try:
            number = self.validate_data(number)
        except (ValueError, TypeError):
            print("Wrong input!")
            return None
        result = self.main_logic(number)
        if not result:
            print("It`s impossible!")
        else:
            print(result)
        return None

    @staticmethod
    def name() -> str:
        return "331 б)"


@register
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


@register
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
