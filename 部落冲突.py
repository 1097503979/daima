from collections import Counter
def inEnemy(enemy, enemy_heroes):
    """
    检查特定英雄是否出现在敌方英雄列表中。
    
    :param enemy: 需要检查的敌方英雄名称。
    :param enemy_heroes: 敌方英雄的列表。
    :return: 如果敌方英雄列表中包含特定英雄，则返回True，否则返回False。
    """
    return any(enemy == e for e in enemy_heroes)

def generateSuitableHeroes(enemy_heroes):
    """
    根据敌方英雄的情况，生成推荐的适合英雄或法术。
    
    :param enemy_heroes: 敌方英雄的列表。
    :return: 推荐的适合英雄或法术的列表。
    """
    suitable_heroes = []
    core_heroes = []
    # 如果有多头，把雷龙加入列表
    if inEnemy("多头", enemy_heroes):
        suitable_heroes.append("雷龙")
    
    # 如果有单头，把矿猪、女巫、根蔓加入推荐
    if inEnemy("单头", enemy_heroes):
        suitable_heroes.extend(["矿猪", "女巫", "根蔓","雷龙","骷髅法术"])
    if inEnemy("天鹰火炮外置", enemy_heroes):
        suitable_heroes.extend(["矿猪", "女巫", "根蔓","雷龙","攻城战车"])    
    # 如果大本外置，把地震法术和烈焰车、攻城气球加入列表
    if inEnemy("大本营外置", enemy_heroes):
        suitable_heroes.extend(["地震法术","烈焰车", "攻城气球","雷龙"])
    if inEnemy("大本营天鹰火炮分两头", enemy_heroes):
        suitable_heroes.extend(["滚木车", "烈焰车", "攻城气球"])
    if inEnemy("回形阵", enemy_heroes):
        suitable_heroes.extend(["滚木车", "狗球", "飞艇"])
    if inEnemy("部落城堡有援军外置",enemy_heroes):
        suitable_heroes.extend(["天使","野猪","毒药"])
    if inEnemy("采集器外置", enemy_heroes):
        suitable_heroes.extend(["超哥","烈焰车","攻城气球","雷龙"])  
    if inEnemy("储金罐外置", enemy_heroes):
        suitable_heroes.extend(["超哥","蓝胖","烈焰车", "攻城气球","雷龙"])        
    hero_counts = Counter(suitable_heroes)

    # 筛选出现次数超过1次的英雄
    core_heroes = [hero for hero in hero_counts if hero_counts[hero] > 1]#这里就已经选出并显示了妙手

    # # 将所有出现两次的英雄添加到推荐列表中 这行不要也行
    # suitable_heroes.extend(core_heroes)


    return suitable_heroes, core_heroes#没这一行就显示None  后面一行也要return 不然显示ValueError: too many values to unpack (expected 2)

# 可选：单头 天鹰火炮外置 大本营外置 部落城堡有援军外置 采集器外置 储金罐外置 大本营天鹰火炮分两头 回形阵
enemy_heroes = ["多头","大本营外置","单头","天鹰火炮外置","大本营天鹰火炮分两头","回形阵","天鹰火炮外置","部落城堡有援军外置",""]  
suitable_heroes,core_heroes = generateSuitableHeroes(enemy_heroes)
print(f"可选{suitable_heroes}")  # 输出推荐的适合英雄或法术
print(f"妙手{core_heroes}")
阵容 = {
    "阵容1": ["天使","狗球","飞艇"],
    "阵容2": ["天使","狗球","攻城气球"],
    "阵容3": ["天使","狗球","滚木车"],
    "阵容4": ["狗球","飞艇"],
    "阵容5": ["狗球","攻城气球"],
    "阵容6": ["狗球","滚木车"],
    "阵容7": ["天使","矿猪","女巫"],
    "阵容8": ["天使","超哥","女巫","雷龙"],
    "阵容9": ["矿猪","治疗","女巫","钻机"],
    "阵容10": ["矿猪","治疗","女巫","飞艇"],
    "阵容11": ["矿猪","治疗","女巫","烈焰车"],
    "阵容12": ["矿猪","治疗","女巫","滚木车"],
    "阵容13": ["天使","矿猪","治疗"],
    "阵容14": ["天使","超哥","矿猪","治疗"],
    "阵容15": ["天使","超哥","矿猪","治疗"],
    "阵容16": ["天使","矿猪","治疗","蓝胖"],
    "阵容17": ["天使","超哥","矿猪","治疗","蓝胖"],
    "阵容18": ["天使","超哥","矿猪","治疗","蓝胖"],
    "阵容19": ["天使","矿猪","治疗","钻机"],
    "阵容20": ["天使","超哥","矿猪","治疗","钻机"],
    "阵容21": ["天使","超哥","矿猪","治疗","钻机"],
    "阵容22": ["天使","矿猪","治疗","钻机"],
    "阵容23": ["天使","超哥","矿猪","治疗","钻机"],
    "阵容24": ["天使","超哥","矿猪","治疗","钻机"],
    "阵容25": ["天使","矿猪","治疗","投石车"],
    "阵容26": ["天使","超哥","矿猪","治疗","投石车"],
    "阵容27": ["天使","超哥","矿猪","治疗","投石车"],
    "阵容28": ["天使","矿猪","治疗","攻城战车"],
    "阵容29": ["天使","超哥","矿猪","治疗","攻城战车"],
    "阵容30": ["天使","超哥","矿猪","治疗","攻城战车"],
}
# 检查suitable_heroes中的值是否在阵容字典的任何阵容中出现过
intersection = set(suitable_heroes).intersection(*(阵容.values()))
#老师推荐加的 加上这段下面的英雄就有用了，英雄的问题还没解决
zhenrongSet=[]
for _,v in 阵容.items():
    zhenrongSet.extend(v)
    #检查suitable_heroes中的值是否在阵容字典的任何阵容中出现过共
    intersection = set(suitable_heroes).intersection(zhenrongSet)

# 如果有交集，遍历阵容字典并打印每个阵容中交集的值
if intersection:
    for 阵容编号, 英雄列表 in 阵容.items():
        # 找出当前阵容中与交集相同的值
        values_in_team = [英雄 for 英雄 in 英雄列表 if 英雄 in intersection]
        # 如果当前阵容中有与交集相同的值，则打印这些值
        # if values_in_team:
        #     print(f"推荐{阵容编号}: {英雄列表}")#values_in_team改成英雄列表
        if len(set(英雄列表).intersection(set(suitable_heroes)))>=3:
            print(f"极佳阵容{英雄列表}")
else:
    print("没有找到交集。")

