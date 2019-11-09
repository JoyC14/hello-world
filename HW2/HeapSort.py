#!/usr/bin/env python
# coding: utf-8

# In[11]:


def heapify(arr, n, i): 
	largest = i  #假設根是最大值
	l = 2 * i + 1
	r = 2 * i + 2
    
#如果左邊子節點存在且大於根節點
	if l < n and arr[i] < arr[l]: 
		largest = l 

 # 如果右邊子節點存在且大於根節點
	if r < n and arr[largest] < arr[r]: 
		largest = r 

 # 如果最大值不等於i，就交換
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr, n, largest) 

#給定一個陣列長度排序
def heapSort(arr): 
	n = len(arr) 

#建立maxheap
	for i in range(n, -1, -1): 
		heapify(arr, n, i) 

#一個一個出取元素
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0) 

#設一個數列
arr = [ 4, 5, 7, 2, 3] 
heapSort(arr) 
n = len(arr) 
print(arr)


# In[ ]:




