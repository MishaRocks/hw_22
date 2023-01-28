# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, x_coord, y_coord, state):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.state = state

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.y_coord += speed
        elif direction == 'DOWN':
            self.y_coord -= speed
        elif direction == 'LEFT':
            self.x_coord -= speed
        elif direction == 'RIGTH':
            self.x_coord += speed

    def _get_speed(self):
        speed = 1
        if self.state == 'fly':
            return speed * 1.2
        elif self.state == 'crawl':
            return speed * 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')