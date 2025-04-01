# 이번에는 문서 파일을 읽어서 그 문서 파일 안에 있는 탭 문자(Tab)를 공백 문자(Space) 4개로 바꾸어 주는 스크립트를 작성해 보자.

# 필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
# 입력받는 값은? 탭을 포함한 문서 파일
# 출력하는 값은? 탭이 공백으로 수정된 문서 파일
# 다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.

# python tabto4.py src dst
# tabto4.py는 우리가 작성해야 할 파이썬 프로그램 이름, src는 탭을 포함하고 있는 원본 파일 이름, dst는 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 파일 이름이다.

# 예를 들어 a.txt에 있는 탭을 4개의 공백으로 바꾸어 b.txt에 저장하고 싶다면 다음과 같이 수행해야 한다.

# python tabto4.py a.txt b.txt

import sys
o_f_n=sys.argv[1]
f_n=sys.argv[2]

f=open(o_f_n,'r')
data=f.read()
f.close()

new_data=data.replace('\t',' '*4)
x=open(f_n,'w')
x.write(new_data)
x.close()
