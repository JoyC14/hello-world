# binary search tree(二元搜索樹)
是二元樹的延伸，可以利用在搜索、排序和提供資料集合基本結構。

定義:

1.左子樹不為空，則左子樹的所有節點的鍵值(Key)小於根節點的鍵值。

2.右子樹不為空，則右子樹的所有節點的鍵值(Key)大於根節點的鍵值。

3.左右子樹也都是二元搜索樹。

4.節點不會有重複的鍵值。



## 新增(insert)
def insert(self, root, val)
如果要在BST中放入新元素，但應該要放入哪一個位置呢，就要與節點比大小

從BST的最上方開始尋找該放進的位置

與最上方的節點比較

若比目前節點小，則往左邊移動

  比目前節點大，則往右邊移動
  
如果插入是空值，則建立一個節點

 def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

## 查詢(search)
def search(self, root, target)

1.若binary tree為空樹，或binary tree裡面沒有搜尋的值，則搜尋失敗

2.若值小於節點則往左子樹查找，找到值回傳以及它的子節點

3.若值大於節點則往右子樹查找，找到值回傳以及它的子節點

和插入操作類似，也是不斷的比較，前提是如果相等就不用比較了，如果不等就按照插入的方式進行比較。

## 刪除(delete)
def delete(self, root, target)
有三種處理方式

1.要刪除的節點沒有子節點，將其父節點的左或右子節點設置為None，如果它是根節點（沒有父節點），可以直接移除。

2.有一個子節點時，將子節點取代被移除的節點的位置。

3.有兩個子節點時，將樹作中序(in-order)排列後，

可以選擇被移除節點的前驅(predecessor)節點或後繼(successor)節點來替換

或者可以從左子樹找到最大值或右子樹找到最小值的節點，

來取代被移除的節點位置，並同時將找到的節點之子節點取代自身的位置。


## 修改(modify)
def modify(self, root, target, new_val)
先搜尋，找到後進行修改

參考資料:https://emn178.pixnet.net/blog/post/94574434
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html


