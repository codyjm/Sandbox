"""
Cody Moxham
print every second letter of name
"""
name = input("Enter name: ")
while len(name) == 0:
    name = input("Enter a name: ")

for i in range(len(name)):
    if i % 2 == 1:
        print(name[i])
