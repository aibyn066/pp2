import os

path = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles"

if os.path.exists(path):
    print(f"Путь существует: {path}")
  
    filename = os.path.basename(path)
    print(f"Имя файла: {filename}")
   
    directory = os.path.dirname(path)
    print(f"Папка: {directory}")
    
else:
    print("Путь не существует.")