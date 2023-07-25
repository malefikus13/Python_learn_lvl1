# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

class PetyaAndKatya:
    def __init__(self):
        self.x = None
        self.y = None

    def input_hints(self, s, p):
        # Находим два числа x и y, удовлетворяющие условиям суммы и произведения
        for i in range(1, 1001):
            for j in range(1, 1001):
                if i + j == s and i * j == p:
                    self.x = i
                    self.y = j
                    return

    def get_numbers(self):
        return self.x, self.y


s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

katya = PetyaAndKatya()
katya.input_hints(s, p)

x, y = katya.get_numbers()
print(f"Задуманные числа: {x} и {y}")