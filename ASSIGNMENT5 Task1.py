dict1 = {}
name = input()
marks = float(input())
dict1[name] = marks
print(dict1)
n = input()
if n in dict1:
    print(f"{n} marks: {marks}")
else:
    print("Student not found")