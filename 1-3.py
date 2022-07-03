my_list = [42, 43]
my_dict = {
    "foo": {
        "a": 12,
        "b": (1, 2, 3, 4, my_list)
    },
    "bar": {
        "c": 12,
        "d": {5, 6, 7, 8}
    },
    "moo": {
        "e": 12,
        "f": {"Lol": ["L", "o", "l"]}
    }
}
#1 Значение ключа "foo"
print(my_dict["foo"])
#2 Значение ключа "b"
print(my_dict["foo"]["b"])
#3 В my_list добавить 44
my_list.append(44)
print(my_list)