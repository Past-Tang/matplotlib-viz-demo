import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif']=['SimHei']

import matplotlib.dates as mdates

# 读取Excel数据
data = pd.read_excel('W.xlsx')

# 筛选需要的列
data_filtered = data[['姓名', '日期', '签退时间']]

# 转换日期和签退时间为datetime格式
data_filtered['日期'] = pd.to_datetime(data_filtered['日期'])
data_filtered['签退时间'] = pd.to_datetime(data_filtered['签退时间'], format='%H:%M', errors='coerce').dt.time

def convert_time_to_num(t):
    """
    将时间转换为数值表示，用于绘图
    """
    return t.hour + t.minute / 60 + t.second / 3600 if t is not None else None

# 添加签退时间数值列
data_filtered['签退时间数值'] = data_filtered['签退时间'].apply(convert_time_to_num)

def time_formatter(x, pos):
    """
    自定义时间格式化函数
    """
    if x is not None and x >= 0 and x < 24:
        hours = int(x)
        minutes = int((x % 1) * 60)
        return f"{hours:02d}:{minutes:02d}"
    return ""

# 绘制图形
if __name__ == '__main__':
    plt.figure(figsize=(17, 18))

    # 组织循环，对每个员工的数据进行绘制
    for name, group in data_filtered.groupby('姓名'):
        dates = mdates.date2num(group['日期'])
        times = group['签退时间数值']
        plt.plot_date(dates, times, '-', label=name)

    # 设置x轴时间格式
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

    # 设置y轴时间格式
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(time_formatter))
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(24))

    # 自动调整x轴日期格式
    plt.gcf().autofmt_xdate()

    # 设置图形标签
    plt.xlabel('工作日期', fontsize=14)
    plt.ylabel('下班打卡时间', fontsize=14)
    plt.title('电子信息与自动化学院教师下班打卡时间表', fontsize=34)

    # 设置图例
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

    # 显示网格线
    plt.grid(True)

    # 显示图形
    plt.show()
