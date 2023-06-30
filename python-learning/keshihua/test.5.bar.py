from pyecharts.charts import Bar
#from pyecharts.options import LabelOpts
from pyecharts.options import *
bar = Bar()
bar.add_xaxis(['中国', '美国', '日本'])
bar.add_yaxis('GDP', [30, 20, 10], label_opts=LabelOpts(position='right'))
bar.reversal_axis()    # 反转xy数轴
bar.set_global_opts(
    title_opts=TitleOpts(title="GDP", pos_bottom="1%",pos_left='center')

)






bar.render('基础柱状图.html')