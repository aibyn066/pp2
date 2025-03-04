import os

path = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles"


if os.path.exists(path):
    print(f"Путь существует: {path}")

    print(f"Читаемый: {'Да' if os.access(path, os.R_OK) else 'Нет'}")
    print(f"Записываемый: {'Да' if os.access(path, os.W_OK) else 'Нет'}")
    print(f"Исполняемый: {'Да' if os.access(path, os.X_OK) else 'Нет'}")
else:
    print(f"Путь не существует: {path}")