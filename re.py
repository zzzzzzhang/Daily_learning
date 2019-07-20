# coding: utf-8
import re

dateOne = r'2019/06/06 08:00'
s1 = re.match(r'2.*9',dateOne) 
print(s1.span())
print(s1.group())
s2 = re.match(r'08:00',dateOne) 
print(s2)

dateOne = r'2019/06/06 08:00'
s1 = re.search(r'2.*9',dateOne) 
print(s1.span())
print(s1.group())
s2 = re.search(r'08:00',dateOne) 
print(s2.span())
print(s2.group())

dateOne = r'2019/06/06 08:00'
s = re.sub(r'/','-',dateOne)
print(s)

dateOne = r'2019/06/06 08:00'
s = re.sub(r'/','-',dateOne)
print(s)

def transform(matched):
    if matched.group() == ' 08:00':
        return '-00'
    elif matched.group() == ' 20:00':
        return '-12'
    else:
        return 'None'

s = re.sub(r' 08:00',transform,s)
print(s)

dateOne = r'2019/06/06 08:00'
pattern = re.compile(r'2019.*?6')
s1 = pattern.match(dateOne).group()
print(s1)
s2 = pattern.search(dateOne).group()
print(s2)
s3 = pattern.findall(dateOne)
print(s3)

dateOne = r'2019/06/06 08:00'
pattern = re.compile(r'(\d*)/(\d*)/(\d*) (\d*):(\d*)')
s1 = pattern.match(dateOne)
print(s1.group(0))
print(s1.group(1))
print(s1.group(2))
print(s1.group(3))
print(s1.group(4))
print(s1.group(5))

dateOne = r'2019/06/06 08:00'
pattern = re.compile(r'(?P<YYYY>\d*)/(?P<MM>\d*)/(?P<DD>\d*) (?P<hh>\d*):(?P<mm>\d*)')
s1 = pattern.match(dateOne)
print(s1.groupdict())

dateOne = r'2019/06/06 08:00'
s1 = re.match(r'(?P<YYYY>\d*)/(?P<MM>\d*)/(?P<DD>\d*) (?P<hh>\d*):(?P<mm>\d*)',dateOne)
print(s1.groupdict())