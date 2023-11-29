from collections import deque
import copy


class IntcodeComputer:
    def __init__(self, data: list[int]):
        self.registers = copy.deepcopy(data)
        self.input_data = deque()
        self.output_data = deque()

    def run(self):
        i = 0
        while True:
            instruction = self.registers[i]
            opcode = instruction % 100
            match opcode:
                case 1 | 2 | 5 | 6 | 7 | 8:
                    param_one = instruction % 1000 // 100
                    param_two = instruction // 1000
                    value_one = self.registers[i + 1] if param_one else self.registers[self.registers[i + 1]]
                    value_two = self.registers[i + 2] if param_two else self.registers[self.registers[i + 2]]
                    match opcode:
                        case 1 | 2 | 7 | 8:
                            store_reg = self.registers[i + 3]
                            match opcode:
                                case 1:
                                    self.registers[store_reg] = value_one + value_two
                                case 2:
                                    self.registers[store_reg] = value_one * value_two
                                case 7:
                                    self.registers[store_reg] = 1 if value_one < value_two else 0
                                case 8:
                                    self.registers[store_reg] = 1 if value_one == value_two else 0
                            i += 4

                        case 5:
                            i = value_two if value_one else i + 3
                        case 6:
                            i = value_two if not value_one else i + 3

                case 3 | 4:
                    store_reg = self.registers[i + 1]
                    match opcode:
                        case 3:
                            self.registers[store_reg] = self.input_data.popleft()
                        case 4:
                            self.output_data.append(self.registers[store_reg])
                    i += 2

                case 99:
                    break
