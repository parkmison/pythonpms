#DOTALL, S
import re
# p = re.compile('[a-z]+')
# m = p.match('python')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())
p=re.compile('a.b', re.DOTALL)
m=p.match('a\nb')
print(m)

