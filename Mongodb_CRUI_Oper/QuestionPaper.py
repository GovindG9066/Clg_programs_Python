from pymongo import MongoClient

Client=MongoClient("mongodb://27017")
db=Client["College1"]
Student=db["Student"]

Student_data=[
    {"Roll_no":21,"Name":"Ram","Course":"MCA","Marks":82,"Grade":9},
    {"Roll_no":91,"Name":"Sham","Course":"BBA","Marks":66,"Grade":10},
    {"Roll_no":30,"Name":"Manu","Course":"MCA","Marks":85,"Grade":8},
    {"Roll_no":45,"Name":"Kumar","Course":"BSC","Marks":92,"Grade":8},
    {"Roll_no":62,"Name":"Manisha","Course":"BCA","Marks":91,"Grade":7}
]

if Student.count_documents({})==0:
    Student.insert_many(Student_data)

for stu in Student.find():
    print(stu)