import os, sys
from shutil import copyfile
import xml.etree.ElementTree as ET

# Open a file
path = "./images"
dirs = os.listdir( path )

for name in dirs:
    file_name = name.partition('.')
    try:
        new_file = './images/annotations/' + file_name[0] + '.xml'
        copyfile('./images/annotations/20171117211540.xml', new_file)

        tree = ET.parse(new_file)
        root = tree.getroot()
        for filename in root.iter('filename'):
            filename.text = name
            filename.set('updated', 'yes')
        tree.write(new_file)

    except:
        pass
