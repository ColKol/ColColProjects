def Level(Width, Height, PlayerPos, BoxPos, LevelName):
    PlayerOrigin = PlayerPos.copy()
    BoxOrigin = BoxPos.copy()
    
    RunLevel = True
    while RunLevel:
        print("")
        print("Level " + str(LevelName))
        for y in range(Height):
            Line = ""
            for x in range(Width):
                Coord = str(x) + "," + str(y)
                if Coord in Walls:
                    Line += "||"
                elif x == PlayerPos[0] and y == PlayerPos[1]:
                    Line += "{}"
                elif x == BoxPos[0] and y == BoxPos[1]:
                    Line += "[]"
                elif x == FinishPos[0] and y == FinishPos[1]:
                    Line += "::"
                else:
                    Line += "  "
            print(Line)

        if BoxPos[0] == FinishPos[0] and BoxPos[1] == FinishPos[1]:
            break
        
        Input = input("Input: ")
        Input = Input.lower()

        MovePos = PlayerPos.copy()
        BoxMovePos = BoxPos.copy()
        
        if Input == "w":
            MovePos[1] -= 1
        elif Input == "a":
            MovePos[0] -= 1
        elif Input == "s":
            MovePos[1] += 1
        elif Input == "d":
            MovePos[0] += 1
        elif Input == "r":
            PlayerPos = PlayerOrigin.copy()
            MovePos = PlayerPos.copy()
            BoxPos = BoxOrigin.copy()
            BoxMovePos = BoxPos.copy()
        
        if MovePos == BoxPos:
            BoxMovePos[0] += MovePos[0] - PlayerPos[0]
            BoxMovePos[1] += MovePos[1] - PlayerPos[1]
        
        MoveCoord = str(MovePos[0]) + "," + str(MovePos[1])
        BoxCoord = str(BoxMovePos[0]) + "," + str(BoxMovePos[1])
        
        if MoveCoord not in Walls and BoxCoord not in Walls:
            PlayerPos = MovePos.copy()
            BoxPos = BoxMovePos.copy()
    print("")
    print("Level Completed!")

def Menu():
    SelectedLevel = 1
    LevelNumber = 3
    RunMenu = True
    while RunMenu:
        Line = ""
        for x in range(1, LevelNumber + 1):
            if x == SelectedLevel:
                Line += "[" + str(x) + "]"
            else:
                Line += " " + str(x) + " "
        print("")
        print("Level Select")
        print(Line)
        Input = input("Input: ")
        Input = Input.lower()
        if Input == 'a' and SelectedLevel > 1:
            SelectedLevel -= 1
        elif Input == 'd' and SelectedLevel < LevelNumber:
            SelectedLevel += 1
        elif Input == 'p':
            return SelectedLevel

GameLoop = True
while GameLoop:
    SelectedLevel = Menu()
    if SelectedLevel == 1:
        Width = 9
        Height = 5
        PlayerPos = [2,2]
        BoxPos = [4,2]
        FinishPos = [6,2]
        Walls = ['0,0','1,0','2,0','3,0','4,0','5,0','6,0','7,0','8,0','0,1','8,1','0,2','8,2','0,3','8,3','0,4','1,4','2,4','3,4','4,4','5,4','6,4','7,4','8,4']
        Level(Width, Height, PlayerPos, BoxPos, SelectedLevel)
        
    elif SelectedLevel == 2:
        Width = 6
        Height = 6
        PlayerPos = [1,3]
        BoxPos = [2,3]
        FinishPos = [4,3]
        Walls = ["2,0","3,0","4,0",'5,0','0,1','1,1','2,1','5,1','0,2','5,2','0,3','3,3','5,3','0,4','3,4','4,4','5,4','0,5','1,5','2,5','3,5']
        Level(Width, Height, PlayerPos, BoxPos, SelectedLevel)
    
    elif SelectedLevel == 3:
        Width = 9
        Height = 8
        PlayerPos = [1,3]
        BoxPos = [3,3]
        FinishPos = [7,4]
        Walls = ['4,0','5,0','6,0','7,0','8,0','0,1','1,1','2,1','3,1','4,1','8,1','0,2','8,2','0,3','2,3','4,3','6,3','7,3','8,3','0,4','4,4','8,4','4,4','8,4','0,5','1,5','2,5','3,5','7,5','8,5','3,6','7,6','3,7','4,7','5,7','6,7','7,7']
        Level(Width, Height, PlayerPos, BoxPos, SelectedLevel)
