import xml.etree.ElementTree as ET

mydoc = ET.parse('C:/Users/Pedro/Desktop/TFG/b/gt/all_topics.xml')

root = mydoc.getroot()

list_topics = []

for i in range(0,134):
    topic_number = root[i][0].text
    topic_name = root[i][1].text
    s=topic_number + " " + topic_name+"\n"
    list_topics.append(s)

count = 0

new_list_topics = []

while(count != 135):

    if(count < 123):
        new_list_topics.append(list_topics[count])

    if(count == 123):
        new_list_topics.append("124 NOT_EXIST\n")

    if(count > 123):
        new_list_topics.append(list_topics[count -1])

    count += 1

print(new_list_topics)