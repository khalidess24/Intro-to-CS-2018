

class Sentences:
    def __init__(self):
        self.sentence = {'pirate':'ahoi maties'}


class Flag:
    def __init__(self, x, r = 30, speed = random(2,10)):
        self.dialect = None
        self.x = x
        self.y = 0
        self.r = r
        self.speed = speed
        self.dialects = ['pirate','somethingelse']
        
    def assignFlag(self):
        x = int(random(len(self.dialects)))
        self.dialect = self.dialects[x]

class Screen:
    def __init__(self,mkFlagRate = 4, w=500,h=500):
        self.w = w
        self.h = h
        self.rate = mkFlagRate
        self.flags = []
        
    
    def createFlags(self):
        # for i in self.rate:
        self.flags.append(Flag(50))
            

        
    
    def display(self):
        ellipse(self.flags[0].x, self.flags[0].y, self.flags[0].r*2,self.flags[0].r*2)
        self.flags[0].y += self.flags[0].speed
        
    

g = Screen()
g.createFlags()

# z.assignFlag()



def setup():
    size(g.w,g.h)
    
def draw():
    background(255)
    g.display()
    
