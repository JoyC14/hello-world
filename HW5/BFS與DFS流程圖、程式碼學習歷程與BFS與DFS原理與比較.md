## BFS(廣度優先搜尋法)
是一種圖形(graph)搜索演算法

從一個節點開始，將每個鄰居節點都一層一層的拜訪下去，深度最淺的節點會優先被拜訪

從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。

以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。

採用「先進先出」(First-in First-Out, FIFO) 的方式管理節點，因此通常在「廣度優先搜尋」裏會有個佇列 (queue) 結構，通常以迴圈的方式呈現

<img src='https://github.com/JoyC14/notes/blob/master/img/BFS.jpg' height=400 weight=400>

## DFS(深度優先搜尋法)
搜尋節點的最深處，一直往尚未訪問過的第一個鄰居節點走去的一種方法

<img src='https://github.com/JoyC14/notes/blob/master/img/DFS.jpg' height=400 weight=400>

參考資料:https://magiclen.org/dfs-bfs/

http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html

http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
