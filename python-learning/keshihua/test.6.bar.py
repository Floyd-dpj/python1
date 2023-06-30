from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *
bar1 = Bar()
bar1.add_xaxis(['中国', '美国', '日本'])
bar1.add_yaxis('GDP', [30, 20, 10], label_opts=LabelOpts(position='right'))
bar1.reversal_axis()    # 反转xy数轴
bar1.set_global_opts(
    title_opts=TitleOpts(title="GDP", pos_bottom="5%",pos_left='center')
)
bar2 = Bar()
bar2.add_xaxis(['中国', '美国', '日本'])
bar2.add_yaxis('GDP', [50, 30, 5], label_opts=LabelOpts(position='right'))
bar2.reversal_axis()    # 反转xy数轴
bar2.set_global_opts(
    title_opts=TitleOpts(title="GDP", pos_bottom="5%",pos_left='center')
)
bar3 = Bar()
bar3.add_xaxis(['中国', '美国', '日本'])
bar3.add_yaxis('GDP', [150, 130, 15], label_opts=LabelOpts(position='right'))
bar3.reversal_axis()    # 反转xy数轴
bar3.set_global_opts(
    title_opts=TitleOpts(title="GDP", pos_bottom="5%",pos_left='center')
)
timeline = Timeline(
    {'theme': ThemeType.ROMANTIC}
)
timeline.add(bar1, '2021年GDP')
timeline.add(bar2, '2022年GDP')
timeline.add(bar3, '2023年GDP')

# 设置时间的属性
timeline.add_schema(
    play_interval=3000,  # 单位是毫秒
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render('基础柱状图-时间线.html')

