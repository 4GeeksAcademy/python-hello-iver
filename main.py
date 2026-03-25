import random

who = ['the dog ','my granma ','his turtle ','my bird ']
what = ['eat ','pissed ','crushed ','broked ']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']

def generate_excuse():
    excuse = "" 
    who_random = random.choice(who)
    excuse += who_random 
    what_random = random.choice(what)
    excuse += what_random  
    when_random = random.choice(when)
    excuse += when_random 
    print(excuse)

generate_excuse() 