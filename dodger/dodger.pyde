import time
import os

path = os.getcwd()
imagelist = os.listdir(path+'/images')

class Sentences:
    def __init__(self):
        self.sentence = {'pirate':'ahoi maties'}


class Flag:
    def __init__(self, x):
        self.dialect = None
        self.x = x
        self.y = 0
        self.r = int(random(15,25))
        self.speed = random(3,10)
        
    
        self.images = {}
        for i in imagelist:
            self.images.update({i.replace(".png",""):loadImage(path+'/images/'+i)})
        
        
        
        
        
    def assignFlag(self):
        dialectList = list(self.images.keys())
        x = int(random(len(self.images)))
        self.dialect = dialectList[x]
        
        
class Screen:
    def __init__(self,mkFlagRate = 6, w=500,h=500):
        self.w = w
        self.h = h
        self.rate = mkFlagRate
        self.maxFlags = 6
        self.flags = []
        
    
    def createFlags(self):
        flag = Flag(int(random(0,self.w)))
        flag.assignFlag()
        self.flags.append(flag)

        
    
    def display(self):
        if len(self.flags) < self.maxFlags:
            self.createFlags()
        
        for i in range(len(self.flags)):
            image(self.flags[i].images[self.flags[i].dialect],self.flags[i].x,self.flags[i].y,self.flags[i].r*2,self.flags[i].r*2)
            # ellipse(self.flags[i].x, self.flags[i].y, self.flags[i].r*2,self.flags[i].r*2)
            self.flags[i].y += self.flags[i].speed
            
        
        for i in range(len(self.flags)-i):
            if self.flags[i].y > self.h:
                del(self.flags[i])
        
        
    

g = Screen()
g.createFlags()

# z = Flag(50)
# z.assignFlag()
# print(z.dialect)


def setup():
    size(g.w,g.h)
    
def draw():
    background(255)
    g.display()
    
def mousePressed():
    noLoop()
    
