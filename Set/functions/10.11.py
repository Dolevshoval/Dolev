from random import randint
world= ['black', 'white']
display=""
name= world[randint(0,len(world)-1)]
for i in name:
    display+="_"
while name!=display:
    n=input(display)
    if n in name:
        display=display.replace(display[name.find(n)],n)
        n = input(display)


