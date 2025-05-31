def maior(*i):
    i = sorted(i)
    print(f'O maior numero e {i[-1]} o menor e {i[0]}')


maior(0,6,3,1,34,-35)
maior(0,5)
maior()