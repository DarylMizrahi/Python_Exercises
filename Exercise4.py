list_of_names = ["Daryl  Mizrahi", "Gabriel", "Sacha Rebbouh", "Maxime"]

def name_checker (namesList):
    for i in namesList:
        yield i

for name in name_checker(list_of_names):
    if " " not in name:
        print(name)