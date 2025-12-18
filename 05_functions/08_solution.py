def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name = "vishal", city = "pune")
print_kwargs(name = "vishal", city = "pune", age = 22)
print_kwargs(name = "vishal")