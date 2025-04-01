def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))


# 이 파일을 
# 터미널에서 
# python mod1_2.py를 하면 __name__ == "__main__"이 참이 되어 if 문 다음 문장이 수행된다.

# 이와 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러 사용할 때는 __name__ == "__main__"이 거짓이 되어 if 문 다음 문장이 수행되지 않는다.