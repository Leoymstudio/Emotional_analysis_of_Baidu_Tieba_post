# 首先，安装所需的库
# pip install pandas xlrd requests

import pandas as pd
import requests

# 读取Excel文件
df = pd.read_excel('all_data.xlsx')

# 获取IP地址列表
ip_list = df['ip'].tolist()


# 处理GeoAtlas数据
# 注意：DataV.GeoAtlas通常是阿里云的产品，这里只能假设API的使用，具体代码可能会根据实际API的文档不同而有所调整

# 假设我们有一个函数根据IP地址来获取地理位置
# 修改get_geolocation_from_datav函数
def get_geolocation_from_datav(ip):
    # 这里的URL和参数你需要替换成DataV.GeoAtlas实际的API
    url = "https://datav.geoatlas.api"
    params = {"ip": ip}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # 检查返回的JSON数据结构以确保正确访问city_name字段
        if 'city' in data and 'name' in data['city']:
            return f"IP属地: {data['city']['name']}"
        else:
            return "IP所在地未知"
    else:
        return "IP解析失败"


# 分析IP地址列表获取每个IP的地理位置
locations = [get_geolocation_from_datav(ip) for ip in ip_list]


# 这里locations将是一个类似["IP属地: 重庆", "IP属地: 上海", ...]的列表

# 创建地理空间型图表
# 注意：创建地理空间型图表通常依赖于具体的库和平台，比如在Python中，可以使用Basemap或者Folium等库，
# 而在DataV.GeoAtlas中，你可能需要根据平台的指南来操作。以下的代码只假定我们在Python环境下操作。

# 假设有一个地图可视化的函数
def create_geo_spatial_chart(locations):
    # 你需要将其替换成实际创建图表的代码
    pass


create_geo_spatial_chart(locations)
