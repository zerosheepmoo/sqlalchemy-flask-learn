from .app import db, app

# metadata 에 등록한 table 과 db 를 생성
db.create_all()

# from .models import User
# row 생성
# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')

# db 에 반영
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

# 쿼리
# User.query.all()
# User.query.filter_by(username='admin').first()

# 관계
# from .models import Category, Post

# py = Category(name='Python')
# Post(title='Hello Python!', body='Python is pretty cool', category=py)
# p = Post(title='Snakes', body='Ssssssss')
# py.posts.append(p)
# db.session.add(py)

# Category 를 세션 add 한 것만으로도 Post 가 add 댐!
# 빠르게 로드 되는데, lazy loaded. 
# print('py post is: ', '')
# print(py.posts)

# 문제는 보틀넥이 생길 수 있다.
# 그럴 때는 다음과 같이 single 하게 실행 시키면 된다.
# from sqlalchemy.orm import joinedload
# query = Category.query.options(joinedload('posts'))
# for category in query:
#     print(category, category.posts)

# `with_parent` 사용 가능
# Post.query.with_parent(py).filter(Post.title != 'Snakes').all()

if __name__ == '__main__':
    app.run(debug=True, threaded=True)