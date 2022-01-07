def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k=="name"):
            print(f"당신의 이름은 :" +k)