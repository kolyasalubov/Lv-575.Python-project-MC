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


class task_88a(AlgoInterface):

    def execute(self) -> None:
        n = int(input("Enter number n:"))
        if str(n * n).find("3") != -1:
            print("YES")
        else:
            print("NO")
        return None

    @staticmethod
    def name() -> str:
        return "88a"


class task_88b(AlgoInterface):

    def execute(self) -> None:
        n = input("Enter number n:")
        print(n[::-1])
        return None

    @staticmethod
    def name() -> str:
        return "88b"

class task_322(AlgoInterface):

    def execute(self) -> None:
        def divisor(number):
            sum_of_divisors = 0
            for i in range(1, math.ceil(math.sqrt(number))):
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
