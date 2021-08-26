# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:08:49 2021

@author: jbrownlow
make change for a dollar

"""

# Change4aDollar
#assignment in AVC CIS 177 python programming


#This assignment is to determine the total number of ways to make change for a dollar.  
#Write a Python program, produce the solution, make a pdf and put it in your Github account.
#Turn in the Github URL.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6.28, 50)
y = np.cos(x)

plt.figure(1) 
plt.plot(x,y, label='cos from 0 to 2$pi$')
plt.plot(x, np.sin(x), label='sin')


plt.title('Cosine')
plt.xlabel('radians')
plt.ylabel('value ')
plt.legend()
plt.grid()
