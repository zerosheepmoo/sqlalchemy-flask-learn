# App Setup

## Installation

> [flask 설치 가이드](https://flask.palletsprojects.com/en/2.0.x/installation/)

```bash
# 환경설정
mkdir myproject
cd myproject
python3 -m venv venv

# 환경 활성화
. venv/bin/activate

# 플라스크 설치
pip3 install Flask
```

### Run

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Simple Desc

- [flask-sqlalchemy 공식문서](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)

- flask 앱은 [Flask 클래스](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask)
  의 인스턴스다.
  - config 나 url을 이 클래스로 설정
- [sqlalchemy full docu](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy)를 참고하며 읽도록 하자.
- You have to commit the session, but you don’t have to remove it at the end of the request, Flask-SQLAlchemy does that for you.

## 주의

### 시간제한

Certain database backends may impose different inactive connection timeouts, which interferes with Flask-SQLAlchemy’s connection pooling.

By default, MariaDB is configured to have a 600 second timeout. This often surfaces hard to debug, production environment only exceptions like 2013: Lost connection to MySQL server during query.

If you are using a backend (or a pre-configured database-as-a-service) with a lower connection timeout, it is recommended that you set SQLALCHEMY_POOL_RECYCLE to a value less than your backend’s timeout.
