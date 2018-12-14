import os

path = os.getcwd()
imagelist = os.listdir(path+'/images')
sentencelist = os.listdir(path+'/sentences')
sentencelist.remove('.DS_Store')
sentencelist.remove('test.py')


img=""
ScreenHeight = 500
ScreenWidth = 500


class Avatar:
    def __init__(self,x,y):
        self.ScreenHeight = y
        self.ScreenWidth = x
        self.x= x/2
        self.y= y
        self.right=0
        self.up=0
        self.down=0
        self.left=0
        self.speed=8
        self.r=35
        self.avatar=loadImage(path+'/Avatar.png')
        
        
        
    def display(self):
        image(self.avatar,self.x,self.y,self.r*2,self.r*2)
    
        
    def update(self):
        self.x+= self.speed*(self.right-self.left)
        self.y+= self.speed*(self.down-self.up)
        if not (self.x>=0):
            self.x=0
        if not (self.x<= (self.ScreenWidth -self.r*2)):
            self.x= (self.ScreenWidth-self.r*2)
        if not (self.y>=0):
            self.y=0
        if not (self.y<= (self.ScreenHeight -self.r*2)):
            self.y= (self.ScreenHeight-self.r*2)
            
        
    def CollisionDetection(self,flag):
        distance = ((self.x - flag.x)**2 + (self.y - flag.y)**2)**0.5
        if  distance <= (self.r+flag.r-2): #(self.r+flag.r)<=
            return True
            # print('ye')
        else:
            return False
            # print('ne')



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
        self.r = int(random(30,40))
        self.speed = random(3,7)
        
    
        self.images = {}
        for i in imagelist:
            self.images.update({i.replace(".png",""):loadImage(path+'/images/'+i)})
        

    def assignFlag(self):
        dialectList = list(self.images.keys())
        x = int(random(len(self.images)))
        self.dialect = dialectList[x]
        
        
class Screen:
    def __init__(self,mkFlagRate = 10, w=1200,h=640):
        self.w = w
        self.h = h
        self.rate = mkFlagRate
        self.maxFlags = 6
        self.flags = []
        self.a = None
        self.sentence = None
        self.decodedSentence = None
        self.targetdialect = None
        self.gameplay = True
        self.rightAnswers = 0
        self.wrongAnswers = 0
        self.score = self.rightAnswers
        
        
    def assignSentence(self):
        s = Sentence()
        self.sentence = s.sentences[int(random(0,len(s.sentences)-1))]
        self.targetdialect = s.sentences
        
        sentence = self.sentence.values()[0]
        self.decodedSentence = sentence.decode('utf-8')
        
    
    def createFlags(self):
        flag = Flag(int(random(0,self.w)))
        flag.assignFlag()
        self.flags.append(flag)
        
    def createAvatar(self,x,y):
        self.a = Avatar(x,y)

        
    
    
    def display(self):
        #displays flags
        if len(self.flags) < self.maxFlags:
            self.createFlags()
        
        for i in range(len(self.flags)):
            image(self.flags[i].images[self.flags[i].dialect],self.flags[i].x,self.flags[i].y,self.flags[i].r*2,self.flags[i].r*2)
            # ellipse(self.flags[i].x, self.flags[i].y, self.flags[i].r*2,self.flags[i].r*2)
            self.flags[i].y += self.flags[i].speed
            
        
        for i in range(len(self.flags)-i):
            if self.flags[i].y > self.h:
                del(self.flags[i])
        
        #display sentence
        fill(255)
        #s.sentences[5].values()[0]
        
        text(unicode(self.decodedSentence),self.w/2,45)
        
        #display avatar
        self.a.display()
        self.a.update()
        
        #collision detection
        
        
        # text('Score:'+str(self.score),self.)
        
        
        
        for flag in self.flags:
            if self.a.CollisionDetection(flag) is True:
                if self.sentence.keys()[0] == flag.dialect:
                    self.rightAnswers += 0
                    
                    self.gameplay = False
                    self.assignSentence()
                    
                if self.sentence.keys()[0] != flag.dialect:
                    self.wrongAnswers -= 0
                    
                    self.gameplay = False
                    # self.assignSentence()
                    
        
        
        

g = Screen()
g.createFlags()
g.createAvatar(g.w,g.h)
g.assignSentence()
# print(g.sentence)

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
# print(x)

# print(s.sentences[5].values())
# z = Flag(50)
# z.assignFlag()
# print(z.dialect)

map = loadImage(path+'/idrisi_cropped.jpg')


textsize = 40
def setup():
    size(g.w,g.h)
    
    f = createFont("BCompset.ttf",textsize)
    textFont(f)
    # f = loadFont("DecoTypeNaskh-48.vlw")
    textMode(SHAPE)
    textAlign(CENTER)
    textFont(f)    
    
    
if keyCode == 32:
    g.gameplay = not g.gameplay

def draw():

    
    if g.gameplay == True:
        
            
        background(map)
        g.display()
        
    elif g.gameplay == False:
        fill(0,255,0)
        textSize(textsize+18)
        text(unicode(g.decodedSentence),g.w/2,45+50)
        textSize(textsize)
        
        if keyCode == 32:
            g.gameplay = not g.gameplay
    
    # print(g.gameplay)


        

def keyPressed():
    if keyCode==UP:
        g.a.up=1
    if keyCode==DOWN:
        g.a.down=1
    if keyCode==RIGHT:
        g.a.right=1
    if keyCode==LEFT:
        g.a.left=1
            
def keyReleased():
    if keyCode==UP:
        g.a.up=0
    if keyCode==DOWN:
        g.a.down=0
    if keyCode==RIGHT:
        g.a.right=0
    if keyCode==LEFT:
        g.a.left=0
