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
#7 Множество
print(my_dict["bar"]["d"])
#8 Удалить "о"
my_dict["moo"]["f"]["Lol"].remove("o")
print(my_dict["moo"]["f"]["Lol"])
#9 Добавить ключ "k" со значением ["k","e","k"]
my_dict["moo"]["f"]["k"]=["k","e","k"]
print(my_dict)
#10 Удалить словарь
my_dict.clear()
print(my_dict)