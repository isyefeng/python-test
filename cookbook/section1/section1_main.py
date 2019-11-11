'''cookbook section test'''

def drop_first_last(arrays):
    first,*middle,last=arrays
    return middle

''' *号可以存放不确定数量的变量 '''
y=drop_first_last(['jhjs','adga','sdg','asdfg','dfasdf'])
print(y)

arrayss = [
    ('one',1,2),
    ('two','hellow'),
    ('therr',3,4)
]

for first,*last in arrayss:
    print(last)

