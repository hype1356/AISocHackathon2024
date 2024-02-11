import re

def csvRead():
    csv_input = open("csv/Aviation Quiz.csv", 'r')
    lines = csv_input.readlines()[1:]
    questionStatements = [] #list
    answers = [] #list
    id = 0
    for line in lines:
        question = re.search("([0-9]+),\"(.*)", line)
        if(question):
            id = question.group(1)
            questionStatements.append(question.group(2))
            continue
        a = re.search("(A).\\s(.*)", line)
        b = re.search("(B).\\s(.*)", line)
        c = re.search("(C).\\s(.*)(\",)?", line)
        d = re.search("(D).\\s(.*)", line)
        e = re.search("(E).\\s(.*)(\",)?", line)
        for m in [a,b,c,d,e]:
            if(not m): 
                continue
            key = int(id)
            if(key >= len(answers)):
                answers.append({})
            answers[key][m.group(1)] = m.group(2)
    return (questionStatements, answers)