# SSH를 이용한 원격 접속 및 코드 원격빌드(파이참에서) 관련 설정.

### ** 원격빌드 관련 환경정보 **

- 서버: 우분투 16.04
- 클라이언트: 맥OS 모하비



### 1. 맥에서 리눅스 서버 원격접속 방법

- 우분투 터미널에서 아래의 명령어를 입력하여 SSH 패키지를 설치한다.

  ```
  sudo apt-get install ssh
  ```

- 우분투 터미널에서 `ifconfig`를 이용하여 ip주소를 알아낸다.

- 맥 터미널에서 아래의 명령어를 실행하면 리눅스서버에 접속 할 수 있다.

  ```
  ssh username@ip주소
  ```

- 만일 코드는 서버에서 돌리고 matplotlib처럼 displa와 관련된 것은 클라이언트(맥북)에서 보고 싶을 경우 X11 포워딩을 이용해야한다. 이 때는 아래의 명령어로 우분투 서버에 접속 해야한다.

  ```
  ssh -X username@ip주소
  ```

- 공용/집 와이파이나 휴대폰 핫스팟(테더링) 기능을 이용하여 접속하면 반응이 없고 **time out**에러가 발생할 수 있다. 이 경우에는 기본값으로 설정된 22번 포트를 원하는 포트로 바꿔야한다. 아마 22번 포트는 막혀있는 듯 하다.. 정확한 이유는 모름.

  - 우분투 서버에 `sudo vi /etc/ssh/sshd_config`를 입력한후 포트설정에서 새로운 포트를 추가한다.
  - 그 후 맥에서 우분투 서버에 접속 할 때는 `ssh -X -p 새로운포트번호 username@ip주소`를 사용한다.

- 설정 변경 후에는 반드시 `service ssh restart`를 해 주어야 설정이 반영된다.



### 2. 파이참 원격빌드 방법

- 1) 먼저 서버가 되는 우분투에 SSH관련 패키지를 설치해주어야한다. 패키지가 설치되어 있지 않으면 서버에 접속할 수 없다...

- ```
  apt-get install openssh-server
  ```

- 2) 기본 SFTP 포트번호는 22로 설정되어 있으나 포트번호를 변경하고 싶다면 아래 명령어를 이용하여 포트번호에 해당하는 값을 바꾸고, 변경내용 반영하기 위해 SSH를 재시작 해준다.

- ```
  vi /etc/ssh/sshd_config # ssh 설정 파일에 접속
  service ssh restart
  ```

- 3) 나머지 설정은 두번째 레퍼런스를 참조하여 진행하자.



### 3. SSH를 이용하여 원격서버(우분투)의 볼륨을 클라이언트(맥북)에 마운트 시키는 방법.

- 1) homebrew를 설치한다(https://brew.sh/index_ko).

- 2) 터미널에 아래 명령어를 실행한다.  

  ```
  brew cask install osxfuse
  brew install sshfs
  ```

- 3) 터미널에 아래 명령어를 실행한다.

- ```
  # 외부에서 공용 와이파이나 핫스팟으로 연결시
  # reconnect 옵션은 연결이 끊겼을 때 재연결하는 옵션임.
  sshfs -o reconnect -p xxx caitech@xxx.xxx.xx.xx:/home/caitech /Users/ku/caitech -ovolname=caitech
  
  # 연구실에서 연결시
  sshfs -o reconnect caitech@xxx.xxx.xx.xx:/home/caitech /Users/ku/caitech -ovolname=caitech
  
  # /local/mount/point 폴더는 해당 명령어 수행 후 '볼륨'으로 변환됨.
  
  # 변환될 볼륨의 이름을 -ovolname= 뒤에 적어주면 됨.
  ```

- 4) 끝. 정말 쉽다… 놀랍다...



### 레퍼런스

- [Ubuntu 16.04에서 SFTP 접속 포트 변경하기](http://developer-joe.tistory.com/176)
- [PyCharm SSH 연결하기](https://simonjisu.github.io/datascience/2018/06/24/pycharmssh.html)
- [원격서버 볼륨 마운트하는 방법](https://apple.stackexchange.com/questions/5209/how-can-i-mount-sftp-ssh-in-finder-on-os-x-snow-leopard)