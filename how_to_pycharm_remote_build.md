# SSH를 이용한 원격 접속 및 코드 원격빌드(파이참에서) 관련 설정.

### ** 원격빌드 관련 환경정보 **

- 서버: 우분투 16.04
- 클라이언트: 맥OS 모하비



### 1. 맥에서 리눅스 서버 원격접속 방법

- 우분투 터미널에서 아래의 명령어를 입력하여 SSH 패키지를 설치한다.
  - sudo apt-get install ssh
- 우분투 터미널에서 ifconfig를 이용하여 ip주소를 알아낸다.
- 맥 터미널에서 아래의 명령어를 실행하면 리눅스서버에 접속 할 수 있다.
  - ssh username@ip주소



### 2. 원격빌드 방법

- 먼저 서버가 되는 우분투에 SSH관련 패키지를 설치해주어야한다. 패키지가 설치되어 있지 않으면 서버에 접속할 수 없다...

  - apt-get install openssh-server

- 기본 SFTP 포트번호는 22로 설정되어 있으나 포트번호를 변경하고 싶다면 아래 명령어를 이용하여 포트번호에 해당하는 값을 바꾸고, 변경내용 반영하기 위해 SSH를 재시작 해준다.

  - vi /etc/ssh/sshd_config
  - service ssh restart

- 나머지 설정은 두번째 레퍼런스를 참조하여 진행하자.


### 레퍼런스

- [Ubuntu 16.04에서 SFTP 접속 포트 변경하기](http://developer-joe.tistory.com/176)
- [PyCharm SSH 연결하기](https://simonjisu.github.io/datascience/2018/06/24/pycharmssh.html)