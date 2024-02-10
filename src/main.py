import requests
import re
import csv_parser

#URL for server with LM
url = "http://10.147.17.182:6420/v1/chat/completions"

#Query the LM with a preprompt and a prompt
def lmQuery(preprompt, prompt):
    data = { 
    "messages": [ 
        { "role": "system", "content": preprompt },
        { "role": "user", "content": prompt }
    ], 
    "temperature": 0.5, 
    "max_tokens": 5,
    "stream": False
    }
    r = requests.post(url, json=data)
    content = re.search("\"content\":\s\"(.*)\"", r.text)
    return content.group(1)
    
(questionStatement, answers) = csv_parser.csvRead()