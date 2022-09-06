class Square2():
    def __init__(self, lado):
        self.lado = lado

    def calculate_area(self):
        self.area = self.lado**2
        print(f'A área do quadrado é de {self.area}')
    
    def calculate_perimeter(self):
        self.perimeter = self.lado * 4
        print(f'O perímetro do quadrado é de {self.perimeter}')