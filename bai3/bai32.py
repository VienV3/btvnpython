#tuong tac voi file
import io
#ghi vao file
def write_file(file_name,ndung):
    f=io.open(file_name,"w",encoding="utf-8")
    f.write(ndung)
    f.close()
#ghi list ndung vao file
def write_file_from_list(file_name,list_lines):
    f=io.open(file_name,"w",encoding="utf-8")# w== ghi de
    f.write("\n".join(list_lines))
    f.close()
#ghi them noi dung moi vao file co san
def write_file_line(file_name,ndung_line):
    f=io.open(file_name,"a",encoding="utf-8")
    f.write("%s \n"%ndung_line)#viet them dong moi vao, a==ghi them    
    f.close()
#doc file 
def read_file(file_name):
    f=io.open(file_name,"r",encoding="utf-8")
    ndung=f.read()
    f.close()
    return ndung
#doc file xong chuyen thanh dang list
def read_file_list(file_name):
    f=io.open(file_name,"r",encoding="utf-8")
    ndung=f.read()
    f.close()
    return ndung.split("\n")

if __name__=="__main__":
#    file_name="abc.txt"
#   ndung="day la noi dung test \n dung la noi dug test"
#   write_file(file_name,ndung)

#   L=["dong3","dong4","dong2","dong3","dong1",]
#   #L=list(set(L))#loc trung khong theo thu tu
#  L=list(dict.fromkeys(L)) #loc trung theo th tu
#   file_name="abc2.txt"
#  write_file_from_list(file_name,L)


#   file_name="abc2.txt"
#   ndung_line="new line 1"
#   write_file_line(file_name,ndung_line)
##  ndung_line="new line 2"
#   write_file_line(file_name,ndung_line)
#   ndung_line="new line 3"
#   write_file_line(file_name,ndung_line)

    file_name="abc.txt"
   #data=read_file(file_name)
    L=read_file_list(file_name)