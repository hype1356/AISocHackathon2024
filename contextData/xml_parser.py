import re
import lxml.etree as ET

tree = ET.parse("./")

# <span class="SECTION PART-SECTION">
# data = [] #array of lines to output for embeddings (one element = one line)
# lines = file.readlines() #file's lines
# lineNumber = 0

# # increment lineNumber
# def nextLine():
#     global lineNumber
#     lineNumber += 1

# #readSection() to read a whole section
# def readSection():
#     indent = 1
#     while(indent > 0):
#         line = lines[lineNumber]
#         closeSpan = re.findall("(</span>)", line) #span by itself
#         openSpan = re.findall("(<span class=)", line)
#         indent += len(openSpan)
#         indent -= len(closeSpan)
#         nextLine()
#     return ""
        
#     # while(indent > 0):
#     #     line = lines[lineNumber]
#     #     closeSpan = re.search("</span>", line) #span by itself
#     #     openSpan = re.search("<span class=", line)
#     #     if(closeSpan):
#     #         # print("CLOSE")
#     #         if(openSpan):
#     #             pass
#     #         else:
#     #             indent -= 1
#     #         nextLine()
#     #         continue
#     #     if(openSpan):
#     #         # print("OPEN")
#     #         indent += 1
#     #         nextLine()
#     #         continue
#     #     nextLine()
#     # return ""
        

# while(lineNumber < len(lines)):
#     line = lines[lineNumber]
    
#     sectionSpan = re.search("<span class=\"SECTION PART-SECTION\">", line)
#     if(sectionSpan):
#         nextLine()
#         data.append(readSection()) #append string return to data array
#         continue
#     nextLine()
    
