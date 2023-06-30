class Phone:
    name = None                  # type: int
    __current_voltage = None     # type: int
    var1: int = 10
    def __keep_single_core(self):
        print("让CPU单核运行")
class Phone2022(Phone):
    IMEI = None

phone = Phone2022()
phone.name = 1
print(type(phone.name))
print(type(phone.IMEI))
print(phone.name)
print(phone.var1)