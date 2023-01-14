# importing packages and modules
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import json

with open("data.json", "r") as json_data:
    db = json.load(json_data)

people = list(db.keys()) # placeholder, needs to get list members from tele API
logDb = []

for person in people:
    db[person] = {}
    for subject in people:
        db[person][subject] = 0

def addLog(person1, person2, amount):
    logDb.append(str(datetime.datetime.now()) + ": " + person1 + " owe " + person2 + "$" + amount)

def updateJSON():
    with open('data.json', 'w') as fp:
        json.dump(db, fp)

def addMember(name):
    people.append(name)
    db[name] = {}
    for person in people:
        db[name][person] = 0
    for key in people:
        if key != name:
            db[key][name] = 0
    updateJSON()
    print("added success!")
    
def userExists(name):
    return name in people
            

def netOwe(person1, person2): # person 1 owes person 2 $X
    return db[person1][person2] - db[person2][person1] 

def addOweTransaction(person1, person2, amount):
    db[person1][person2] += amount
    addLog(person1, person2, amount)
    print("transaction added")


def tabulise(database):
    if len(people) == 0:
        return
    # populate cell data into matplot
    data = []
    for person in people:
        curOwes = []
        subjects = database[person]
        for person2 in subjects:
            curOwes.append(subjects[person2])
        data.append(curOwes)

    fig, ax = plt.subplots()

    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    ax.table(cellText = data, rowLabels = people, colLabels = people, loc = 'center')
    fig.tight_layout()
    

def getImage():
    tabulise(db)
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches = 'tight')
    buf.seek(0)
    return buf

