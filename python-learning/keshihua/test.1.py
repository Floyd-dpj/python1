import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts

# 处理数据
f_us = open("D:/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()

f_jp = open("D:/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()

f_in = open("D:/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

# 对数据头部进行除留
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 对数据尾部进行处理
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# 将JSON数据转化成python数据
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取 tred key 值
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期 用于x轴 只需要2020年内的  （到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# 获取数据 用于y轴 只需要2020年内的  （到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis('美国确诊人数', us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数', jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数', in_y_data, label_opts=LabelOpts(is_show=False))
line.set_global_opts(
    title_opts= TitleOpts(title='2020年美日印三国确诊人数对比折线图', pos_bottom='1%',pos_left='center'),
    legend_opts= LegendOpts(is_show=True),  # 控制图例是否可以显示
    toolbox_opts= ToolboxOpts(is_show=True),  # 控制工具箱是否显示
    visualmap_opts= VisualMapOpts(is_show=True)  # 控制视觉映射是否显示
)
line.render("2020年美日印三国确诊人数对比折线图.html")

f_us.close()
f_jp.close()
f_in.close()

