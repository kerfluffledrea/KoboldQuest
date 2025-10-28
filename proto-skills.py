import random
with open("KoboldSkills", "r") as f:
    skills = []
    for s in f:
        skills.append(s.strip())
    print(skills)

    usedskills = []
    for i in range(12):
        new_skill = skills[random.randint(0,len(skills)-1)]
        while new_skill in usedskills:
            new_skill = skills[random.randint(0,len(skills)-1)]
        usedskills.append(new_skill)

    print(usedskills)
    print("+++ " + usedskills[0])
    for i in range(12):
        if i < 6 and i > 0:
            print("+ " + usedskills[i])
        elif i >= 5 and i < 11:
            print("- " + usedskills[i])
    print("--- " + usedskills[11])
