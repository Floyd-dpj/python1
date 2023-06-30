from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = (
    ('北京市', 99),
    ('上海市', 199),

)
map.add('测试地图', data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, 'max': 9, 'label': '1-9', 'color': '#FFFAFA'},
            {'min': 10, 'max': 99, 'label': '10-99', 'color': '#649ed8'},
            {'min': 100, 'max': 499, 'label': '100-499', 'color': '#FF9966'},
            {'min': 500, 'max': 999, 'label': '500-999', 'color': '#FF6666'},
            {'min': 1000,  'label': '1000以上', 'color': '#990033'},
        ]
    )
)
map.render("测试地图.html")