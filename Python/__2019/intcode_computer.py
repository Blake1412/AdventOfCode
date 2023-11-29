import copy


class IntcodeComputer:
    def __init__(self, data: list[int]):
        self.data = copy.deepcopy(data)

    def run(self):
        i = 0
        while True:
            opcode = self.data[i]
            match opcode:
                case 1:
                    self.data[self.data[i + 3]] = self.data[self.data[i + 1]] + self.data[self.data[i + 2]]
                case 2:
                    self.data[self.data[i + 3]] = self.data[self.data[i + 1]] * self.data[self.data[i + 2]]

                case 99:
                    break
            i += 4
