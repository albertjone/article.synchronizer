apt-get remove docker docker-engine docker.io containerd runc -y

sudo apt-get remove docker docker-engine docker.io containerd runc -y

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

apt-get update -y

apt-get install docker-ce docker-ce-cli containerd.io -y

docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=robot@mysql -d mysql:5.6

docker exec -it mysql bash

mysql -uroot -probot@mysql

# 创建数据库(数据库名:solo;字符集utf8mb4;排序规则utf8mb4_general_ci)
create database solo DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;


docker run --detach --name solo --network=host \
--env RUNTIME_DB="MYSQL" \
--env JDBC_USERNAME="root" \
--env JDBC_PASSWORD=robot@mysql"" \
--env JDBC_DRIVER="com.mysql.cj.jdbc.Driver" \
--env JDBC_URL="jdbc:mysql://127.0.0.1:3306/solo?useUnicode=yes&characterEncoding=UTF-8&useSSL=false&serverTimezone=UTC" \
--rm \
b3log/solo --listen_port=8080 --server_scheme=https --server_host=www.dawncreat.com --server_port=443


cd / && mkdir dockerData/nginx dockerData/nginx/conf dockerData/nginx/logs dockerData/nginx/www dockerData/nginx/ssl -p