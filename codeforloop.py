for letter in "noura":
    print(letter)


kids = ["adam", "lily","amalia"]
print(len(kids))
for kid in kids:
    print(kid)


for kid in range(len(kids)):
    print(kid)

name = "noura"
for y in range(len(name)):
    print(y)

for kid in range(len(kids)):
    print(kids[kid])


for number in range(6):
    if number % 2 ==0:
        print(number, "is even")
    else:
        print(number, "is odd")

language = ["python", "css", "java", "html"]
for l in range(len(language)):
    if language[l] == "python":
        print(l, "is the right language")
    else:
        print(l, "is not the right language")

for n in range(5, 10):
    if n == 8:
        continue
    print(n, "is the choosen number")