# list compheresion

with open('num2.txt') as data:
    numbers = [n for n in data.readlines()]
with open('num1.txt') as data:
    numbers2 = [n for n in data.readlines()]
results = [int(n) for n in numbers if n in numbers2]
print(results)

# dictionary compheresion
sentence = 'what is the name of that one thing'
word_count = {word: len(word) for word in sentence.split()}
print(word_count)

weather_c = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 12,
    "friday": 20,
    "saturday": 25,
    "sunday": 14
}

weather_f = {day: (temp*(9/5)+32) for (day,temp) in weather_c.items()}
print(weather_f)
