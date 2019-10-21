# coding=utf-8
class Car():
    def __init__(self,make,model,year):
        """初始化描述骑车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' \
                    + self.make + ' ' + self.model
        return long_name.title()

class Battery():
    """模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size = 70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("this car has a " +str(self.battery_size) + "-kwh battery")
    def get_range(self):
        """答应一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70 :
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "this car can go approximately " + str(range)
        message += "miles on a full charge"
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year,size = 70):
        super().__init__(make,model,year)
        self.battery = Battery(size)

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("this car has a" + str(self.battery.battery_size) + '-kwh battery')

my_tesla = ElectricCar('tesla' , 'model' ,2016,85)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
print(my_tesla.battery)
my_tesla.battery.get_range()