#coding=utf-8
import  re
pattern=re.compile(r'\d+\.\d*')
result=pattern.findall("3.232424,4.234242,3424242,4234234.131")
for item in result:
    print(item)