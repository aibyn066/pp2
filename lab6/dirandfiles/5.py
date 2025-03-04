file_path = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles/task4.txt"
data = ["apple", "banana", "cherry"]

with open(file_path,"w") as a:
    for item in data:
        a.write(item + "\n")

print("Данные записаны в файл.")
