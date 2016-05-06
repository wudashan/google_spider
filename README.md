# 谷歌镜像爬虫
`google.py` 负责从特定网站爬取谷歌镜像地址存入到数据库

`ping.py` 负责更新数据库谷歌镜像url，检测是否还能访问

`dbconn.php` 和 `welcome.php` 可选,放置在网站目录下

`dbconn.php` 负责创建数据库连接

`welcome.php` 负责从数据库随机选一条有效的谷歌镜像url,然后跳转
