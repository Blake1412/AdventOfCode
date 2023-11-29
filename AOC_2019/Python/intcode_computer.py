from collections import deque, defaultdict


class IntcodeComputer:
    registers: defaultdict[int, int]

    def __init__(self, data: list[int]):
        self.registers = defaultdict(int, {k: v for k, v in enumerate(data)})
        self.__input_data = deque()
        self.output = None
        self.__reg_pointer = 0
        self.__relative_base = 0

    def run(self) -> bool:
        while True:
            instruction = self.registers[self.__reg_pointer]
            opcode = instruction % 100
            match opcode:
                case 1 | 2 | 5 | 6 | 7 | 8:
                    value_one = self.registers[self.__get_param_reg(instruction % 1000 // 100, 1)]
                    value_two = self.registers[self.__get_param_reg(instruction % 10000 // 1000, 2)]
                    match opcode:
                        case 1 | 2 | 7 | 8:
                            store_reg = self.__get_param_reg(instruction % 100000 // 10000, 3)
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

                case 3 | 4 | 9:
                    match opcode:
                        case 3 | 4:
                            store_reg = self.__get_param_reg(instruction % 1000 // 100, 1)
                            match opcode:
                                case 3:
                                    self.registers[store_reg] = self.__input_data.popleft()
                                case 4:
                                    self.__reg_pointer += 2
                                    self.output = self.registers[store_reg]
                                    return False
                        case 9:
                            self.__relative_base += self.registers[self.__get_param_reg(instruction % 1000 // 100, 1)]
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

    def __get_param_reg(self, code: int, position: int):
        match code:
            case 0:
                return self.registers[self.__reg_pointer + position]
            case 1:
                return self.__reg_pointer + position
            case 2:
                return self.__relative_base + self.registers[self.__reg_pointer + position]
