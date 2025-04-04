name = input("My name is ...")
age = int(input("My age is ..."))
currentyear = int(input("This year is ..."))
year = currentyear - age + 100 

copies = int(input("Copies?"))

for copy in range(copies):
    print(f"{name} will turn 100 years old in {year}")