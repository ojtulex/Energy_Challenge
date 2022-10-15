# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:58:49 2022

@author: Ploughman
"""
# Dual and Triple Energy challenge
# Import matplotlib.pyplot and matplotlib_venn library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_unweighted, venn2_circles, venn3
#%matplotlib inline
#v=venn2(subsets={'10':"more energy", '01':"less emission", '11':'Dual energy challenge'}, set_labels=("more energy","less emission"))
#plt.show()

#v=venn2(subsets={'10':1, '01':1, '11':1}, set_labels=("more energy","less emission"))
#v.get_patch_by_id('10').set_alpha(1.0)
#v.get_patch_by_id('10').set_color('red')
#v.get_label_by_id('10').set_text('More \n Energy')
#v.get_patch_by_id('01').set_alpha(1.0)
#v.get_patch_by_id('01').set_color('green')
#v.get_label_by_id('01').set_text('Less \n Emission')
#v.get_patch_by_id('11').set_alpha(0.3)
#v.get_patch_by_id('11').set_color('green')
#v.get_label_by_id('11').set_text('Dual \n Energy \n Challenge')
#plt.show()

v=venn3(subsets={'100':1, '010':1, '001':1, '110':1,'101':1,'011':1,'111':1 }, set_labels=("more energy","less emission", "sustainable"))
v.get_patch_by_id('100').set_alpha(1.0)
v.get_patch_by_id('100').set_color('red')
v.get_label_by_id('100').set_text('More \n Energy')
v.get_patch_by_id('010').set_alpha(1.0)
v.get_patch_by_id('010').set_color('green')
v.get_label_by_id('010').set_text('Less \n Emission')
v.get_patch_by_id('001').set_alpha(0.5)
v.get_patch_by_id('001').set_color('blue')
v.get_label_by_id('001').set_text('Sustainable')
v.get_patch_by_id('111').set_alpha(0.3)
v.get_patch_by_id('111').set_color('green')
v.get_label_by_id('111').set_text('Triple \n Energy \n Challenge')
v.get_label_by_id('110').set_text('x')
v.get_label_by_id('101').set_text('y')
v.get_label_by_id('011').set_text('z')
#v.get_label_by_id('A').set_text('Set "A"')
plt.show()