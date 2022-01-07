try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나누면 않되!!")
except IndexError:
    print("인덱싱 않되!!!")

# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# print("야호")

# try:
#     f=open('none','r')
# except FileNotFoundError as e:
#     print(str(e))
# else:
#     data=f.read()
#     print(data)
#     f.close()

# f=open('foo.txt','w')
# try:
#     #무언가 함
#     data=f.read()
#     print(data)
# except Exception as e:#exception은 모든에러 다 잡아줌
#     print(e)
# finally:
#     f.close()

