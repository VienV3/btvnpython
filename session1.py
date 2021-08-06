#score=int(input("Nhap vao diem cua ban:"))
#if score<=5:
  #  print("hoc kem qua")
#elif score>5 and score<7:
 #   print("hoc trung binh")
#elif score>=7 and score < 9:
 #   print("hoc kha")
#elif score>=9:
#    print("hoc gioi.")
#else:
#    print("ky tu nhap khong hop le")
#import time
#dem = 0
#while True:
#    print("dem=",dem)
 #   dem +=1
 #   time.sleep(1)
 #   if dem > 5:
 #       break
#print("thoat chuong trinh!")
""" start=1
stop=10
step=2 
for i in range(start,stop,step):
    print("i",i)    """
""" L=["vu","van","vien"]
for index,name in enumerate(L):
    print("Index",index,"Name:",name) 

for index in range(0,len(L)):
    name=L[index]
    print("Index",index,"Name:",name) """

""" L=["Vu","van","vien","hoc","gioi"]
#L1=L[0:len(L):2]
L2=L[:-2]
print(L2) """
""" for i in range(1,10):
    if(i==5):
        break
    print("i=",i)
print("main") """
""" 
nhap vao so nguyen
a: tinh binh phuong so do, qua 1000 thi bao so to qua khong tinh duoc
b:tinh binh phuong tu 1->n
 """
x=int(input("Nhap vao so nguyen:"))
# cau a
kq=x**2
if kq<=1000:
    print("Binh Phuong La:%s"%kq)
else:
    print("so to qua khong tinh duoc")
#cau b
for m in range( 1 , x+1):
    kqc=m**2
    print("Binh phuong: %s"%kqc)
