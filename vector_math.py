import math
from data import *
def scale_vector(vector,scalar):
   return Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)
   #return (vector.x*scalar,vector.y*scalar,vector.z*scalar)

def dot_vector(v1,v2):
   return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def length_vector(vector):
   return math.sqrt(vector.x**2+vector.y**2+vector.z**2)

def normalize_vector(vector):
   l=length_vector(vector)
   x=vector.x/l 
   y=vector.y/l
   z=vector.z/l
   return Vector(x,y,z)
def difference_point(point1,point2):
   x=point1.x-point2.x 
   y=point1.y-point2.y 
   z=point1.z-point2.z
   return Vector(x,y,z)
def difference_vector(vector1,vector2):
   x=vector1.x-vector2.x 
   y=vector1.y-vector2.y
   z=vector1.z-vector2.z
   return Vector(x,y,z)

def translate_point(point,vector):
   x=point.x+vector.x  
   y=point.y+vector.y
   z=point.z+vector.z
   return Point(x,y,z)

def vector_from_to(from_point,to_point):
   x=to_point.x-from_point.x 
   y=to_point.y-from_point.y 
   z=to_point.z-from_point.z
   return Vector(x,y,z)
