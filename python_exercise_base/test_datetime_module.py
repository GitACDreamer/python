'常用内建模块的使用datetime'

# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

from datetime import datetime, timedelta, timezone
import re


def testUsualModule():
    # 获取当前时间
    print(datetime.now())

    # 设置时间
    date = datetime(2017, 5, 31, 16, 40)
    print(date)

    # timestamp
    print(date.timestamp())

    # time tuple
    print(date.timetuple())

    # timestamp to datetime
    print(datetime.fromtimestamp(1496220000.0))

    # timestamp to utc datetime
    print(datetime.utcfromtimestamp(1496220000.0))

    # str to datetime
    cday = datetime.strptime('2017-05-31 16:40:00', '%Y-%m-%d %H:%M:%S')
    print(cday)

    # datetime to str
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %a ,%b %d'))

    # time 加减
    now = datetime.now()
    print(now)
    print(now + timedelta(hours=10))
    print(now - timedelta(days=1))
    print(now + timedelta(days=2, hours=12))

    # 本地时间转换成UTC时间
    # 创建时区UTc+8:00
    tz_utc_8 = timezone(timedelta(hours=8))
    now = datetime.now()
    print(now)
    newNow = now.replace(tzinfo=tz_utc_8)
    print(newNow)

    # 时区转换
    utc_dt = datetime.now().replace(tzinfo=timezone.utc)
    print(utc_dt)
    # 设置为北京时间
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)
    # 设置为东京时间
    tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt)
    # 将北京时间转换成东京时间
    tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt_tz = timezone(
        timedelta(hours=int(int(re.split(r'[UTC\:]', tz_str)[3]))))
    dt = dt.replace(tzinfo=dt_tz)
    print(dt.timestamp())


if __name__ == '__main__':
    testUsualModule()
    to_timestamp('2015-6-1 10:10:30', 'UTC+9:00')
    to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
