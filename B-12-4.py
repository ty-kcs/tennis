import pyxel
class Ball:
        speed = 1
        r = 10
        color = 6

        def __init__(self):
            self.restart()
        
        def move(self):
            self.x += self.vx * Ball.speed
            self.y += self.vy * Ball.speed
        
        #restartメソッドの追加。
        def restart(self):
            self.x = pyxel.rndi(0, 199)
            self.y = 0
            angle = pyxel.rndi(30, 150)
            self.vx = pyxel.cos(angle)
            self.vy = pyxel.sin(angle)

class Pad:
        length = 20
        color = 14
        width = length * 2
        height = 5

        def __init__(self):
            self.x = 100
        
        def catch(self, ball):
        #座標が一致していれば
            if (ball.y >= 195 and ball.x >= self.x - Pad.length and ball.x <= self.x + Pad.length):
                return True
        #そうでなければ
            else:
                return False

class App:
    def __init__(self):
        pyxel.init(200, 200)
        self.game_over = False
        self.lost_balls = 0
        self.get_balls = 0
        self.points = 0
        self.balls = [Ball()]
        self.pad = Pad()
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sound(1).set(notes='G2G2', tones='NN', volumes='33', effects='NN', speed=10)
        pyxel.run(self.update, self.draw)
     

    def update(self):
        
        self.pad.x = pyxel.mouse_x
        if self.lost_balls >= 10:
            self.game_over = True
        
        if self.game_over:
            return
        
        if self.get_balls % 10 == 0 and self.get_balls != 0:
            self.balls.append(Ball())
            self.get_balls = 0
            Ball.speed = 1
        
        for b in self.balls:
            b.move()

            #左右に来た場合の処理
            if (b.x > 200 and b.vx > 0) or (b.x < 0 and b.vx < 0):
                b.vx *= -1

            if self.pad.catch(b): #ボールが受け取れた時の処理
                self.points += 1
                self.get_balls += 1
                pyxel.play(0, 0)
                b.restart()
                Ball.speed += 0.5
                b.move()
                 
            elif b.y >= 195:  #それ以外の処理
                pyxel.play(0, 1)
                Ball.speed += 0.5
                self.lost_balls += 1
                b.restart()
                Ball.speed += 0.5
                b.move()

    def draw(self):
        if self.game_over:
            pyxel.text(75, 100, "GAME OVER!!", 6)
        else:
            pyxel.cls(7)
            for b in self.balls:
                pyxel.circ(b.x, b.y, Ball.r, Ball.color)
            pyxel.rect(self.pad.x - Pad.length, 195, Pad.width, Pad.height, Pad.color)
            pyxel.text(5, 5, "points:" + str(self.points), 6)

app = App()
pyxel.run(app.update, app.draw)




    

