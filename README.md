# luoxiang
用Python获取罗翔老师所有b站视频的弹幕并做成词云图

### 操作步骤

1、luo_ciyun.py文件用来保存up发的所有视频的弹幕为csv文件的

运行前需要修改下py文件里的headers信息和params替换成自己的，在up主空间页面里，按F12，查看network请求，可以直接复制 curl链接，
通过一个网站工具可以直接转换成Python形式的请求：这个转换不懂的话可以参考这篇文章：https://mp.weixin.qq.com/s/fVDwNdVDZo_0q6jAMWCGAA

2、bilibili_ciyun.py文件用来读取csv文件并生成词云图的

注意：更改代码中font_path的字体路径，我填的是我Mac电脑的字体路径，换成你自己的

backgroud_Image里面填的是生成词云图的背景图，把图放在和代码同一个目录，名称换成你自己的

##### 觉得不错，麻烦来个三连[B站视频](https://www.bilibili.com/video/BV1xg4y1B7iJ)


#### 代码中也有相关的注释，有疑问可以通过我公众号「Python知识圈」加我微信讨论，谢谢

## 微信公众号
欢迎关注个人微信公众号 “Python知识圈” （ID：PythonCircle）

![Python知识圈公众号二维码](http://blog.pyzhishiquan.com/img/20200427091312.jpg)

