scores = ["78", "56", "67", "45"]
print("high score: ")
for i in range(len(scores)+1):
    print("{}. {}".format(i+1, numbers[i]))
newscores = int(input("New high score: "))
for i in range(len(scores)+1):
    print("{}. {}".format(i+1, numbers[i]))