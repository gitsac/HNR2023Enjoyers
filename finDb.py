people = ["a", "b", "c"]

db = {}

for person in people:
    db[person] = {}
    for subject in people:
        if subject != person:
            db[person][subject] = 0

def netOwe(person1, person2): # person 1 owes person 2 $X
    return db[person1][person2] - db[person2][person1] 



