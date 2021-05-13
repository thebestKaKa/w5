#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger


async def block_up(ip_adr):
    logger.info("[Block up] APP执行参数为: {ip_adr}", ip_adr=ip_adr)

    return {"status": 0, "result": "执行阻断操作：" + ip_adr}



