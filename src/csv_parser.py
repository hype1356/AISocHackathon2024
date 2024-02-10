import re

def csvRead():
    csv_input = open("csv/Aviation Quiz.csv", 'r')
    lines = csv_input.readlines()[1:]
    questionStatements = [] #list
    answers = [] #
    for i in range(0, len(lines), 5): #5 lines per question entry
        question = re.search("([0-9]+),\"(.*)", lines[i])
        a = re.search("(A).\\s(.*)", lines[i + 2])
        b = re.search("(B).\\s(.*)", lines[i + 3])
        c = re.search("(C).\\s(.*)\\\",", lines[i + 4])
        questionStatements.append(question.group(2))
        answer = {}
        answers.append(answer)
        for m in [a, b, c]:
            answer[m.group(1)] = m.group(2)
    return (questionStatements, answers)