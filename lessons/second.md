# 모델 선언하기

- `db.Model`로 Base class 를 콜할 수 있다.
- 자동으로 `__tablename__` 어트리뷰트를 만들어준다.
  - CamelCase => camel_case

## 순서

1. 모델을 만든다.
1. create_all() 로 등록한다.
1. db 관련 작업들...
1. drop_all() 한다.

## 간단한 예시

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```

- `Column` 사용하기
  - 첫번째 아규먼트는 타입

### 타입테이블

타입 | 설명
:---:|:---:
Integer | an integer
String(size) | a string with a maximum length (optional in some databases, e.g. PostgreSQL)
Text | some longer unicode text
DateTime | date and time expressed as Python datetime object.
Float | stores floating point values
Boolean | stores a boolean value
PickleType | stores a pickled Python object
LargeBinary | stores large arbitrary binary data

## 일 대 다 관계

```python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)

```

- `relationship()`
- `ForeignKey`
- one-to-one relationship you can pass `uselist=False` to `relationship()`
- `backref`는 `Address` class에 프로퍼티를 생성함
  - `my_address.person` 로 사람 접근 가능

### `lazy` 스테이터스

- `'select'` / `True` (which is the default, but explicit is better than implicit) means that SQLAlchemy will load the data as necessary in one go using a standard select statement.
- `'joined'` / `False` tells SQLAlchemy to load the relationship in the same query as the parent using a `JOIN` statement.
- `'subquery'` works like `'joined'` but instead SQLAlchemy will use a subquery.
- `'dynamic'` 은 많은 아이템을 갖고 있고 추가적인 sql 필터를 항상 적용 시켜주고 싶을 때 유용하다.
  - 아이템을 로딩하기 전에 refine 할 수 있는 또 다른 쿼리를 반환한다.
  - 동적 `user.addresses` 관계에 해당하는 쿼리 객체는 `Address.query.with_parent(user)`를 사용하여 생성할 수 있으며, 여전히 필요에 따라 relationship 에서 lazy 또는 eager 로드를 사용할 수 있다.
  - 주의할 점은 쿼리하는 동안에는 다른 로딩 전략으로 바꿀 수 없으므로 `lazy=True` 를 위해서는 이를 피하는 것이 좋다.

### `backref()` 에서의 lazy

```python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', lazy='select',
        backref=db.backref('person', lazy='joined'))
```

## 다 대 다 관계

[공식 문서](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships)

- helper table 을 만들기

```python
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
```

- `Page.tags` to be loaded immediately after loading a Page, but using a separate query.
- This always results in two queries when retrieving a Page, but when querying for multiple pages you will not get additional queries.
