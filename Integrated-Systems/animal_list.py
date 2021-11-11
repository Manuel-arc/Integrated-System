animal = open("animal.txt").read().split('\n')

animals = ["dog", "cat", "deer"]


for i in range(len(animal)):
    animal[i] = animal[i].lower()

for item in animal:
    if item in animals:
        print(item)
