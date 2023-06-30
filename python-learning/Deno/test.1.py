from pyecharts.charts import Line            #折线图
from pyecharts.options import  TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts   #标题的控制选项

line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),    #按住ctrl+p将所要传入的标题弹出
    legend_opts=LegendOpts(is_show=True),           #控制图例是否可以显示
    toolbox_opts=ToolboxOpts(is_show=True),         #控制工具箱是否显示
    visualmap_opts=VisualMapOpts(is_show=True)      #控制视觉映射是否显示

)
line.render()
