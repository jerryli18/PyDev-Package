'''
Created on Jan 27, 2015

@author: Jerry
'''
#this is my totem project
import random

def hair_normal():
#this returns normal hair
    a1 = 15*"/"
    a2 = 15*"/"
    a3 = 15*"/"
    return a1+"\n"+a2+"\n"+a3

def face_square():
#this returns square face
    a1 = "|"+13*" "+"|" 
    return a1
    
def eyes_square():
#this returns square eyes
    a1 = "|"+4*"_"+5*" "+4*"_"+"|"
    a3 = "|"+"|"+" "+"0"+" "+"|"+" "+" "+" "+"|"+" "+"0"+" "+"|"+"|"
    a4 = "|"*2+"_"*3+"|"+3*" "+"|"+3*"_"+"|"*2
    return a1+"\n"+a3+"\n"+a4

def nose_pig():
#this returns a pig nose
    a1 = "|"+6*" "+"|"+6*" "+"|"+"\n"
    a2 = "|"+5*" "+"O"+" "+"O"+5*" "+"|"
    return a1+a2

def mouth_smiley():
#this returns a smiley mouth
    a1 = "|"+" "*2+"\\"+7*"_"+"/"+2*" "+"|"
    return a1

def chin_square():
#this returns a square chin
    a1 = "|"+13*"_"+"|"
    return a1

def hair_mohawk():
#this returns a mohawk
    a1 = 7*" "+"/"+7*" "
    a2 = 6*" "+3*"/"+6*" "
    a3 = 5*"_"+5*"/"+5*"_"
    return a1+"\n"+a2+"\n"+a3

def eyes_diamond():
#this returns diamond eyes
    a1 = "|"+" "+"/"+"."+"\\"+5*" "+"/"+"."+"\\"+" "+"|"
    a2 = "|"+" "+"\\"+" "+"/"+5*" "+"\\"+" "+"/"+" "+"|"
    return a1+"\n"+a2

def nose_round():
#this returns a round nose
    a1 = "|"+6*" "+"|"+6*" "+"|"+"\n"
    a2 = "|"+5*" "+"C"+"|"+" "+5*" "+"|"
    return a1+a2

def mouth_flat():
#this returns a flat mouth
    a1 = "|"+" "*2+" "+7*"_"+" "+2*" "+"|"
    return a1

def chin_round():
#this returns a round chin
    a1 = "\\"+13*"_"+"/"
    return a1

def hair_curls():
#this returns hair curls
    a1 = 15*"@"
    a2 = 15*"@"
    a3 = 15*"@"
    return a1+"\n"+a2+"\n"+a3

def eyes_glasses():
#this returns glasses
    a1 = "|"+4*"_"+5*" "+4*"_"+"|"
    a3 = "|"+"|"+" "+"0"+" "+"|"+"_"+"_"+"_"+"|"+" "+"0"+" "+"|"+"|"
    a4 = "|"*2+"_"*3+"|"+3*" "+"|"+3*"_"+"|"*2
    return a1+"\n"+a3+"\n"+a4

def nose_pointed():
#this returns pointed nose
    a1 = "|"+6*" "+"|"+6*" "+"|"+"\n"
    a2 = "|"+5*" "+"<"+"|"+" "+5*" "+"|"
    return a1+a2

def mouth_underbite():
#this returns an underbite mouth
    a1 = "|"+" "*2+" "+7*"^"+" "+2*" "+"|"
    return a1

def chin_bearded():
#this returns a beard
    a1 = "|"+13*"w"+"|"
    return a1

def ears_normal():
#this returns normal ears
    a1 = "d"+6*" "+"|"+6*" "+"b"
    return a1

def bowtie_plain():
#this returns a plain bowtie
    a1 = " "+"|"+4*" "+"\\"+1*" "+"/"+4*" "+"|"+" "
    a2 = " "+"|"+5*" "+"O"+5*" "+"|"+" "
    a3 = " "+"|"+4*"_"+"/"+" "+"\\"+4*"_"+"|"+" "
    return a1+"\n"+a2+"\n"+a3

def head1():
#this returns head 1
    return hair_normal()+"\n"+eyes_square()+"\n"+ears_normal()+ "\n"+nose_pig()+"\n"+ mouth_smiley()+"\n"+chin_square()+"\n"+bowtie_plain()

def head2():   
#this returns head 2
    return hair_mohawk()+"\n"+face_square()+"\n"+eyes_diamond()+"\n"+ears_normal()+"\n"+ nose_round()+"\n"+mouth_flat()+"\n"+chin_round()+"\n"+bowtie_plain()

def head3():
#this returns head 3
    return hair_curls()+"\n"+face_square()+"\n"+eyes_glasses()+"\n"+ears_normal()+"\n"+nose_pointed()+"\n"+mouth_underbite()+"\n"+chin_bearded()+"\n"+bowtie_plain()

def totem():
#this prints the totem
    print head1()+"\n"+head2()+"\n"+head3()

def hair_random():
#this returns random hair
    num = random.randint(1,3)
    if num == 1:
        return hair_normal()
    elif num == 2:
        return hair_mohawk()
    else:
        return hair_curls()
    
def eyes_random():
#this returns random eyes
    num = random.randint(1,3)
    if num == 1:
        return eyes_square()
    elif num == 2:
        return face_square()+"\n"+eyes_diamond()
    else:
        return face_square()+"\n"+eyes_glasses()

def nose_random():
#this returns random nose
    num = random.randint(1,3)
    if num == 1:
        return nose_pig()
    elif num == 2:
        return nose_round()
    else:
        return nose_pointed()
    
def mouth_random():
#this returns random mouth
    num = random.randint(1,3)
    if num == 1:
        return mouth_flat()
    elif num == 2:
        return mouth_underbite()
    else:
        return mouth_smiley()
    
def chin_random():
#this returns random chin
    num = random.randint(1,3)
    if num == 1:
        return chin_square()
    elif num == 2:
        return chin_round()
    else:
        return chin_bearded()

def bowtie_random():
#this randomly prints a bowtie or not
    num = random.randint(1,2)
    if num == 1:
        return bowtie_plain()
    else: 
        return 15*" "+"\n"+15*" "+"\n"+15*" "
    
def randomhead():
#this returns random head
    return hair_random()+"\n"+eyes_random()+"\n"+ears_normal()+ "\n"+nose_random()+"\n"+ mouth_random()+"\n"+chin_random()+"\n"+bowtie_random()

def randompole():
#this prints a random pole
    print randomhead()+"\n"+randomhead()+"\n"+randomhead()

if __name__ == '__main__':
    pass

totem()
randompole()