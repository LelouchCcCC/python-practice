import json
data = [{'name': 123}, {'sex': 'male'}, {'gender': 'ok'}]
data2 = {'mei': 241}
data = json.dumps(data)
data2 = json.dumps(data2)

print(data, type(data))
print(data2, type(data2))

class student:
    name = None
    gender = None

stu_1 = student()
stu_1.name = 'qweqw'
stu_1.gender = 'fd'
print(stu_1.gender)

