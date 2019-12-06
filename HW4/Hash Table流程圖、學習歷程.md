## hash table

Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」

<img src='https://github.com/JoyC14/notes/blob/master/img/hash%20table.jpg' height=400 weight=400>

## hash function

定義h()的定義域(domain)為整個Key的宇集合U，值域(range)應小於Table的大小m：

h:U→{0,1,...,m−1},where|U|≫m

盡可能讓Key在經過Hash Function後，在值域(也就是Table的index)能夠平均分佈(uniform distributed)，如此才不會有「兩筆資料存進同一個Table空格(稱為slot)」的情況。

若把Table想像成「書桌」，slot想像成書桌的「抽屜」，那麼為了要能更快速找到物品，當然是希望「每一個抽屜只放一個物品」，如此一來，只要拿著Key，透過Hash Function找到對應的抽屜(Hash Function的功能是指出「第幾個」抽屜，也就是抽屜的index)，就能保證是該Key所要找的物品。
反之，如果同一個抽屜裡有兩個以上的物品時，便有可能找錯物品。

1.Division Method：m有限制，但是比較快。

2.Multiplication Method：m沒有限制，但是比較慢。

參考資料:http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
