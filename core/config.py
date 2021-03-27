from pydantic import AnyHttpUrl
from typing import List
import os


class Settings:
    ENV = os.environ.get("fast_env", "DEV")  # 本次启动环境
    APP_NAME = "fastapi-vue-admin"
    # api前缀
    API_PREFIX = "/api"
    # jwt密钥,建议随机生成一个
    SECRET_KEY = "ShsUP9qIP2Xui2GpXRY6y_4v2JSVS0Q2YOXJ22VjwkI"
    # token过期时间
    ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60
    # 跨域白名单
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:9528"]
    # db配置
    DB_URL = "mysql+pymysql://fastapi_vue:YmmPsJwxEJFZzpFW@localhost:3306/fastapi_vue"
    
    # 启动端口配置
    PORT = 8999
    # 是否热加载
    RELOAD = True
    # 上传文件存储位置
    UPLOAD_FOLDER = "./upload_files"
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    # CMDB模板文件存储位置
    CMDB_FOLDER = "./cmdb_files"
    if not os.path.exists(CMDB_FOLDER):
        os.mkdir(CMDB_FOLDER)

settings = Settings()
