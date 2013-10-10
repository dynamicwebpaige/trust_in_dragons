#! /usr/bin/python

f = open('emailquery.txt', 'r')
array = []
for line in f:
	array.append(line)
	print line[0]

f.close()

#data = f.read()
#print data

#for line in data:
#	head, sep, tail = data.partition(',')
#	print head
#	print tail
