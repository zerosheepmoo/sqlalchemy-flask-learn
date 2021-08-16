# Select / Insert / Delete

## Insert

- Create the Python object
- Add it to the session
- Commit the session

```python
me = User('admin', 'admin@example.com')
db.session.add(me)
db.commit()
```

## Delete

- use `delete` instead of `add`

## Select

- [공식문서 BaseQuery](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.BaseQuery)
- [Query API (sqlalchemy)](https://docs.sqlalchemy.org/en/14/orm/query.html#query-api)

```python
peter = User.query.filter_by(username='peter').first()
```

## 기타

`render_template` 이용해서 뷰로 쿼리할 수 있음.

```python
@app.route('/user/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_user.html', user=user)
```
