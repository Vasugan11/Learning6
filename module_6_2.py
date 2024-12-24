class Vehicle:
    __COLOR_VARIANTS = ['corrida', 'nevada', 'niagara', 'regatta', 'iguana']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.__model}, {self.__engine_power}, {self.__color}, Владелец: {self.owner}')

    def set_color(self, new_color):
        new_color = new_color.lower()
        for i in range(len(self.__COLOR_VARIANTS)):
            self.__COLOR_VARIANTS[i] = self.__COLOR_VARIANTS[i].lower()
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Vacula', 'vaz2101', 59, 'corrida')

vehicle1.print_info()
vehicle1.set_color('MURENA')
vehicle1.set_color('NIAGARA')
vehicle1.owner = 'Mycola'
vehicle1.print_info()