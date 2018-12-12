from xml.parsers.expat import ParserCreate
from urllib2 import urlopen
import urllib2
import subprocess
import sys
global result
def num2str(num):
    global numWord
    if numWord.get(num) != None:
        return numWord.get(num)
    else:
        s = ''
        if num < 0:
            s += 'minus '
            num = -num
        if num < 10:
			s += numWord.get(num%10)
	else:
			s += numWord.get(num-num%10)+' '+numWord.get(num%10)
        return s

def fetch_xmldata(url):
	
    req = urllib2.Request(url)
    #req.add_header('User-Agent',
    #               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
    #`1               Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36')
    f = urllib2.urlopen(req)
   # print('Status:', f.status)
    return f.read().decode()
    
def speak(sentence):
    cmd = 'echo '+sentence+' |festival --tts'
    print subprocess.check_output(cmd, shell=True)

class DefaultSaxHandler(object):
    def __init__(self):
        self.city = ''
        self.forecast = []

    def start_element(self, name, attrs):
        #print('sax:start_element: %s, atts: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.city = attrs['city']
        if name == 'yweather:forecast':
            self.forecast.append({'date':attrs['date'],
                                  'text':attrs['text'],
                                  'high':round((int(attrs['high']) - 32) / 1.8),
                                  'low' :round((int(attrs['low']) - 32) / 1.8)})

    def end_element(self, name):
        #print('sax:end_element: %s' % name)
        pass

    def char_data(self, text):
        #print('sax:char_data: %s' % text)
        pass

def handler_xmldata(xmldata):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xmldata)
    return {'city':handler.city, "forecast":handler.forecast}
'''
if __name__ == '__main__':
    global numWord
    numWord = {0:'zero',1: 'one',2: 'two', 3: 'three', 4: 'four', 5:'five', 6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
               11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
               19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    URL = r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather' \
          r'.forecast%20where%20woeid%20%3D%202427936&format=xml'
    xml = fetch_xmldata(URL)
    result= handler_xmldata(xml.encode('utf-8'))
    print(result['city'])
    city = result['city']
    print(result['forecast'][0]['text'])
    weather = result['forecast'][0]['text']
    ht = result['forecast'][0]['high']
    lt = result['forecast'][0]['low']
    print(result)
    speak('the location is '+city)
    speak('the weather today is '+weather+'in '+city)

    speak('the maximum temperature is '+ num2str(ht)+' degree Celsius '+'and the minimum temperature is '+
               num2str(lt)+' degree Celsius.')
    if(weather == 'Rain'):
       speak('Remember to bring your umbrella')

    if lt > 0 and lt < 7:
        speak('it is a little cold outside, remember to put on more clothes')
    elif lt >= 7 and ht <= 25:
        speak('it is a little cold outside, remember to put on more clothes')
'''
def getWeatherReport():
    URL = r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather' \
          r'.forecast%20where%20woeid%20%3D%202427936&format=xml'
    xml = fetch_xmldata(URL)
    global result
    result= handler_xmldata(xml.encode('utf-8'))
    return result
    
def outputAdvice():
    global result
    global numWord
    numWord = {0:'zero',1: 'one',2: 'two', 3: 'three', 4: 'four', 5:'five', 6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
               11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
               19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    city = result['city']
    weather = result['forecast'][0]['text']
    ht = result['forecast'][0]['high']
    lt = result['forecast'][0]['low']
    speak('the weather today is '+weather+'in '+city)

    speak('the maximum temperature is '+ num2str(ht)+' degree Celsius '+'and the minimum temperature is '+
               num2str(lt)+' degree Celsius.')
    if(weather == 'Rain'):
       speak('Remember to bring your umbrella')

    if lt > 0 and lt < 7:
        speak('it is a little cold outside, remember to put on more clothes')
    elif lt >= 7 and ht <= 25:
        speak('the weather today is good, have a nice day')
    elif lt <= 0:
		speak('it is very cold today, pay attention to keep warm')
		
#if __name__ == '__main__':
#	getWeatherReport()
#	print result
#	outputAdvice()
