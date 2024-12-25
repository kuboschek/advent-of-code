import time
from math import trunc

def solve(input_str: str):
    lines = input_str.strip().split('\n')

    A = int(lines[0].split("Register A: ")[1])
    B = int(lines[1].split("Register B: ")[1])
    C = int(lines[2].split("Register C: ")[1])

    program = list(map(int, lines[4].split("Program: ")[1].split(",")))
    output = []

    IP = 0

    print(f"A: {A}, B: {B}, C: {C}, Program: {program}")

    while IP < len(program):
        opcode = program[IP]
        operand = program[IP + 1]


        print(f"A: {A}, B: {B}, C: {C}, IP: {IP}, Opcode: {opcode}, Operand: {operand}")

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
            print(f"Operand: {operand}")
            B = operand % 8
            print(f"B: {B}")

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

        # bdv - Like adv but register B
        elif opcode == 6:
            operand = apply_combo_operand(A, B, C, operand)
            B = A // 2**operand

        # cdv - Like adv but register C
        elif opcode == 7:
            operand = apply_combo_operand(A, B, C, operand)
            C = A // 2**operand

        IP += 2

    return ",".join(map(str, output))

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

def main():
    with open('sample-input', 'r') as file:
        input_str = file.read()
    print("Sample Input Result:", solve(input_str))

    with open('real-input', 'r') as file:
        input_str = file.read()
    print("Real Input Result:", solve(input_str))

if __name__ == '__main__':
    main()