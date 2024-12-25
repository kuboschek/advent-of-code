import time
from math import trunc

def solve(A: int, B: int, C: int, program: list) -> list:
    output = []
    IP = 0

    while IP < len(program):
        opcode = program[IP]
        operand = program[IP + 1]

        # adv - division
        if opcode == 0:
            operand = apply_combo_operand(A, B, C, operand)
            A = A // 2**operand
        
        # bxl - XOR
        elif opcode == 1:
            B = B ^ operand

        # bst - mod 8
        elif opcode == 2:
            operand = apply_combo_operand(A, B, C, operand)
            B = operand % 8

        # jnz - jump if not zero
        elif opcode == 3:
            if A != 0:
                IP = operand
                continue
        
        # bxc - B XOR C
        elif opcode == 4:
            B = B ^ C

        # out - Output
        elif opcode == 5:
            operand = apply_combo_operand(A, B, C, operand)
            output.append(operand % 8)

            # Early return
            if output[len(output) - 1] != program[len(output) - 1]:
                return output

        # bdv - Like adv but register B
        elif opcode == 6:
            operand = apply_combo_operand(A, B, C, operand)
            B = A // 2**operand

        # cdv - Like adv but register C
        elif opcode == 7:
            operand = apply_combo_operand(A, B, C, operand)
            C = A // 2**operand

        IP += 2

    return output

def apply_combo_operand(A, B, C, operand):
    if operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    elif operand == 7:
        raise Exception("Invalid operand 7")

    return operand

def print_program(program: list):
    instructions = {
        0: "adv",
        1: "bxl",
        2: "bst",
        3: "jnz",
        4: "bxc",
        5: "out",
        6: "bdv",
        7: "cdv"
    }

    for i in range(0, len(program), 2):
        opcode = program[i]
        operand = program[i + 1]
        instruction = instructions.get(opcode, 'unknown')
        if operand == 4:
            operand_str = "A"
        elif operand == 5:
            operand_str = "B"
        elif operand == 6:
            operand_str = "C"
        else:
            operand_str = str(operand)
        
        if instruction == "adv":
            action = f"A //= 2**{operand_str}"
        elif instruction == "bxl":
            action = f"B ^= {operand}"
        elif instruction == "bst":
            action = f"B = {operand_str} % 8"
        elif instruction == "jnz":
            action = f"if A != 0: IP = {operand_str}"
        elif instruction == "bxc":
            action = "B ^= C"
        elif instruction == "out":
            action = f"output.append({operand_str} % 8)"
        elif instruction == "bdv":
            action = f"B //= 2**{operand_str}"
        elif instruction == "cdv":
            action = f"C //= 2**{operand_str}"
        else:
            action = "Unknown operation"
        print(f"{instruction} {operand_str} -> {action}")


def main():
    with open('sample-input', 'r') as file:
        input_str = file.read()
        lines = input_str.strip().split('\n')

        A = int(lines[0].split("Register A: ")[1])
        B = int(lines[1].split("Register B: ")[1])
        C = int(lines[2].split("Register C: ")[1])

        program = list(map(int, lines[4].split("Program: ")[1].split(",")))

        print("Sample Input Program:")
        print_program(program)

        other_a = 0
        while True:
            other_a += 1

            result = solve(other_a, B, C, program)

            if result == program:
                print("Sample Input Result:", other_a)
                break

    with open('real-input', 'r') as file:
        input_str = file.read()
        lines = input_str.strip().split('\n')

        A_in = int(lines[0].split("Register A: ")[1])
        B_in = int(lines[1].split("Register B: ")[1])
        C_in = int(lines[2].split("Register C: ")[1])

        program = list(map(int, lines[4].split("Program: ")[1].split(",")))

        print("Real Input Program:")
        print_program(program)

        octals = []

        for code in reversed(program):
            num = 
            result = solve


        while True:
            A = other_a
            B = B_in
            C = C_in

            output = []
            count = 0

            while A != 0:
                B = A % 8
                B ^= 5
                C //= 2**B # Shift right B
                B ^= 6 # Flip bit 2 and 1
                A //= 8 # Shift right 3
                B ^= C
            
                if (B % 8) != program[count]:
                    break

                if count == len(program) - 1:
                    print("Real Input Result:", other_a)
                    return

                count += 1

            if result == program:
                print("Real Input Result:", other_a)
                break

            other_a += 1

if __name__ == '__main__':
    main()