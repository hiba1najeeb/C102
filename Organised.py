import os
import shutil 
from_dir = "C:/Users/user/Downloads/C102_assets-main/C102_assets-main"
to_dir = "C:/Users/user/Downloads/test"
list_of_files = os.listdir(from_dir)

for fname in list_of_files:
    name,extension = os.path.splitext(fname)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpeg','.jpg','.jfif']:
        path1 = from_dir+'/'+fname
        path2 = to_dir+'/'+"image"
        path3 =to_dir+'/'+"image"+'/'+fname
        if os.path.exists(path2):
            print("moving"+fname+"...........")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+fname+"...........")
            shutil.move(path1,path3)

    