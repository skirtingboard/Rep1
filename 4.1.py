
#сколько определенная буква повторяется в тексте
'''def strcounter(s): #O(M*N)
    for sym in set(s):
        counter = 0
        for sub_sum in s:
            if sym == sub_sum:
                counter+=1 
        print(sym, counter)

strcounter(input('Введите текст: '))'''

def strcounter(s): # O ( N )
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)

strcounter('aabbbccd')