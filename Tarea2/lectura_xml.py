import xml.etree.ElementTree as ET

print('Archivo xml')

tree = ET.parse('data1.xml')
root = tree.getroot()

for elem in root:
   for subelem in elem:
      print(subelem.text)
      print(type(subelem))


