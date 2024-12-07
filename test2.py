#문제2
#결과화면과 같이 나오도록 해당 소스 코드를 완성하시오. (주어진 소스 코드를 임의로 변경하지 말것)
#참조할 코드: append() bgcolor() color()  forward()  left() len() shape() if문  반복문

import turtle as t #거북이 모듈 불러오기 
shape = ['circle', 'triangle', 'square', 'turtle', 'classic','circle'] # 거북이 모양 선택
#1. shape 리스트에서 글자수가 7개 이상인 모양('triangle','classic')을 모두 출력하시오.
#반드시 for문과 end=' '를 사용해서 수행할 것
# triangle classic 


#2. shape 리스트를 이용해 거북이 모양을 'turtle'로 지정하시오.


#거북이 색상 선택
color = ['red', 'orange', 'pink', 'yellow','green'] # 리스트:중복허용,순서o, 인덱스(번지)
color_tuple = {'red', 'orange', 'pink', 'yellow'} # 튜플:중복허용,순서o => 읽기모드(자물쇠), 인덱스(번지)
color_set = {'red', 'orange', 'pink', 'yellow'} # 집합:중복불가,순서x
color_dict = {'red':2, 'orange':3, 'pink':1, 'yellow':4} # 딕셔너리: 인덱스(키):값
#3. color 리스트의 마지막 인덱스에 요소값 'green'를 추가하시오.


#4. color 리스트를 이용해 거북이 선(이동) 색깔과  자체 색상을 각각 red, green로 지정하시오.


#5. color 리스트를 이용해 스크린의 배경색을 오렌지색으로 지정하시오.


#6. 거북이를 왼쪽으로 90도 회전 후 앞으로 100만큼 이동하는 코드를 완성하시오. 
#  (수행횟수: 3번, 반드시 while문을 사용해서 수행할 것)
t.forward(100)  #거북이를 앞으로 100 만큼 이동
i=0 #임의로 i값을 변경하지 말 것
while i<3:
    t.left(90)
    t.forward(100)
    i=i+1
    
t.forward(100)  #거북이를 앞으로 100 만큼 이동
#7. 거북이를 이용해 단계별(3단계=>10단계)로 원(360도)을 생성하는 코드를 완성하시오. 
# 반지름은 30~100까지 10씩 증가




input()  # 일시정지를 위해 사용