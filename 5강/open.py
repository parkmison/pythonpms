#f = open("C:/pythonpms/6강/새파일.txt",'w',encoding="UTF-8")
#for i in range(1, 11):
#    data=f"{i}번째 줄입니다.\n"
#    f.write(data)
#f.close

#f = open("C:/pythonpms/6강/새파일.txt",'r',encoding="UTF-8")
#while True:#While true 하면 무한반복
#    line=f.readline()
#    if not line: break#line이 없으면 빠져나감(진짜 무한반복하면 안되니까) = false로 인식하면
#    print(line)
#f. close

f = open("C:/pythonpms/6강/새파일.txt",'r',encoding="UTF-8")
lines = f.readlines()
for line in lines:
    print(line.strip("\n"))
f.close()

