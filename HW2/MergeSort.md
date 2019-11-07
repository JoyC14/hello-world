
# Mergesort(合併排序法)

屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)

## 流程圖

<img src='https://github.com/JoyC14/notes/blob/master/img/MergeSort.png' height=400 weight=400>

用MergeSort把數列{5,3,8,6,2,7,1,4}排序成{1,2,3,4,5,6,7,8}

1.Divide把數列拆成兩個小數列

(1)先把{5,3,8,6,2,7,1,4}分成{5,3,8,6}與{2,7,1,4}

(2)再把{5,3,8,6}分解成{5,3}與{8,6}

(3){2,7,1,4}分解成{2,7}與{1,4}。

(依此類推，直到每個數列剩下一個元素)

2.Conquer：按照「由小到大」的順序，「合併」小數列

(1)考慮數列{5}與{3}，比較大小後，合併成數列{3,5}

(2)考慮數列{8}與{6}，比較大小後，合併成數列{6,8}

(3)考慮數列{3,5}與{6,8}，比較大小後，合併成數列{3,5,6,8}

(依此類推，最後，考慮數列{3,5,6,8}與{1,2,4,7}，比較大小後，合併成數列{1,2,3,4,5,6,7,8})


參考網站http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html
