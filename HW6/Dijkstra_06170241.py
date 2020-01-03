#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
    
    def Dijkstra(self, s): 
        output={}
        picked = []
        distance = []        
        a = [] 
        for i in range(self.V):
            a.append(i)
        for j in a:
            if j == s:
                distance.append(0)
            else:
                distance.append(math.inf)
        new_distance=[]   
        for k in a:                
            new_distance.append(distance[k])
        minimum = min(new_distance)
        picked.append(minimum)
        for m in a:
            if self.graph[minimum][m] != 0:                
                distance[m] = self.graph[minimum][m]
            else:
                if m == s:
                    distance[m] = 0
                else:
                    distance[m] = math.inf
        a.remove(minimum)              
        while a:
            new_distance=[]            
            for k in a:                
                new_distance.append(distance[k])
            minimum = min(new_distance)
            for c in range(len(a)):
                if new_distance[c]==minimum:
                    picked.append(a[c])
                    break
            for n in a: 
                if self.graph[a[c]][n] != 0:
                    if distance[n] > self.graph[a[c]][n]+distance[a[c]]:
                        distance[n] = self.graph[a[c]][n]+distance[a[c]]
                    else:
                        distance[n]=distance[n]
                else:
                    pass
            a.remove(a[c])
        for l in range(self.V):
            output.setdefault(str(l),distance[l])
        return output 
    
    def Kruskal(self):
        result =[] 
  
        i = 0 
        e = 0 
  
           
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        
        while e < self.V -1 : 
  
            
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
           
      
        for u,v,weight  in result: 
          
            print ("%d -- %d == %d" % (u,v,weight)) 


# In[ ]:




