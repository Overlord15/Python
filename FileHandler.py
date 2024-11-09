import os
with open ('number.txt','a+') as file:
	for number in range (1,1000001):
		file.write(str(number) + '\n')