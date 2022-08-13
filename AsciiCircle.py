import math 

run = True
while(run):
    print("")
    Radius = int(input("Radius: "))
    print("")
    LeftLine = "//"
    RightLine = "\\\\"
    
    for y in range(-Radius, Radius + 1):
        Line = ""    
        LocationY = math.sqrt(Radius ** 2 - y * y)
        LocationY = round(LocationY)
        if y > 0:
            LeftLine, RightLine = "\\\\", "//"
        
        for x in range(-Radius, Radius + 1):
            LocationX = math.sqrt(Radius ** 2 - x * x)
            LocationX = round(LocationX)
            if x != LocationY and x != -LocationY and LocationX != -y and LocationX != y:
                Line += "  "
            else:
                if x != Radius and x!= -Radius:
                    X1 = math.sqrt(Radius ** 2 - (x - 0.5) ** 2)
                    X2 = math.sqrt(Radius ** 2 - (x + 0.5) ** 2)
                    Rise = X2 - X1
                    Angle = math.degrees(math.atan(Rise))
                    
                    if Angle > 22.5 and Angle < 67.5:
                        Line += LeftLine
                    elif Angle < -22.5 and Angle > -67.5:
                        Line += RightLine
                    elif Angle > 67.5 or Angle < -67.5:
                        Line += "||"
                    else:
                        Line += "=="
                else:
                    Line += "||"
        print(Line)
