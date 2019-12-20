Hash Table希望能夠將存放資料的「Table」的大小(size)降到「真正會存放進Table的資料的數量」，也就是「有用到的Key的數量」


1.Division Method：m有限制，但是比較快。

2.Multiplication Method：m沒有限制，但是比較慢。


## Division Method

要把大範圍的|U|對應到較小範圍的{0,1,...,m−1}，最直覺的做法就是利用Modulus(mod)取餘數。

假設Table大小為m，定義Hash Function為：

h(Key)=Keymodm

例如，選定Table大小為m=8，那麼以下的Key與Table之index將有對應關係如下：

h(14)=14mod8=6

代表「編號14」的物品要放進「第6格」抽屜。

h(23)=23mod8=7

代表「編號23」的物品要放進「第7格」抽屜。

h(46)=46mod8=6

代表「編號46」的物品要放進「第6格」抽屜。

h(50)=50mod8=2

代表「編號50」的物品要放進「第2格」抽屜。

# 優點

以Division Method實現Hash Function的優點就是非常快，只要做一次餘數(一次除法)運算即可。

# 缺點

較為理想的Table大小m是「距離2p夠遠」的質數，像是701。

換句話說，Table大小m必須慎選。

例如，要儘量避開「2的指數(2p)」，否則就只有「最低位的p-bit」會影響Hash Function的結果。

轉換成二進位會更容易看出，以m=8=23為例，h(Key)=Keymod23的意思就是，只取「以二進位表示的Key的最低位的3個bit」來決定Key對應到的Table之index
