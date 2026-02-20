<div align="center">
  <img src="assets/logo.svg" alt="Matplotlib Viz Demo" width="680"/>

  # Matplotlib Viz Demo

  **教师考勤打卡时间数据可视化分析工具**

  [![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
  [![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-11557c?style=flat-square)](https://matplotlib.org)
  [![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas)](https://pandas.pydata.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
</div>

---

## 项目概述

Matplotlib Viz Demo 是一组基于 Matplotlib 和 Pandas 的数据可视化脚本，专门用于分析教师考勤打卡数据。程序从 Excel 文件中读取教师的签到/签退时间记录，通过多种图表形式（全员总览折线图、个人独立子图）直观展示每位教师的上下班打卡时间趋势，便于考勤管理和异常分析。

## 技术栈

- **Python**: 核心编程语言
- **Matplotlib**: 图表绘制引擎，含 `matplotlib.dates` 日期处理模块
- **Pandas**: Excel 数据读取与 DataFrame 处理
- **openpyxl**: Excel `.xlsx` 文件解析后端

## 功能特性

- **Excel 数据读取** -- 使用 Pandas 直接读取 `.xlsx` 考勤数据文件，自动解析日期和时间列
- **全员总览图** (`0.py`) -- 在一张大图上绘制所有教师的签退时间折线，支持按姓名分组着色
- **个人独立子图** (`1.py`) -- 为每位教师生成独立子图，每人一行，支持自动分页（每页 60 人）
- **签到时间分析** (`3.py`, `4.py`) -- 与签退分析对称，展示上班签到时间趋势
- **快速预览** (`数据可视化.py`) -- 简化版脚本，快速绘制单人签到时间折线图
- **时间轴格式化** -- 自定义 Y 轴时间格式化器，将数值转换为 `HH:MM` 格式显示
- **中文支持** -- 配置 SimHei 字体，完美支持中文标题、标签和图例
- **自动布局** -- `autofmt_xdate()` 自动旋转日期标签，`tight_layout()` 防止子图重叠

## 安装说明

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/Past-Tang/matplotlib-viz-demo.git
   cd matplotlib-viz-demo
   ```

2. 安装依赖：
   ```bash
   pip install matplotlib pandas openpyxl
   ```

3. 准备数据文件：
   - 将考勤 Excel 文件命名为 `W.xlsx` 或 `数据样本.xlsx` 放在项目根目录
   - Excel 文件需包含 `姓名`、`日期`、`签到时间`、`签退时间` 列

## 使用方法

每个脚本为独立案例，直接运行即可：

```bash
# 全员签退时间总览（一张大图）
python 0.py

# 每位教师独立签退时间子图
python 1.py

# 全员签到时间总览
python 3.py

# 每位教师独立签到时间子图
python 4.py

# 快速预览（简化版）
python 数据可视化.py
```

## 配置说明

### 中文字体配置

所有脚本已内置 SimHei 字体配置：

```python
plt.rcParams['font.sans-serif'] = ['SimHei']
```

如系统未安装 SimHei，可替换为其他中文字体（如 `Microsoft YaHei`）。

### 图表尺寸

在各脚本中可调整 `figsize` 参数：

| 脚本 | 默认尺寸 | 说明 |
|:---|:---|:---|
| `0.py` / `3.py` | `(17, 18)` | 全员总览大图 |
| `1.py` / `4.py` | `(15, 5*N)` | N 为教师数量，每人 5 英寸高 |
| `数据可视化.py` | `(12, 6)` | 快速预览小图 |

### 分页设置

`1.py` 和 `4.py` 中可调整 `teachers_per_figure` 参数（默认 60），控制每页显示的教师数量。

## 项目结构

```
matplotlib-viz-demo/
├── 0.py                 # 全员签退时间总览折线图
├── 1.py                 # 每位教师独立签退时间子图
├── 3.py                 # 全员签到时间总览折线图
├── 4.py                 # 每位教师独立签到时间子图
├── 数据可视化.py          # 快速预览脚本
├── W.xlsx               # 考勤数据源文件
├── 数据样本.xlsx          # 备用数据样本
├── myplot.png           # 示例输出图片
├── assets/
│   └── logo.svg         # 项目 Logo
├── LICENSE              # MIT 许可证
└── README.md
```

## 核心函数

### `convert_time_to_num(t)`
将 `datetime.time` 对象转换为浮点数（小时 + 分钟/60），用于 Y 轴数值绘制。

### `time_formatter(x, pos)`
Matplotlib 自定义格式化器，将 Y 轴浮点数值转换回 `HH:MM` 时间格式显示。

## 数据格式要求

Excel 文件需包含以下列：

| 列名 | 类型 | 说明 |
|:---|:---|:---|
| `姓名` | 字符串 | 教师姓名 |
| `日期` | 日期 | 考勤日期 |
| `签到时间` | 时间 (`HH:MM`) | 上班打卡时间 |
| `签退时间` | 时间 (`HH:MM`) | 下班打卡时间 |

## 依赖项

| 包 | 版本 | 用途 |
|:---|:---|:---|
| matplotlib | >= 3.5 | 图表绘制与日期处理 |
| pandas | >= 1.4 | Excel 读取与数据处理 |
| openpyxl | >= 3.0 | Excel `.xlsx` 解析后端 |

## 常见问题

### 中文显示为方块？
安装 SimHei 字体，或将 `rcParams['font.sans-serif']` 改为系统已有的中文字体名称。

### 图表窗口闪退？
确保脚本末尾有 `plt.show()`。如在 IDE 中运行，检查 Matplotlib 后端设置。

### 如何保存为图片？
在 `plt.show()` 之前添加：
```python
plt.savefig('output.png', dpi=300, bbox_inches='tight')
```

### 数据量太大导致图表拥挤？
调整 `teachers_per_figure` 参数减少每页人数，或增大 `figsize` 尺寸。

## 许可证

[MIT License](LICENSE)

## 免责声明

本项目仅供学习参考使用。示例数据中的姓名和时间均为脱敏处理后的模拟数据，不代表真实情况。