from peewee import *
import random
host="localhost"
db_name="bulk_insert"
db_user="root"
db_pass=""
db=MySQLDatabase(db_name,host=host,user=db_user,passwd=db_pass)

#schema
class Score(Model):
    sbd=CharField()
    toan=FloatField()
    van=FloatField()
    anh=FloatField()
    class Meta:
        database=db

if __name__=="__main__":
    Score.create_table()
    
    