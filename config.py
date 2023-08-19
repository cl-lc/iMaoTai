# -*- coding: utf-8 -*-

import os

ITEM_MAP = {
    "10213": "53%vol 500ml贵州茅台酒（癸卯兔年）",
    "10214": "53%vol 375ml×2贵州茅台酒（癸卯兔年）",
    "10056": "53%vol 500ml茅台1935",
    "2478": "53%vol 500ml贵州茅台酒（珍品）"
}

# 需要预约的商品(默认只预约2个赚钱的茅子)
########################
ITEM_CODES = ['10213', '10214']

# push plus 微信推送,具体使用参考  https://www.pushplus.plus
# 例如： PUSH_TOKEN = '123456'
########################
# 不填不推送消息，一对一发送
# 为了安全，这里使用的环境配置。git里面请自行百度如何添加secrets。pycharm也可以自主添加。如果你实在不会，就直接用明文吧（O.o）
PUSH_TOKEN = os.environ.get("PUSHPLUS_KEY")
########################

# 个人用户 credentials 路径
# 不配置，使用默认路径，在项目目录中;如果需要配置，你自己应该也会配置路径
# 例如： CREDENTIALS_PATH = './myConfig/credentials'
########################
CREDENTIALS_PATH = './credentials'
########################

# 预约规则配置
# 因为目前支持代提的还是少，所以还是建议默认预约最近的门店
########################
# 预约本市出货量最大的门店
MAX_ENABLED = False
# 预约你的位置附近门店
DISTANCE_ENABLED = True
########################
