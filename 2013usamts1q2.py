numbers_left = [0, 9, 0, 1, 2, 3, 4, 5,
                6, 7, 8, 9, 0, 1, 2, 3,
                4, 5, 6, 7, 8, 9]

one = [0,1,2,3,4,5]
two = [0,1,2,3,4,5,6,7]
three = [0,1,2,3]
four = [0,1,2]
five = [0,1,2,3,4]
six = [0,1]
seven = [0,1,2,3,4,5,6]

import itertools
from time import time
from copy import copy

def condition_two(problem):
    #print('c2')
    condition_two = True
    for row in xrange(1,5):
        for column in xrange(0,6):
                if problem[row][column] > problem[row][column-1]:
                    condition_two = False
    return condition_two

def condition_three(problem):
    #print('c3')
    condition_three = True
    for row in xrange(0,4):
        for column in xrange(0,5):
            if ((problem[row][column]+
                 problem[row+1][column]+
                 problem[row][column+1]+
                 problem[row+1][column+1]) % 3) == 0:
                condition_three = False
    return condition_three

def solution(problem):
    position_in_case = 0
    for row in xrange(0,5):
        for column in xrange(0,6):
            if problem[row][column] == None:
                problem[row][column] = case[position_in_case]
                position_in_case += 1
            elif problem[row][column] in [0,1,2,3,4,5,6,7,8,9]:
                pass
            elif case[position_in_case] not in problem[row][column]:
                return False

t = time()
#<-----------------Start Program------------------------>
for case in itertools.permutations(numbers_left,22):
    problem = [
           [one, two, four, five, 7, seven],
           [one, 8, four, five, six, 6],
           [one, three, 2, 4, six, seven],
           [5, three, four, five, 1, seven],
           [one, 3, four, five, six, seven]]
    if solution(problem):
        if (condition_two(problem) and condition_three(problem)) is not True:
            pass
        else:
            print('Test pass!')
            print(problem)
            break
print(time()-t)
