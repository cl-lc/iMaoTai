# -*- coding: utf-8 -*-

import logging
import sys

import config
import login
import process

def run(event, context):
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
                        stream=sys.stdout,
                        datefmt=DATE_FORMAT)

    print("====== MainStartRun =======")

    process.get_current_session_id()

    # 校验配置文件是否存在
    configs = login.config
    if len(configs.sections()) == 0:
        logging.error("配置文件未找到配置")
        sys.exit(1)

    
    for section in configs.sections():
        mobile = section
        province = configs.get(section, 'province')
        city = configs.get(section, 'city')
        token = configs.get(section, 'token')
        userId = configs.get(section, 'userid')
        lat = configs.get(mobile, 'lat')
        lng = configs.get(mobile, 'lng')

        p_c_map, source_data = process.get_map(lat=lat, lng=lng)

        process.UserId = userId
        process.TOKEN = token
        process.init_headers(user_id=userId, token=token, lng=lng, lat=lat)
        # 根据配置中，要预约的商品ID，城市 进行自动预约
        try:
            for item in config.ITEM_CODES:
                max_shop_id = process.get_location_count(province=province,
                                                        city=city,
                                                        item_code=item,
                                                        p_c_map=p_c_map,
                                                        source_data=source_data,
                                                        lat=lat,
                                                        lng=lng)
                # print(f'max shop id : {max_shop_id}')
                if max_shop_id == '0':
                    continue
                shop_info = source_data.get(str(max_shop_id))
                title = config.ITEM_MAP.get(item)
                shopInfo = f'商品:{title};门店:{shop_info["name"]}'
                logging.info(shopInfo)
                reservation_params = process.act_params(max_shop_id, item)
                # 核心预约步骤
                r_success = process.reservation(reservation_params, mobile, title)
                # 为了防止漏掉推送异常，所有只要有一个异常，标题就显示失败
                if r_success:
                    # 领取小茅运和耐力值
                    process.getUserEnergyAward(mobile)
        except BaseException as e:
            print(e)
            logging.error(e)

run(None, None)