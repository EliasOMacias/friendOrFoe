
#todo 1: change all inputs to one list
#todo 2: pass names len = 4 to new list to be returned
#todo 3: test
def friend(*x):

    joinedList = []
    for list in x:
        joinedList.extend(list)
    print(joinedList)


friend(['mark','david','john','jim'], ['steve','bob'])
    # added note alright
    # and another
