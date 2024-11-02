#1
def print_params(a = 1, b = "string", c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

#2
values_list = (3, "word", False)
values_dict = {"a" : 1, "b" : "string","c" : True}

print_params(*values_list)
print_params(**values_dict)

#3
value_list_2 = (3, "world")

print_params(*value_list_2, 42)
