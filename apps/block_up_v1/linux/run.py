#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger


async def block_up(id):
    logger.info("[block up] APP执行参数为: {id}", id=id)

    return {"status": 0, "result": "告警等级二，禁用：" + id + "号接口"}



