import xml.etree.cElementTree as ET

f = open("order.xml", encoding="UTF-8")
string = f.read()
tree = ET.ElementTree(ET.fromstring(string))
root = tree.getroot()
# print(root.tag)
# print(root.text)
for child in root:
    print("tag: ", child.tag, "text: ", child.text)
f.close()