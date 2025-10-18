tuplex = (1, 2, 3.1415, "Hi")
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

tuplex = ("hi", "jim", "bob")
print(tuplex)

tuplex = (2, 4, 6, 8, 9, 123, 123, 768, 56)
count_ = tuplex.count(123)
print(count_)

_slice = tuplex[3:5]
print(_slice)

__slice = tuplex[:3]
print(__slice)