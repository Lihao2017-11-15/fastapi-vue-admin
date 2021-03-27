# fastapi-vue-admin
使用fastapi和vue-element-admin构建的管理后台

目前配置直接写在配置文件中,生产环境推荐使用Nacos作为配置中心

## 项目初始化
```shell
pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple
```
- windows下可能需要安装如下软件：
Micorosoft visio c++
https://go.microsoft.com/fwlink/?LinkId=691126
- 安装cryptography openssl报错:
下载安装https://slproweb.com/products/Win32OpenSSL.html
将安装后目录的include下的openssl目录复制到python的include目录下
将安装后目录中lib下的libcrypto.lib和libssl.lib复制到python的libs目录下
- 在安装mysqlclient时会出现报错，解决方法如下:
https://blog.csdn.net/alvechen/article/details/95040255

## 数据库初始化
- 数据库创建一个名为fastapi_vue的mysql数据库,编码格式utf8mb4
- 数据库更新使用alembic
``` shell
alembic init alembic
执行后会生成alembic相关文件和目录
```
- 修改./alembic.ini文件42行
```
sqlalchemy.url = driver://user:pass@localhost/dbname
改成实际的数据库连接，如：
sqlalchemy.url = mysql+pymysql://usr:pwd@localhost:3306/fastapi_vue
```
- 修改./alembic/env文件，添加如下内容
``` python
import os
import sys
# 把当前项目路径加入到path中
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models.base import Base
target_metadata = Base.metadata
注释掉 target_metadata = None
```
- 生成执行文件
```
alembic revision --autogenerate -m "first commit"
# 执行上面后数据库中会自动新建alembic_version表

alembic upgrade head
# 执行上面后数据库中会自动新建./modes下面定义的表
```


## 项目启动
```shell script
python main.py
```

## 初始化数据
```
表结构创建完成后执行目录下的init.sql文件插入初始数据
```
### 查看项目swagger
访问http://localhost:端口号/docs即可

![swagger](asserts/swagger.png)

### 启动前端
```shell script
cd front
npm install --registry=https://registry.npm.taobao.org
npm run dev
```

#### 登陆页面
初始账户密码:admin/123456
![login](asserts/login.png)

#### 主页
![dashboard](asserts/dashboard.png)

#### 用户管理
![users](asserts/users.png)

![edit_user](asserts/user_edit.png)

![add_user](asserts/user_add.png)

#### 角色管理
![role](asserts/role.png)

![edit_role_user](asserts/edit_role_user.png)

授权每个角色拥有的菜单
![edit_role_menu](asserts/edit_role_menu.png)

授权每个角色的接口访问权限
![edit_role_perm](asserts/edit_role_perm.png)

#### 权限管理
需要授权的接口
![perm](asserts/perm.png)

#### 菜单管理
![menu](asserts/menu.png)

#### 操作记录
![record](asserts/record.png)

#### cmdb模型管理
![cmdb_List](asserts/cmdbList.png)
##### cmdb新增模型
![cmdb_type_add](asserts/cmdb_add_type.png)

点击模型可以查看修改属性
##### cmdb模型属性
![cmdb_type_item](asserts/cmdb_type_item.png)

#### cmdb实例管理
![cmdb_instance](asserts/cmdb_instance.png)

点击可以查看类型下所有录入实例
##### cmdb实例详情
![cmdb_instance_detail](asserts/cmdb_instance_lists.png)
##### 数据录入
![cmdb_add_instance](asserts/cmdb_add_instance.png)

可以通过Excel进行批量导入
![cmdb_import](asserts/cmdb_import.png)

针对Linux服务器提供web terminal功能
![cmdb_terminal](asserts/web_terminal.png)
![terminal_detail](asserts/terminal_detail.png)