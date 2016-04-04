# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 11:45:04 2016

@author: YI
"""
#the usage of defaultdict
from collections import defaultdict

colors = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colors = defaultdict(list)

for name, color in colors:
    favourite_colors[name].append(color)

print favourite_colors

#add a key in the key
tree = lambda: defaultdict(tree)
a_dict = tree()
a_dict['colors']['favourite'] = 'yellow'

import json
print json.dumps(a_dict)
## output: {"colours": {"favourite": "yellow"}}

#the usage of Counter
from collections import Counter
result = Counter(name for name, color in colors)

print result

#the usage of deque
from collections import deque

#deque is like the list, you can remove/add elements 
#from the begining and the end
d = deque()
d.append(7)  

d = deque(range(5))
d.popleft() 

#the usage of namedtuple
from collections import namedtuple
man = namedtuple('human', 'name age job')
Yi = human(name='Yi', age=28, job='Graduate Student')

print Yi
print Yi.age
print Yi._asdict() #convert to dict
