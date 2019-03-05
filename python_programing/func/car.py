#这是关于汽车相关操作的函数集合
def make_car(brand, model, **car_info):
    #获取汽车的信息创建汽车的字典
    car_detail = {}
    car_detail['brand'] = brand
    car_detail['model'] = model
    for key,value in car_info.items():
        car_detail[key] = value
    return car_detail