## BFS(廣度優先搜尋法)

BFS是一種圖形(graph)搜索演算法，以某個頂點作為起始點，一開始拜訪該頂點、再接著拜訪該頂點的所有相鄰頂點，接下來再拜訪下一層的頂點，直到所有的頂點皆拜訪過為止。

從一個節點開始，將每個鄰居節點都一層一層的拜訪下去，深度最淺的節點會優先被拜訪。

從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。

以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。

採用「先進先出」(First-in First-Out, FIFO) 的方式管理節點，因此通常在「廣度優先搜尋」裏會有個佇列 (queue) 結構，通常以迴圈的方式呈現

<img src='https://github.com/JoyC14/notes/blob/master/img/BFS.jpg' height=400 weight=400>

## DFS(深度優先搜尋法)

DFS 就像試探著走迷宮，從起點開始、任意選一點與起點相鄰的點行走，行走過的點會被標記起來

再將下一個點視為起點、繼續選擇與該點相鄰的點行走… 直到發現所有的點都已被標記過，即相鄰此點的所有點都已經走過了，則退回上一個分叉路口，繼續探訪。

直到所有的點都被標記過了，則搜索完畢。

搜尋節點的最深處，一直往尚未訪問過的第一個鄰居節點走去的一種方法。

<img src='https://github.com/JoyC14/notes/blob/master/img/DFS.jpg' height=400 weight=400>

## BFS DFS比較

*DFS*

優點：節省空間，得到最短路徑。

缺點：時間複雜度高，不一定是最佳的結果。

*BFS*

優點：獲得最短路徑（探索深度而不是權值）

缺點：極為巨大的記憶體需求（能夠高達幾十MB）造成程式堆疊溢位。

DFS可以運用在查找和爬蟲中，如果爬蟲的話那麼更多是優先找到不同連結，可用於統計等。而在查找中比如迷宮類可以利用DFS判斷是否存在路徑，出路等等。
BFS也可以運用在算法和爬蟲之中。

而BFS優先處理自己周圍的資源。所以在爬蟲可以用於遍歷網站，搜尋整個網站的價值信息等等。


原文網址：https://kknews.cc/code/3453n3y.html



參考資料:https://magiclen.org/dfs-bfs/

http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html

http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
