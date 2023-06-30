# 数据定义的类
class Record:
    # data = None
    # order_id = None
    # money = None
    # province = None
    def __init__(self, data, order_id, money, province):
        self.date = data
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"

