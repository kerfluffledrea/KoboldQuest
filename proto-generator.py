import random

syls = []
skills = []

with open("syllables.txt", 'r') as f:
    for l in f:
        syls.append(l.replace('\n',''))

with open("skills.txt", "r") as f2:
    for s in f2:
        skills.append(s.strip())

max_index = len(syls)-1
name = syls[random.randint(0, max_index)].title()
fuckin_luck_thing = 0.99
while random.random() < fuckin_luck_thing:
    roll = random.random()
    if(roll < 0.1):
        name += ' ' + syls[random.randint(0, max_index)].title()
    elif(roll < 0.25):
        name += '' + syls[random.randint(0, max_index)]
    elif(roll < 0.5):
        name += '-' + syls[random.randint(0, max_index)]
    else:
        name += '\'' + syls[random.randint(0, max_index)]
    fuckin_luck_thing /= 1.5
usedskills = []
for i in range(12):
    new_skill = skills[random.randint(0,len(skills)-1)]
    while new_skill in usedskills:
        new_skill = skills[random.randint(0,len(skills)-1)]
    usedskills.append(new_skill)

print("# " + name)
print("**Super Duper Good at " + usedskills[0] + "**")
print("**Super Duper bad at " + usedskills[11] + "**")
for i in range(12):
    if i == 0:
        print("\n*Good at...*")
    elif i < 6 and i > 0:
        print(" - " + usedskills[i])
    elif i < 11:
        if i == 6:
            print("\n*Bad at...*")
        print("- " + usedskills[i])