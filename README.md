# Dockers
dockerの環境をまとめたもの

## 自分
https://hub.docker.com/u/bokotomo/

## apche2.4
```
cd tomo-apache
docker-compose -up -d
```

## nginx1.13
```
cd tomo-nginx
docker-compose -up -d
```

## php7.1.9
```
cd tomo-php7
docker-compose -up -d
```

## php7.1.9, mysql8, phpmyadmin
```
cd tomo-php7-mysql-phpmyadmin
docker-compose -up -d
```

## django
```
cd tomo-django
docker-compose run web django-admin.py startproject test .
docker-compose up -d
```

## tomo-slack-post
```
cd tomo-slack-post
docker-compose up -d
curl -X POST -d text=ok 127.0.0.1:5000/api/v1/send
```

## mysql接続
```
mysql -h127.0.0.1 -P3306 -pdev -udev -Ddev
```

