import io
class File_interact:
    #constructor
    def __init__(self,file_name):
        self.file_name=file_name
    #dinh nghia ham ghi file
    def write_file(self,ndung):
        f=io.open(self.file_name,"w",encoding="utf-8")
        f.write(ndung)
        f.close()

    def write_file_from_list(self,list_lines):
        f=io.open(self.file_name,"w",encoding="utf-8")
        f.write("\n".join(list_lines))
        f.close()
    
    def write_file_line(self,ndung_line):
        f=io.open(self.file_name,"a",encoding="utf-8")
        f.write("%s\n"%ndung_line)
        f.close()
    
    def read_file(self):
        f=io.open(self.file_name,"r",encoding="utf-8")
        ndung=f.read()
        f.close()
        return ndung
    def read_file_list(self):
        f=io.open(self.file_name,"r",encoding="utf-8")
        ndung=f.read()
        f.close()
        return ndung.split("\n")
        





















""" 
def write_file(file_name,ndung):
    f=io.open(file_name,"w",encoding="utf-8")
    f.write(ndung)
    f.close()
def write_file_from_list(file_name,list_lines):
    f=io.open(file_name,"w",encoding="utf-8")
    f.write("\n".join(list_lines))
    f.close()
 """