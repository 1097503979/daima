# 初始化两个原始账本，这里使用字典来模拟
ledger1 = {
'巴贝拉': {'日期': '3月27日', '订单编号': '2024030004', '买家': '李强', '数量': 2, '单价': 55, '库存': 434, '库存箱数': 15, '页码': 1}  ,
'拉罗萨': {'日期': '3月27日', '订单编号': '2024030004', '买家': '李强', '数量': 2, '单价': 55, '库存': 142, '库存箱数': 15, '页码': 7}  ,
'尼扎': {'日期': '3月27日', '订单编号': '2024030004', '买家': '李强', '数量': 2, '单价': 55, '库存': 999, '库存箱数': 15, '页码': 13}    ,
'内比奥罗': {'日期': '3月27日', '订单编号': '2024030004', '买家': '李强', '数量': 2, '单价': 55, '库存': 999, '库存箱数': 15, '页码': 19}  ,
'巴罗洛': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 5, '单价': 650, '库存': 999, '库存箱数': 30, '页码': 23},
'格利尼': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 999, '库存箱数': 30, '页码': 29},
'多姿桃': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 999, '库存箱数': 30, '页码': 33},
'加维': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 999, '库存箱数': 30, '页码': 37},
'阿内斯': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 999, '库存箱数': 30, '页码': 41},
'柯蒂斯': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 999, '库存箱数': 30, '页码': 45},
'皮诺': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 47},
'莫斯卡托2018': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 51},
'莫斯卡托2020': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 53},
'3Rose': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 57},
'瓦波利切拉': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 59},
'普拉龙骨': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 63},
'阿玛罗尼': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 65},
'奥古斯都': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 69},
'无醇': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 71},
'克拉尔多河金': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 101},
'克拉尔多河银': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 103},
'普罗塞克金': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 105},
'普罗塞克金1.5': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 107},
'普罗塞克银': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 109},
'普罗塞克银1.5': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 111},
'桃红起泡': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 113},
'尼扎珍藏': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 115},
'巴罗洛珍藏': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 117},
'莫斯卡托2021': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 119},
'奥古斯都1.5': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 1, '库存箱数': 30, '页码': 121},
'阿玛罗尼1.5': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 123},
'蓝皮诺': {'日期': '3月32日', '订单编号': '2024030004', '买家': '章泽天', '数量': 14, '单价': 650, '库存': 180, '库存箱数': 30, '页码': 125}
}
ledger2 = {
    "巴贝拉": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 434,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 1
    },
    "拉罗萨": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 142,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 2
    },
    "尼扎": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 170,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 3
    },
        "内比奥罗": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 204,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 4
    },
    "巴罗洛": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 144,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 5
    },
        "格利尼": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 265,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 6
    },
        "多姿桃": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 323,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 7
    },
        "加维": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 516,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 8
    },
        "阿内斯": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 207,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 9
    },
        "柯蒂斯": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 247,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 10
    },
        "皮诺": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 264,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 11
    },
        "蓝皮诺": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 28,  # 剩余瓶数
        "库存箱数": 999,  # 剩余箱数
        "页码": 12
    },
        "莫斯卡托2020": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 249,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 13
    },
        "莫斯卡托2021": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 203,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 14
    },
        "3rose": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 133,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 15
    },
        "瓦波利切拉": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 210,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 16
    },
        "普拉龙骨": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 79,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 17
    },
        "阿玛罗尼": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 47,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 18
    },
        "奥古斯都": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 54,
        "库存": 55,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 19
    },
        "尼扎珍藏": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 106,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 20
    },
        "巴罗洛珍藏": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 75,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 21
    },
        "克拉尔多河金": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 175,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 22
    },
        "克拉尔多河银": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 49,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 23
    },
        "普罗塞克金": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 108,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 24
    },
        "普罗塞克银": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 118,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 25
    },
        "桃红起泡": {
        "日期": "3月27日",
        "订单编号": "2024030004",
        "买家": "展会售出",
        "数量": 2,
        "单价": 55,
        "库存": 60,  # 剩余瓶数
        "库存箱数": 15,  # 剩余箱数
        "页码": 28
    },
}

