import random

# 定义所有英雄及其对应的类型和位置（去除重复项）
hero_positions = {
    "对抗路": ["杨戬","橘子","关羽","马超","狂铁","狂暴钟馗","夏洛特","姬小满","廉颇","钟无艳","老夫子","夏侯","亚瑟","哪吒", "孙策", "程咬金", "暗信",'司空震','花木兰','元歌','亚连','狂暴黄忠','海诺',"光信",'吕布','芈月'],
    "发育路": ["守约","艾琳","虞姬","后羿","伽罗", "马可","公孙离", "黄忠",'狄仁杰','李元芳','敖隐','狼狗','莱西奥','孙尚香'],
    "中路": ["杨玉环","王昭君","西施","高渐离","火舞","海月","小乔","专精大乔","扁鹊",'周瑜','弈星','安琪拉',"金蝉",'妲己','甄姬','武则天','嬴政','海诺'],
    "打野": ["典韦","梦琪","达摩","赵云","雅典娜","哪吒","老虎","阿珂","嫦娥","曹操","司空震","李白","猴子","宫本","镜","澜","司马懿","暃","云缨","曜","阿古朵","兰陵王", "韩信", "橘右京","大司命",'玄策','司空震',"露露",'凯','李元芳','露娜','芈月'],
    "游走": ["孙膑","牛魔","廉颇","鲁班大师","庄周","张飞","黄刀吕布","刘禅", "东皇太一", "庄周","太乙", "大乔", "蔡文姬", "桑启", "牛魔", "瑶","明世隐","朵莉亚","鲁班大师","鬼谷子"]
}

# 定义回血/法师英雄列表
# 根据敌方英雄填充 suitable_heroes
suitable_heroes = []

healing_heroes = {"橘子","杨玉环", "蔡文姬", "程咬金","狂铁","橘右京", "桑启", "杨戬","夏侯","扁鹊","芈月","海诺","朵莉亚","曹操"}
magic = ["艾琳","嫦娥","瑶", "大乔","狂暴钟馗", "孙膑", "芈月", "露娜","司空震","朵莉亚","诸葛亮"]
tanker = ["程咬金","东皇太一","廉颇","猪八戒","盾山","夏侯","蒙恬","白起","孙策","钟馗","阿古朵","牛魔","鲁班大师","庄周","张飞","刘禅","凯"]
assass={"元歌","李白","光信","橘子","夏洛特","暗信","马超","女娲","猴子","韩信","司空震","守约","伽罗","狼狗","孙膑","夏洛特","镜","澜","暃","玄策","老虎","芈月","露露","马可","吕布","阿珂","瑶","小明","大乔","桑启","武则天"}



forbid={"","钟无艳","兰陵王","云中君","东皇太一",""}#禁用
our_heroes = {#我方选人
    "对抗路": [""],  
    "发育路": ["艾琳"],  
    "中路": ["甄姬"],  
    "打野": ["澜"],   
    "游走": [""]    }
enemy_heroes = {#敌方选人
    "对抗路": ["亚瑟"],
    "发育路": ["马可"],
    "中路": [""],
    "打野": ["宫本"],
    "游走": ["刘禅"]      }

# 遍历 our_heroes 字典，将只包含空字符串的列表替换为一个空列表 [] 无视""
for position, heroes in our_heroes.items():
    if all(hero == "" for hero in heroes):
        our_heroes[position] = []

# 根据我方英雄填充 available_heroes
available_heroes = []
for position, heroes in hero_positions.items():
    for hero in heroes :
        if hero not in our_heroes[position]:
                available_heroes.append(hero)

# # 增加我方英雄在available_heroes中出现的概率 没用
# for hero in our_heroes.values():
#     for _ in range(100):
#         for position in our_heroes:
#             if not our_heroes[position]:  # 如果当前位置没有英雄，则添加
#                 available_heroes.append(hero)
# 根据敌方英雄选择合适的我方英雄
if "哪吒" in enemy_heroes["对抗路"or"打野"]:
    suitable_heroes.extend(["太乙","女娲","大乔"])
# lanling
lanling = ["后羿", "伽罗"]
lanling = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in lanling)
if lanling:
    suitable_heroes.extend(["兰陵王","蒙恬","小乔"])
