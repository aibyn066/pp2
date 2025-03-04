
file_path = "/Users/ajbynkumargali/Desktop/projects_pp2/lab6/dirandfiles/task4.txt"
with open(file_path,"r") as a:
    line_counter=len(a.readlines())
print(line_counter)