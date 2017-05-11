try:
    from tkinter import *
except ImportError:
    from Tkinter import *
try:
    from tkinter.filedialog import askopenfilename
except ImportError:
    from tkFileDialog import askopenfilename
try:
    from tkinter.messagebox import *
except ImportError:
    from tkMessageBox import *

#    O = ball
#   # = wall
#   * = da box
#   X = gate
#   A = imoveablebox/do not put in game/ error/ lots of bugs
#   R = occupied gate
    

def makeLevel(string):
    p = []
    with open(string, 'r') as f:
        for line in f:
            line = line.strip()
            foo = []
            for i in line:
               foo.append(i)
            p.append(foo)
    return p

def findPlayer():
    for i in range(w):
        for j in range(h):
            if(p[j][i] == 'O'):
                return(i,j)

def daSquare(x, y, color):
    canvas.create_rectangle(x, y, x+wid, y+hei, fill=color)

def daDot(x, y, color):
    canvas.create_oval(x, y, x+wid, y+hei, fill=color)

def draw():
    canvas.delete("all")
    for i in range(wid, width, wid):
        canvas.create_line(i, 0, i, height)

    for i in range(hei, height, hei):
        canvas.create_line(0, i, width, i)

    for i in range(w):
        for j in range(h):
            if(p[j][i] == '#'):
                daSquare(i*wid, j*hei, "#252525")
            if(p[j][i] == 'O'):
                daDot(i*wid, j*hei, "red")
            if(p[j][i] == '*'):
                daSquare(i*wid, j*hei, "green")
            if(p[j][i] == 'X'):
                daSquare(i*wid, j*hei, "yellow")
            if(p[j][i] == 'A'):
                daSquare(i*wid, j*hei, "green")
                daDot(i*wid, j*hei, "red")
            if(p[j][i] == 'R'):
                daSquare(i*wid, j*hei, "pink")
            
            
def kill(event):
    root.destroy()

def deviation(x, y):
    #global ply_y, ply_x
    if(p[y][x] == 'O'):
        p[y][x] = ' '
    if(p[y][x] == 'A'):
        p[y][x] = 'X'

def shift_na(x, y):
    if(p[y][x] == 'X'):
        p[y][x] = 'A'
    if(p[y][x] == ' '):
        p[y][x] = 'O'

def deviation_stvar(x, y):
    if(p[y][x] == '*'):
        p[y][x] = ' '
    if(p[y][x] == 'R'):
        p[y][x] = 'X'
        
def shift_stvar_na(x, y):
    if(p[y][x] == ' '):
        p[y][x] = '*'
    if(p[y][x] == 'X'):
        p[y][x] = 'R'


def move(x, y):
#    print("Hey lul, remove this #")
    global ply_y, ply_x
    if(p[ply_y + y][ply_x + x] in allowed):
        deviation(ply_x, ply_y)
        ply_y += y
        ply_x += x
        shift_na(ply_x, ply_y)

    elif(p[ply_y + y][ply_x + x] in moving):
        if(p[ply_y + 2*y][ply_x + 2*x] in allowed):
            deviation_stvar(ply_x + x, ply_y + y)
            shift_stvar_na(ply_x + 2*x, ply_y + 2*y)
            deviation(ply_x, ply_y)
            ply_y += y
            ply_x += x
            shift_na(ply_x, ply_y)
            

def hookup():
    for i in p:
        for j in i:
            if(j == 'X'):
                return False
            elif(j == 'A'):
                return False
    return True

def movement(n):
    global ply_x, ply_y

    if(n == 'Up'):
        move(0, -1)

    elif(n == 'Down'):
        move(0, 1)

    elif(n == 'Left'):
        move(-1, 0)

    elif(n == 'Right'):
        move(1, 0)

    draw()
    if(hookup()):
        showinfo("You won!", "Congratulations, you won!")
        root.destroy()
    
    

def restart():
    global p
    global ply_x, ply_y
    p = makeLevel(level)
    ply_x, ply_y = findPlayer()
    draw()
    
    


def keyHandler(event):
    foo = event.keysym
    movement(foo)
    if(event.char == 'r'):
        restart()


def askLevel():
    top = Tk()
    top.withdraw()
    level = askopenfilename(initialdir = "level", filetypes = [('All files', '.*')], title = "Choose da level you want to play")
    top.destroy()

    try:
        return(makeLevel(level))
    except IOError:
        top = Tk()
        top.withdraw()
        if(askretrycancel("Error!", "There was an error trying to open your level. Do you want to try again?")):           
            try:
                return(askLevel())
            finally:
                top.destroy()
        else:
            top.destroy()
            return(False)
    
p = askLevel()
if(not p):
    pass
else:
    w = len(p[0])
    h = len(p)

    allowed = [' ', 'X']
    moving = ['*', 'R']


    max_width = 1000
    max_height = 1000


    wid = hei = 50

    if(wid*w > max_width or hei*h > max_height):
        wid = hei = min(max_width//w, max_height//h)
    width = wid * w
    height = hei * h



    ply_x, ply_y = findPlayer()





    root = Tk()
    root.title("Sokoban lul")
    root.focus_force()

    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw()

    root.bind_all("<Escape>", kill)
    root.bind_all("<Key>", keyHandler)

    root.mainloop()
