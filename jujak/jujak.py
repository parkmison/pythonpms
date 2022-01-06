proxy_list = ['1proxy', '2proxy', '3proxy']


def vote(proxy, gall, no):
    print(f"{proxy}를 통하여 {gall}의 {no}에 추천 하였습니다.")


gall = 'pridepc_new4'
no = '1234'

for proxy in proxy_list:
    vote(proxy, gall, no)