import pandas as pd
import requests

with open('Vello vs. AaronCatalan - HSReplay.net', 'r') as f:
    html = f.read()


g = 0
z = 0
s = 0
c = 0 
b = 0
p = 0
h = 0
new_row = [0,0,0,0,0,0,0,0,0]


 
d = {'Golden': [0],'Grumbled': [0], 'Grumble': [0], 'Zola': [0],'Saronite': [0],
      'Primordial': [0], 'Hagatha': [0],'Card': [0] , 'Board': [0]}
data = pd.DataFrame(data = d)
data.head()
    
while True:
    comand = 'default'
    comand = input ("Who walks on pox'd rocks where stalks the Shudderwock")
    
    if ('add' in comand) or ('ADD' in comand):
        v = int(comand.replace(['ADD','add',' '],'')
        golden = v%10
        new_row.insert(1, golden)
        grumbled = (v - golden)/10
        new_row.insert(0, grumbled)
        new_row.insert(2, g)
        new_row.insert(3, z)
        new_row.insert(4, s)
        new_row.insert(5, c)
        new_row.insert(6, b)
        new_row.insert(7, p)
        new_row.insert(8, h)
        data = data.append(new_row)
    elif ('g' in comand) or ('G' in comand):
        g = int(comand.replace(['G','g',' '],'')
    elif ('z' in comand) or ('Z' in comand):
        z = int(comand.replace(['Z','z',' '],'')
    elif ('s' in comand) or ('S' in comand):
        s = int(comand.replace(['S','s',' '],'')
    elif ('c' in comand) or ('C' in comand):
        c = int(comand.replace(['C','c',' '],'')
    elif ('b' in comand) or ('B' in comand):
        b = int(comand.replace(['B','b',' '],'')
    else:
        print ("Type a valid comand")