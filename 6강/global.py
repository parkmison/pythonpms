a=1
def vartest():
    global a#a를 전체에 영향 
    a=a+1
vartest()
print(a)