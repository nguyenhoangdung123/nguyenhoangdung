scores = ["78", "56", "67", "45"]
print("high score: ")
for i in range(len(scores)+1):
    print("{}. {}".format(i+1, numbers[i]))
newscore = int(input("New high score: "))
scores.append(newscore)
score.sort(reverse=True)
for i in range(len(scores)+1):
    print("{}. {}".format(i+1, numbers[i]))