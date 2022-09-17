import math
import random

Width = 10
Height = 10

Hoopx = random.randint(0, Width)
Hoopy = random.randint(0, Height)

Distance = 5
c = 5

Loop = True
while Loop:
    h = Distance / 2
    k = math.sqrt((c**2) - (h)**2)
    a = (0 - k) / (Distance - h)**2

    for y in range(Height, 0 - 1, -1):
        Line = '[]'

        for x in range(0, Width + 1):
            Quadratic = (a * (x - h)**2) + k
            RoundFactored = round(Quadratic)
            if y == RoundFactored:
              Line += "{}"
            elif x == Hoopx and y == Hoopy:
              Line += "[]"
            else:
              Line += "  "
        print(Line)

    Floor = "  []" + "[]" * Width
    print(Floor)
    print('Strength: ' + str(c))
    print('Distance: ' + str(Distance))
    Input = input("Input: ")
    Input = Input.lower()
  
    if Input == 'd' and c**2 - ((Distance + 1) / 2)**2 > 0 and Distance < Width:
        Distance += 1
    elif Input == 'a' and Distance > 2 and math.sqrt(((c + 1)**2) - (h)**2) <= Height:
        Distance -= 1
    elif Input == 'w' and math.sqrt(((c + 1)**2) - (h)**2) <= Height:
        c += 1
    elif Input == 's' and (c - 1)**2 - (Distance / 2)**2 > 0:
        c -= 1
    elif Input == 'p':
      QuadraticTest = (a * (Hoopx - h)**2) + k
      if round(QuadraticTest) == Hoopy:
        break

print('')
print('You Scored!')
