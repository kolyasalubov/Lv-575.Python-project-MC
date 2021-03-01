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