import re

pattern = re.compile("\[[0-9]{1,2}[\.\/][0-9]{1,2}[\.\/][0-9]{4}, [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\] .+:")

with open("filename", mode="r", encoding="utf-8") as file:
    text = file.read()
counterDict = dict({})
lines = re.findall(pattern, text)
for line in lines:
    phone = line.split('] ')[1].split(':')[0].strip()
    if "הנושא" in phone:
        continue
    if counterDict.get(phone) is None:
        counterDict[phone] = 1
    else:
        counterDict[phone] += 1
sortedDict = dict((sorted(counterDict.items(), key=lambda item: item[1])))
average = 0
counter = 0
for key in sortedDict.keys():
    print(key, sortedDict[key])
    average += sortedDict[key]
    counter += 1

average = int(average / counter)
print(f"average messages per person: {average}")
