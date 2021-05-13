#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger


async def multi_burst(id):
    logger.info("[multi_burst] APP执行参数为: {id}", id=id)

    return {"status": 0, "result": "多场站爆发对应执行策略：" + id}



