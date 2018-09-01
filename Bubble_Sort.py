
import time
import matplotlib.pyplot as plt


#Reading file line by line
with open("input.txt") as f:
    content = f.readlines()

#Removing whitespaces
content = [x.strip() for x in content] 

#converting list into int
newcontent=list(map(int,content))


#bubble sort function
def bubblesort(alist):
    n=len(alist)

    for i in range(n):
        for j in range(0,n-i-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]

    return (alist)

#Dictionary to save results as key value pair of (number of iterations:time taken)
newlist={}

#iterating and increasing the number of elements by 500
for j in range(500,len(newcontent)+1,500):
    avg_list=[]

    #running each iteration 3 times and taking average
    for i in [1,2,3]:
        temp_list=newcontent[:j]
        start_time=time.process_time()
        sorted_list=bubblesort(temp_list)
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

