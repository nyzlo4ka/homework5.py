immutable_var = 5, "food", 10.6, False
print(immutable_var)
# print(type(immutable_var))   =>   <class 'tuple'>
# immutable_var[2] = 2   =>   TypeError: 'tuple' object does not support item assignment
#   Объекты класса tulpe неизменяемы. Поддерживают два вида операций - конкатенацию и умножение.
#   Поменять значение можно только в том случае, если объект в Кортеже будет класса 'list', напимер:
# immutable_var = 5, ["food", 10.6], False
# immutable_var[1][1] = 2
# print(immutable_var)   =>   (5, ['food', 2], False)

mutable_list = [8.97, "Pause", True, 56, 3]
mutable_list[3] = 777
mutable_list[0] = "Привет"
print(mutable_list)
