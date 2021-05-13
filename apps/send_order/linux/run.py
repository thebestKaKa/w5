#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger


async def send_order(ip_adr):
    logger.info("[send order] APP执行参数为: {ip_adr}", ip_adr=ip_adr)

    return {"status": 0, "result": "发送阻断命令：" + ip_adr}



