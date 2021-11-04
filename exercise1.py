try:
    fhand = open("mailbox.txt")
except:
    print('File cannot be opened')
    exit()


lines=fhand.readlines()
Sultan=[]
file=open('output.txt', 'w')
for line in lines:
       if 'ESMTP' in line:
           ind=line.find('ESMTP id ')
           en_ind=line.find(';')
           word=line[ind+9:en_ind]
           if word not in Sultan:
                   Sultan.append(word)
           Sultan.sort()
for word in Sultan:
       print(word)
       file.write(word)
       file.write('\n')
fhand.close()
