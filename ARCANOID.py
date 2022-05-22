from pygame import*
import sys
window = display.set_mode((1500,700))
window.fill((189,147,163))

clock = time.Clock()
run = True
back = (189,147,163)
class Area():
   def __init__(self, x=0, y=0, width=100, height=100, color=None):
       self.rect = Rect(x, y, width, height)
       self.fill_color = back
       if color:
           self.fill_color = color
   def color(self, new_color):
       self.fill_color = new_color
   def fill(self):
       draw.rect(window, self.fill_color, self.rect)
   def collidepoint(self, x, y):
       return self.rect.collidepoint(x, y)       
   def colliderect(self, rect):
       return self.rect.colliderect(rect)
    
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=100, height=100):
        super().__init__(x=x, y=y, width=width, height=height, color=None)
        self.image = image.load(filename)  
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = Picture("ball.png",350,400,63,61)
platform = Picture("platform.png",350,650,424,67)

font.init()
font1 = font.SysFont("monotip",70)

speed_x = 3
speed_y = 3
move_right = False
move_left = False

start_x = 5 
start_y = 5
count = 9 
monsters = []
for j in range(3):
   y = start_y + (100 * j) 
   x = start_x + (60 * j) 
   for i in range (count):
       d = Picture('enemy.png', x, y, 108, 101)
       monsters.append(d)
       x = x + 150
   count = count - 1

finish = False
while run:
 
    platform.fill()
    for e in event.get():
        if e.type == QUIT:
            run =False
            quit()
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_a:
               move_left = True
            if e.key == K_d:
               move_right = True

                
        if e.type == KEYUP:
            if e.key == K_a:
               move_left = False
            if e.key == K_d:
               move_right = False
    if move_left:
       platform.rect.x -= 5
    if move_right:
       platform.rect.x += 5

    if not finish:
       ball.fill()#залитть цветом прямоугольник
       
       for m in monsters:
          m.draw()
          if m.rect.colliderect(ball.rect):
             
          
          
          
       ball.rect.x +=speed_x
       ball.rect.y +=speed_y
       
       if ball.colliderect(platform.rect):
          speed_y *= -1
          
       if ball.rect.y <0:
          speed_y *= -1
       if ball.rect.x <0 or ball.rect.x >1450:
          speed_x *= -1

       if ball.rect.y >650:
          text = font1.render("YOU LOSE!",True,(152,89,200))
          window.blit(text,(650,400))
       
       
       ball.draw()#отобразить картинку на прямоугольнике и на экране
       platform.draw()


    display.update()
    clock.tick(60)
