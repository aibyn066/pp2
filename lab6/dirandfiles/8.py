import os
path = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles/test7.txt"

if not os.path.exists(path):
    print("Файл не существует")
else:
    if not os.access(path,os.W_OK):
        print("Нет доступа для удаления файла")
    else:
        os.remove(path)
        print(f"Файл успешно удалён.")

