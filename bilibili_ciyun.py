from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba

'''
原创作者：pk哥
Date：2020/5/10

直接读取上一个程序保存的csv弹幕文件，生成词云图

1、注意：更改下下方font_path的字体路径，我填的是我Mac电脑的字体路径，换成你自己的

2、backgroud_Image里面填的是生成词云图的背景图，把图放在和代码同一个目录，名称换成你自己的

3、对Python感兴趣的同学可以关注我的个人公众号「Python知识圈」，有疑问也可以通过公众号加我微信，一起探讨交流
'''

df = pd.read_csv('luox.csv', header=None)

text = ''
for line in df[1].replace('comments', ''):
    text += ' '.join(jieba.cut(line, cut_all=False))
print(text)

# 背景图放在和代码同一目录下，名称改成你自己的
backgroud_Image = plt.imread('luox2.jpeg')

# 下方的font_path后面需要换成自己电脑的字体路径，来用规定词云图的字体的

wc = WordCloud(background_color='white', mask=backgroud_Image, font_path='/System/Library/Fonts/Supplemental/Songti.ttc',
               max_words=2000, max_font_size=80, random_state=42,)
wc.generate_from_text(text)
# 看看词频高的有哪些,把无用信息去除
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
print(sort[:50])
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
wc.to_file("luox_cy2.jpg")
print('生成词云成功!')