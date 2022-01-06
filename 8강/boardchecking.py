
def getTotalPage(m,n):#m=게시글수, n=한 페이지당 보여 줄 게시글의 수
    if(m%n)==0: #한 페이지마다 글을 10개 보여줄건데, 글이 10개라면 1페이지임. 
        return m//n 
    else:
        return m//n + 1
print(getTotalPage(30,10)) 