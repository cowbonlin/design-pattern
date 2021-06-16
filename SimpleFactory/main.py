class Operation:
    def __init__(self):
        number_a = 0
        number_b = 0

    # todo: Add an abstract get_result() member function


class OperationAdd(Operation):
    def get_result(self) -> float:
        return self.number_a + self.number_b

class OperationSub(Operation):
    def get_result(self) -> float:
        return self.number_a - self.number_b

class OperationMul(Operation):
    def get_result(self) -> float:
        return self.number_a * self.number_b

class OperationDiv(Operation):
    def get_result(self) -> float:
        return self.number_a / self.number_b # ZeroDivisionError might be raised

class OperationFactory:
    @staticmethod
    def create_operate(operate: str) -> Operation:
        if operate == '+':
            return OperationAdd()
        elif operate == '-':
            return OperationSub()
        elif operate == '*':
            return OperationMul()
        elif operate == '/':
            return OperationDiv()
        else:
            raise ValueError(f'{operate} is not supported yet')

if __name__ == '__main__':
    oper = OperationFactory.create_operate('/')
    oper.number_a = 3
    oper.number_b = 5

    result = oper.get_result()
    print(result)
