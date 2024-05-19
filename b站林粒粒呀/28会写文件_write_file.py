# 任务1：在一个新的名字为＂poem．txt＂的文件里，写入以下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高处不胜寒。
# 方法1
with open('./28poem.txt', 'w', encoding='utf-8') as file:
    file.write('我欲乘风归去，\n')
    file.write('又恐琼楼玉宇，\n')
    file.write('高处不胜寒。')
# 方法2
with open('./28poem.txt', 'w', encoding='utf-8') as file:
    file.write('我欲乘风归去, \n又恐琼楼玉宇, \n高处不胜寒,\n')

# 任务2：在上面的＂poem．txt＂文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。
with open('./28poem.txt', 'a', encoding='utf-8') as file:
    file.write('起舞弄清影，\n')
    file.write('何似在人间。')
