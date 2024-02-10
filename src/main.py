import requests
import re
import csv_parser
import csv_output

#URL for server with LM
url = "http://10.147.17.182:6420/v1/chat/completions"

#Query the LM with a preprompt and a prompt
def lmQuery(preprompt, prompt, temp):
    data = { 
    "messages": [ 
        { "role": "system", "content": preprompt },
        { "role": "user", "content": prompt }
    ], 
    "temperature": temp,  
    "max_tokens": 5,
    "stream": False
    }
    r = requests.post(url, json=data)
    content = re.search("\"content\":\s\"(.*)\"", r.text)
    return content.group(1)
    
(questionStatement, answers) = csv_parser.csvRead()

preprompt = "Pick the most suitable answer from the answers given below the question. Start with 'A', 'B' or 'C'."
def getPrompt(i):
    prompt = questionStatement[i]
    for key in answers[i]:
        prompt += f"\n{key}: {answers[i][key]}"
    return prompt


output = []#['C', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'T', 'A', 'A', 'A', 'B', 'A', 'C', 'A', 'T', 'A', 'A', 'B', 'A', '(', 'B', 'A', 'B', 'A', 'A', 'A', 'C', 'B', 'T', 'T', 'T', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'C', 'C', 'A', 'B', 'A', 'C', 'B', 'C', 'A', 'A', 'B', 'B', 'C', 'B', 'A', 'A', 'A', 'B', 'C', 'C', 'C', 'B', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'T', 'A', 'B', 'A', 'C', 'T', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'B', 'B', 'C', 'A']
#           ['C', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'C', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'A', 'C', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'C', 'C', 'A', 'B', 'A', 'C', 'B', 'C', 'A', 'A', 'B', 'B', 'C', 'B', 'A', 'A', 'A', 'B', 'C', 'C', 'C', 'B', 'C', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'B', 'A', 'C', 'A', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'B', 'B', 'C', 'A']
for i in range(0, 100):
    prompt = getPrompt(i)
    # print(prompt)
    set = False #boolean if a char has been appended to output for this question
    for temp in range(0, 11, 1): #for loop to increment between 0 and 1.0 for temperature
        query = lmQuery(preprompt, prompt, temp / 10)[0]
        if("ABC".find(query) != -1): #if result from query is an A B or C
           output.append(query)
           set = True
           break
    if(not set):
        output.append('A')
    

print(output)
print(len(output))
csv_output.writeCSV(output)