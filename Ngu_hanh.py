from tkinter import *
import random
root = Tk()
root.title("Ngũ Hành")
width = 525
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)
root.config(bg="#006699")

player_earth = PhotoImage(file='E:/Q/earth-user.png')
player_fire = PhotoImage(file='E:/Q/fire-user.png')
player_metal = PhotoImage(file='E:/Q/metal-user.png').subsample(5)
player_water = PhotoImage(file='E:/Q/water-user.png')
player_wood = PhotoImage(file='E:/Q/wood-user.png')

comp_earth = PhotoImage(file = 'E:/Q/earth-comp.png')
comp_fire = PhotoImage(file = 'E:/Q/fire-comp.png')
comp_metal = PhotoImage(file = 'E:/Q/metal-comp.png').subsample(5)
comp_water = PhotoImage(file = 'E:/Q/water-comp.png')
comp_wood = PhotoImage(file = 'E:/Q/wood-comp.png')

start = PhotoImage(file = 'E:/Q/start.png').subsample(5)
win = PhotoImage(file = 'E:/Q/win.png').subsample(5)
draw = PhotoImage(file = 'E:/Q/draw.png').subsample(5)
lose = PhotoImage(file = 'E:/Q/lose.png').subsample(5)

player_img = Label(root, image = player_earth,bg = '#4080bf')
player_img.grid(row = 2,column = 1,padx = 30,pady =30)
comp_img = Label(root,image = comp_earth,bg = '#4080bf')
comp_img.grid(row = 2, column = 3,padx = 30,pady =30)
# Lbl Player
lbl_player = Label(root, font = ("Arial", 15),text = 'Player',bg='#0088cc',fg='white')
lbl_player.grid(row =1,column =1)
# Lbl Comp
lbl_comp = Label(root, font = ("Arial", 15),text = 'Computer',bg='#0088cc',fg='white')
lbl_comp.grid(row =1,column =3)
# Score
player_score = Label(root, text = '0', font = ('Arial', 30),bg='#0088cc',fg = 'white')
breaklbl = Label(root,text='-',font=('Arial',30),bg = '#0088cc',fg = 'white')
comp_score = Label(root, text = '0',font=('Arial',30),bg='#0088cc',fg='white')
player_score.grid(row=3,column=1)
breaklbl.grid(row=3,column=2)
comp_score.grid(row=3,column=3)
#Message
msg = Label(root, font = ("Arial", 15),bg='#0088cc',fg='white')
msg.grid(row=2,column=2)
msg.configure(image=start)

#Update Player Score
def updatePlayerScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = score
#Update Computer Score
def updateCompScore():
    score = int(comp_score['text'])
    score += 1
    comp_score['text'] = score
#Logic
def Earth():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_earth)
    MatchProcess()

def Fire():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_fire)
    MatchProcess()

def Metal():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_metal)
    MatchProcess()

def Water():
    global player_choice
    player_choice = 4
    player_img.configure(image=player_water)
    MatchProcess()

def Wood():
    global player_choice
    player_choice = 5
    player_img.configure(image=player_wood)
    MatchProcess()

def MatchProcess():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_img.configure(image=comp_earth)
        ComputerEarth()
    elif comp_choice == 2:
        comp_img.configure(image=comp_fire)
        ComputerFire()
    elif comp_choice == 3:
        comp_img.configure(image=comp_metal)
        ComputerMetal()
    elif comp_choice == 4:
        comp_img.configure(image=comp_water)
        ComputerWater()
    else:
        comp_img.configure(image=comp_wood)
        ComputerWood()
#
def ComputerEarth():
    if player_choice == 4:
        msg.configure(image = win)
    elif player_choice == 5:
        msg.configure(image = lose)
        updatePlayerScore()
    else:
        msg.configure(image = draw)
        updateCompScore()

def ComputerFire():
    if player_choice == 3:
        msg.configure(image = win)
        updateCompScore()
    elif player_choice == 4:
        msg.configure(image=lose)
    else:
        msg.configure(image = draw)
        updatePlayerScore()

def ComputerMetal():
    if player_choice == 5:
        msg.configure(image = win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image = lose)
        updateCompScore()
    else:
        msg.configure(image=draw)

def ComputerWater():
    if player_choice == 2:
        msg.configure(image = win)
        updateCompScore()
    elif player_choice == 1:
        msg.configure(image=lose)
    else:
        msg.configure(image = draw)
        updatePlayerScore()

def ComputerWood():
    if player_choice == 1:
        msg.configure(image = win)
        updatePlayerScore()
    elif player_choice == 3:
        msg.configure(image = lose)
        updateCompScore()
    else:
        msg.configure(image=draw)

def ExitApp():
    root.destroy()
    exit()

sm_player_earth = player_earth.subsample(3, 3)
earth = Button(root, image = sm_player_earth, command=Earth,bg='#336699')
earth.grid(row = 4, column = 0)

sm_player_fire = player_fire.subsample(3, 3)
fire = Button(root, image = sm_player_fire, command=Fire,bg='#336699')
fire.grid(row = 4, column = 1)

sm_player_metal = player_metal.subsample(3, 3)
metal = Button(root, image = sm_player_metal, command=Metal,bg='#336699')
metal.grid(row = 4, column = 2)

sm_player_water = player_water.subsample(3, 3)
water = Button(root, image = sm_player_water, command=Water,bg='#336699')
water.grid(row = 4, column = 3)

sm_player_wood = player_wood.subsample(3, 3)
wood = Button(root, image = sm_player_wood, command=Wood,bg='#336699')
wood.grid(row = 4, column = 4)

#
btn_quit = Button(root, text = "Quit",command=ExitApp)
btn_quit.grid(row=5,column=2)


root.mainloop()