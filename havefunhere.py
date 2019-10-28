
##### Questions comes from intenet resources #########


##start to use pycharm

#2019-09-06
#This is how to convert from string exppression to equation
#it is very simple just use eval() function and python will return numerical result

def eval_ (expressions):
	return eval(expressions)

print eval_ ('- (3 + ( 2 - 1 ) )')


###################################################################################################
###################################################################################################

#2019-09-08
#This is a question asked by Facebook to find out the lonest, 2 unique number sequence ina list

#####################################################################################################
n = [1, 3, 5, 3, 1, 3, 1, 3]




def findSequence(seq):
	y = []
	finallist = []

	for i in range (0, len(seq)):
		for m in range (i, len(seq)):
			y.append(seq[i:m])

	for value in y:
		length = len(set(value))
		if length <= 2:
			finallist.append(len(value))
		else:
			continue	
	return max(finallist)





# there are two ways to express string.
print "In this sequence, the longest sequence number is %d \n" %(findSequence (n))
print "In this sequence, the longest sequence number is {} \n".format(findSequence (n))






