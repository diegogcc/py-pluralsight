f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write('What are the roots that clutch, ')
f.write('what branches grow \n')
f.close()

g = open('wasteland.txt', mode='rt', encoding='utf-8')
g.read(8)  # 'what are'
g.read()  # ' the roots that clutchwhat branches grow \nother things'
g.seek(0)  # Returns the reading point to the beginning
g.readline()  # 'what are the roots that clutchwhat branches grow \n'
g.seek(0)
g.readlines()  # ['what are the roots that clutchwhat branches grow \n', 'other things']
g.close()

h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['Son of man, \n',
    'for you know only, \n',
    'A heap of broken images.'])
h.close()