#Josh Yurche
#Find the weather forecast for your city
import re
import urllib.request

city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

#print("url is : " + url)

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")

#print("test1")

m = re.search('<span class="phrase">', data1)

start = m.end()
end = start + 300
newString = data1[start:end]

#print("test2")

#print(newString)

m = re.search('</span></span>',newString)
end = m.start()-1
newString1 = newString[0:end]

print(newString1)
