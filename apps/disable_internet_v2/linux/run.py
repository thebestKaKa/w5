#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger


async def disable_internet(id):
    logger.info("[disable_internet_v0] APP执行参数为: {id}", id=id)

    return {"status": 0, "result": "告警等级三，断开：" + id + "号设备网络"}



