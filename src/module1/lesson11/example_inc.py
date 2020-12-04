class Phone:
    def __init__(self, color, brand, hz, max_U):
        self.color = color
        self.brand = brand
        self._hz = hz   # частичное сокрытие
        self.__max_U = max_U  # полное сокрытие

    def info(self):
        print(self._to_str1())

    # Хотим, чтобы пользователь не мог пользоваться этим методом
    def _to_str1(self):
        return '''
        Phone with:
            color: {color}
            brand: {brand}
            hz: {hz}
            max_U: {max_U}
        '''.format(color=self.color, brand=self.brand, hz=self._hz, max_U=self.__max_U)

    # Хотим, чтобы пользователь не мог пользоваться этим методом
    def __to_str2(self):
        return '''
        Phone with:
            color: {color}
            brand: {brand}
        '''.format(color=self.color, brand=self.brand)


phone1 = Phone("Black", "BMW", 400, 124)
print(phone1.brand)
print(phone1.color)
print(phone1._hz)
print(phone1._to_str1())
print(phone1.__max_U)
print(phone1.__to_str2())
phone1.info()