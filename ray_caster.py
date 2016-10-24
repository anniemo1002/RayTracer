from cast import *
from commandline import *
from sys import *
from data import *

#output file
def output_file(width, height):
   f=open('image.ppm',"w")
   f.write('P3\n')
   f.write(str(width)+' '+str(height)+'\n225\n')
   return f



#input file 
def input_file():
   if len(argv)<2:
      print 'usage:python ray_caster.py <filename> [-eye x y z][-view min_x max_x min_y max_y width height] [-light x y z r g b][-ambient r g b]'
      exit()
   try:
      f=open(argv[1],'r')
   except:
      print 'could not open file', argv[1]
      exit()

   line_num=1
   sphere_list=[]   
   for l in f:
      try:
         list=l.split(' ')
         num_list=[float(x) for x in list]
         if len(num_list)==11:
            pt=Point(num_list[0],num_list[1],num_list[2])
            radius=num_list[3]
            color=Color(num_list[4],num_list[5],num_list[6])
            ambient=num_list[7]
            diffuse=num_list[8]
            specular=num_list[9]
            roughness=num_list[10]
            sphere=Sphere(pt,radius,color,Finish(ambient,diffuse,specular,roughness))
            sphere_list.append(sphere)
         else: 
            print 'malformed sphere on line',line_num, 'skipping'
      except:
         print 'malformed sphere on line', line_num, 'skipping'
      line_num+=1
   return sphere_list
    
def main():
   eye_point=eye()
   v=view()
   min_x=v[0]
   max_x=v[1]
   min_y=v[2]
   max_y=v[3]
   width=int(v[4])
   height=int(v[5])
   l_tup=light()
   l=Light(Point(l_tup[0],l_tup[1],l_tup[2]),Color(l_tup[3],l_tup[4],l_tup[5]))
   color=ambient()

#call the function
#def main():
   cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,input_file(),color,l,output_file(width, height))

if __name__=='__main__':
   main()



