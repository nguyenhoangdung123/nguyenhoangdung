items = ["com","bun","pho","chao"]
print(items)
print(*items, sep=', ') #seperator
# index
print("Index 1")
print(items[1])
print("Index 2")
print(items[2])

# print("Index -1")
i = int(input("enter index: "))
print(items[-1])
print(*items, sep=', ')