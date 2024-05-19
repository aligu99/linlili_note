# 官方内置函数(较少） https://docs.python.org/zh-cn/3/library/functions.html

# 取一段数字的中位数

# 1、采用数字和数学模块import语句简化 https://docs.python.org/zh-cn/3/library/statistics.html
import statistics

print(statistics.median([69, 124, -32, 27, 217]))
print(statistics.mean([69, 124, -32, 27, 217]))

# 2、采用数字和数学模块form…import…语句简化，按住ctrl+median可以查看import里引入的代码

from statistics import median, mean

print(median([69, 124, -32, 27, 217]))
print(mean([69, 124, -32, 27, 217]))


# 3、可以采用第三发库引入 https://pypi.org/project/pip/ 与1、2类似，import[模块名]或者from [模块名] import [函数名，变量名]
# 引入方法：=>去终端输入：pip install + [模块名]引入，就可以用这个模块函数

# 简化前
def median(num_list):
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    # 如果一共有奇数个数字，取中间那个
    if n % 2 == 1:
        return sorted_list[n // 2]
    # 如果一共有偶数个数字，取中间两个的平均值
    else:
        return sorted_list[n // 2 - 1] + sorted_list[n // 2] / 2


print(median([69, 124, -32, 27, 217]))

# 安装第三方库：
# 在终端Windows PowerShell中输入pip install akshare
# import akshare
# print(akshare.get_cffex_daily('20220222')
