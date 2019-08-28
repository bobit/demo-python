from wordcloud import WordCloud

f = open(u'testfile.txt', 'r').read()

wordcloud = WordCloud(background_color="white", width=1000, height=860, margin=2).generate(f)
import matplotlib.pyplot as plt

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('test1.png')