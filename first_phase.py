#scan image in zig zag fashion
#if sd is 11 and pixel is odd valued then increase pixel value and append 0 to sd
#if pixel is even valued then append those number of zeroes to sd
#if sd is 0 and pixel is odd valued then no change append 1 to sd
#dont forget to increment sd and pixels
#only append bits upto len of LP chart
global_x=0
global_y=0
right=1
left=0
diag_down=0
diag_up=0
def hide_in_image(data):
    global secret_data
    if len(data)==1:
        x,y=find_next()
        secret_data+='1'
    else
        if data[1]=='0':
            x,y=find_next()
            pixel[x][y]-=1
            secret_data+='0'
        else:
            x,y=find_next()
            pixel[x][y]+=1
            secret_data+='0'
def find_next()
    #check for boundaries
    global global_x
    global global_y
    global secret_data
    x=global_x
    y=global_y
    while pixel[x][y]%2==0:
        if right==1:
            y+=1
            secret_data+='0'
            diag_down=1
        elif down==1:
            x+=1
            secret_data+='0'
            diag_up=1
        elif diag_up==1:
            if x==0 or y==LIM-1:
                right=1
            else:
                secret_data+='0'
                y+=1
                x-=1
        elif diag_down==1:
            if x==0 or y==LIM-1:
                down=1
            else:
                secret_data+='0'
                y-=1
                x+=1
    global_x=x
    global_y=y
    return x,y
def hide(secret_data):
    i=0
    while i<len(secret_data):
        if i==(len-1):
            hidden+=secret_data[i]
            break
        if secret_data[i]=='0':
            hidden+=secret_data[i]
            i+=1
            hidden+=secret_data[i]
        else:
            hide_in_image(secret_data[i])
        i+=1
    return hidden
