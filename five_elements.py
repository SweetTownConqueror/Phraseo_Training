from random import randrange
import random

f = open("five_elements.txt", "w")

for x in range(0, 10):
    #print "We're on time %d" % (x)
    cap = "%03d"%randrange(301)
    dist = randrange(100)
    level = randrange(131)
    freq = round(random.uniform(75.0,190.9), 1)
    sqwak = "%04d"%randrange(10000)
    text = "\n\nDans le "+cap+" de votre position pour "+str(dist)+" nautiques et demi niveau "+str(level)+" un appareil sur "+str(freq)+" avec "+str(sqwak)+" au tronspondeur Confirmer dès que vous avez le visue"
    print(text)
    f = open("five_elements.txt", "a")
    f.write(text)
    f.close()

f = open("five_elements.txt", "a")
f.write("\n\n\n\n")
f.write("-----------------------------------------------------------------------------------")
f.write("-----------------------------------------------------------------------------------")
f.write("\n\n\n")
f.close()
arr = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Fox", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whisky", "X-ray", "Yankee", "Zoulou"]
for x in range(0, 10):
    #TODO: rajouter indicatif indicatif = arr[random.randint(0, 27)]+arr[random.randint(0, 27)]
    indicatif = ""
    qnh = str(random.randint(950, 1101))
    qfe = "1102"
    while int(qfe) >= int(qnh):
    	qfe = str(random.randint(950, 1101))
    information = arr[random.randint(0, 25)]
    sqwak = "%04d"%randrange(10000)
    text = "\n\n"+indicatif+" QNH "+qnh+" QFE "+qfe+", transpondeur "+sqwak+",  information "+information
    print(text)
    f = open("five_elements.txt", "a")
    f.write(text)
    f.close()