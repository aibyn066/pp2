first_file = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles/task4.txt"
second_file = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles/task7.txt"

with open(first_file, "r") as file:
    content = file.read()

with open(second_file, "w") as copy:
    copy.write(content)
