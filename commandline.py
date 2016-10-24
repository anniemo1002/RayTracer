from sys import*
from data import *
#get the optional argv

list=argv[2:]
def float_default(name,index,default):
   try:
      x=list[index]
      try:
         return float(x)
      except:
         print 'bad argument for', name
         return default
   except:
      print 'missing argument for' ,name
      return default

def eye():
   if '-eye' in list:
      i=list.index('-eye')
      x=float_default('eye_x',i+1,0.0) 
      y=float_default('eye_y',i+2,0.0)
      z=float_default('eye_z',i+3,-14.0) 
      return Point(x,y,z)
   else:
      return Point(0.0,0.0,-14.0)
def view():
   if '-view' in list:
      i=list.index('-view')
      min_x=float_default('view_min_x',i+1,-10.0)
      max_x=float_default('view_max_x',i+2,10.0)
      min_y=float_default('view_min_y',i+3,-7.5)
      max_y=float_default('view_max_y',i+4,7.5)
      width=float_default('view_width',i+5,512)
      height=float_default('view_height',i+6,384)
      return (min_x,max_x,min_y,max_y,width,height)
   else:
      return (-10,10,-7.5,7.5,512,384)


def light():
   if '-light' in list:
      i=list.index('-light')
      x=float_default('light_x',i+1,-100)
      y=float_default('light_y',i+2,100)
      z=float_default('light_z',i+3,-100)
      r=float_default('light_r',i+4,1.5)
      g=float_default('light_g',i+5,1.5)
      b=float_default('light_b',i+6,1.5)
      return (x,y,z,r,g,b)
   else:
      return (-100,100,-100,1.5,1.5,1.5)

def ambient():
   if '-ambient' in list:
      i=list.index('-ambient')
      r=float_default('ambient_r',i+1,1.0)
      g=float_default('ambient_g',i+2,1.0)
      b=float_default('ambient_b',i+3,1.0)
      return Color(r,g,b)
   else:
      return Color(1.0,1.0,1.0)
