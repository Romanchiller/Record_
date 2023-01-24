x = {}


f = open('1.txt','rt', encoding='utf-8')
result = f.readlines()
x[len(result)] = [f'{f.name}\n']
x[len(result)] += result
f.close()

f = open('2.txt','rt', encoding='utf-8')
result = f.readlines()
x[len(result)] = [f'{f.name}\n']
x[len(result)] += result
f.close()

f = open('3.txt','rt', encoding='utf-8')
result = f.readlines()
x[len(result)] = [f'{f.name}\n']
x[len(result)] += result
f.close()

sorted_dict = dict(sorted(x.items()))


with open('super.txt', 'a',encoding='utf-8') as s:
    for key, value in sorted_dict.items():
        s.write(value[0])
        s.write(f'{str(key)}\n')
        s.writelines(value[1:])
        s.write('\n')

