import re
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall('''
autoexec.exe
autoexec.bat
autoexec.jpg
''')
print(l)