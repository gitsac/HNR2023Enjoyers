# importing packages and modules
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

people = ["a", "b", "c"] # placeholder, needs to get list members from tele API

db = {}

for person in people:
    db[person] = {}
    for subject in people:
        db[person][subject] = 0

def netOwe(person1, person2): # person 1 owes person 2 $X
    return db[person1][person2] - db[person2][person1] 

def addOweTransaction(person1, person2, amount):
    db[person1][person2] += amount


def tabulise(database):
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

