import re

#Input a 100-length char array of A, B or C to write
def writeCSV(results):
    input = open("csv/Aviation Quiz.csv", "r")
    file = open("csv/submission.csv", "w")
    i = 0
    for line in input:
        r = re.search("C\.\s.*\",", line)
        if(r):
            file.write(line.strip() + results[i] + "\n")
            i += 1
        else:
            file.write(line)