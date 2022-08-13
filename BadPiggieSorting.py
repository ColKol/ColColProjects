import pygame
import random
print()
print('1: Bubble Sort')
print('2: Insertion Sort')
print('3: Selection Sort')
print('4: Merge Sort')
SortType = int(input("Sorting Algorithm: "))
print()
ListLength = int(input("List Length: "))
List = []

for i in range(ListLength):
    List.append(i)
SortedList = List.copy()
random.shuffle(List)

if SortType == 1:#BubbleSort
    pos = 0
    iteration = 1
    def Algorithm():
        global pos
        global iteration
        global Birdx
        Birdx.insert(0, pos)
        Birdx.insert(1, pos + 1)
        V1 = List[pos]
        V2 = List[pos + 1]
        if V1 > V2:
            List[pos] = V2
            List[pos + 1] = V1
        pos += 1
        if pos == ListLength - iteration:
            pos = 0
            iteration += 1
elif SortType == 2:#InsertionSort
    pos = 2
    iteration = 1
    def Algorithm():
        global pos
        global iteration
        global Birdx
        if pos == 0:
            iteration += 1
            pos = iteration
        else:
            pos -= 1
        V1 = List[pos]
        V2 = List[pos - 1]
        Birdx.insert(0, pos)
        Birdx.insert(1, pos - 1)
        if V1 > V2 or pos == 0:
            pos = 0
        elif V1 < V2:
            List[pos] = V2
            List[pos - 1] = V1
elif SortType == 3:#SelectionSort
    pos = 0
    ite = 0
    Lowest = ListLength
    LowestPos = 0
    Comparing = True
    def Algorithm():
        global pos
        global ite
        global Lowest
        global LowestPos
        global Birdx
        Birdx.insert(0, LowestPos)
        Birdx.insert(1, pos + ite)
        if pos + ite > ListLength - 1:
            List[LowestPos] = List[ite]
            List[ite] = Lowest
            ite += 1
            pos = 0
            Lowest = ListLength
        else:
            V1 = List[ite + pos]
            if V1 < Lowest:
                Lowest = V1
                LowestPos = pos + ite
            pos += 1
#Very Bad
elif SortType == 4:#MergeSort
    pos = 0
    oldpos = 0
    MergeSize = 1
    CopyList = List.copy()
    Merger = []
    Merge1 = []
    Merge2 = []
    CopyMerger = []
    SortState = 1
    def Algorithm():
        global SortState
        global Merge1
        global Merge2
        global MergeSize
        global CopyList
        global CopyMerger
        global pos
        global oldpos
        global ListLength
        global Birdx
        if SortState == 1:
            if len(CopyList) >= MergeSize * 2:
                for i in range(MergeSize * 2):
                    if i < MergeSize:
                        Merge1.append(CopyList[0])
                    else:
                        Merge2.append(CopyList[0])
                    del CopyList[0]
            else:
                Merge1 = CopyMerger
                Merge2 = CopyList
            SortState = 2
        elif SortState == 2:
            if Merge1 == []:
                Merger.extend(Merge2)
                Merge2 = []
                oldpos = pos
                SortState = 3
            elif Merge2 == []:
                Merger.extend(Merge1)
                Merge1 = []
                oldpos = pos
                SortState = 3
            else:
                V1 = Merge1[0]
                V2 = Merge2[0]
                Birdx.insert(0, List.index(V1))
                Birdx.insert(1, List.index(V2))
                if V1 < V2:
                    Merger.append(Merge1[0])
                    del Merge1[0]
                else:
                    Merger.append(Merge2[0])
                    del Merge2[0]
            CopyMerger = Merger.copy()
        else:
            if pos > ListLength - 1 or oldpos > ListLength - 1:
                pos = 0
                MergeSize *= 2
                CopyList = List.copy()
                SortState = 1
            elif len(Merger) > 0:
                ReplacePos = List.index(Merger[0])
                if len(CopyList) >= MergeSize * 2:
                    List[ReplacePos] = List[pos]
                    List[pos] = Merger[0]
                    Birdx.insert(0, pos)
                    pos += 1
                else:
                    List[ReplacePos] = List[oldpos]
                    List[oldpos] = Merger[0]
                    Birdx.insert(0, oldpos)
                    oldpos += 1
                Birdx.insert(1, ReplacePos)
                del Merger[0]
            else:
                SortState = 1

WIDTH = 1280
HEIGHT = 720
FPS = 30
piglength = round(WIDTH / ListLength)
maxheight = round(HEIGHT / 3 * 2)
background = pygame.image.load('INSERT FILE PATH')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

class Pig(pygame.sprite.Sprite):
    def __init__(self, order, pHeight):
        super().__init__()
        self.image = pygame.image.load('INSERT FILE PATH')
        self.image = pygame.transform.scale(self.image, (piglength, round(maxheight / ListLength * pHeight)))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH / ListLength * order
        self.rect.bottom = HEIGHT
        self.value = List[order]
    def update(self):
        position = List.index(self.value)
        self.rect.left = WIDTH / ListLength * position

Birdx = [WIDTH, WIDTH]
class Bird(pygame.sprite.Sprite):
    def __init__(self, Bid):
        super().__init__()
        self.image = pygame.image.load('INSERT FILE PATH')
        self.image = pygame.transform.scale(self.image, (piglength, round(HEIGHT / 3)))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.id = Bid
    def update(self):
        self.rect.left = WIDTH / ListLength * Birdx[self.id]

#create sprites
all_sprites = pygame.sprite.Group()
for e in range(ListLength):
    pigheight = (List[e] + 1)
    all_sprites.add(Pig(e, pigheight))
for e in range(2):
    all_sprites.add(Bird(e))

#initialise Pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Vizualizer")
clock = pygame.time.Clock()

pygame.mixer.music.load('INSERT FILE PATH')
pygame.mixer.music.play(-1)

#LOOP
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False       
    #run algorithm
    if List != SortedList:
        Algorithm()
    #update and render
    all_sprites.update()
    screen.blit(background, (0,0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
