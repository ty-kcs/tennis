import pyxel

def court():
 #コートの描画
        pyxel.cls(1)
        # 四角形を描画、引数は(左上の点の座標x, y, 幅w, 高さh, 色)
        pyxel.rect(35, 0, 180, 195, 2)
        pyxel.rect(123.5, 0, 3, 100, 7)
        pyxel.rect(57.5, 100 , 135, 3, 7)
        pyxel.rect(57.5,0, 3, 195, 7) #シングルス左
        pyxel.rect(192.5, 0, 3, 195, 7)#シングルス右
        pyxel.rect(215, 0, 3, 195, 7)
        pyxel.rect(215, 0, 3, 195, 7)
        pyxel.rect(35, 195, 183, 3, 7)
        pyxel.rect(35, 0, 3, 195, 7)
        pyxel.rect(123.5, 190, 3, 5, 7)



class Racquet:
    
    def __init__(self, height, width, color):
        self.h = height
        self.center_x = pyxel.mouse_x
        self.center_y = 210
        self.w = width
        self.color = color
        self.angle = 0
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.angle += 7
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.angle -= 7
    def draw(self):
        pyxel.line(self.center_x - self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle),self.center_x - self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle), self.color) #左の縦線
         
        pyxel.line(self.center_x + self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle),self.center_x + self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle), self.color)#右の縦線
        
        pyxel.line(self.center_x - self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle),self.center_x + self.w/2 * pyxel.cos(self.angle) - self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) - self.h/2 * pyxel.cos(self.angle), self.color)#上の横線
        
        pyxel.line(self.center_x - self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y + self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle),self.center_x + self.w/2 * pyxel.cos(self.angle) + self.h/2 * pyxel.sin(self.angle),self.center_y - self.w/2 * pyxel.sin(self.angle) + self.h/2 * pyxel.cos(self.angle), self.color)#下の横線
        
    def hit(self, ball):
        #座標が一致していれば
        if (ball.y >= 209 and ball.x >= self.center_x - self.w/2 and ball.x <= self.center_x + self.w/2):
            return True
        #そうでなければ
        else:
            return False
        
class Ball:
        r = 2.5
        color = 10

        def __init__(self):
            self.restart()
            self.points = 0
            self.speed = self.points + 2
            self.angel = 0
        
        def move(self):
            self.speed = self.points + 2
            self.x += self.vx * self.speed
            self.y += self.vy * self.speed
            
        def move_hit(self):
            if self.speed >= 5:
                self.speed = self.points +2
            else:
                self.speed = 7
            self.x += self.vx * self.speed
            self.y += self.vy * self.speed
        
        def restart(self):
            self.x = pyxel.rndi(57, 192)
            self.y = 0
            if self.x <=55:
                self.angle = 90
            elif self.x >= 190:
                self.angle = 90
            else:
                self.angle = pyxel.rndi(75, 105)
            self.vx = pyxel.cos(self.angle)
            self.vy = pyxel.sin(self.angle)
            
        def draw(self):
            pyxel.circ(self.x, self.y, Ball.r, Ball.color)

class Target:
    length = 25
    height = 2.5
    color = 4
    
    def __init__(self):
        self.restart()
        
    def restart(self):
        self.x = pyxel.rndi(55, 185)
        self.y = 2.5
    
    def draw(self):
        pyxel.rect(self.x, self.y, Target.length, Target.height, Target.color)
    
    def hit(self, ball):
        #座標が一致していれば
        if (ball.y <= 5 and ball.x >= self.x and ball.x <= self.x + Target.length) and ball.vy < 0:
            return True
        #そうでなければ
        else:
            return False

class Clock:
  # 最初の位置と色を(x,y,c)で指定してインスタンス生成
  def __init__(self,x,y,c):
    self.x = x
    self.y = y
    self.c = c
    self.sec = 0
    self.min = 0

  # 更新ごとに経過秒数を設定する
  def update(self):
    # フレームカウントを30で割って経過秒数を得て、それを内部時間の変数self.tに代入
    # 小数点以下を切り捨てるため、//を使う
    self.sec = pyxel.frame_count // 30
    self.min = self.sec // 60
  def draw(self):
    pyxel.text(self.x,self.y,"Time: %02d:%02d" % (self.min,self.sec%60),self.c)
    if self.sec >= 50 and pyxel.frame_count % 30 < 15 and self.sec < 60:
        pyxel.text(self.x, self.y -60, "The game ends in:"+str(60 - self.sec), self.c)


class App:
    def __init__(self):
        pyxel.init(250, 250)
        org_colors = pyxel.colors.to_list() # 表示色リストの取得
        pyxel.colors[1] = 0x6c935c # 緑色
        pyxel.colors[2] = 0x3c638e # 青色  
        self.game_over = False
        self.ball_hit = False
        self.racquet = Racquet(5, 20, 4)
        self.ball = Ball()
        self.target = Target()
        self.clock = Clock(105,240,10)
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sound(1).set(notes='C4', tones='S', volumes='1', effects='F', speed=5)
    
    def start(self):
        pyxel.run(self.update, self.draw)
           
        
    def update(self):
        if self.clock.sec >= 60:
            self.game_over = True
        
        if self.game_over:
            return
        
        self.racquet.center_x = pyxel.mouse_x
        self.racquet.update()
        self.clock.update()
        
        if self.ball_hit:
            self.ball.move_hit()
            
        elif self.ball_hit == False:
            self.ball.move()
        
        if self.ball.x < 0 or self.ball.x > 250 or self.ball.y < 0 or self.ball.y > 250:
            self.ball.restart()
            self.ball_hit = False
            
        if self.racquet.hit(self.ball): #ラケットに当たったら
            self.ball.angle = self.racquet.angle 
            self.ball.vy = pyxel.cos(self.ball.angle) * -1
            self.ball.vx = pyxel.sin(self.ball.angle) * -1
            self.ball_hit = True
            pyxel.play(0,1)
            
        if self.target.hit(self.ball): #ターゲットに当たったら
            self.target.restart()
            self.ball_hit = False
            pyxel.play(0, 0)
            self.ball.points += 1
        
    def draw(self):
        pyxel.cls(0)
        court()
        self.racquet.update()
        
        # ラケットの描画
        self.racquet.draw()
        #ボールの描画
        self.ball.draw()
        #ターゲットの描画
        self.target.draw()
        #時間の描画
        self.clock.draw()
        #ポイントの描画
        pyxel.text(3, 5, "points:" + str(self.ball.points), 10)
        
        if self.game_over:
            pyxel.text(90, 125, "GAME FINISHED!! Your Score:"+str(self.ball.points), 10)
            pyxel.stop()
        
                     
        
class Pre_game:
    def __init__(self, app):
        self.app = app
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(2)
        pyxel.text(10, 125, "Press Space Key to start!", 7)
        pyxel.text(10, 150, "Use the TouchPad to move the racquet ", 7)
        pyxel.text(10, 100, "Press arrow keys to change the angle of the racquet", 7)
        pyxel.text(10, 175, "Aim at the target!", 7)

    def update(self):
        if pyxel.btn(pyxel.KEY_U):
            self.app.start()

app = App()
pre_game = Pre_game(app)
