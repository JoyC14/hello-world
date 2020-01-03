## Dijkstra

Dijkstra's algorithm 是以某一節點為出發點，計算從該節點出發到所有其他節點 的最短路徑。

首先以某一節點當作出發點，在與其相連且尚未被選取的節點裡，選擇加入離出發點距離 最短的節點，並且透過新增的節點更新到達其他節點的距離。
如此重覆加入新節點，直到所有的節點都被加入為止。


Dijkstra's Algorithm是一種「每次挑選當前最佳選擇(optimal solution)」的Greedy Algorithm：

把vertex分成兩個集合，其中一個集合「S」中的vertex屬於「已經找到從起點vertex出發至該vertex的最短路徑」，另一個集合「Q」中的vertex則還沒有。

這裡的Q就是Min-Priority Queue，其中每一個HeapNode的element即為「vertex的index」，key即為「vertex的distance」，表示從起點走到該vertex的path成本。

對所有vertex的predecessor與distance進行初始化(見圖一(b))，並更新起點vertex之distance為0；
若Graph中有V個vertex，便執行V次迴圈。

在每一個迴圈的開始，從Q中挑選出「distance值最小」的vertex，表示已經找到「從起點vertex抵達該vertex之最短距離」，並將該vertex從Q中移除，放進S集合。

利用ExtractMin()挑選「distance值最小」的vertex，即為Greedy Algorithm概念。

每一次迴圈都會藉由Relax()更新「從起點vertex到達仍屬於Q集合的vertex之path距離」，並將path距離存放於distance[]。並且利用DecreaseKey()更新Q中vertex的Key(也就是distance)。

步驟四與步驟五為完整的一次迴圈。

進到下一個迴圈時，會繼續從Q中挑選出「distance最小」的vertex，放進S。

重複上述步驟，直到Q中的vertex都被放進S為止。

如此便能得到從起點vertex抵達其餘vertex的最短路徑。


<img src='https://github.com/JoyC14/notes/blob/master/img/Dijkstra%E5%9C%96.jpg' height=400 weight=400>

<img src='https://github.com/JoyC14/notes/blob/master/img/Dijkstra.jpg' height=400 weight=400>


## Kruskal



參考資料:http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html

http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html
