from random import randrange
import random

f = open("five_elements_en.txt", "w")

for x in range(0, 10):
    #print "We're on time %d" % (x)
    cap = "%03d"%randrange(301)
    dist = randrange(100)
    level = randrange(131)
    freq = round(random.uniform(75.0,190.9), 1)
    sqwak = "%04d"%randrange(10000)
    text = "\n\nIn the "+cap+" of your position for "+str(dist)+" nautiques level "+str(level)+" an aircraft on "+str(freq)+" with "+str(sqwak)+" on sqwak confirm at see"
    print(text)
    f = open("five_elements_en.txt", "a")
    f.write(text)
    f.close()

f = open("five_elements_en.txt", "a")
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
    qnh = list(qnh)
    qnh = "-".join(qnh)
    qfe = "1102"
    while int(qfe.replace("-", "")) >= int(qnh.replace("-", "")):
    	qfe = str(random.randint(950, 1101))
    qfe = list(qfe)
    qfe = "-".join(qfe)
    information = arr[random.randint(0, 25)]
    sqwak = "%04d"%randrange(10000)
    sqwak = list(sqwak)
    sqwak = "-".join(sqwak)
    text = "\n\n"+indicatif+" QNH "+qnh+" QFE "+qfe+", squawk "+sqwak+",  information "+information
    print(text)
    f = open("five_elements_en.txt", "a")
    f.write(text)
    f.close()