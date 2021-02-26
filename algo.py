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


class task_86a(AlgoInterface):

    def execute(self) -> None:
        ''' input natural number N \n
        find amount of its digits '''
        number = int(input("Eneter number N: "))
        # number must be natural
        print(len(str(number)) if number > 0 else "Number is not natural")
        return None

    @staticmethod
    def name() -> str:
        return "86 a)"


class task_86b(AlgoInterface):

    def execute(self) -> None:
        ''' input natural number N \n
         find sum of its digits '''
        number = int(input("Eneter number N: "))
        number_str = str(number)
        sum_ = sum(map(int, list(number_str)))
        print(sum_)

        return None

    @staticmethod
    def name() -> str:
        return "86 б)"


class task_330(AlgoInterface):

    def execute(self) -> None:
        ''' input natural number N \n
            find all "ideal" numbers that is less than N \n

            "ideal" - number the sum of witch deviders(without the number itself)
            is equal to the number'''

        number = int(input("Enter number N: "))

        def get_deviders(numb):
            # complexity O(sqrt(numb))

            # using set to avoid duplicates of deviders
            deviders = {1}
            # starting from 2 because 1 is always devider of natural number
            for i in range(2, int(numb**0.5) + 2):
                if numb % i == 0:
                    deviders.add(numb/i)
                    deviders.add(i)
            return deviders

        # general complixity of print all "ideal" numbers till number N
        # O(n*sqrt(n)) <==> O(n^(3/2))
        for i in range(2, number):
            if sum(get_deviders(i)) == i:
                print(i)

        # alternative form (cons: print all values after forloop ends)
        # print(*(i for i in range(2, number)  if sum(get_deviders(i)) == i ))

        return None

    @staticmethod
    def name() -> str:
        return "330"


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
