#nhap tuoi tinh xem bao gio nguoi ta 100 tuoi
import datetime
nametext=input("Nhap ten cua ban:")
tuoinumber=int(input("nhap tuoi cua ban:"))
timenow=datetime.datetime.now()
print("Hom nay ngay: ",timenow.strftime("%d/%m/%Y"))
#nam bao nhieu thi ban 100 tuoi
howtime100=100-tuoinumber
yearnow=timenow.strftime("%Y")
""" year=datetime.timedelta(days=365)
whentime100=year*howtime100 """
#print(whentime100)
print("So nam de ban 100 tuoi la",howtime100)
#print("Vao nam "+str(time100)+" ban se 100 tuoi")
print("Ten cua ban la:", nametext)
print("Tuoi cua ban "+nametext+" la:",tuoinumber)
