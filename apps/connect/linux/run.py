#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import random


async def connect(ip_adr):
    logger.info("[connect] APP执行参数为: {ip_adr}", ip_adr=ip_adr)
    if random.randint(0, 1) == 0:
        return {"status": 0, "result": 0}
    else:
        return {"status": 1, "result": 1}



