# Создайте класс NumberString наследуйте его от класса UserString, определите для него метод number_count(self),
#  который будет считать количество цифр в строке.


from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for i in self:

            if i.isdigit(): count +=1
        return count

s = NumberString("asd123")
print(s.number_count())

