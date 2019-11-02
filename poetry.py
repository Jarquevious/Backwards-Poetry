import random 

poem ='''
Hold fast to dreams
For if dreams die
Life is a broken-winged bird
That cannot fly.

Hold fast to dreams
For when dreams go
Life is a barren field
Frozen with snow.
'''
poems = poem.split("\n")   

#TODO: get a list of strings that contains lines of poem

def lines_printed_backwards(poem_lines_list):
    ''' This function takes in a list of 
    strings containing the lines of 
    your poem as arguments and 
    will print the poem 
    lines out in reverse 
    with the line numbers reversed.'''
    for i in poem_lines_list:
        print(i[::-1])
    
    
    


def lines_printed_random(poem_lines_list):
    ''' Your code should implement the lines_printed_random() 
    function which will randomly select lines from a list of 
    strings and print them out in random order. Repeats are 
    okay and the number of lines printed should be equal 
    to the original number of lines in the poem 
    (line numbers don't need to be printed). 
    Hint: try using a loop and randint()  '''
    for i in poem_lines_list:
        print(random.choice(poems))

    
 
def my_own_rearrange():
    '''
    This function will print 3 random lines
    followed by 'hold fast to dreams' three 
    times on three different lines
    '''
# poemss = random.choice(random.randrange(poems))



x=0
while x <= 3:
    for i in poems:
        print(i)
        print('Hold fast to dreams')
    x += 3   
    print('Hold fast to dream')

#TODO: get a list of strings that contains lines of poem
#Use lines = poem.split("\n")
 
 
#Testing code
lines_printed_backwards(poems)
lines_printed_random(poems)
my_own_rearrange()
