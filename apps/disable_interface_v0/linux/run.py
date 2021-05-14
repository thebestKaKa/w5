#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger


async def disable_physical_interface(id):
    logger.info("[disable_physical_interface] APP执行参数为: {id}", id=id)

    return {"status": 0, "result": "告警等级一，禁用：" + id + "号接口"}



