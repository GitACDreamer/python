'ORM 对象关系映射框架'


class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Filed):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(mcs, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
        print('SQL :%s' % sql)
        print('ARGS: %s', str(args))


class Filed(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Filed):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Filed):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    password = StringField('password')
    email = StringField('email')

def main():
    # 创建一个用户
    user = User(id=12345, name='Bob', password='123456',email='leland@163.com')
    # 保存到数据库
    user.save()

if __name__ == '__main__':
    main()
