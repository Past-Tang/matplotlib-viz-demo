import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import time

plt.rcParams['font.sans-serif']=['SimHei']

# 加载Excel文件
file_path = 'W.xlsx'
data = pd.read_excel(file_path)

# 提取相关列：'姓名'、'日期'、'签退时间'
data_filtered = data[['姓名', '日期', '签退时间']]

# 将'日期'转换为datetime类型，'签退时间'转换为time类型
data_filtered['日期'] = pd.to_datetime(data_filtered['日期'])
data_filtered['签退时间'] = pd.to_datetime(data_filtered['签退时间'], format='%H:%M', errors='coerce').dt.time

# 函数将时间转换为适合绘图的数值格式
def convert_time_to_num(t):
    return t.hour + t.minute / 60 + t.second / 3600 if t is not None else None

data_filtered['签退时间数值'] = data_filtered['签退时间'].apply(convert_time_to_num)

# 函数用于将y轴标签格式化为时间格式
def time_formatter(x, pos):
    if x is not None and x >= 0 and x < 24:
        hours = int(x)
        minutes = int((x % 1) * 60)
        return f"{hours:02d}:{minutes:02d}"
    return ""

# 获取教师的唯一姓名
unique_teachers = data_filtered['姓名'].unique()

# 每个图形中的教师数量，如果需要，创建多个图形
n_teachers = len(unique_teachers)
teachers_per_figure = 60  # 每个图形中的教师数量
n_figures = (n_teachers + teachers_per_figure - 1) // teachers_per_figure

for fig_num in range(n_figures):
    start_idx = fig_num * teachers_per_figure
    end_idx = min(start_idx + teachers_per_figure, n_teachers)
    current_teachers = unique_teachers[start_idx:end_idx]

    # 为当前教师创建子图
    n_rows = len(current_teachers)
    fig, axes = plt.subplots(n_rows, 1, figsize=(15, 5 * n_rows))
    fig.subplots_adjust(hspace=0.6)

    for i, teacher in enumerate(current_teachers):
        ax = axes[i] if n_rows > 1 else axes

        # 筛选每个教师的数据
        teacher_data = data_filtered[data_filtered['姓名'] == teacher]

        # 绘制每个教师的数据
        dates = mdates.date2num(teacher_data['日期'])
        times = teacher_data['签退时间数值']
        ax.plot_date(dates, times, '-', label=teacher, marker='x')

        # 设置x轴格式
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.set_xlabel('日期', fontsize=14)

        # 设置y轴格式
        ax.yaxis.set_major_formatter(plt.FuncFormatter(time_formatter))
        ax.yaxis.set_major_locator(plt.MaxNLocator(24))
        ax.set_ylabel('签退时间', fontsize=14)

        # 标题和图例
        ax.set_title(f'{teacher}的签退时间', fontsize=16)
        ax.legend(loc='upper left', fontsize=12)

        # 显示网格线
        ax.grid(True)

    # 调整布局以提高可见性
    plt.tight_layout()
    plt.show()
