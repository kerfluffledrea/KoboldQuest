import random
with open("syllables") as f:
    syls = []
    for l in f:
        syls.append(l.replace('\n',''))

    for i in range(100):
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
        print(name)