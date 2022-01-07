import re
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))