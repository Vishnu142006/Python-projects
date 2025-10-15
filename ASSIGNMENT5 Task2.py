n = int(input())
list1 = list(map(int,input().split()))
print("Original list:",list1)
a = list1[0:5]
print("Extracted first five elements:", list(a))

a.reverse()
print("Reversed extracted elements:",a)