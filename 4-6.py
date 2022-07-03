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

#4 Значение ключа "b"
print(my_dict["foo"]["b"])
#5 Множество
print(my_dict["bar"]["d"])
#6 Множество +"9"
list=list(my_dict["bar"]["d"])
list.append(9)
my_dict["bar"]["d"]=set(list)
print(my_dict["bar"]["d"])