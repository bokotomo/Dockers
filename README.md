# Dockers
dockerの環境をまとめたもの

## 自分
https://hub.docker.com/u/bokotomo/

## apche2.4
```
cd tomo-apache2-4
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
mysql -h127.0.0.1 -P3306 -pdev -udev -Ddev
```


