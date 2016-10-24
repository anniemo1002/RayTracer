from collisions import *
from vector_math import *
from data import *

def distance(p1, p2):
   return length_vector(difference_point(p1,p2)) 

def cast_ray(ray,sphere_list,light,color):
   list=find_intersection_points(sphere_list,ray)
   if list==[]:
      return Color(1, 1, 1)
   else:
      s=list[0][0]
      pt=list[0][1]
      min_d=distance(pt,ray.pt)
      #interscetion[ (sphere,point)]
      for tup in list:
         
         p = tup[1]
         dis=distance(p,ray.pt)
         if dis<min_d:
            min_d=dis        
            s=tup[0]#sphere to return
            pt=tup[1]#intersection point

      r = s.color.r*s.finish.ambient*color.r
      g = s.color.g*s.finish.ambient*color.g
      b = s.color.b*s.finish.ambient*color.b

      N=sphere_normal_at_point(s,pt)
      pe=translate_point(pt,scale_vector(N,0.01))
      Ldir=normalize_vector(vector_from_to(pe,light.pt))      
      dot_product=dot_vector(N,Ldir)
      #shadow
      if dot_product<=0:
         dot_product=0
      else:
         intersection_list=find_intersection_points(sphere_list,Ray(pe,Ldir))
         if intersection_list!=[]:
            for tup in intersection_list:
               if distance(tup[1],pe)<distance(pe,light.pt):
                  dot_product=0

      r += s.finish.diffuse*dot_product*light.color.r*s.color.r
      g += s.finish.diffuse*dot_product*light.color.g*s.color.g
      b += s.finish.diffuse*dot_product*light.color.b*s.color.b

#part5
      reflection_vector=difference_vector(Ldir,(scale_vector(N,2*dot_product)))
      Vdir=normalize_vector(vector_from_to(ray.pt,pe))
      si=dot_vector(reflection_vector,Vdir)
      if si<=0:
         si=0
      else:
         light_contribution=s.finish.specular*si**(1/s.finish.roughness)
         r+=light.color.r*light_contribution
         g+=light.color.g*light_contribution
         b+=light.color.b*light_contribution
        
      return Color(r,g,b) 

   


def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color,light,file):




   y=max_y
   while y>min_y:
      x=min_x   
      while x<max_x:
         point=Point(x,y,0)

         vector=vector_from_to(eye_point,point)
         c=cast_ray(Ray(eye_point,vector),sphere_list,light,color)
         c=Color(int(c.r*255),int(c.g*255),int(c.b*255))
         file.write(str(c.r)+" "+ str(c.g)+" "+ str(c.b)+'\n')
         x=x+(max_x-min_x)/float(width)
      y=y-(max_y-min_y)/float(height)
