from peewee import * 
import random

host="localhost"
db_name="bulk_insert"
db_user="root"
db_pass=""
db=MySQLDatabase(db_name,host=host,user=db_user,passwd=db_pass)
class Student(Model):
    #id=PrimaryKeyField()
    name=CharField()
    age=IntegerField()
    class Meta:
        database=db
if __name__=="__main__":
    #tao bang bang peewee schema
    """ Student.create_table()
    for i in range(30):
        print("i=",i)
        name=f"vien_{i}"
        age=random.randint(20,30)
        instane=Student(name=name,age=age)
        instane.save() """
    #size ?
    #list comprehensive
    data_soure=[
        {"name":f"vien_{i}","age":random.randint(20,30)}
        for i in range(10000)
    ]
    Student.insert_many(data_soure).execute()
    #56