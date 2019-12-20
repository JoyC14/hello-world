#!/usr/bin/env python
# coding: utf-8

# In[4]:


from collections import defaultdict 

class Graph:
     
    def __init__(self): 
         self.graph = defaultdict(list) 
 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
    
    
    def BFS(self, s):
        state2 = []
        queue = [s]

        while queue:
            s = queue.pop(0)
            
            if s not in state2:
                state2.append(s)
                w = self.graph[s]
                
                for v in w:
                    queue.append(v)
        return state2

    def DFS(self, s): 
        stack = [s]
        stateb = []

        while stack:
            s = stack.pop(-1)
            if s not in stateb:
                stateb.append(s)
                w = self.graph[s]
                for v in w:
                    stack.append(v)
        return stateb


# In[ ]:





# In[ ]:




