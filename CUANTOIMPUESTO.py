import fnmatch
import os
import xml.etree.ElementTree as ET
filesfound = []
importe = []
total = 0
#TODO hacer que lea de algún lugar la ruta
for file in os.listdir('.'):
    if fnmatch.fnmatch(file,'*.xml'):
        filesfound += file.split('\n')
#print (filesfound)
for i in range (len(filesfound)):
    tree = ET.parse ('.' + filesfound[i])
    root = tree.getroot()
    for child in root[3][0][2]:
        importe = child.attrib
        print (importe['Concepto'] + " " + importe['Importe'])
        total += float(importe['Importe'])       
print ("%s%d " % ("Gran Total: ", total))
