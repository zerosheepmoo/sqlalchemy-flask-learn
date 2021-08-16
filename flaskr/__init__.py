import json
from os import ctermid
from .app import db, app
from sqlalchemy.orm import joinedload
from .models import User, Post, Category

# metadata 에 등록한 table 과 db 를 생성
db.create_all()

@app.route('/add-t')
def add_two_users():
    res = {"admin": False, "guest": False}
    # row 생성
    admin_data = User.query.filter_by(username='admin').all()
    guest_data = User.query.filter_by(username='guest').all()
    if not admin_data:
        admin = User(username='admin', email='admin@example.com')
        db.session.add(admin)
        res["admin"] = repr(admin)
    if not guest_data:
        guest = User(username='guest', email='guest@example.com')
        db.session.add(guest)
        res["guest"] = repr(guest)
    # db 에 반영
    db.session.commit()
    return json.dumps(res)

@app.route('/del-t')
def delete_two_users():
    res = {"admin": False, "guest": False}
    admin_data = User.query.filter_by(username='admin').first()
    guest_data = User.query.filter_by(username='guest').first()
    if admin_data:
        db.session.delete(admin_data)
        res["admin"] = True
    if guest_data:
        db.session.delete(guest_data)
        res["guest"] = True

    db.session.commit()
    return json.dumps(res)
    
# 관계
@app.route('/add-post')
def add_post():
    py = Category(name='Python')
    Post(title='Hello Python!', body='Python is pretty cool', category=py)
    p = Post(title='Snakes', body='Ssssssss')
    py.posts.append(p)
    db.session.add(py)

    # Category 를 세션 add 한 것만으로도 Post 가 add 댐!
    # 빠르게 로드 되는데, lazy loaded. 
    print('py post is: ')
    print(py.posts)
    db.session.commit()

    return {}

# 문제는 보틀넥이 생길 수 있다.
# 그럴 때는 다음과 같이 single 하게 실행 시키면 된다.
@app.route('/posts')
def get_post():
    query = Category.query.options(joinedload('posts'))
    for category in query:
        print(category)
        print(category.posts)

    return {}

@app.route('/del-posts')
def del_posts():
    print(Post.query.all())
    for post in Post.query.all():
        db.session.delete(post)

    print(Category.query.all())
    for cate in Category.query.all():
        db.session.delete(cate)
    db.session.commit()
    
    return {}
    
@app.route('/posts/nosna')
def get_no_snake_posts():
    py = Category.query.first()
    if py:
        # `with_parent` 사용 가능
        print(Post.query.with_parent(py).filter(Post.title != 'Snakes').all())
    return {}


if __name__ == '__main__':
    app.run(debug=True, threaded=True)