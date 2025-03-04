import os
path = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles"

newdir = os.path.join(path,'for6task')
if not os.path.exists(newdir):
    os.mkdir(newdir)
    print('Папка создана')

for i in range(26):  
    letter = chr(65 + i)
    file_path = os.path.join(newdir, f"{letter}.txt")

    with open(file_path,"w") as a:
        a.write(f'hello {letter}')