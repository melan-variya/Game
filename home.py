from tkinter import *
import random

GAME_WIDTH=600
GAME_HEIGHT=500
SPEED=300
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="#33cc33"
FOOD_COLOR="#ff0000"
BACKGROUND_COLOR="#000000"
global res
res=True
def check_collision(snake):
    x,y=snake.coordinates[0]
    if x<50 or y<50 or x>=GAME_WIDTH+50 or y>=GAME_HEIGHT+50:
        print('Game over :(')
        return True
    for a,b in snake.coordinates[1:] :
        if a==x and b==y:
            print('Game over :(')
            return True
    return False


def gameover(res):
    canva.delete(ALL)
    canva.create_text(canva.winfo_width() / 2, canva.winfo_height() / 2, text='GAME OVER!',font=("bold",50), fill='red')
    res=False

class Snake:
    def __init__(self):
        self.body_parts=BODY_PARTS
        self.coordinates=[]
        self.squares=[]
        for i in range(0,BODY_PARTS):
            self.coordinates.append([50,50])
        for x,y in self.coordinates:
            square=canva.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)



class Food:
    def __init__(self):
        self.generate_food()

    def generate_food(self):
        x = random.randint(2, ((GAME_WIDTH) / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(2, ((GAME_HEIGHT) / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coor = [x, y]
        canva.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake , food):
    x, y = snake.coordinates[0]
    print(res)
    if res:
        if direction=='up':
            y-=SPACE_SIZE
        elif direction=='down':
            y+=SPACE_SIZE
        elif direction=='left':
            x-=SPACE_SIZE
        elif direction=='right':
            x+=SPACE_SIZE
    snake.coordinates.insert(0,(x,y))
    square=canva.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    
    print(x,y,food.coor[0],food.coor[1])
    if x==food.coor[0] and y==food.coor[1]:
        global score
        score+=1
        lable.config(text='Score:{}'.format(score))
        canva.delete("food")
        food.generate_food()
    else:
        del snake.coordinates[-1]
        canva.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_collision(snake):
        gameover(res)

    win.after(SPEED,next_turn,snake,food)

    


def change_direction(new_direction):
    if res:
        global direction
        if new_direction=='left':
            if direction!='right':
                direction='left'
        elif new_direction=='right':
            if direction!='left':
                direction='right'
        elif new_direction=='up':
            if direction!='down':
                direction='up'
        elif new_direction=='down':
            if direction!='up':
                direction='down'



win=Tk()
win.title=("Snake Game!")
win.resizable(False,False)
score=0
direction="down"

lable=Label(win,text="SCORE {}".format(score),font=("Cursive",40))
canva=Canvas(win,bg=BACKGROUND_COLOR,height=GAME_HEIGHT+100,width=GAME_WIDTH+100)

lable.pack()
canva.pack()
win.update_idletasks()
win_width=win.winfo_width()
win_height=win.winfo_height()
screen_width=win.winfo_screenwidth()
screen_height=win.winfo_screenheight()

x=int((screen_width/2)-(win_width/2))
y=int((screen_height/2)-(win_height/2))

win.geometry(f"{win_width}x{win_height}+{x}+{y}")

snake=Snake()
food=Food()
next_turn(snake,food)

if res:
    win.bind('<Left>',lambda event: change_direction('left'))
    win.bind('<Right>',lambda event: change_direction('right'))
    win.bind('<Up>',lambda event: change_direction('up'))
    win.bind('<Down>',lambda event: change_direction('down'))


win.mainloop()