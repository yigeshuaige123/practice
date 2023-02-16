

lista = [20,40,30,50,10]
#lista.sort(lista)   # sort是对原序列直接排序，sorted是存储于新建的序列当中
listb = sorted(lista,reverse = True) # sorted() 排序函数 reverse 为倒序
print(f'lista is {lista}')
print(f'lista is {listb}')