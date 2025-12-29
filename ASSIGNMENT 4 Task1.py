filename = "sample1.txt"
print("Starting program...")

try:
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"File '{filename}' not found.")


filename = "sample2.txt"
print("Starting program...")

try:
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"File '{filename}' not found.")