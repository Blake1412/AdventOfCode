from collections import deque
import copy


class IntcodeComputer:
    def __init__(self, data: list[int]):
        self.registers = copy.deepcopy(data)
        self.__input_data = deque()
        self.output = None
        self.__reg_pointer = 0

    def run(self) -> bool:
        while True:
            instruction = self.registers[self.__reg_pointer]
            opcode = instruction % 100
            match opcode:
                case 1 | 2 | 5 | 6 | 7 | 8:
                    param_one = instruction % 1000 // 100
                    param_two = instruction // 1000
                    value_one = self.registers[self.__reg_pointer + 1] if param_one else self.registers[self.registers[self.__reg_pointer + 1]]
                    value_two = self.registers[self.__reg_pointer + 2] if param_two else self.registers[self.registers[self.__reg_pointer + 2]]
                    match opcode:
                        case 1 | 2 | 7 | 8:
                            store_reg = self.registers[self.__reg_pointer + 3]
                            match opcode:
                                case 1:
                                    self.registers[store_reg] = value_one + value_two
                                case 2:
                                    self.registers[store_reg] = value_one * value_two
                                case 7:
                                    self.registers[store_reg] = 1 if value_one < value_two else 0
                                case 8:
                                    self.registers[store_reg] = 1 if value_one == value_two else 0
                            self.__reg_pointer += 4

                        case 5:
                            self.__reg_pointer = value_two if value_one else self.__reg_pointer + 3
                        case 6:
                            self.__reg_pointer = value_two if not value_one else self.__reg_pointer + 3

                case 3 | 4:
                    store_reg = self.registers[self.__reg_pointer + 1]
                    match opcode:
                        case 3:
                            self.registers[store_reg] = self.__input_data.popleft()
                        case 4:
                            self.__reg_pointer += 2
                            self.output = self.registers[store_reg]
                            return False
                    self.__reg_pointer += 2

                case 99:
                    return True

    def add_input(self, *values: int):
        self.__input_data.extend(values)

    def run_to_completion(self) -> list[int]:
        output_values = []
        while not self.run():
            output_values.append(self.output)
        return output_values

