# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

class DegreeOfTwo:
    def __init__(self, n):
        self.n = n
    
    def generate_deg(self):
        deg = []
        k = 0
        power = 1
        while power <= self.n:
            deg.append(power)
            k += 1
            power = 2 ** k
        return deg

n = int(input("Введите число N: "))
deg_generator = DegreeOfTwo(n)
result = deg_generator.generate_deg()
print(result)
