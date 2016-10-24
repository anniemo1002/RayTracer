from vector_math import *
import math
from data import *
def sphere_intersection_point(ray,sphere):
   a=dot_vector(ray.dir,ray.dir)
   b=2*dot_vector(difference_vector(ray.pt,sphere.center),ray.dir)
   c=dot_vector(vector_from_to(ray.pt,sphere.center),vector_from_to(ray.pt,sphere.center))-sphere.radius**2
   if b**2-4*a*c<0:
      return None
   else:
      t1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
      t2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
      p1=Point((ray.pt.x+ray.dir.x*t1),(ray.pt.y+ray.dir.y*t1),(ray.pt.z+ray.dir.z*t1))
      p2=Point((ray.pt.x+ray.dir.x*t2),(ray.pt.y+ray.dir.y*t2),(ray.pt.z+ray.dir.z*t2))   
      if (t1<0 or t2<0):
         if (t1<0 and t2<0):
            return None
         elif t1<0:
            return p2
         else:
            return p1

      elif t1>t2:
         return p2
      else:
         return p1

def find_intersection_points(sphere_list,ray):
   list=[]
   for x in sphere_list:
      point= sphere_intersection_point(ray,x)
      if point!=None:
         list.append((x,point))

   return list
         


def sphere_normal_at_point(sphere,point):
   v=vector_from_to(sphere.center,point)
   return normalize_vector(v)
