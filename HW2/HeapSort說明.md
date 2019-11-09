# Heap Sort(堆積排序法)

是Binary(二元數)的一種 可分成

1.Min Heap(最小堆積):父節點的值小於子節點
樹根(root)一定最所有節點的最小值

2.Max Heap(最大堆積):父節點的值大於子節點
樹根(root)一定最所有節點的最大值

## 流程圖

Max Heap
<img src='https://github.com/JoyC14/notes/blob/master/img/HeapSort.jpg' height=400 weight=400>

每一個父節點有兩個子節點

1.跟兩個子節點比大小

2.把較大的數跟父節點交換

3.將最上面的數取出

4.最後一個數放在最上面

重複以上的步驟，從heap的最後一個node開始，一路往上，直到root，便能得到排好序的數列
