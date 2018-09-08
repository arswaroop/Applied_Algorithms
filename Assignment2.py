import time
import matplotlib.pyplot as plt


#Reading file line by line
with open("E:\Code\Applied_Algorithms\input2.txt") as f:
    content = f.readlines()

#Removing whitespaces
content = [x.strip() for x in content] 

#converting list into int
newcontent=list(map(int,content))

def maxopp(newcontent,start,mid,end):
    leftsum=0
    leftbest=0
    
    for i in range(mid-1,end-1,-1):
        leftsum=leftsum+newcontent[i]
        if leftbest<leftsum:
            leftbest=leftsum
    
    rightsum=0
    rightbest=0

    for j in range(mid+1,end+1,1):
        rightsum=rightsum+newcontent[i]
        if rightsum<rightbest:
            rightbest=rightsum

    return leftbest+rightbest+newcontent[mid]


def max_continuous_sum(newcontent,start,end):
    mid = (start+end)/2
    m1 = max_continuous_sum(newcontent,start,mid)
    m2 = max_continuous_sum(newcontent,mid+1,end)
    m3 = maxopp(newcontent,start,mid,end)
    return max(m1,m2,m3)


newlist={}

for j in range(500,5001,500):
    avg_list=[]
    start=0
    end=j
    #running each iteration 3 times and taking average
    for i in [1,2,3]:
        temp_list=newcontent[:j]
        start_time=time.process_time()
        sorted_list=max_continuous_sum(temp_list,start,end)
        end_time=time.process_time()
        avg_list.append(end_time-start_time)
     
    #saving the key value pairs to the dictionary after average
    temp_dict={j:sum(avg_list)/float(len(avg_list))}
    newlist.update(temp_dict)


#plot
lists=sorted(newlist.items())
x,y=zip(*lists)
plt.plot(x,y,'xb-')
plt.show()