# 定义一个函数来添加新的酒类记录
def add_wine(wine_name, delivery_date, order_number, buyer, quantity, unit_price, page_number):
    # 用户选择更新的账本
    chosen_ledger = int(2)
    if chosen_ledger not in [1, 2]:
        print("无效的选择，请输入1或2。")
        return

    # 更新或添加酒类记录到选择的账本
    ledger = ledger1 if chosen_ledger == 1 else ledger2
    # 更新或添加酒类记录到账本1
    if wine_name in ledger:
        # 如果记录已存在，更新数量和价格
        ledger[wine_name]['数量'] = quantity
        # ledger[wine_name]['单价'] = (ledger[wine_name]['数量'] * ledger[wine_name]['单价'] + quantity * unit_price) / (ledger[wine_name]['数量'])
        ledger[wine_name]['库存'] -= quantity
        ledger[wine_name]['库存箱数'] = (ledger[wine_name]['库存'] // 6)
        
        ledger[wine_name]['订单编号'] = order_number#在这里加就行了
        ledger[wine_name]['单价'] = unit_price
        ledger[wine_name]['买家'] = buyer
        ledger[wine_name]['日期'] = delivery_date
    else:
        # 否则，创建新的记录
        ledger[wine_name] = {
            "日期": delivery_date,
            "订单编号": order_number,
            "买家": buyer,
            "数量": quantity,
            "单价": unit_price,
            "库存": quantity,
            "库存箱数": quantity // 6,
            "页码": page_number
        }

    # 显示更新后的账本记录
    print(f"{wine_name} {wine_name} {wine_name} {wine_name} {wine_name} {wine_name} {wine_name} {wine_name} {wine_name} {wine_name} {wine_name} {wine_name} 已更新。")
    print(ledger[wine_name])

# 例子1
add_wine("巴贝拉", "3月28日", "2024030010", "春糖自用推广酒", 2, 55, 10)

# 例子2
add_wine("尼扎", "3月28日", "2024030010", "春糖自用推广酒", 3, 120, 20)

# 例子3
add_wine("拉罗萨", "3月28日", "2024030010", "春糖自用推广酒", 1, 75, 20)

# 例子4
add_wine("巴罗洛", "3月28日", "2024030010", "春糖自用推广酒", 2, 210, 20)  # 注意：这里将订单编号和买家信息进行了更新
#例子 5
add_wine("内比奥罗", "3月28日", "2024030010", "春糖自用推广酒", 1, 88, 20) 

# 例子1
add_wine("巴罗洛珍藏", "3月28日", "2024030010", "春糖自用推广酒", 3, 330, 10)

# 例子2
add_wine("尼扎珍藏", "3月28日", "2024030010", "春糖自用推广酒", 2, 280, 20)

# 例子3
add_wine("阿内斯", "3月28日", "2024030010", "春糖自用推广酒", 1, 68, 20)

# 例子4
add_wine("加维", "3月28日", "2024030010", "春糖自用推广酒", 1, 75, 20)  # 注意：这里将订单编号和买家信息进行了更新
#例子 5
add_wine("柯蒂斯", "3月28日", "2024030010", "春糖自用推广酒", 1, 63, 20) 



# 例子2
add_wine("蓝皮诺", "3月28日", "2024030010", "春糖自用推广酒", 1, 60, 20)

# 例子3
add_wine("瓦波利切拉", "3月28日", "2024030010", "春糖自用推广酒", 4, 130, 20)


#例子 5
add_wine("普拉龙骨", "3月28日", "2024030010", "春糖自用推广酒", 1, 260, 20) 
#例子 5
add_wine("普罗塞克银", "3月28日", "2024030010", "春糖自用推广酒", 1, 130, 20) 

# 例子1
add_wine("巴贝拉", "3月27日", "2024030004", "展会售出", 2, 55, 10)

# 例子2
add_wine("拉罗萨", "3月27日", "2024030004", "展会售出", 2, 75, 20)

# 例子3
add_wine("格利尼", "3月27日", "2024030004", "展会售出", 3, 60, 20)

# 例子4
add_wine("多姿桃", "3月27日", "2024030004", "展会售出", 3, 58, 20)  # 注意：这里将订单编号和买家信息进行了更新
#例子 5
add_wine("加维", "3月27日", "2024030004", "展会售出", 1, 75, 20) 

# 例子1
add_wine("阿内斯", "3月27日", "2024030004", "展会售出", 2, 68, 10)

# 例子2
add_wine("柯蒂斯", "3月27日", "2024030004", "展会售出", 2, 63, 20)

# 例子3
add_wine("蓝皮诺", "3月27日", "2024030004", "展会售出", 2, 60, 20)

# 例子4
add_wine("3rose", "3月27日", "2024030004", "展会售出", 3, 48, 20)  # 注意：这里将订单编号和买家信息进行了更新



# 打印最终的账本1状态
print("\n店里卖酒账本：")
for wine, details in ledger1.items():
    print(f"{wine}: {details}")

# 打印账本2状态，由于没有添加记录，所以保持为空
print("\n出展用酒账本：")
for wine, details in ledger2.items():
    print(f"{wine}: {details}")
