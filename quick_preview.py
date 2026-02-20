import pandas as pd
import datetime
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

file_path = "数据样本.xlsx"
data = pd.read_excel(file_path)

print(data['姓名'])


data['签到时间'] = pd.to_datetime(data['签到时间'], errors='coerce',format='%H:%M')[0:32]
data['日期'] = pd.to_datetime(data['日期'], errors='coerce',)[0:32]


plt.figure(figsize=(12, 6))

plt.plot(data['日期'][1:22], data['签到时间'][1:22])
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('**', fontsize=20)
plt.xlabel('Date')
plt.ylabel('Off-Work Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()