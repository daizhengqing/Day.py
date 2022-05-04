import arrow;

class Day ():
  def __init__ (self, time = None):
    self.originalTime = time;

    self.time = arrow.get(time) if (time != None) else arrow.now()
  
  # 获取时间戳
  # Day().valueOf(int = True) // 1637553124
  # Day().valueOf() // 1637553124.029572
  # Day('2021-10-09').valueOf() // 1633737600.0
  def valueOf (self, int = False):
    return self.time.int_timestamp if (int) else self.time.timestamp();

  # 返回datetime.date对象
  def date (self):
    return self.time.date()

  # 返回iso 8601的字符串
  # Day().iso() // '2019-01-19T18:30:52.442118+00:00'
  def iso (self):
    return self.time.isoformat();

  # 格式化日期
  # Day(1633737600).format('YYYY-MM-DD') // '2021-10-09'
  def format (self, formatter):
    return self.time.format(formatter);

  # 验证时间格式
  # Day('2021-10-09').validate('YYYY-MM-DD')  // true
  def validate (self, formatter):
    return True if (self.originalTime == self.time.format(formatter)) else False;

  # 获取年
  # 传参数的话会替换年, 然后返回Day对象
  # 也就是可以支持链式调用
  # 比如 Day('2021-10-19').year(2018).valueOf() // 1539907200.0
  # 不传参数则返回年
  # Day('2021').year() // 2021
  def year (self, year = None):
    if (year != None):
      self.time = self.time.replace(year = year)

      return self;
    
    return self.time.year;

  # 月
  def month (self, month = None):
    if (month != None):
      self.time = self.time.replace(month = month)

      return self;
    
    return self.time.month;

  # 月的第n日
  def day (self, day = None):
    if (day != None):
      self.time = self.time.replace(day = day)

      return self;
    
    return self.time.day;

  # 时
  def hour (self, hour = None):
    if (hour != None):
      self.time = self.time.replace(hour = hour)

      return self;
    
    return self.time.hour;
  
  # 分
  def minute (self, minute = None):
    if (minute != None):
      self.time = self.time.replace(minute = minute)

      return self;
    
    return self.time.minute;

  # 秒
  def second (self, second = None):
    if (second != None):
      self.time = self.time.replace(second = second)

      return self;
    
    return self.time.second;

  # 周
  # 传参数的话设置日期到本年的第n周
  # 不传参数返回日期在本年的第n周
  def week (self, week = None):
    result = self.time.week + 1;

    if (week != None):
      self.time = self.time.shift(weeks = week - result);

      return self;

    return result;

  # 星期几
  # 传参数的话会设置日期到本周的星期几；
  # 不穿参数返回星期1 - 7
  def weekday (self, weekday = None):
    result = self.time.weekday() + 1;

    if (weekday):
      self.time = self.time.shift(days = weekday - result);

      return self;
    
    return result;

  # 季度
  # 传参数的话设置日期到第n个季度
  # 不传返回当前季度
  def quarter (self, quarter = None):
    result = self.time.quarter;

    if (quarter):
      self.time = self.time.shift(quarters = quarter - result);

      return self;
    
    return result;

  # 求一组时间的最小值(最早的日期)
  # Day().min(['2021', '2021-10-21', Day('1928')])
  def min (self, days):
    min = None;

    for item in days:
      if (type(item) == Day):
        time = item.valueOf()
      else:
        time = Day(item).valueOf()
    
      if (min == None or time < min):
        result = item;

        min = time;

    return result;

  # 求一组时间的最大值(最晚的日期)
  # Day().min(['2021', '2021-10-21', Day('1928')])
  def max (self, days):
    max = None;

    for item in days:
      if (type(item) == Day):
        time = item.valueOf()
      else:
        time = Day(item).valueOf()

      if (max == None or time > max):
        result = item;

        max = time;

    return result;

  # 加上指定时间
  # Day('2021-10-02').add(1, 'year').add(2, 'month').add(10, 'day').format('YYYY-MM-DD') // '2022-12-12' 
  def add (self, num, unit):
    num = abs(num);

    if (unit == 'year'):
      self.time = self.time.shift(years = num)
    elif (unit == 'month'):
      self.time = self.time.shift(months = num)
    elif (unit == 'day'):
      self.time = self.time.shift(days = num)
    elif (unit == 'hour'):
      self.time = self.time.shift(hours = num)
    elif (unit == 'minute'):
      self.time = self.time.shift(minutes = num)
    elif (unit == 'second'):
      self.time = self.time.shift(seconds = num)
    elif (unit == 'week'):
      self.time = self.time.shift(weeks = num)
    elif (unit == 'weekday'):
      self.time = self.time.shift(weekdays = num)
    elif (unit == 'quarter'):
      self.time = self.time.shift(quarters = num)

    return self;

  # 减去指定时间
  # Day('2021-10-02').subtract(1, 'year').subtract(2, 'month').subtract(10, 'day').format('YYYY-MM-DD') // '2020-07-23'
  def subtract (self, num, unit):
    num = -abs(num);

    if (unit == 'year'):
      self.time = self.time.shift(years = num)
    elif (unit == 'month'):
      self.time = self.time.shift(months = num)
    elif (unit == 'day'):
      self.time = self.time.shift(days = num)
    elif (unit == 'hour'):
      self.time = self.time.shift(hours = num)
    elif (unit == 'minute'):
      self.time = self.time.shift(minutes = num)
    elif (unit == 'second'):
      self.time = self.time.shift(seconds = num)
    elif (unit == 'week'):
      self.time = self.time.shift(weeks = num)
    elif (unit == 'weekday'):
      self.time = self.time.shift(weekdays = num)
    elif (unit == 'quarter'):
      self.time = self.time.shift(quarters = num)

    return self;

  # 获取时间所在月份的天数
  def days_in_month (self):
    range = self.time.span('month');

    return Day(range[1]).day();

  # 设置时间到年的第一天
  def year_start (self):
    self.time = self.time.span('year')[0];

    return self;

  # 设置时间到年的最后一天
  def year_end (self):
    self.time = self.time.span('year')[1];

    return self;

  # 设置时间到月的第一天
  def month_start (self):
    self.time = self.time.span('month')[0];

    return self;

  # 设置时间到月的最后一天
  def month_end (self):
    self.time = self.time.span('month')[1];

    return self;

  # 设置时间到季的第一天
  def quarter_start (self):
    self.time = self.time.span('quarter')[0];

    return self;

  # 设置时间到季的最后一天
  def quarter_end (self):
    self.time = self.time.span('quarter')[1];

    return self;

  # 设置时间到周的第一天
  def week_start (self):
    self.time = self.time.span('week')[0];

    return self;

  # 设置时间到周的最后一天
  def week_end (self):
    self.time = self.time.span('week')[1];

    return self;

  # 设置时间到天的开始时间
  def day_start (self):
    self.time = self.time.span('day')[0];

    return self;

  # 设置时间到天的结束时间
  def day_end (self):
    self.time = self.time.span('day')[1];

    return self;

  # 设置时间到小时的开始时间
  def hour_start (self):
    self.time = self.time.span('hour')[0];

    return self;

  # 设置时间到小时的结束时间
  def hour_end (self):
    self.time = self.time.span('hour')[1];

    return self;
  
  # 设置时间到分钟的开始时间
  def minute_start (self):
    self.time = self.time.span('minute')[0];

    return self;

  # 设置时间到分钟的结束时间
  def minute_end (self):
    self.time = self.time.span('minute')[1];

    return self;

  # 判断当前时间是否在两个时间中间
  # 这两个时间可以不用按顺序传
  # Day().between('2021-05', '2022-02') // True
  # Day().between('2021-05', '2021-03') // False
  def between (self, a, b):
    if (type(a) != Day):
      a = Day(a);
    
    if (type(b) != Day):
      b = Day(b);
    
    if (a.valueOf() > a.valueOf()):
      return self.time.is_between(b.time, a.time)
    else:
      return self.time.is_between(a.time, b.time)

  # 对比时间相差
  # Day().diff('2020-10-01', 'second') // 36058422.200670004
  # Day().diff('2020-10-01', 'minute') // 600973.7033992648
  # Day().diff('2020-10-01', 'hour') // 10016.228390780556
  # Day().diff('2020-10-01', 'day') // 417.3428496558688
  # Day().diff('2020-10-01', 'week') // 59.620407102119835
  # Day().diff('2020-10-01', 'month') // 13
  # Day().diff('2020-10-01', 'quarter') // 1 
  # Day().diff('2020-10-01', 'year') // 1
  def diff (self, time, unit):
    if (type(time) != Day):
      time = Day(time);
    
    if (unit == 'second'):
      result = time.valueOf() - self.valueOf();
    elif (unit == 'minute'):
      result = (time.valueOf() - self.valueOf()) / 60;
    elif (unit == 'hour'):
      result = (time.valueOf() - self.valueOf()) / 60 / 60;
    elif (unit == 'day'):
      result = (time.valueOf() - self.valueOf()) / 60 / 60 / 24;
    elif (unit == 'week'):
      result = (time.valueOf() - self.valueOf()) / 60 / 60 / 24 / 7;
    elif (unit == 'month'):
      year = time.year() - self.year();
      result = time.month() - self.month() + year * 12;
    elif (unit == 'quarter'):
      year = time.year() - self.year();
      result = time.quarter() - self.quarter() + year * 4;
    elif (unit == 'year'):
      result = time.year() - self.year()

    return abs(result)
