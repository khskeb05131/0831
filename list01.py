#리스트를 만들기 위해서는 대괄호를 사용한다
#괄호, 중괄호, 대괄호
#len() 함수를 통해 리스트 내 원로의 수를 센다.
#max() 함수와 min() 함수는 최대/최소 값을 찾는다
#count() 함수는 리스트 내 특정 값이 등장한 횟수를 센다.
a_list = [1,2,3]
print(a_list)
print("a_list has {} elements.".format(len(a_list)))
print("the maximum value in a_list is {}.".format(max(a_list)))
print("the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer',5,['star','circle',9]]
print(another_list)
print("another_list also has {} elements.".format(len(another_list)))
print("5 is in another_list {} time.".format(another_list.count(5)))
print(a_list[0])
print(a_list[1])
print(a_list[2])
print(a_list[-1])
print(a_list[-2])
print(a_list[0:2])

list_lotto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]