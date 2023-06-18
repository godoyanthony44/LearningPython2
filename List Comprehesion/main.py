with open('num2.txt') as data:
    numbers = [n for n in data.readlines()]
with open('num1.txt') as data:
    numbers2 = [n for n in data.readlines()]
results = [int(n) for n in numbers if n in numbers2]
print(results)
