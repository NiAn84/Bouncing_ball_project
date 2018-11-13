from tkinter import *
import random
import time

class Ball:
def __init__(self, canvas, paddle, color):
self.canvas = canvas
self.paddle = paddle
self.id = canvas.create_oval(10, 75, 25, 90, fill=color)
starts = [-3, -2, -1, 1, 2, 3]
random.shuffle(starts)
self.x = starts[0]
self.y = 2
self.lives = 3
self.canvas_heigt = self.canvas.winfo_height()
self.canvas_width = self.canvas.winfo_width()
self.hit_bottom = False
self.score = self.canvas.create_text(40, self.canvas_heigt - 50, text="Lives: " + str(self.lives))

def hit_paddle(self, pos):
paddle_pos = self.canvas.coords(self.paddle.id)
if pos[2] >= paddle_pos[0] and pos[0] < paddle_pos[2]:
if pos[3] >= paddle_pos[1] and pos[3] < paddle_pos[3]:
return True
return False
def draw(self):
self.canvas.move(self.id, self.x, self.y)
pos = self.canvas.coords(self.id)
if pos[1] <= 0:
self.y = 2
if pos[3] >= self.canvas_heigt:
self.lives -=1
if self.lives == 0:
self.hit_bottom = True
else:
self.y = -2
if self.hit_paddle(pos):
self.y = -2
if pos[0] <= 0:
self.x = 2
if pos[2] >= self.canvas_width:
self.x = -2
self.canvas.delete(self.score)
self.score = self.canvas.create_text(40, self.canvas_heigt - 50, text="Lives: " + str(self.lives))

class Paddle:
def __init__(self, canvas, color):
self.canvas = canvas
self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
self.canvas.move(self.id, 200, 300)
self.x = 0
self.canvas_width = self.canvas.winfo_width()
self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

def draw(self):
self.canvas.move(self.id, self.x, 0)
pos = self.canvas.coords(self.id)
if pos[0] <= 0:
self.x = 0
elif pos[2] >= self.canvas_width:
self.x = 0

def turn_left(self, evt):
self.x = -3
def turn_right(self, evt):
self.x = 3
class Brick:
COLORS = {0: '#999999', 1: '#555555', 2: '#222222'}

def __init__(self, canvas, ball, x, y, hits):
self.canvas = canvas
self.width = 75
self.height = 20
self.ball = ball
self.hits = hits
self.deleted = False
color = Brick.COLORS[hits]
self.id = canvas.create_rectangle(x - self.width / 2,
y - self.height / 2,
x + self.width / 2,
y + self.height / 2,
fill=color, tags='brick')
# super(Brick, self).__init__(canvas, item)

def hit_ball(self, brick_pos):
pos = self.canvas.coords(self.ball.id)
if pos[2] >= brick_pos[0] and pos[0] < brick_pos[2]:
if pos[1]-5 <= brick_pos[3] and pos[1]-5 < brick_pos[3]:
self.hit()
return True
return False

def draw(self):
pos = self.canvas.coords(self.id)
if self.hit_ball(pos):
self.ball.y = 2

def delete(self):
self.deleted = True
self.canvas.delete(self.id)

def hit(self):
if self.hits == 0:
self.delete()
class Game:
def __init__(self, master):
super(Game, self).__init__(master)
self.lives = 3
self.width = 610
self.height = 400
self.canvas = tk.Canvas(self, bg='#aaaaff',
width=self.width,
height=self.height)
self.canvas.pack()
self.pack()

self.items = {}
self.ball = None
self.paddle = Paddle(self.canvas, self.width/2, 326)
self.items[self.paddle.item] = self.paddle
for x in range(5, self.width - 5, 75):
self.add_brick(x + 37.5, 50, 2)
self.add_brick(x + 37.5, 70, 1)
self.add_brick(x + 37.5, 90, 1)

self.hud = None
self.setup_game()
self.canvas.focus_set()
self.canvas.bind('',
lambda _: self.paddle.move(-10))
self.canvas.bind('',
lambda _: self.paddle.move(10))

def setup_game(self):
self.add_ball()
self.update_lives_text()
self.text = self.draw_text(300, 200,
'Press Space to start')
self.canvas.bind('', lambda _:
self.start_game())


tk = Tk()
tk.title("Bouncing Ball Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'green')

brick_width = 75
brick_height = 20
bricks = []
x = int(75/2)+1
y = 10
num_bricks = int(800/brick_width)+1
for j in range(3):
for i in range(num_bricks):
prob = random.randint(1, 101)
hit = 0
if prob < 30:
hit = 1
b = Brick(canvas, ball, x+(i*brick_width), y + (j*brick_height), hits=hit)
bricks.append(b)

while 1:
if not ball.hit_bottom:
ball.draw()
paddle.draw()
for b in bricks:
if not b.deleted:
b.draw()
tk.update_idletasks()
tk.update()
time.sleep(0.01)