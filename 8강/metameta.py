#메타문자
import re
# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)

#메타문자 ^. 맨처음
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life','My Life'))

#메타문자 %. 맨끝
print(re.search('short$', 'Life is too short'))
print(re.search('short$','Life is too short, you need python'))

#메타문자 \b 공백 
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))
# print(p.search('one subclass is'))

#그루핑 ()
p=re.compile('(ABC)+')
m=p.search('ABCABCABC OK?')
print(m)
print(m.group())