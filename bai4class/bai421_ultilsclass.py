from bai42 import *
#tao instant class moi
file_interact1=File_interact("code.html")
ndung="hello cac ban \n minh la vien"
file_interact1.write_file(ndung)

list_lines=["1","2","3","4","5"]
file_interact1.write_file_from_list(list_lines)