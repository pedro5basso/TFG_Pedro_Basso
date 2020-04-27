import xml.etree.ElementTree as ET

mydoc = ET.parse('C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.xml')

root = mydoc.getroot()

for i in range(0,134):
    topic_number = root[i][0].text
    topic_name = root[i][1].text
    print(topic_number + " " + topic_name)