import pygame;
import copy;
import itertools;
pygame.init();

winSize = (500,500);

win = pygame.display.set_mode(winSize);
pygame.display.set_caption("Sudoku");

white = (245,245,245);
gray = (200,200,200);
black = (0,0,0);
yellow = (255,211,0)

N = 9;
"""
board = [
    [0,5,0,0,7,6,2,0,9],
    [0,0,0,0,3,9,0,4,5],
    [3,9,7,0,0,0,0,0,1],
    [1,0,0,0,6,8,3,0,7],
    [9,8,3,0,0,1,0,0,0],
    [0,0,0,2,0,3,9,0,8],
    [5,4,0,0,1,2,8,0,3],
    [0,0,1,0,0,0,0,9,0],
    [0,0,6,3,0,0,0,0,0]

];
"""
board = [[0 for i in range(N)] for j in range(N)];
#board = [[0, 0, 0, 0, 3, 0, 0, 0, 0], [0, 0, 0, 0, [5, 6], 0, 0, 0, 0], [0, 0, 0, 0, [1, 4, 6, 9], 0, 0, 0, 0], [0, 0, 0, 0, 7, 0, 0, 0, 0], [0, 0, 0, 0, [6, 9], 0, 0, 0, 0], [0, 0, 0, 0, [2, 4, 5, 6], 0, 0, 0, 0], [0, 0, 0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, [5, 9], 0, 0, 0, 0], [0, 0, 0, 0, [9, 1, 4, 6], 0, 0, 0, 0]]
#board = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 6, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9]];

#board = [[0, 0, 8, 0, 7, 0, 0, 0, 9], [3, 0, 0, 1, 8, 0, 0, 0, 0], [0, 0, 0, 9, 0, 0, 0, 0, 2], [4, 0, 3, 0, 0, 0, 0, 1, 0], [8, 2, 0, 0, 0, 0, 0, 3, 4], [0, 7, 0, 0, 2, 4, 5, 0, 8], [6, 0, 0, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 9, 7, 0, 0, 1], [9, 0, 0, 0, 3, 0, 6, 0, 0]];
#board = [[[2, 5], [1, 4, 5, 6], 8, [2, 4, 5], 7, [2, 3, 5, 6], [1, 3, 4], [4, 5], 9], [3, 9, [2, 4, 5], 1, 8, [2, 5], [4, 7], [4, 5, 7], 6], [7, [1, 4, 5, 6], [1, 4, 5, 6], 9, [4, 5, 6], [3, 5, 6], [1, 3, 4], 8, 2], [4, [5, 6], 3, 8, [5, 6], 9, 2, 1, 7], [8, 2, [5, 6], 7, [1, 5, 6], [1, 5, 6], 9, 3, 4], [1, 7, 9, 3, 2, 4, 5, 6, 8], [6, [1, 4, 5], [1, 2, 4, 5, 7], [2, 4, 5], [1, 4, 5], 8, [4, 7], 9, 3], [[2, 5], 3, [2, 4, 5], 6, 9, 7, 8, [2, 4], 1], [9, 8, [1, 2, 4, 7], [2, 4], 3, [1, 2], 6, [2, 4, 7], 5]];#board = board = [[0 for i in range(N)] for i in range(N)];
# y-wing
#board = [[6, 3, [4, 7, 8], [4, 5, 7, 9], 2, [5, 7, 8, 9], 1, [4, 5, 7], [4, 5, 8]], [1, 9, [4, 7], 3, [4, 8], [5, 7], [2, 5, 7, 8], 6, [2, 4, 5]], [2, 5, [4, 7, 8], [1, 4, 7], 6, [1, 7, 8], 9, 3, [4, 8]], [3, 6, [2, 5], 8, 7, [2, 5], 4, 1, 9], [9, 7, [2, 5], 6, 1, 4, [2, 5], 8, 3], [8, 4, 1, [2, 5], 9, 3, [2, 5, 7], [2, 5, 7], 6], [[4, 5], 8, 9, [1, 2, 4], 3, [1, 2], 6, [2, 4, 5], 7], [[4, 5, 7], 2, 3, [4, 7], [4, 8], 6, [5, 8], 9, 1], [[4, 7], 1, 6, [2, 4, 7, 9], 5, [2, 7, 8, 9], 3, [2, 4], [2, 4, 8]]]
oldBoard = [board];
active = [-1,0];
pressed = False;
shift = False;
ctrl = False;

fonts = {}

