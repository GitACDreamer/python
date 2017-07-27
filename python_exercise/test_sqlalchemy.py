'SQL ORM技术的使用'

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接
engin = create_engine(
    'mysql+pymysql://root:123456@localhost:3306/student?charset=utf8', max_overflow=5, encoding='utf-8')

# 创建对象的基类
Base = declarative_base()


class user(Base):
    # 表的名称
    __tablename__ = 'user'
    # 表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    # 一对多
    books = relationship('book')


class book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    # 多的一方的book表是通过外键关联到user表
    user_id = Column(Integer, ForeignKey('user.id'))


def testOrm():
    try:
        # 创建DBSession
        DBSesssion = sessionmaker(bind=engin)

        # 创建session
        session = DBSesssion()
        # 创建user对象
        new_user = user(id=12, name='Silly')
        # 添加到session
        session.add(new_user)
        # 提交保存到数据库
        session.commit()

        # 创建query查询,filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
        userOne = session.query(user).filter(user.id == 1).one()
        print('type:', type(userOne))
        print('name:', userOne.name)
        for bookOne in userOne.books:
            print('(id,book)=', bookOne.id, bookOne.name)
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        # 关闭session
        session.close()


if __name__ == '__main__':
    testOrm()
