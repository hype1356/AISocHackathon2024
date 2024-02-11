import requests
import re
import csv_parser
import csv_output
import prompt_augmenter

#URL for server with LM
url = "http://10.147.17.246:6420/v1/chat/completions"
alphaNum = "[A-Za-z0-9]"
#Query the LM with a preprompt and a prompt
def lmQuery(preprompt, prompt):
    data = { 
    "messages": [ 
        { "role": "system", "content": preprompt }, #PREPROMPT
        { "role": "user", "content": prompt } #PROMPT
    ], 
    "temperature": 0.2,  
    "max_tokens": 100,
    "stream": False
    }
    r = requests.post(url, json=data)
    content = re.search("\"content\":\s\"(.*)\"", r.text)
    return content.group(1)
    
(questionStatement, answers) = csv_parser.csvRead()

def getContext(question):
    r = re.search(rf"({alphaNum}+\.{alphaNum}+)", question)
    if(r):
        context = []
        file = open("./contextData/output", "r")
        for line in file.readlines():
            r1 = re.search(rf"({alphaNum}+\.{alphaNum}+)", line)
            if(r1 and r1.group(1) == r.group(1)):
                context.append(line)
        return ' '.join(context)
    else:
        return prompt_augmenter.get_context(question, "./contextData/output")

# So for instance the following:
# What type of microphone must be installed to meet the recording requirements of paragraph (a)(2) of 14 CFR 23.1457?
# Options:
# A. Handheld microphone
# B. Area microphone
# C. Boom microphone
# C. Boom microphone
def getPrompt(i):
    preprompt = f"""
[INST] Choose the most suitable response between 'A', 'B', 'C' to answer the question.

Do not explain your answer.


Here is context to help: 
{getContext(questionStatement[i])}

[/INST]
"""
    prompt = " [INST] " + questionStatement[i]
    for key in answers[i]:
        prompt += f"\n{key}: {answers[i][key]}"
    prompt += " [\INST]"
    # print(preprompt + prompt)
    return (preprompt, prompt)


output = []#['C', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'T', 'A', 'A', 'A', 'B', 'A', 'C', 'A', 'T', 'A', 'A', 'B', 'A', '(', 'B', 'A', 'B', 'A', 'A', 'A', 'C', 'B', 'T', 'T', 'T', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'C', 'C', 'A', 'B', 'A', 'C', 'B', 'C', 'A', 'A', 'B', 'B', 'C', 'B', 'A', 'A', 'A', 'B', 'C', 'C', 'C', 'B', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'T', 'A', 'B', 'A', 'C', 'T', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'B', 'B', 'C', 'A']
#           ['C', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'C', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'C', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'C', 'C', 'A', 'B', 'A', 'C', 'B', 'C', 'A', 'A', 'B', 'B', 'C', 'B', 'A', 'A', 'A', 'B', 'C', 'C', 'C', 'B', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'B', 'A', 'C', 'A', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'B', 'B', 'C', 'A']
for i in range(94, 100):
    (preprompt, prompt) = getPrompt(i)
    output.append(lmQuery(preprompt, prompt))
    
def lambdaFunc(x):
    r = re.search("([A-C])\:", x)
    if(r):
        return r.group(1)
    else:
        return "A"

print(output)
output = list(map(lambda x : lambdaFunc(x), output))
print(output)
csv_output.writeCSV(output)
