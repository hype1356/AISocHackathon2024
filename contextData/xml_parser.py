import lxml.etree as ET
import re

tree1 = ET.parse("./contextData/vol1.xml")
tree2 = ET.parse("./contextData/vol2.xml")
tree3 = ET.parse("./contextData/vol3.xml")
tree4 = ET.parse("./contextData/vol4.xml")
tree5 = ET.parse("./contextData/vol5.xml")

output = open("./contextData/output", "w")

new_root = ET.Element("combined_data")

for tree in [tree1, tree2, tree3, tree4, tree5]:
    for child in tree.getroot():
        new_root.append(child)

tree = ET.ElementTree(new_root)

target_section = tree.xpath("//SECTION")
def prettyToString(section):
    str2 = re.sub(r"(^\s+)|(\n)", "", ET.tostring(section, encoding="unicode", method="text"))
    str1 = re.sub(r"\s{2,}", " ", str2)
    str = re.sub(r"\[.*?\]", "", str1)
    return str

#TEMP TO DELETE
def dirtyToString(section):
    return ET.tostring(section, encoding="unicode")

def oneOne(section):
    ps = section.xpath(".//NOTE") + section.xpath(".//P")[1:]
    ps = list(map(lambda p : prettyToString(p), ps))
    for i in range(len(ps) - 1, 0, -1):
        paren = re.search("^\(", ps[i])
        if(paren):
            ps[i - 1] += ps[i]
            ps.pop(i)
    for p in ps:
        output.write(p + "\n")

def oneTwo(section):
    ps = section.xpath(".//P")[1:]
    for p in ps:

        output.write(prettyToString(p) + "\n")

oneOne(target_section[0])
oneTwo(target_section[1])

for section in target_section[2:]:
    str = prettyToString(section)
    output.write(str + "\n")