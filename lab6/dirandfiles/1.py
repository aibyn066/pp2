import os
path = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6"
all_items = os.listdir(path)


for item in all_items:
    if os.path.isdir(os.path.join(path,item)):
        print(f"only dir= {item}")

for item in all_items:
    if  os.path.isfile(os.path.join(path,item)):
        print(f"only file= {item}")