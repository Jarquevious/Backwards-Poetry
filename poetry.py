import random as random  

poem ='''Hold fast to dreams
For if dreams die
Life is a broken-winged bird
That cannot fly.
Hold fast to dreams
For when dreams go
Life is a barren field
Frozen with snow.'''
poems = poem.split("\n")   

#TODO: get a list of strings that contains lines of poem

def lines_printed_backwards(poems):
    ''' This function takes in a list of 
    strings containing the lines of 
    your poem as arguments and 
    will print the poem 
    lines out in reverse 
    with the line numbers reversed.'''
    index = len(poems)
    poems.reverse()

    for i in poems:
        print(f'{str(index)} {i}')
        index -= 1
    
    
    
    


def lines_printed_random(poem_lines_list):
    ''' Your code should implement the lines_printed_random() 
    function which will randomly select lines from a list of 
    strings and print them out in random order. Repeats are 
    okay and the number of lines printed should be equal 
    to the original number of lines in the poem 
    (line numbers don't need to be printed). 
    Hint: try using a loop and randint()  '''
    for i in poems:
        lines_random = random.randint(0, (len(poems)-1)) 
        print(poems[lines_random])

    

    
 
def my_own_rearrange():
    '''
    This function will print 3 random lines
    followed by 'hold fast to dreams' three 
    times on three different lines
    '''
    for poem in poems:
        print(poem[::-1])
    


#TODO: get a list of strings that contains lines of poem
#Use lines = poem.split("\n")
 
 
#Testing code
lines_printed_backwards(poems)
lines_printed_random(poems)
my_own_rearrange()
