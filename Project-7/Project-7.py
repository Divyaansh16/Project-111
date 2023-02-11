import os
import shutil
from_dir=r"C:\Users\Secret user\Desktop\Web-Work\Whitehat Junior\Python\Project\Project-7\Downloads"
to_dir=r"C:\Users\Secret user\Desktop\Web-Work\Whitehat Junior\Python\Project\Project-7\Document_files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for i in list_of_files:
    name,extention=os.path.splitext(i)
    print(name)
    print(extention)