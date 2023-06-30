from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *

f = open('D:/1960-2019全球GDP数据.csv', 'r', encoding='GB2312')
data_lines = f.readlines()
f.close()

# 处理数据
data_lines.pop(0)
# 使用字典存储数据
data_dict = {}
for line in data_lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)
time_line = Timeline(
    {'theme': ThemeType.ROMANTIC}
)
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:15]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)', y_data, label_opts=LabelOpts(position= 'right'))
    bar.reversal_axis()
    year= str(year)
    bar.set_global_opts(
        title_opts=TitleOpts(title="1960-2019全国GDP前15国家", pos_top='5%')
    )
    time_line.add(bar, year)
# 设置时间的属性
time_line.add_schema(
    play_interval=500,  # 单位是毫秒
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

time_line.render('1960-2019全国GDP前8国家.html')