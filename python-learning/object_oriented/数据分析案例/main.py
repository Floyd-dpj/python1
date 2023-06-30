from file_define import *
from data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts
from  pymysql import Connection

text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")
jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

all_data =jan_data + feb_data
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
cursor = conn.cursor()
conn.select_db("py_sql")
# cursor.execute("alter table orders character set utf8")
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) values('{record.date}', '{record.order_id}','{record.money}', '{record.province}');"
    cursor.execute(sql)







# data_dict ={}
# 每个月的金额 # 柱状图显示每月全国各地的销售额
# for record in all_data:
#     if record.date in data_dict.keys():
#         data_dict[record.date] += record.money
#     else:
#         data_dict[record.date] = record.money
# bar = Bar(init_opts= InitOpts(theme= ThemeType.ROMANTIC))
# bar.add_xaxis(list(data_dict.keys()))
# bar.add_yaxis("销售额", list(data_dict.values()),label_opts=LabelOpts(is_show=False))
# bar.set_global_opts(
#     title_opts= TitleOpts(title='每日消费额',pos_top='3%')
# )
# bar.render("每日销售额柱状图.html")



#每个省的金额
# for record in all_data:
#     if record.province in data_dict.keys():
#         data_dict[record.province] += record.money
#     else:
#         data_dict[record.province] = record.money
# data_list = []
# # print(data_list)
# for province,money in data_dict.items():
#     data_list.append((province, money))
# print(data_list)
# map = Map()
# map.add('每个省一年的销售额', data_list, "china")
# map.set_global_opts(
#     title_opts=TitleOpts(title="每个省一年的销售额", pos_bottom="1%",pos_left='center'),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {'min': 1, 'max': 11999, 'label': '1-9', 'color': '#FFFAFA'},
#             {'min': 11000, 'max': 13999, 'label': '10-99', 'color': '#649ed8'},
#             {'min': 14000, 'max': 16999, 'label': '100-499', 'color': '#FF9966'},
#             {'min': 17000, 'max': 19999, 'label': '500-999', 'color': '#FF6666'},
#             {'min': 100000,  'label': '1000以上', 'color': '#990033'},
#         ]
#     )
# )
# map.render("每个省一年的销售额.html")