# yuange
yuange = ["妲己","西施","后羿"]
yuange = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in yuange)
if yuange:
    suitable_heroes.extend(["元歌","吕布"])
# donghuangtaiyib
donghuangtaiyib = ["东皇太一"]
donghuangtaiyib = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in donghuangtaiyib)
if donghuangtaiyib:
    suitable_heroes.extend(["凯","橘右京","蔡文姬"])
# milaidi
milaidi = ["米莱迪"]
milaidi = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in milaidi)
if milaidi:
    suitable_heroes.extend(["火舞","周瑜","光信","姜子牙"])
# lulub
lulub = ["露露"]
lulub = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in lulub)
if lulub:
    suitable_heroes.extend(["李白","艾琳","司马","芈月","司空震"])
# anqila
anqila = ["黄忠"]
anqila = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in anqila)
if anqila:
    suitable_heroes.extend(["安琪拉","女娲","黄刀吕布"])
# yixing
yixing = ["弈星"]
yixing = any(hero in our_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in yixing)
if yixing:
    suitable_heroes.extend(["廉颇"])
# xiahou
xiahou = ["夏侯"]
xiahou = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in xiahou)
if xiahou:
    suitable_heroes.extend(["橘子","露露"])
# libai
libaib = ["李白"]
libaib = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in libaib)
if libaib:
    suitable_heroes.extend(["韩信","墨子","虞姬"])
# mengtian
libaib = ["亚瑟","钟馗","甄姬"]
libaib = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in libaib)
if libaib:
    suitable_heroes.extend(["蒙恬"])

# sunbin
sunbin = ["孙膑"]
sunbin = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in sunbin)
if sunbin:
    suitable_heroes.extend(["蔡文姬","钟馗"])
# tank
tank = ["程咬金","猪八戒","廉颇","夏侯","蒙恬","白起","孙策","钟馗","阿古朵","牛魔","鲁班大师","庄周","张飞","刘禅","凯"]
tank = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in tank)
if tank:
    suitable_heroes.extend(["吕布", "貂蝉","马可","典韦","杨戬"])
# guangxin
guangxin = ["钟馗","元歌","孙策","花木兰","虞姬","庄周","米莱迪"]
guangxin = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in guangxin)
if guangxin:
    suitable_heroes.extend(["光信"])
#ailin
ailin = ["虞姬","庄周"]
ailin = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in ailin)
if ailin:
    suitable_heroes.extend(["艾琳"])
#direnjie 
direnjie = ["海月","玄策","芈月","扁鹊","后羿","李元芳"]
direnjie = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in direnjie)
if direnjie:
    suitable_heroes.extend(["狄仁杰"])
#jialuo 
jialuo = ["海月","瑶","夏侯","刘禅","张飞","刘备"]
jialuo = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in jialuo)
if jialuo:
    suitable_heroes.extend(["伽罗"])
#lanlingwang 
lanlingwang = ["后羿","伽罗","米莱迪","元歌","小乔"]
lanlingwang = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in lanlingwang)
if lanlingwang:
    suitable_heroes.extend(["兰陵王"])    
#lanlingwangb 
lanlingwangb = ["兰陵王"]
lanlingwangb = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in lanlingwangb)
if lanlingwangb:
    suitable_heroes.extend(["守约","阿古朵","刘备","狄仁杰"])
#huowu
huowu = ["李白","西施","露露","典韦"]
huowu = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in huowu)
if huowu:
    suitable_heroes.extend(["火舞"])
#dunshanb
dunshanb = ["盾山"]
dunshanb = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in dunshanb)
if dunshanb:
    suitable_heroes.extend(["小乔","黄忠","鲁班","吕布","钟馗"])
#huowub
huowub = ["火舞"]
huowub = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in huowub)
if huowub:
    suitable_heroes.extend(["暃"])
# zhongkui
zhongkui = ["钟馗","刘禅"]
zhongkui = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in zhongkui)
if zhongkui:
    suitable_heroes.extend(["吕布", "甄姬","阿古朵","武则天","庄周","米莱迪"])
# chenyaojingb
chenyaojingb = ["陈咬金"]
chenyaojingb = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in chenyaojingb)
if chenyaojingb:
    suitable_heroes.extend(["明世隐","亚瑟"])
# simayib
simayib = ["司马懿"]
simayib = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in simayib)
if simayib:
    suitable_heroes.extend(["曹操","李元芳","凯"])
