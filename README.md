# Scrapy 妹子图

## 一、介绍

**Scrapy** 爬取妹子图网站(ituba.cc)

默认存储环境 MongoDB

## 二、开发环境 MacOS

Python 3.7

MongoDB 4.0.2

Scrapy 2.2

## 三、使用说明

1. 数据库 MongoDB 配置(默认)
   需要安装 MongoDB

```bash
# vi Meizitu/meizitu/settings.py
MONGO_URI = '127.0.0.1:27017' # 设置为你的MongoDB路径
MONGO_DATABASE = 'scrapy' # 本项目默认创建的MongoDB库名
```

2. 本地图片存储(可选)
   选择该配置，图片会下载在用户目录下的 meizi 目录
   例如 /Users/acke/meizi/

```bash
# vi Meizitu/meizitu/settings.py

# 注释掉MongoDBPipeLine那一行
# 开启LocalPipeLine
ITEM_PIPELINES = {
'meizitu.pipelines.MongoPipeLine': 100,
#  'meizi.pipelines.LocalPipeLine': 200,
}
```

3. 配置成功后运行

```bash
git clone https://github.com/YIKAILucas/meizitu.git
cd Meizitu
pip install -r requirements.txt

python3 main.py
```

## 四、效果图

![效果图](https://i.loli.net/2020/06/29/pmyvNXH9x7PgKJ6.png)

![](https://i.loli.net/2020/06/29/kQKFj6MpsIfgzac.png)

## 后续 Feature

- [ ] 1. 添加另一个妹子图网站(https://www.mzitu.com/)
- [ ] 2. 添加 URL 去重策略和图片去重策略（PS:妹子图网站有大量图片重复）
- [ ] 3. 引入 IP 池项目
