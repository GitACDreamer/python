'xml的解析'

from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax: start_element: %s , attr: %s' % (name, attrs))

    def end_element(self, name):
        print('sax: end_element: %s' % name)

    def char_data(self, text):
        print('sax: char_data: %s' % text)


class WeatherSaxHandler(object):
    def __init__(self):
        self.weather = {}
        self.nowdate = {}

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
            self.weather['country'] = attrs['country']
        if name == 'yweather:condition':
            self.nowdate = int(attrs['date'][5:7])
        if name == 'yweather:forecast':
            if self.nowdate == int(attrs['date'][:2]):  # today
                self.weather['today'] = {}
                self.weather['today']['text'] = attrs['text']
                self.weather['today']['low'] = attrs['low']
                self.weather['today']['high'] = attrs['high']
            elif (self.nowdate + 1) == int(attrs['date'][:2]):
                self.weather['tomorrow'] = {}
                self.weather['tomorrow']['text'] = attrs['text']
                self.weather['tomorrow']['low'] = attrs['low']
                self.weather['tomorrow']['high'] = attrs['high']

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
weatherData = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''


def testXmlParse():
    hander = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = hander.start_element
    parser.EndElementHandler = hander.end_element
    parser.CharacterDataHandler = hander.char_data
    parser.Parse(xml)


def parse_weather(xml):
    hander = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = hander.start_element
    parser.EndElementHandler = hander.end_element
    parser.CharacterDataHandler = hander.char_data
    parser.Parse(xml)
    return hander.weather


if __name__ == '__main__':
    testXmlParse()
    weather = parse_weather(weatherData)

    print('Weather', str(weather))
