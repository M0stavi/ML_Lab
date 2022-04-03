# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:28:19 2022

@author: Asus
"""

arr = [(-1,-1,-1,-1)]*100000
check = [(-1,-1)]*100000

# arr[0] = (1,-1,-1,-1)

# point = (1,2)

# print(arr[0][4])

result = [(-1,-1,-1)]

dis = [100000000]

def dist(point1, point2):
    x = point1[0]-point2[0]
    y = point1[1]-point2[1]
    x=x*x
    y=y*y
    return (x+y)

# print(dist((0,0),(1,1)))


def insert(point, idx, xy):
    # print("a")
    # print(point[0])
    # print(point[1])
    x = point[0]
    y = point[1]
    if(arr[1][0] == -1):
        # print("here: ", arr[1][0])
        # arr[0][2] = x
        # arr[0][3] = y
        # arr[0][1] = 0
        # arr[0][0] = 1
        arr[1] = (1,0,x,y)
        print("idx x y:", idx, x, y)
        # print(arr[1])
    elif(arr[idx][0] == -1):
        
        # print("ss")
        # print(idx)
        
        # xy2 = -1
        # if(xy == 0):
        #     xy2 = 1
        # elif(xy == 1):
        #     xy2 = 0
        # arr[idx][0] = 1
        # arr[idx][2] = x
        # arr[idx][3] = y
        arr[idx] = (1,xy,x,y)
        print("idx x y:", idx, x, y)
    elif(arr[idx][0]==1):
        # print("ss")
        # print(arr[idx])
        # print(xy)
        xy3 = arr[idx][1]
        idx2 = -1
        comp = -1
        xy2 = -1
        if(xy3 == 0):
            xy2 = 1
            comp = arr[idx][2]
            if(comp <= x):
                idx2 = idx*2+1
            if(comp > x):
                idx2 = idx*2
        elif(xy3 == 1):
            xy2 = 0
            comp = arr[idx][3]
            if(comp <= y):
                idx2 = idx*2+1
            if(comp > y):
                idx2 = idx*2
        # print("Comp: ", point, arr[idx])
        
        # print("GG: ", point, xy2)
        # print("GG: ", xy2, idx2)
        insert(point, idx2, xy2)
        
ara = []
            
        
def nearest(point, idx):
    # print("GG: ", arr[idx][3])
    if(arr[idx][0] == -1):
        return
    xy = arr[idx][1]
    
    p2 = (arr[idx][2],arr[idx][3])
    
    c_dis = dist(point,p2)
    
    # xx=arr[idx][4]
    
    tf = 0
    
    ln = len(ara)
    
    for ii in range(0,ln):
        print("GG GG: ", ara[ii],idx)
        if(ara[ii]== idx):
            tf=1
    print("TF ",tf)
    
    if(tf == 0):
        # check[idx]=(1,-1)
        # print(check[idx])
        if(dis[0] > c_dis):
            dis[0] = c_dis
            result[0] = (arr[idx][2], arr[idx][3], idx)
        
    
    if(xy==0):
        if(point[0] < arr[idx][2]):
            next_branch = idx*2
            other_branch = idx*2+1
        else:
            next_branch = idx*2+1
            other_branch = idx*2
    elif(xy==1):
        if(point[1] < arr[idx][3]):
            next_branch = idx*2
            other_branch = idx*2+1
        else:
            next_branch = idx*2+1
            other_branch = idx*2
    
    nearest(point, next_branch)
    p3 = (arr[other_branch][2], arr[other_branch][3])
    alt_dis = dist(point, p3)
    if(alt_dis < dis[0]):
        nearest(point, other_branch)
            
            
            
    
    
        
    
    

# insert(point)    

print("Enter total number of points: ")
x = int(input())

for i in range(x):
    print("Enter x & y coordinates of point:(form: xi yi): ")
    # print(arr[1])
    xi = int(input())
    yi = int(input())
    pi = (xi,yi)
    insert(pi, 1, -1)
    # print(arr[1])
print("Enter query point: ")
x = int(input())
y = int(input())
point = (x,y)
print("Enter K value: ")
k = int(input())
neighb_nearest = []
for i in range(k):
    
    dis[0] = 100000000
    
    # result = (-1,-1,-1)
    
    nearest(point, 1)
    
    idd = result[0][2]
    
    print("GG@: ", idd)
    
    print(len(ara))
    
    ara.append(idd)
    
    # check[idd][0]=1
    
    # x = result[0]
    neighb_nearest.append((result[0][0],result[0][1]))
print("Nearest points are: ", neighb_nearest)

    
    
