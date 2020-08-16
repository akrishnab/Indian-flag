'''This program uses Python Turtle library to draw Indian flag
Written by Anantha Krishna B


'''
from turtle import*

#The dimensions of rectangle are length is a  and breadth is b
#ratio of a and b must be 3:2 as per government norms
# (c,d) is the coordinate of bottom leftmost corner of flag

#draw orange strip
def makeorange(a,b,c,d):
	pu()
	goto(0-c,b-d)
	pd()
	fillcolor('#FF9933')#prescribed orange color
	begin_fill()
	fd(a)
	rt(90)
	fd((b)/3)
	rt(90)
	fd(a)
	rt(90)
	fd(b/3)
	end_fill()

#make white strip	
def makewhite(a,b,c,d):
	pu()
	goto(0-c,((2*b)/3)-d)
	pd()
	fillcolor('#FFFFFF')#prescried white color
	begin_fill()
	rt(180)
	fd(b/3)
	rt(270)
	fd(a)
	rt(270)
	fd(b/3)
	rt(270)
	fd(a)
	end_fill()

#draw green strip		
def makegreen(a,b,c,d):
	pu()
	goto(0-c,0-d)
	pd()
	fillcolor('#138808')#prescribed green color 
	begin_fill()
	rt(180)
	fd(a)
	rt(-90)
	fd(b/3)
	rt(-90)
	fd(a)
	rt(-90)
	fd(b/3)
	end_fill()

#draw Ashoka chakra		
def makechakra(a,b,c,d):
	pencolor('#000080')#prescribed navy blue color
	pu()
	goto(a/2-c,b/3-d)
	pd()
	rt(-90)
	circle(b/6)
	goto(a/2-c,b/2-d)
	for i in range(0,24):
		fd(b/6)
		pu()
		goto(a/2-c,b/2-d)
		pd()
		rt(15)
	
def tri_color_flag(a,b,c,d):
#integrate all the strips and chakra	
	if a/b == 1.5:	#ratio should be 1.5
		makeorange(a,b,c,d)
		makewhite(a,b,c,d)
		makegreen(a,b,c,d)
		makechakra(a,b,c,d)
		pu()
		goto(-325,-200)
		pd()
		pencolor('blue')
		font1=("Itallic", 16, 'normal', 'bold', 'italic', 'underline')
		write("Happy Independence day",				font=font1)
			
		done()
	else:
		
		pu()
		goto(-325,-200)
		pd()
		write("Enter valid ratio of dimensions!!")
		done()

#test the code
if __name__=="__main__":
	tri_color_flag(300,200,100,100)
	