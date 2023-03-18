from __future__ import division;
import math;

print(5.0/2)
print('I am a full stack developer');
print(12.0/4.0);
print(10.0//2);
print(1.0//2.0);
print(math.sqrt(9));

##const PI
print(math.pi);
print(math.factorial(5));
print(math.sqrt(100));
print(math.ceil(-78.89));
print(math.asinh(89));
print(math.floor(78.90));

##Datatype conversion
s_1='3';
print(int(s_1));
f_1=3.14;
print(int(f_1));

##Data Type conversion
a='15';
b='10';

'''Build in function'''
##File input/output
##create file
f_w=open('p1.txt','w');
f_w.write("I am a full stack software Engineer\n");
print(f_w);

##append
f_a=open('./p1.txt','a');
f_a.write(".I have append that I am a programmer");
print(f_a);
##read
f_rd=open('./p1.txt','r');
print(f_rd.read);
print(f_w.tell())

##ReadLine Method
read_line=f_w.readline();
print(read_line);

for line in f_w:
    print(line);
f_w.close();

##Print function

##Input Function






