import sys
# %s 10자리수를 맞춰서 출력 

print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

#왼쪽부터 시작

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

# 앞에 채워넣을 수 있다

print('{:_>10}'.format('nice'))

#중앙정렬

print('{:^10}'.format('nice'))

# $.은 몇 글자 이상이면 짤라버린다 (공간은 5개만 있다)
print('%5s' % ('nice'))
print('%.5s' % ('python study'))


#10개를 갖고 있으나 5개만 가져와라
print('{:10.5}' .format('python study'))

# %d 정수 출력

print('%d,%d' % (1,2))
print('{},{}' .format(1,2))

print('')