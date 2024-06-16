
#todo 1: pass complete names of four
#todo 2: delete names longer than four
#todo 3: create names of four from individual characters
#todo 4: check for uniqueness and remove duplicates
def friend(x):

    real_friends = []
    for name in x:
        if len(name) == 4:
            real_friends += name
        else:
            newName = ''
            while len(newName) < 4:
                for name in x:
                    newName += name
            real_friends += newName
    return(real_friends)


    # added note alright
    # and another
