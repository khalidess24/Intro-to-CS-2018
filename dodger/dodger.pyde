# from __future__ import unicode_literals
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import time
import os

path = os.getcwd()
imagelist = os.listdir(path+'/images')
sentencelist = os.listdir(path+'/sentences')
sentencelist.remove('.DS_Store')
sentencelist.remove('test.py')


class Sentence:
    def __init__(self):
        # self.sentence = {'pirate':'ahoi maties'}
        self.sentences = []
        for i in sentencelist:
            city = open(path+"/sentences/"+i,'r') #encoding='utf-8'
            for line in city:
                x = (line.rstrip().split(","))
                self.sentences.append({x[0]:x[1]})


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
        
        fill(255,0,0)
        #s.sentences[5].values()[0]
        text(unicode(x),250,30)
    

g = Screen()
g.createFlags()

# this instantiates the sentence class, 
# which has a list of dictionaries all the sentences. it looks like this {'dialect':'sentence'}
s = Sentence()

#this is how you call a specific sentence, where s is the instantiated sentence class, 
#sentences[5] calls the 5 element in the list of sentences
# this 5th element is a dictionary, so calling its values() will give you a list of all its values 
#(in this case there is only one value so you call the 1st element of that list at index 0 to get the sentence
# the next line decodes it into utf-8(which is what arabic script is encoded in)
# pretend it is displaying properly and keep going, this should be an easy fix later
                                                                                                    
x = s.sentences[5].values()[0]
x = x.decode("utf-8")
print(x)

# print(s.sentences[5].values())
# z = Flag(50)
# z.assignFlag()
# print(z.dialect)


def setup():
    size(g.w,g.h)
    f = createFont("BCompset.ttf",32)
    textFont(f)
    # f = loadFont("DecoTypeNaskh-48.vlw")
    textMode(SHAPE)
    textAlign(CENTER)
    textFont(f)    
    
def draw():
    background(255)
    g.display()

    
    
def mousePressed():
    noLoop()
  
