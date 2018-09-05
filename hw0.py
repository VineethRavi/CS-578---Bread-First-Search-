import csv
import sys
import time

sys.setrecursionlimit(10000)


def BFS(stack,node_val): 
    global visited
    if stack==[]:
        return node_val    
       
    t=stack.pop(0)
    
    visited[t[0]]=True
    
    if t[1]<=node_val[1]:
        node_val=t;
        
        
    for i in range(0,len(adjList[t[0]])):
        if visited[adjList[t[0]][i][0]]==False:
            visited[adjList[t[0]][i][0]]=True
            stack.append(adjList[t[0]][i])


    return BFS(stack,node_val)
    
    
file = open('nodes.csv')
csv_file = csv.reader(file)

array=[]
adjList=[]

stack=[]

node_val=[]

start = time.time()

for row in file:
    a=row.split()
    a[0]=a[0][1:-2]
    a[1]=a[1][1:-1]
    a[0]=a[0].split(':')
    a[1]=a[1].split(':')
    a[0][0]=int(a[0][0])
    a[0][1]=int(a[0][1])
    a[1][0]=int(a[1][0])
    a[1][1]=int(a[1][1])
    array.append(a)
    
    
for i in range(0,4039):
    adjList.append([])
    
for i in range(0,len(array)):
    adjList[array[i][0][0]].append(array[i][1])
    adjList[array[i][1][0]].append(array[i][0])
 
stack.append(array[0][0]);

node_val=array[0][0]; 

visited=[False]*(len(adjList))

node_val = BFS(stack,node_val) 

end = time.time()
print("The time taken for the algorithm computation is :- %f seconds." % ((end-start)))
print("The smallest node value is %d and the corresponding node ID is %d." % (node_val[1],node_val[0]))