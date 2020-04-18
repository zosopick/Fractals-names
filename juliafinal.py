'''
This code makes a fractal out of your name.
'''


from PIL import Image
import pandas as pd

def speller(name):
#The speller function takes your input apart into your first and last name
     

     s_split=name.split()

     first=[]
     last=[]
     for  i in range(len(s_split[0])):
          first.append(s_split[0][i])
         

     for j in range(len(s_split[1])):
          last.append(s_split[1][j])
     return(first,last)

def numberator(list):

#The numberator() function assigns value to every letter of your name. I did not use standard alphabetical order number assigning
# but instead used the way how ancient greeks wrote their numbers (had to improvise a bit for some letters).
#More on the way they're encoded here: https://greeknumber.weebly.com/uploads/3/8/9/4/38945097/498534559.gif?425

     dictionary={'a':1,'b':2,'c':500,'d':4,'e':5,'f':500,'g':3,'h':8,'i':10,'j':10,'k':20,'l':30,'m':40,'n':50,'o':70,'p':80,'q':420,
                 'r':100,'s':200,'t':300,'u':400,'v':400,'w':800,'x':600,'y':400,'z':7,'A':1,'B':2,'C':500,'D':4,'E':5,'F':500,'G':3,'H':8,'I':10,'J':10,'K':20,'L':30,'M':40,'N':50,'O':70,'P':80,'Q':420,
                 'R':100,'S':200,'T':300,'U':400,'V':400,'W':800,'X':600,'Y':400,'Z':7}



     var1=(pd.Series(list)).map(dictionary)
     var2=pd.DataFrame(var1)
     var3=[]
     for i in range(len(var2)):
          var3.append(var2[0][i])
          
     Esum=sum(var3)
     return Esum




def draw_julia(a,b):
     aval=a/(10**((len(str(a))+1)))+0.6
     bval=((b/(10**len(str(b))))/2)+0.2
     w, h, zoom = 7680,4320,1
     bitmap = Image.new("RGB", (w, h), "white")   
     pix = bitmap.load() 
     cX=-aval
     cY=bval 
     moveX, moveY = 0.0, 0.0
     maxIter = 255
   
     for x in range(w): 
        for y in range(h): 
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY 
            i = maxIter 
            while zx*zx + zy*zy < 4 and i > 1: 
                tmp = zx*zx - zy*zy + cX 
                zy,zx = 2.0*zx*zy + cY, tmp 
                i -= 1
  

            pix[x,y] = (i << 21) + (i << 10) + i*8
  
     bitmap.show()
     bitmap.save('{}.png'.format(s))

 
if __name__ == "__main__":

     s=input('Please enter your name: ')
     x=speller(s)
     value1=numberator(x[0])
     value2=numberator(x[1])
     draw_julia(value1,value2)


