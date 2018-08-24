<img src="./miscellaneous/mysql_structure.png">

<br>

## MySQL monitor 실행 방법.

```
# mysql monitor가 있는 경로로 들어간다.
cd /usr/local/mysql/bin/

# 사용자는 root이고 password를 안 보이게 입력하겠다.
# -u 뒤에 다른 도메인을 입력하면 그 도메인의 MySQL 서버에 접속하는 것임.
./mysql -uroot -p 
```

<br>

## SQL client

- 컴퓨터에 설치한것은 정확히 말하면 MySQL server와 MySQL client가 모두 설치 된 것이다.
- MySQL server는 DB가 저장된 컴퓨터를 말하고, client는 서버에 담긴 자료를 열람하기를 원하는 컴퓨터이다.
- MYSQL은 client tool을 이용해야만 sever에서 여러가지 조작이 가능하다.
- MySQL server를 설치하면 기본적으로 MySQL monitor라는 client tool이 설치된다. 이외에도 GUI 환경에서 컨트롤 할 수 있는 MySQL workbench라는 프로그램도 있다.



