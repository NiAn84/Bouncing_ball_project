from tkinter import *
import random
import time
class Ball:
    def __init__(self, canvas, paddle, color, bricks):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        starts = [-1, 1]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_heigt = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] < paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] < paddle_pos[3]:
                return True
        return False


    def hit_brick(self, pos):
        brick = 0
        for l in self.bricks: #iterate through list
            brick_piece = l
            if pos[3] == l[1] and l[0] <= pos[0] <= l[2]: #for a hit from over
                brick += 1
            if pos[1] == l[3] and l[0] <= pos[0] <= l[2]: #for a hit from under
                brick += 2
            if pos[2] == l[0] and l[1] <= pos[1] <= l[3]: #for a hit from right side
                brick += 3
            if pos[0] == l[2] and l[1] <= pos[1] <= l[3]: #for a hit from left side
                brick += 4
   #         if brick > 0:

        return brick

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_heigt:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -1
            self.x = random.randrange(-1,1) #skickar iväg bollen åt random håll vid paddelträff
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= self.canvas_width:
            self.x = -1
        if self.hit_brick(pos) == 4:
            self.x = 1
            #self.canvas.delete(brick)
        if self.hit_brick(pos) == 3:
            self.x = -1
            #self.canvas.delete(brick)
        if self.hit_brick(pos) == 1:
            self.y = -1
            #self.canvas.delete(brick)
        if self.hit_brick(pos) == 2:
            self.y = 1
            #self.canvas.delete(brick)
#        if self.hit_brick(pos) > 4:
#            Canvas.delete(brick_hit)

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-space>', self.stop_paddle)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0


    def turn_left(self, evt):
            self.x = -3
    def turn_right(self, evt):
            self.x = 3
    def move_up(self, evt):
        self.y = -3
    def move_down(self, evt):
        self.y = 3
    def stop_paddle(self, evt):
        self.y = 0
        self.x = 0

class Obstacle:
    def __init__(self,canvas):
        self.canvas = canvas


class Brick(Obstacle):
    def __init__(self,canvas):
        self.canvas = canvas
        super(Brick, self).__init__(canvas)


class Level:
    def level(self, canvas):
        level = 1
        row = 0
        bricks = []
        try:

            for line in open(str(level) + ".txt", "r"):
                row = row + 1
                data = line.split(";")

                if data[0] == ".":
                    pass
                else:
                    brick = (0, 20 + (row * 20), 50, 40 + (row * 20), data[0])
                    bricks.append(brick)

                if data[1] == ".":
                    pass
                else:
                    brick = (50, 20 + (row * 20), 100, 40 + (row * 20), data[1])
                    bricks.append(brick)

                if data[2] == ".":
                    pass
                else:
                    brick = (100, 20 + (row * 20), 150, 40 + (row * 20), data[2])
                    bricks.append(brick)

                if data[3] == ".":
                    pass
                else:
                    brick = (150, 20 + (row * 20), 200, 40 + (row * 20), data[3])
                    bricks.append(brick)

                if data[4] == ".":
                    pass
                else:
                    brick = (200, 20 + (row * 20), 250, 40 + (row * 20), data[4])
                    bricks.append(brick)

                if data[5] == ".":
                    pass
                else:
                    brick = (250, 20 + (row * 20), 300, 40 + (row * 20), data[5])
                    bricks.append(brick)

                if data[6] == ".":
                    pass
                else:
                    brick = (300, 20 + (row * 20), 350, 40 + (row * 20), data[6])
                    bricks.append(brick)

                if data[7] == ".":
                    pass
                else:
                    brick = (350, 20 + (row * 20), 400, 40 + (row * 20), data[7])
                    bricks.append(brick)

                if data[8] == ".":
                    pass
                else:
                    brick = (400, 20 + (row * 20), 450, 40 + (row * 20), data[8])
                    bricks.append(brick)

                if data[9] == ".":
                    pass
                else:
                    brick = (450, 20 + (row * 20), 500, 40 + (row * 20), data[9])
                    bricks.append(brick)

                if data[10] == ".":
                    pass
                else:
                    brick = (500, 20 + (row * 20), 550, 40 + (row * 20), data[10])
                    bricks.append(brick)

                if data[11] == ".":
                    pass
                else:
                    brick = (550, 20 + (row * 20), 600, 40 + (row * 20), data[11])
                    bricks.append(brick)



        except IOError:
            pass
        self.bricks = bricks

        for l in self.bricks:
            pos1 = l[0]
            pos2 = l[1]
            pos3 = l[2]
            pos4 = l[3]
            color = l[4]
            canvas.create_rectangle(pos1, pos2, pos3, pos4, fill=color)

        return self.bricks


class Game():
    def __init__(self):
        tk = Tk()
        tk.title("Bouncing Ball Game")
        tk.resizable(0, 0)
        tk.wm_attributes("-topmost", 1)
        canvas = Canvas(tk, width=600, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        tk.update()
        paddle = Paddle(canvas, 'blue')
        bricks = Level.level(self, canvas)
        ball = Ball(canvas, paddle, 'green', bricks)
        while True:
            if not ball.hit_bottom:
                ball.draw()
                paddle.draw()
                tk.update_idletasks()
                tk.update()
            else:
                exit()
            time.sleep(0.01)


def main():
    Game()

if __name__ == '__main__':
    main()