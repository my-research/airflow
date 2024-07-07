# apache airflow

이 프로젝트는 astro cli 를 이용하여 local 에서 airflow 개발 환경을 구성합니다.

astro 를 통해 local 개발 환경 세팅 방법

- [https://www.astronomer.io/docs/astro/cli/install-cli](https://www.astronomer.io/docs/astro/cli/install-cli)
- [https://www.astronomer.io/docs/astro/cli/get-started-cli](https://www.astronomer.io/docs/astro/cli/get-started-cli)
- [https://www.astronomer.io/docs/learn/pycharm-local-dev](https://www.astronomer.io/docs/learn/pycharm-local-dev)

# how to run project

실행

```bash
astro dev start
```

종료

```bash
astro dev stop
```

재실행

```bash
astro dev restart
```

# 학습 목록

[dag 를 생성하는 3가지 방법](#),
[bash operator 사용](#),
[dag 에서 task direction 설정](#),
[bashOperator 를 이용하여 shell script 실행](#),
[PythonOperator 사용하기](#),
[bash operator 사용](#),

# airflow 설치

- [https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'
```
