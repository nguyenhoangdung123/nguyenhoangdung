player = {
    "x": 1,
    "y": 2
}
escape = {
    "x": 2,
    "y": 3
}
key = {
    "x": 4,
    "y": 4
}

flag = False
while True:
    for i in range(4):
        for j in range(4):
            if(i == player["y"] - 1) and (j == player["x"] -1):
                print("P",end=" ")
            elif(i == escape["y"] - 1) and (j == escape["x"] - 1):
                print("E",end=" ")
            elif(i == key["y"] - 1) and (j == key["x"] - 1):
                if flag == False:
                print("K",end=" ")
                else:
                    print("-",end=" ")
            else:
                print("-",end=" ")
            
        print()

    move = input("A S D W ?").lower()
    if move == "w":
        player["y"] -= 1
        if player["y"] == 1:
            print("out of move !!!!!")
            player["y"] += 1
    elif move == "a":
        player["x"] -= 1
         if player["x"] == 1:
            print("out of move !!!!!")
            player["y"] += 1
    elif move == "s":
        player["y"] += 1
         if player["y"] > 4:
            print("out of move !!!!!")
            player["y"] -= 1
    elif move == "d":
        player["x"] += 1
         if player["x"] > 4:
            print("out of move !!!!!")
            player["y"] -= 1
    if(player["x"] == key["x"]) and ((player["y"] == key["y"])):
        print("Found key !!!!!")
        flag = True

    if(player["x"] == key["x"]) and ((player["y"] == key["y"])):
        if flag == False:
            print("need key !!!")
        else:
            print("you won !!!")
            for i in range(4):
                for i in range(4):
        for j in range(4):
            if(i == player["y"] - 1) and (j == player["x"] -1):
                print("P",end=" ")
            elif(i == escape["y"] - 1) and (j == escape["x"] - 1):
                print("E",end=" ")
            elif(i == key["y"] - 1) and (j == key["x"] - 1):
                if flag == False:
                print("K",end=" ")
                else:
                    print("-",end=" ")
            else:
                print("-",end=" ")
            
        print()


