# registers = {'A': 55593699, 'B': 0, 'C': 0, 'step': 0}
class Program:
    def __init__(self, a):
        self.registers = {'A': a, 'B': 0, 'C': 0, 'step': 0}
    
    def combo(self, operand):
        if operand >= 0 and operand <= 3:
            return operand
        if operand == 4:
            return self.registers['A']
        if operand == 5:
            return self.registers['B']
        if operand == 6:
            return self.registers['C']
        if operand == 7:
            raise Exception('operand 7')
    def step(self):
        self.registers['step'] += 2

    def adv(self, operand):
        self.registers['A'] //= 2**self.combo(operand)
        self.step()
        return ''
    def bxl(self, operand):
        self.registers['B'] ^= operand
        self.step()
        return ''
    def bst(self, operand):
        self.registers['B'] = self.combo(operand) % 8
        self.step()
        return ''
    def jnz(self, operand):
        if self.registers['A'] != 0:
            self.registers['step'] = operand
        else:
            self.step()
        return ''
    def bxc(self, operand):
        self.registers['B'] ^= self.registers['C']
        self.step()
        return ''
    def out(self, operand):
        self.step()
        return str(self.combo(operand) % 8) + ','
    def bdv(self, operand):
        self.registers['B'] = self.registers['A'] // 2**self.combo(operand)
        self.step()
        return ''
    def cdv(self, operand):
        self.registers['C'] = self.registers['A'] // 2**self.combo(operand)
        self.step()
        return ''
    
    def run(self):
        instruction_map = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz, 4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv}
        output = ''
        while self.registers['step'] + 1 < len(mem):
            instr = mem[self.registers['step']]
            operand = mem[self.registers['step'] + 1]
            output += instruction_map[instr](operand)
        return output[:-1]

mem = [2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]
mem_str = ','.join([str(b) for b in mem])

search = 1
a = 0
while search < len(mem):
    search_len = 2 * search + 1
    target = mem_str[(-1 * search_len):]
    if Program(a).run() == target:
        search += 1
        a *= 8
    else:
        a += 1

print(Program(a // 8).run(), a // 8)