#THIS IS A GAME TO TEST YOUR KNOWLEDGE OF DIFFERENT DIALECTS, TRY YOUR BEST TO COLLIDE WITH THE RIGHT FLAG, IF YOU CHOOSE THE WRONG ONE JUST KEEP TRYING! ALSO, PRESS SPACE TO CONTINUE AFTER COLLIDING WITH A FLAG

import os

path = os.getcwd()
imagelist = os.listdir(path+'/images')
sentencelist = os.listdir(path+'/sentences')
sentencelist.remove('.DS_Store')
sentencelist.remove('test.py')


img=""


#class to control movement of Avatar and the collisions between avatar and flags
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
        
        
    #displaying my dear friend borat 
    def display(self):
        image(self.avatar,self.x,self.y,self.r*2,self.r*2)
    
    #function to make sure the avatar doesnt go out of the screen
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
            
     #collision detector returning true or false   
    def CollisionDetection(self,flag):
        distance = ((self.x - flag.x)**2 + (self.y - flag.y)**2)**0.5
        if  distance <= (self.r+flag.r-2): #(self.r+flag.r)<=
            return True
            # print('ye')
        else:
            return False
            # print('ne')


#iterate through a folder with all the excel files, and extract the sentences using the for loop, and make a dictionary out of the sentences in the excel file 
class Sentence:
    def __init__(self):
        # self.sentence = {'pirate':'ahoi maties'}
        self.sentences = []
        for i in sentencelist:
            city = open(path+"/sentences/"+i,'r') #encoding='utf-8'
            for line in city:
                x = (line.rstrip().split(","))
                self.sentences.append({x[0]:x[1]})
                
    
#flag class contains the images for all the flags, and contains the function for randomly assigning a dialect to each flag
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
        
#iterates through all the keys and assigns a random dialect to the flag
    def assignFlag(self):
        dialectList = list(self.images.keys())
        x = int(random(len(self.images)))
        self.dialect = dialectList[x]
        

#screen class contains all the gameplay functionality and display, widht and height of screen, how many flags spawn, list of flags, etc.      
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
        
# assign a target sentence to the screen 
    def assignSentence(self):
        s = Sentence()
        self.sentence = s.sentences[int(random(0,len(s.sentences)-1))]
        self.targetdialect = s.sentences
        
        sentence = self.sentence.values()[0]
        self.decodedSentence = sentence.decode('utf-8')
        
    #creats flags and appends them to flag list 
    def createFlags(self):
        flag = Flag(int(random(0,self.w)))
        flag.assignFlag()
        self.flags.append(flag)
#istantiate the avatar class     
    def createAvatar(self,x,y):
        self.a = Avatar(x,y)

        
    
    
    def display(self):
        # this part makes sure that flags keep spawning
        if len(self.flags) < self.maxFlags:
            self.createFlags()
        #displays the flags 
        for i in range(len(self.flags)):
            image(self.flags[i].images[self.flags[i].dialect],self.flags[i].x,self.flags[i].y,self.flags[i].r*2,self.flags[i].r*2)
        #makes flags drop down 
            self.flags[i].y += self.flags[i].speed
            
        #removes flags after they reacht the bottom
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
        
        
        
        
        
        
        #for loop to check whether correct corresponding sentences or not 
        for flag in self.flags:
            if self.a.CollisionDetection(flag) is True:
                if self.sentence.keys()[0] == flag.dialect:
                    try:
                        self.flags.remove(flag)
                    except:
                        pass
                    self.rightAnswers += 0
                    
                    self.gameplay = False
                    self.assignSentence()
                    
                if self.sentence.keys()[0] != flag.dialect:
                    try:
                        self.flags.remove(flag)
                    except:
                        pass
                    self.wrongAnswers -= 0
                    
                    self.gameplay = False
                    # self.assignSentence()
                    
        
        
        
#some instantiations and assignments 
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

#loading background
map = loadImage(path+'/idrisi_cropped.jpg')



textsize = 40
def setup():
    size(g.w,g.h)
    #loading a font compatible with arabic 
    f = createFont("BCompset.ttf",textsize)
    textFont(f)
    # f = loadFont("DecoTypeNaskh-48.vlw")
    textMode(SHAPE)
    textAlign(CENTER)
    textFont(f)    
    
    # if condition for space bar resuming 
if keyCode == 32:
    g.gameplay = not g.gameplay

# main draw fuunction 
def draw():

    
    if g.gameplay == True:
        
            
        background(map)
        g.display()
        #pauses after each collision to give time for player to see sentence
    elif g.gameplay == False:
        fill(0,255,0)
        textSize(textsize+18)
        text(unicode(g.decodedSentence),g.w/2,45+50)
        textSize(textsize)
        
        if keyCode == 32:
            g.gameplay = not g.gameplay
    
    # print(g.gameplay)


        
#speed of avatar depending on the key that is pressed, going back to zero if the key is released
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
