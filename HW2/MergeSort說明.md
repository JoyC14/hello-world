
# Mergesort(合併排序法)

屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)

## 流程圖

<img src='https://github.com/JoyC14/notes/blob/master/img/MergeSort.jpg' height=400 weight=400>

把數列一直切半直到剩下一個
(長度<=1的話就不再切，長度>1繼續切)

合併排序法的原理就是將要排序的數列，分割到最小單位(將所有數列都分割成只有一個值的數列)再合併，而合併的同時也將一併做排序，因此會分成兩個Function去執行，一個負責分割，另一個負責合併跟排序

Step1 

亂數產生一組list

`sampleList = []
s = 0
while s < 9:
     tempRandNum = random.randint(0,100)
     sampleList.append(tempRandNum)
     s = s + 1`

Step2

合併的Function，合併時會有左邊的List和右邊的List

def mergeList(leftList, rightList):

 Step3
 
 判斷左(右)邊的List，如果只有一邊有值，就可直接回傳
 
 if len(leftList) == 0: 
         return rightList 
     elif len(rightList) == 0: 
         return leftList 
         
Step4

 比較兩邊List的第一個值，如果右邊大於左邊，那麼就將左邊的第一個值放入，並將後面的值繼續做合併和排序的工作，直到將所有的值都比較完為止
 
 elif leftList[0] < rightList[0]:
         return [leftList[0]] + mergeList(leftList[1:], rightList)
     else: 
         return [rightList[0]] + mergeList(leftList, rightList[1:])
         
Step5

分割的Function

def chopList(sourceList):

Step6

如果List只包含一個值，則直接回傳

  if 1 >= len(sourceList):
         return sourceList
         
Step7

找出中間位置

centerKey = int(round(len(sourceList)/2))
     leftList = []
     rightList = []
     
Step8

將List分成左右兩邊

  leftList = sourceList[0:centerKey]
     rightList = sourceList[centerKey:]
     
Step9

不斷分割，直到List內剩下一個值

  leftData = chopList(leftList)
  rightData = chopList(rightList)
     