if "孙策" in enemy_heroes["对抗路"]:
    suitable_heroes.extend(["瑶"])
if "敖隐" in enemy_heroes["发育路"]:
    suitable_heroes.extend(["李元芳"])
if "瑶" in enemy_heroes["游走"]:
    suitable_heroes.extend(["伽罗"])
# simayib
lvbub = ["吕布"]
lvbub = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in lvbub)
if lvbub:
    suitable_heroes.extend(["元歌","镜","狂暴钟馗","橘子","暗信"])

if "亚连" in enemy_heroes["对抗路"]:
    suitable_heroes.extend(["镜"])
# huixuer
huixuer = ["橘子","杨玉环", "蔡文姬", "程咬金", "橘右京", "桑启", "杨戬", "扁鹊","芈月","朵莉亚"]
huixuer = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in huixuer)
if huixuer:
    suitable_heroes.extend(["哪吒","宫本","杨戬"])
if "扁鹊" in enemy_heroes["中路"]:
    suitable_heroes.extend(["哪吒", "狄仁杰","宫本"])
# if "甄姬" or "白起" or "钟无艳" or "玄策" or "钟馗" or "孙策" in enemy_heroes["对抗路" or "中路" or "打野" or "游走"]:
#     suitable_heroes.extend(["庄周","光信"])
# control
control = ["甄姬", "白起", "钟无艳", "玄策", "钟馗", "孙策"]
control = any(hero in enemy_heroes[position] for position in ["对抗路","发育路", "中路", "打野", "游走"] for hero in control)
if control:
    suitable_heroes.extend(["庄周", "光信"])
if "蔡文姬" in enemy_heroes["游走"]:
    suitable_heroes.extend(["牛魔", "哪吒"])
if "兰陵王" in enemy_heroes["打野"]:
    suitable_heroes.extend(["守约","狼狗","阿古朵"])
if "黄忠" in enemy_heroes["发育路"]:
    suitable_heroes.extend(["吕布","钟馗","女娲","守约"])
print("克制链:",suitable_heroes)

# 初始化推荐英雄列表
recommended_heroes = []

# 确保推荐的英雄列表中只有一个英雄在 healing_heroes 列表中 assass
while len(healing_heroes.intersection(recommended_heroes)) != 1 or len(assass.intersection(recommended_heroes)) != 1 or len(forbid.intersection(recommended_heroes)) !=0 or len(set(suitable_heroes).intersection(set(recommended_heroes))) == 0 or len(set(magic).intersection(recommended_heroes))>=2 or len(set(tanker).intersection(recommended_heroes)) >= 2:
    recommended_heroes = []
    # 为每个位置推荐一个英雄
    for position, heroes in hero_positions.items() :
        # 从 available_heroes 中选择一个英雄
        if not our_heroes[position] and enemy_heroes:#enemy_heroes[position]下一行提上来的 下行没用？敌人把[position]去掉才行？
            selected_hero = random.choice([hero for hero in heroes if hero in available_heroes not in our_heroes[position] not in enemy_heroes[position]])
            recommended_heroes.append(selected_hero)

    #把剩余的加上
    for position, heroes in our_heroes.items():
        if isinstance(heroes, list):
            for hero in heroes:
                recommended_heroes.append(hero)
    #防止重复
    while True:
        temp_heroes = set(recommended_heroes)  # 使用集合来消除重复元素
        unique_heroes = list(temp_heroes)  # 将集合转换回列表

        # 如果去重后的英雄列表长度与原列表长度相同，说明没有重复元素
        if len(unique_heroes) == len(recommended_heroes):
            break  # 退出循环

if len(set(suitable_heroes).intersection(set(recommended_heroes)))>=1:
    print("AI推荐妙手", list(set(suitable_heroes).intersection(set(recommended_heroes))))
# else:
#     print("没有明显克制")
    
# # 输出最终推荐的英雄列表
print("推荐阵容：", recommended_heroes)
# # 检查 recommended_heroes 列表中是否包含至少两个 heroes_to_check 中的英雄
# if len(set(magic).intersection(recommended_heroes)) >= 2:
#     print("法师过多，可选司马懿")
# if len(set(tanker).intersection(recommended_heroes)) >= 2:
#     print("坦克过多，可选露露")

