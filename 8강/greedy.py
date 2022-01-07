import re
s='<html><head><title>Title</title>'
print(re.match('<.*>',s).group()) #greedy
print(re.match('<.*?>',s).group()) #non-greedy