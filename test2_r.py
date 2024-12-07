#문제2
#결과화면과 같이 나오도록 해당 소스 코드를 완성하시오. (주어진 소스 코드를 임의로 변경하지 말것)
#참조할 코드: append() bgcolor() color()  forward()  left() len() shape() if문  반복문

import turtle as t1  #거북이 모듈 불러오기 
##### 실습10-5 거북이객체프로그램.py 반드시 분석해 볼 것 #####
t= t1.Turtle() #: 거북이 이동, 모양,원 그리기     shape()
s= t1.Screen()#: 윈도 환경 설정     bgcolor()
shape = ['circle', 'triangle', 'square', 'turtle', 'classic','circle'] # 거북이 모양 선택
#1. shape 리스트에서 글자수가 7개 이상인 모양('triangle','classic')을 모두 출력하시오.
#반드시 for문과 end=' '를 사용해서 수행할 것
# triangle classic  

# for 변수명 in _______:   range(end)  range(6) i=0 1 2 3 4 5  자료형 
# range(start,end,step) range(end)=range(0,end,1) start=0 step=1
for i in range(len(shape)): #i=0 1 2 3 4 5  ~ len(shape)-1  
    if len(shape[i])>=7: print(shape[i], end=' ')
for i in shape: #range() 자료형   변수 i='circle'
    if len(i)>=7: print(i,end=' ') #len('circle')=6  len('triangle')=7 

#2. shape()를 이용해 거북이 모양을 'turtle'로 지정하시오.
t.shape(shape[3])

#거북이 색상 선택
color = ['red', 'orange', 'pink', 'yellow','green'] # 리스트:중복허용,순서o, 인덱스(번지)
color_tuple = {'red', 'orange', 'pink', 'yellow'} # 튜플:중복허용,순서o => 읽기모드(자물쇠), 인덱스(번지)
color_set = {'red', 'orange', 'pink', 'yellow'} # 집합:중복불가,순서x
color_dict = {'red':2, 'orange':3, 'pink':1, 'yellow':4} # 딕셔너리: 인덱스(키):값
#3. color 리스트의 마지막 인덱스에 요소값 'green'를 추가하시오.
color.append('green')

#4. color 리스트를 이용해 거북이 선(이동) 색깔과  자체 색상을 각각 red, green로 지정하시오.
t.color(color[0],color[4])

#5. color 리스트를 이용해 스크린의 배경색을 오렌지색으로 지정하시오.
s.bgcolor(color[1])

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
# 실제 시험 문제에서는 360도 원을 그리는 문제만 출제할 예정
# 반지름은 30~100까지 10씩 증가
for i in range(3, 11): #range  circle(반지름,) i=30 40 50 60 70 80 90 100
    # 반지름을 i*10으로, 각도를 360도로, 단계수를 i로 설정하여 원 그리기
    t.circle(i*10)  #t.circle(i*10)
for i in range(30, 110, 10): #range  circle(반지름,) i=30 40 50 60 70 80 90 100
    # 반지름을 i*10으로, 각도를 360도로, 단계수를 i로 설정하여 원 그리기
    t.circle(i)  #t.circle(i)
input()  # 일시정지를 위해 사용