第一步：通过pycharm生成一个DJANGO的项目文件，配置虚拟环境

第二步：调用python运行项目文件目录下的manage.py，生成一个app文件
    #python manage.py startapp 项目名

第三步：配置项目文件
    1）删除默认生成的templates文件
    2）删除settings.py里 'DIRS': [] 对于路径

第四步：注册app，在settings.py里的 INSTALLED_APPS = [
    # 项目名.包名.类名
]

第五步：配置数据库模板
    1）settings.py中配置数据库模板：
    #DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "数据库名称",
        "USER": "账号",
        "PASSWORD": "密码",
        "HOST": "127.0.0.1",
        "PORT": 3306,
    }
}
    2）models.py里加入预设的数据库表内容
    3）预设数据表内容添加到数据库，"tools"-"Run manage.py task"-
                                                          #makemigrations
                                                          #migrate

第六步：构造静态文件‘static’包括js、css、img等等

第七步：配置页面、函数、html文件
    1）urls.py
        配置路由，引入项目包导入view页面
        #from 项目名 import view
        构建路径适配view文件
        #path('depart/list/',views.depart_list)
    2)views.py
        在views.py生成路径对应的函数和功能
        #def depart_list(request):
            return rander(request,'xxx.html')
    3)templates - html文件
        创建页面文件xxx.html
        引入一系列文件
        #{% load static %}
        #<link rel="stylesheet" href="{% static 'plugins/bootstrap-5.3.0-alpha1-dist/css/bootstrap.min.css' %}">
        #<script src="{% static 'js/jquery.min.js' %}"></script>