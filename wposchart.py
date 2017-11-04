dirx=0
diry=1
lists=[]
c=0
n=10
pchart1=""
for i in range (0,10):
    list1=[]
    for j in range (0,10):
	c+=1
	list1.append(c)
    lists.append(list1)
x=0
y=0
def check(x,y,dirx,diry):
    if x>=0 and y>=0 and x<n and y<n:
	return 0
    return 1
def calc(a):
    if a%2==0:
	s="0"
    else:
	b1=a%2
	a/=2
	b2=a%2
	if b2==0:
	    s="0"
	else:
	    s="1"
	if b1==0:
	    s+="0"
	else:
	    s+="1"
    return s
def calc2(a):
    if a%2==1:
	s="0"
    else:
	b1=a%2
	a/=2
	b2=a%2
	if b2==0:
	    s="1"
	else:
	    s="0"
	if b1==0:
	    s+="0"
	else:
	    s+="1"
    return s
def fschart1():
    x=0
    y=0
    c=0
    dirx=0
    diry=1
    pchart1=""
    while 1:
        print (x,y)
        #print (dirx,diry)
        if check(x,y,dirx,diry)==1:
            break
        print (lists[x][y])
        pchart1+=calc(lists[x][y])
        if dirx!=0 and diry!=0:
            print ("yes")
            while 1:
                #print ("ll",x,y)
                if x+dirx>=0 and y+diry>=0 and x+dirx<n and y+diry<n:
                    x+=dirx
                    y+=diry
                else:
                    break
            if dirx>0:
                dirx=1
                diry=0
            else:
                dirx=0
                diry=1
        elif dirx!=0:
            x+=dirx
            dirx=-1
            diry=1
        else:
            y+=diry
            dirx=1
            diry=-1
    return pchart1
#fschart1()
def fschart2():
    x=0
    y=9
    c=0
    dirx=0
    diry=-1
    pchart2=""
    while 1:
        print (x,y)
        #print (dirx,diry)
        if check(x,y,dirx,diry)==1:
            break
        print (lists[x][y])
        pchart2+=calc2(lists[x][y])
        if dirx!=0 and diry!=0:
            print ("yes")
            while 1:
                #print ("ll",x,y)
                if x+dirx>=0 and y+diry>=0 and x+dirx<n and y+diry<n:
                    x+=dirx
                    y+=diry
                else:
                    break
            if dirx>0:
                dirx=1
                diry=0
            else:
                dirx=0
                diry=-1
        elif dirx!=0:
            x+=dirx
            dirx=1
            diry=1
        else:
            y+=diry
            dirx=-1
            diry=-1
    return pchart2
print (fschart1())
print (fschart2())
