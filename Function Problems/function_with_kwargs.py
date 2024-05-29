def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
print_kwargs(name="Ujjwal", age=20, city="Pune")
print_kwargs(name="Pikachu", age=5)