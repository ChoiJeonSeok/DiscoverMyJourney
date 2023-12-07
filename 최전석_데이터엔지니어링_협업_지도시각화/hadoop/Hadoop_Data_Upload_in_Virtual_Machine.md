## TIL: Hadoop 가상 머신 데이터 업로드와 공유

### 가상 머신에 Hadoop 설치 및 데이터 업로드

1. 가상 머신 생성: VMware를 사용하여 가상 머신 4개를 생성하고, Hadoop 클러스터를 설치한다.
![1_hadoop_실행](https://github.com/ChoiJeonSeok/TIL/assets/82266289/d07c33c6-85dc-4683-89ff-05ac48cc1a7d)<br><br><br>
2. Folder Sharing 설정: VMware에서 "CDATA"라는 이름으로 호스트 컴퓨터의 "C:\Users\art\Downloads\CDATA"와 가상 머신 간의 폴더 공유 설정을 한다.
![2_호스트_가상머신 간 공유폴더 설정](https://github.com/ChoiJeonSeok/TIL/assets/82266289/13e7add2-e5e1-4826-9131-2c4bd7b69ba5)<br><br><br>
3. 데이터 업로드: 호스트 컴퓨터의 "C:\Users\art\Downloads\CDATA" 폴더에 있는 데이터를 가상 머신의 "/mnt/hgfs/CDATA" 또는 "/media/sf_CDATA" 폴더로 복사한다. 
![3_공유폴더 이동 및 파일 확인](https://github.com/ChoiJeonSeok/TIL/assets/82266289/e94828cb-f165-4fc3-8363-a6c58d687b8a)<br><br><br>
4. Hadoop으로 데이터 업로드: 가상 머신 내에서 HDFS로 데이터를 업로드한다.
   ```bash
   hadoop fs -put /mnt/hgfs/CDATA/* ./DATA
   ```
![4_hadoop에 데이터 업로드 후 확인](https://github.com/ChoiJeonSeok/TIL/assets/82266289/ea312943-05c0-4272-a392-dd60f2300f76)


# Hadoop으로 데이터 공유는 어디까지 적절한가?
- 로컬 네트워크 환경을 초과하여 클라우드 서비스처럼 데이터를 공유할 수 있어야 적절하게 Hadoop을 사용하고 있는 것은 아니다. 
- 필요에 맞게 설정해서 사용하면 된다.

### Hadoop의 목적
- Hadoop은 주로 대규모 데이터 처리 및 분석을 위한 분산 데이터 처리 프레임워크이다. 
- 확장성, 성능, 비용 효율성, 내결함성을 갖추고 다양한 데이터 유형 처리를 유연하게 하는 것을 목표로 삼는다.
- 데이터를 장소에 관계없이 공유하는 것이 목적이 아니다.

### 가상 머신과 Hadoop
- 여러 기기를 사용하는 것이 일반적이나, Hadoop을 처음 배울 때 비용 문제로 한 컴퓨터에서 한다면, 서로 다른 하드 디스크를 Hadoop 클러스터 구축에 사용할 수 있겠다. 
- 이러한 경우 Hadoop 클러스터를 구축하기 위해 가상 머신을 사용할 수 있다.
- 아쉽게도 다양한 기기를 이용하지는 못하여 가상 머신으로 독립된 환경과 리소스가 있는 환경을 구축하여 실습을 했다.
- 마스터와 세 개의 워커 노드를 가지고 실습을 진행하였다.

### Hadoop을 통한 데이터 공유
- 호스트와 master VM과의 공유 폴더를 지정하였다. 
- 공유 폴더에 업로드할 파일을 올린 후 master VM에서 hadoop으로 업로드 하였다.
- hadoop fs -put [local_file_path] [hdfs_directory]

### 로컬 호스트와 Hadoop
- 로컬머신의 디렉토리는 master VM에서 `/mnt/hgfs/`로 마운트되었다.

### 팀원이 Hadoop을 이용할 수 있게 하기.
- 로컬 환경에 있는 팀원이 Hadoop을 이용할 수 있게 하려면 브리지 네트워킹을 통해야 한다.
- NAT가 아닌 브리지 네트워킹으로 호스트와 팀원 모두가 설정하면 두 VM은 동일한 로컬 네트워크에 속하게 된다.
- 팀원의 VM은 호스트 컴퓨터의 IP 주소에 접근할 수 있게 된다.

### 팀원의 VM에서 데이터 접근
- 팀원이 데이터를 조회하고 다운로드만 받는 경우 호스트 머신에서 `/etc/hosts`에 등록하지 않아도 된다.
- 팀원은 `hadoop fs -get [hdfs_file_path] [local_directory]`와 같은 명령어를 사용하여 데이터를 다운받을 수 있다.
- 경우에 따라서는 SSH 접속을 설정할 수도 있다.

### 결론.
- Hadoop의 주요 목적은 클러스터 내에서 분산 데이터 처리이며, 다른 네트워크나 지역 간의 직접적인 데이터 공유를 위한 것이 아니다.
- 개별 네트워크 간의 데이터 공유는 클라우드 서비스 등 추가적인 서비스를 이용하는 것이 좋다.
- VPN을 활용하여 로컬 네트워크로 먼저 들어오게 한 뒤 브리지 네트워크 설정을 할 수 있는지 시도해보는 것도 좋을 듯 하다.