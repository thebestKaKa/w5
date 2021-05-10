#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import illegal_login


async def defense(text):
    logger.info("[Illegal_login] APP执行参数为: {text}", text=text)
    text = text.encode("utf-8")
    print("阻断恶意ip网关操作:", text)
    result = "success"
    return {"status": 0, "result": str(result, 'utf8')}



