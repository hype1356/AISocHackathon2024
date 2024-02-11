import re

#Input a 100-length char array of A, B or C to write
def writeCSV(results):
    input = open("csv/Aviation Quiz.csv", "r")
    file = open("csv/submission.csv", "w")
    i = 0
    for line in input:
        r = re.search("^[A-Z]\.\s.*\"\,", line)
        if(r):
            file.write(line.strip() + results[i] + "\n")
            i += 1
        else:
            file.write(line)

writeCSV(['B', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'B', 'A', 'Z', 'B', 'A', 'B', 'A', 'A', 'A', 'C', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'C', 'Z', 'A', 'A', 'C', 'A', 'A', 'B', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'C', 'A', 'B', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'A', 'C', 'A', 'B', 'A', 'A', 'A', 'A', 'Z', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'A', 'C', 'A', 'A', 'C', 'A', 'A', 'A', 'B', 'A', 'A', 'D', 'B', 'A', 'A', 'D', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'E', 'A', 'A', 'C', 'A', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'D', 'A', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'Z', 'B', 'A', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'A', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'D', 'A', 'A', 'A', 'E', 'D', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'E', 'D', 'A', 'A', 'A', 'A', 'Z', 'A', 'E', 'A', 'A', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A'])