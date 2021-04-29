# @Time : 2021/4/29 21:11
# @Author : LiuBin
# @File : FastAPI.py
# @Description : 
# @Software: PyCharm

"""FastAPI
* 异步python web框架
* FastAPI ≈ Pydantic + Starlette
* 搭配ASGI服务器 Uvicorn 或 Hypercorn
* 内置交互文档 - Swagger UI 和 ReDoc
"""

# 1、Route参数类型上
from fastapi import FastAPI, Query, Body, Path
