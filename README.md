# MakeNTU 第一屆工作坊
![MacDown logo](pi.png)

###"用手指與聲納之距離調整Youtube爬下來的音訊檔的音量"

##架構
1. 利用 pafy 取得 youtube 音訊的 url
2. 利用 curl 下載 youtube 音訊
3. 利用 avconv 轉換音訊格式
4. 利用 pyalsaaudio 來播放音樂
5. 利用 RPi.GPIO 取得聲納的資訊
6. 計算距離並控制系統音量

##Credit
MakeNTU [LeoMao](http://leomao.gitlab.io/workshop-slides)