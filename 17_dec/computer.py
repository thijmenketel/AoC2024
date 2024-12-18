A,B,C = 'A','B','C'

class Computer(object):
    def __init__(self, registry) -> None:
        self.IP = 0
        self.STDOUT = []
        self.REG = {
            A: registry[0],
            B: registry[1],
            C: registry[2],
        }

    def adv(self, operand): self.REG[A] = self.REG.get(A) >> self.get_combo_op(operand) # type: ignore
    def bxl(self, operand): self.REG[B] = self.REG.get(B) ^ operand
    def bst(self, operand): self.REG[B] = self.get_combo_op(operand) % 8 # type: ignore
    def jnz(self, operand): self.IP = operand if self.REG.get(A) != 0 else self.IP # type: ignore TODO check IP is changed after op
    def bxc(self, _): self.REG[B] = self.REG.get(B) ^ self.REG.get(C) # type: ignore
    def out(self, operand): self.STDOUT += [self.get_combo_op(operand) % 8] # type: ignore
    def bdv(self, operand): self.REG[B] = self.REG.get(A) >> self.get_combo_op(operand) # type: ignore
    def cdv(self, operand): self.REG[C] = self.REG.get(A) >> self.get_combo_op(operand) # type: ignore

    def get_combo_op(self, operand):
        match operand:
            case _ if 0 <= operand <= 3: return operand
            case 4: return self.REG.get(A)
            case 5: return self.REG.get(B)
            case 6: return self.REG.get(C)
            case _: raise ValueError("YOU DONE FUCKED UP BRO")

    def run_instr(self, opcode, operand):
        {
            0 : self.adv,
            1 : self.bxl,
            2 : self.bst,
            3 : self.jnz,
            4 : self.bxc,
            5 : self.out,
            6 : self.bdv,
            7 : self.cdv,
        }.get(opcode)(operand) # type: ignore

    def reset(self):
        self.IP = 0
        self.STDOUT = []
        self.REG = {A: 0, B: 0, C: 0}

    def run_program(self, program, a_val = None):
        if a_val is not None: self.REG[A] = a_val # type: ignore
        while self.IP < len(program):
            curr_ip = self.IP
            opcode = program[self.IP]
            operand = program[self.IP + 1]
            self.run_instr(opcode, operand)
            if curr_ip == self.IP:
                self.IP += 2
        print(f"{a_val if a_val else ''} - {self.STDOUT}")
        return self.STDOUT
