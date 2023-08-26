names = ["Favour", "Olaleru", "Oluwaseyi", "Joseph", "Neymar", "Beckham", "Lingard"]

person = {
    "name": "Favour",
    "age": 20,
    "address": "NGR"
}
print(person.items())

for key, value in person.items():
    print(f"{key}: {value}")
# for key in person:
#     print(f"{key}: {person[key]}")

# for name in names:
#     print(name)
