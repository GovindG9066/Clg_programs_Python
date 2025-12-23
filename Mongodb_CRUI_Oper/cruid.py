from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["Company_db"]                                         #Database
emp_col=db["EMP"]                                                 #Collection

sample_employees=[
    {"Emp_name":"Riddhi","Emp_Mobile":7854526521,"Sal":7000,"Age":28},
    {"Emp_name":"Arjun","Emp_Mobile":7896341022,"Sal":12000,"Age":32},
    {"Emp_name":"Manoj","Emp_Mobile":6325412558,"Sal":5500,"Age":25},
    {"Emp_name":"Radhika","Emp_Mobile":4568520123,"Sal":8000,"Age":30},
    {"Emp_name":"Sukumar","Emp_Mobile":9638527410,"Sal":4000,"Age":29}
]

if emp_col.count_documents({})==0:
    emp_col.insert_many(sample_employees)

print("Emp with salary between 5000 to 10000")

for emp in emp_col.find({"Sal":{"$gte":5000,"$lte":10000}}):
    print(emp)


new_mobile="7539511230"

emp_col.update_one({"Emp_name":"Riddhi"},{"$set":{"Emp_Mobile":new_mobile}})
print("Update mobile number :")
print(emp_col.find_one({"Emp_name":"Riddhi"}))

print("sort all emp according to age")

for emp in emp_col.find().sort("Age",1):
    print(emp)

print("Update Riddhi Age :") 
emp_col.update_one({"Emp_name":"Riddhi"},{"$set":{"Age":30}})
print(emp_col.find_one({"Emp_name":"Riddhi"}))

print("High Salary :")

high=emp_col.find().sort("Sal",-1).limit(1)
for i in high:
    print(i)