def text(surface, fontFace, size, x, y, text, colour,center=False):
    if size in fonts:
        font = fonts[size]
    else:
        font = pygame.font.Font(fontFace, size)
        fonts[size] = font
    text = font.render(text, 1, colour)
    if(center):
        text_rect = text.get_rect(center=(x, y));
    else:
        text_rect = (x,y);

    surface.blit(text, text_rect)

def mouseHighlight():
    global active;
    for x in range(N):
        for y in range(N):
            width = winSize[1]/N;
            mouse = pygame.mouse.get_pos();
            if(x == active[0] and y == active[1]):
                pygame.draw.rect(win,yellow,(x*width,y*width,width,width));
                if(pygame.mouse.get_pressed()[0] and not pressed):
                    active = [-1,0];

            elif(mouse[0] > x*width and mouse[0] < (x+1)*width and
               mouse[1] > y*width and mouse[1] < (y+1)*width):
                pygame.draw.rect(win,gray,(x*width,y*width,width,width));

                if(pygame.mouse.get_pressed()[0] and not pressed):
                    active = [x,y];

def drawBoard():

    for i in range(1,N):
        y = i*winSize[0]/N
        x = i*winSize[1]/N
        width = 1;
        if(i%int(N**0.5)==0):
            width = 3;
        pygame.draw.line(win,black,(x,0),(x,winSize[1]),width);
        pygame.draw.line(win,black,(0,y),(winSize[0],y),width);

    for i in range(N):
        for j in range(N):
            if(not isinstance(board[i][j], list)):
                if(board[i][j] != 0):
                    y = (j+0.5)*winSize[0]/N;
                    x = (i+0.5)*winSize[1]/N;
                    text(win, None, 40, x, y, str(board[i][j]), black,True);
            else:
                for k in board[i][j]:
                    y = (j+(((k-1)//int(N**0.5))+1)/(N**0.5+1))*winSize[1]/N;
                    x = (i+(((k-1)%int(N**0.5))+1)/(N**0.5+1))*winSize[0]/N;
                    text(win, None, 15, x, y, str(k), black,True);
                    
def nextA(none):
    global active;
    if(not shift):
        active[0]+=1;
        if(active[0] >= N):
            active[0] = 0;
            active[1] += 1;
            if(active[1] >= N):
              active = [0,0];
    else:
        active[0]-=1;
        if(active[0] < 0):
            active[0] = N-1;
            active[1] -= 1;
            if(active[1] < 0):
              active = [N-1,N-1];

def up(none):
    global active;
    if(ctrl):
        pageUp(None);
        return 0;
    active[1] -= 1;
    if(active[1] < 0):
            active[1] = N-1;
def down(none):
    global active;
    if(ctrl):
        pageDown(None);
        return 0;
    active[1] += 1;
    if(active[1] >= N):
        active[1] = 0;
def left(none):
    global active;
    if(ctrl):
        home(None);
        return 0;
    active[0] -= 1;
    if(active[0] < 0):
        active[0] = N-1;
        
def right(none):
    global active;
    if(ctrl):
        end(None);
        return 0;
    active[0] += 1;
    if(active[0] >= N):
        active[0] = 0;

def end(none):
    global active;
    active[0] = N-1;

def home(none):
    global active;
    active[0] = 0;

def pageUp(none):
    global active;
    active[1] = 0;

def pageDown(none):
    global active;
    active[1] = N-1;

def noA(none):
    global active;
    active = [-1,0];
        
def alterBoard(nr):
    global board,oldBoard;      
    oldBoard.append(copy.deepcopy(board));
    if(active[0]==-1):
        return 0;
    if(not shift):
        board[active[0]][active[1]] = nr;
    else:
        if(isinstance(board[active[0]][active[1]], list)):
            if(nr not in board[active[0]][active[1]]):
                board[active[0]][active[1]].append(nr);
            else:
                board[active[0]][active[1]].remove(nr);
        elif(board[active[0]][active[1]] != 0):
            board[active[0]][active[1]] = [board[active[0]][active[1]],nr];
        else:
            board[active[0]][active[1]] = [nr];


def updatePress():
    global pressed;
    if(pygame.mouse.get_pressed()[0]):
        pressed = True;
    else:
        pressed = False;

def events(keys,func):
    if(1 not in keys):
        return 0
    for f in func:
        if(keys[f[0]]):
            f[1](f[2]);
            return 1;

    return 1;

def printBoard(none):
    print(board);

def regret(none):
    global board;
    if(ctrl and oldBoard != []):
        board = oldBoard.pop();

def row(y):
    possible = [];
    for x in range(N):
        if(board[x][y] not  in possible):
            if(isinstance(board[x][y], int)):
                possible.append(board[x][y]);
   
    return possible;

def col(x):
    possible = [];
    for y in range(N):
        if(board[x][y] not in possible):
            if(isinstance(board[x][y], int)):
                possible.append(board[x][y]);
            
    
    return possible;

def box(pos):
    n = int(N**0.5);
    pos = [pos[0]//n*n,pos[1]//n*n];
    possible = [];
    for x in range(n):
        for y in range(n):
             if(isinstance(board[x+pos[0]][y+pos[1]], int)):
                possible.append(board[x+pos[0]][y+pos[1]]);
    
    return possible;
   
def solveTile(pos):
    change = False;
    if(isinstance(board[pos[0]][pos[1]], int)):
        return 0;
    possible = board[pos[0]][pos[1]];
    for i in row(pos[1]):
        if(i  in board[pos[0]][pos[1]]):
            board[pos[0]][pos[1]].remove(i);
            change = True;
    for i in col(pos[0]):
        if(i  in board[pos[0]][pos[1]]):
            board[pos[0]][pos[1]].remove(i);
            change = True;
    for i in box(pos):
        if(i  in board[pos[0]][pos[1]]):
            board[pos[0]][pos[1]].remove(i);
            change = True;
    return change
    
    return possible;
def insertCorrect():
    change = False;
    for x in range(N):
        for y in range(N):
            if(isinstance(board[x][y], list) and len(board[x][y])==1):
                board[x][y] = board[x][y][0];
                change = True;
    return change;

def isInCol(x, ys,nr):
    for y in range(N):
        if(isinstance(board[x][y], list) and y not in ys):
            for i in board[x][y]:
                if(i == nr):
                    return True;
    return False;
       
def isInRow(y, xs,nr):
    for x in range(N):
        if(isinstance(board[x][y], list) and x not in xs):
            for i in board[x][y]:
                if(i == nr):
                    return True;
    return False;

def isInBox(positions,nr):
    n = int(N**0.5);
    startPos = [(positions[0][0]//n)*n,(positions[0][1]//n)*n];
    for x in range(n):
        for y in range(n):
            if(isinstance(board[x+startPos[0]][y+startPos[1]], list)\
               and [x + startPos[0], y + startPos[1]] not in positions):
                for i in board[x+startPos[0]][y+startPos[1]]:
                    if(i == nr):
                        return True;
    return False;

def simularNumbers(pos):
    numbers = [];
    for i in range(len(pos)-1):
        for j in pos[i+1]:
            if(j in pos[i]):
                numbers.append(j);
    return numbers;

def combineLists(lists):
    longList = [];
    for i in lists:
        for j in i:
            if j not in longList:
                longList.append(j);
    return longList;

        
def nakedNples(n):
    change = False;
    # Cols
    for x in range(N):
        for tiles in itertools.combinations(range(N), n):
            if (False not in [isinstance(board[x][y], list) for y in tiles]):
                possible = combineLists([board[x][y] for y in tiles]);
                if (len(possible) == n):
                    for y in range(N):
                        if(isinstance(board[x][y], list) and y not in tiles):
                            board[x][y] = [k for k in board[x][y] if k not in possible];
                            if(board[x][y] != possible):
                                change = True;

    # Row
    for y in range(N):
        for tiles in itertools.combinations(range(N), n):
            if (False not in [isinstance(board[x][y], list) for x in tiles]):
                possible = combineLists([board[x][y] for x in tiles]);
                if (len(possible) == n):
                    for x in range(N):
                        if(isinstance(board[x][y], list) and x not in tiles):
                            board[x][y] = [k for k in board[x][y] if k not in possible];
                            if(board[x][y] != possible):
                                change = True;

    #Box
    for boxN in range(N):
        sqN = int(N**(0.5))
        for tiles in itertools.combinations(range(N), n):
            positions = [[(boxN%sqN)*sqN + k%sqN, (boxN//sqN)*sqN + k//sqN] for k in tiles]
            if (False not in [isinstance(board[pos[0]][pos[1]], list) for pos in positions]):
                possible = combineLists([board[pos[0]][pos[1]] for pos in positions]);
                if (len(possible) == n):
                    for k in range(N):
                        x = (boxN%sqN)*sqN + k%sqN;
                        y = (boxN//sqN)*sqN + k//sqN;
                        if(isinstance(board[x][y], list) and [x, y] not in positions):
                            board[x][y] = [l for l in board[x][y] if l not in possible];
                            if(board[x][y] != possible):
                                change = True;

def hiddenNples(n):
    change = False;
    # Cols
    for x in range(N):
        for tiles in itertools.combinations(range(N), n):
            if (False not in [isinstance(board[x][y], list) for y in tiles]):
                possible = combineLists([board[x][y] for y in tiles]);
                for i in copy.deepcopy(possible):
                    if (isInCol(x, tiles, i)):
                            possible.remove(i);
                            
                if (len(possible) == n):
                    for y in tiles:
                        for i in copy.deepcopy(board[x][y]):
                            if(i not in possible):
                                board[x][y].remove(i);
                                change = True;
    # Row
    for y in range(N):
        for tiles in itertools.combinations(range(N), n):
            if (False not in [isinstance(board[x][y], list) for x in tiles]):
                possible = combineLists([board[x][y] for x in tiles]);
                for i in copy.deepcopy(possible):
                    if (isInRow(y, tiles, i)):
                            possible.remove(i);
                            
                if (len(possible) == n):
                    for x in tiles:
                        for i in copy.deepcopy(board[x][y]):
                            if(i not in possible):
                                board[x][y].remove(i);
                                change = True;

    #Box
    for boxN in range(N):
        sqN = int(N**(0.5))
        for tiles in itertools.combinations(range(N), n):
            positions = [[(boxN%sqN)*sqN + k%sqN, (boxN//sqN)*sqN + k//sqN] for k in tiles]
            if (False not in [isinstance(board[pos[0]][pos[1]], list) for pos in positions]):
                possible = combineLists([board[pos[0]][pos[1]] for pos in positions]);
                for i in copy.deepcopy(possible):
                    if (isInBox(positions, i)):
                            possible.remove(i);
                            
                if (len(possible) == n):
                    for pos in positions:
                        for i in copy.deepcopy(board[pos[0]][pos[1]]):
                            if(i not in possible):
                                board[pos[0]][pos[1]].remove(i);
                                change = True;
    return change;

def findXwingCol():
    y1 = 0;
    found = [];
    xs = [];
    for nr in range(1,N+1):
        for y in range(N):
            for x in range(N):
                if(isinstance(board[x][y], list)  and nr in board[x][y]):
                    xs.append(x);
                    y1 = y;
                    for x1 in range(x+1,N):
                        if(isinstance(board[x1][y], list)  and nr in board[x1][y]):
                            xs.append(x1);
                                
                    if(len(xs) != 2):
                        xs = [];
                        break;
                    else:
                        for y2 in range(y+1,N):
                            if(isinstance(board[xs[0]][y2], list)  and nr in board[xs[0]][y2] and\
                                isinstance(board[xs[1]][y2], list)  and nr in board[xs[1]][y2]):
                                count = 0;
                                for x1 in range(N):
                                    if(isinstance(board[x1][y2], list)  and nr in board[x1][y2]):
                                        count+=1;
                                for x1 in range(N):
                                    if(isinstance(board[x1][y1], list)  and nr in board[x1][y1]):
                                        count+=1;
                                if(count == 4):
                                    found.append([nr,xs,[y1,y2]]);
                                    xs = [];
                                    ys = [];
                                    break;  
    return found;

def findXwingRow():
    x1 = 0;
    found = [];
    ys = [];
    for nr in range(1,N+1):
        for x in range(N):
            for y in range(N):
                if(isinstance(board[x][y], list)  and nr in board[x][y]):
                    ys.append(y);
                    x1 = x;
                    for y1 in range(y+1,N-1):
                        if(isinstance(board[x][y1], list)  and nr in board[x][y1]):
                            ys.append(y1);
                                
                    if(len(ys) != 2):
                        ys = [];
                        break;
                    else:
                        for x2 in range(x+1,N):
                            if(isinstance(board[x2][ys[0]], list)  and nr in board[x2][ys[0]] and\
                                isinstance(board[x2][ys[1]], list)  and nr in board[x2][ys[1]]):
                                count = 0;
                                for y1 in range(N):
                                    if(isinstance(board[x2][y1], list)  and nr in board[x2][y1]):
                                        count+=1;
                                for y1 in range(N):
                                    if(isinstance(board[x1][y1], list)  and nr in board[x1][y1]):
                                        count+=1;
                                if(count == 4):
                                    found.append([nr,[x1,x2],ys]);
                                    xs = [];
                                    ys = [];
                                    break;  
    return found;
                        
def xwing():
    change = False
    foundCol = findXwingCol();
    if(len(foundCol) > 0):
        for fC in foundCol:
            xs = fC[1];
            ys = fC[2];
            for y in range(N):
                if(y not in ys and isinstance(board[xs[0]][y], list) and fC[0] in board[xs[0]][y]):
                    board[xs[0]][y].remove(fC[0]);
                    change = True;
                if(y not in ys and isinstance(board[xs[1]][y], list) and fC[0] in board[xs[1]][y]):
                    board[xs[1]][y].remove(fC[0]);
                    change = True;

    foundRow = findXwingRow();
    if(len(foundRow) > 0):
        for fR in foundRow:
            xs = fR[1];
            ys = fR[2];
            for x in range(N):
                if(x not in xs and isinstance(board[x][ys[0]], list) and fR[0] in board[x][ys[0]]):
                    board[x][ys[0]].remove(fR[0])
                    change = True;
                if(x not in xs and isinstance(board[x][ys[1]], list) and fR[0] in board[x][ys[1]]):
                    board[x][ys[1]].remove(fR[0]);
                    change = True;
    return change;
def rowInBox():
    change = False;
    sqn = int(N**0.5);
    for nr in range(1,N+1):
        
        for i in range(sqn):
            for j in range(sqn):
                row = -1;
                for x in range(sqn):
                    for y in range(sqn):
                        pos = [i*sqn+x,j*sqn+y];
                        if(isinstance(board[pos[0]][pos[1]], list) and nr in board[pos[0]][pos[1]]):
                            if(row == -1):
                                row = pos[0];
                            elif(row != pos[0]):
                                row = -2;
                if(row >= 0):
                    for y in range(N):
         
                        if((y//sqn) != j and \
                           isinstance(board[row][y], list) and nr in board[row][y]):
                            board[row][y].remove(nr);
                            change = True;
    return change
def colInBox():
    change = False;
    sqn = int(N**0.5);
    for nr in range(1,N+1):
        
        for i in range(sqn):
            for j in range(sqn):
                col = -1;
                for x in range(sqn):
                    for y in range(sqn):
                        pos = [i*sqn+x,j*sqn+y];
                        if(isinstance(board[pos[0]][pos[1]], list) and nr in board[pos[0]][pos[1]]):
                            if(col == -1):
                                col = pos[1];
                            elif(col != pos[1]):
                                col = -2;
                if(col >= 0):
                    for x in range(N):
                        if((x//sqn) != i and \
                           isinstance(board[x][col], list) and nr in board[x][col]):
                            board[x][col].remove(nr);
                            
                            change = True;
    return change;

def yWing():
    change = False;
    for x in range(N):
        for y in range(N):
            if(isinstance(board[x][y], list) and len(board[x][y]) == 2):
                
                for y1 in range(N):
                    if(isinstance(board[x][y1], list) and len(board[x][y1]) == 2 and y1 != y):
                        if(board[x][y][0] in board[x][y1] and board[x][y][0]):
                            if(exeYwing(y,y1,x,0)):
                                change = True;
                        if(board[x][y][1] in board[x][y1]):
                            if(exeYwing(y,y1,x,1)):
                                change = True;
    return change;

def exeYwing(y,y1,x,i):
    change = False;
    for x1 in range(N):
        if(isinstance(board[x1][y], list) and\
           len(board[x1][y]) == 2 and x1 != x\
           and board[x][y][(i+1)%2] in board[x1][y]):
            if(board[x1][y][0] in board[x][y1] and board[x1][y][0] not in board[x][y] and\
                isinstance(board[x1][y1], list) and board[x1][y][0] in board[x1][y1]):
                board[x1][y1].remove(board[x1][y][0]); 
                change = True;
            elif(board[x1][y][1] in board[x][y1] and board[x][y1][1] not in board[x][y] and\
                isinstance(board[x1][y1], list) and board[x1][y][1] in board[x1][y1]):
                board[x1][y1].remove(board[x1][y][1]); 
                change = True;
    return change;

def visibleTiles(pos):
    sqN = int(N**0.5);
    box = [(pos[0]//sqN)*sqN,(pos[1]//sqN)*sqN];
    boxList = [];
    for x in range(sqN):
        for y in range(sqN):
            boxList.append([box[0]+x,box[1]+y]);
    tiles = combineLists([[[pos[0],y] for y in range(N)],
                                     [[x,pos[1]] for x in range(N)],
                                      boxList]);
    tiles.remove(pos)
    
    return tiles;
                                    




def chain(master,origPos,prevPos,prevNum,depth,returnValue= False):
    if(depth > 10):
        return returnValue;
    posList = visibleTiles(prevPos);
    for x,y in posList:
        if(isinstance(board[x][y], list) and len(board[x][y]) == 2):
            
            if(prevNum in board[x][y]):
                if(master in board[x][y]):
                    posList1 = visibleTiles([x,y]);
                    posList2 = visibleTiles(origPos);
                        
                    for p in posList1:
                        if (p in posList2 and isinstance(board[p[0]][p[1]], list) and master in board[p[0]][p[1]]):
                            board[p[0]][p[1]].remove(master);
                            print("chain")
                    return returnValue;
                else:
                    
                    if(prevNum == board[x][y][0]):
                        chain(master,origPos,[x,y],board[x][y][1],depth+1,returnValue);
                    else:
                        chain(master,origPos,[x,y],board[x][y][0],depth+1,returnValue);
                
def chainMaster():
    change = False;
    for x in range(N):
        for y in range(N):
            if(isinstance(board[x][y], list) and len(board[x][y]) == 2):
                if(chain(board[x][y][0], [x,y], [x,y], board[x][y][1], 0)):
                    change = True;
                    
                if(chain(board[x][y][1], [x,y], [x,y], board[x][y][0], 0)):
                    change = True;
                    
    
    return change;
                    

def solve(none):
    
    if(insertCorrect()):
        solve(None);
    for x in range(N):
        for y in range(N):
            if(isinstance(board[x][y], list)):
                if(solveTile([x,y])):
                    print("solveTile")
                
    if(insertCorrect()):
        solve(None);
    elif(rowInBox()):
        print("Row In Box")
        solve(None);
    
 
    elif(colInBox()):
        print("Col In Box")
        solve(None);
        
    for n in range(1, 5):
        
        if(nakedNples(n)):
            print("nakedNples",n)
            solve(None);
        
        if(hiddenNples(n)):
            print("hiddenNples",n)
            solve(None);
    
    if(xwing()):
        print("X-Wing")
        solve(None);
        
    if(yWing()):
        print("Y-Wing")
        solve(None);
        
    if(chainMaster()):
        print("chain")
        solve(None);
    
    
def setup(none):
    for x in range(N):
        for y in range(N):
            if(board[x][y]==0):
                board[x][y]=[i+1 for i in range(N)]
def restart(none):
    global board;
    board = [[0 for i in range(N)] for j in range(N)];
    setup(None);

def main():
    global board,shift,ctrl
    tapp = True;
    while True:
        win.fill((245,245,245));
        mouseHighlight();
        updatePress();
        drawBoard();

        pygame.display.update();

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0;

        keys = pygame.key.get_pressed();
        shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT];
        ctrl = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL];

        func = [[pygame.K_TAB,nextA,None],
                [pygame.K_p,printBoard,None],
                [pygame.K_z,regret,None],
                [pygame.K_a,noA,None],
                [pygame.K_UP,up,None],
                [pygame.K_DOWN,down,None],
                [pygame.K_RIGHT,right,None],
                [pygame.K_LEFT,left,None],
                [pygame.K_END,end,None],
                [pygame.K_HOME,home,None],
                [pygame.K_PAGEUP,pageUp,None],
                [pygame.K_PAGEDOWN,pageDown,None],
                [pygame.K_SPACE,solve,None],
                [pygame.K_s,setup,None],
                [pygame.K_r,restart,None],
                [pygame.K_v,visibleTiles,active],
                [pygame.K_0,alterBoard,0],
                [pygame.K_1,alterBoard,1],
                [pygame.K_2,alterBoard,2],
                [pygame.K_3,alterBoard,3],
                [pygame.K_4,alterBoard,4],
                [pygame.K_5,alterBoard,5],
                [pygame.K_6,alterBoard,6],
                [pygame.K_7,alterBoard,7],
                [pygame.K_8,alterBoard,8],
                [pygame.K_9,alterBoard,9]];

        if(not tapp):
            tapp = events(keys,func);


        for f in func:
            if(keys[f[0]] == 1):
                tapp = True;
                break;
            else:
                tapp = False;



setup(None);
#print(simularNumbers([[4,5,8,9],[1,4,6,8]]));
print(main());
#print(combineLists([[4,5,8,9],[1,4,6,8],[2,3,8,9]]))
pygame.quit();
quit();
