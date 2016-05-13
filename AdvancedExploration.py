# -*- coding: utf-8 -*-
"""
Created on Fri May 13 08:45:23 2016

@author: ouj070
"""

import seaborn as sns
import matplotlib.pyplot as plt
from pylab import xticks


sns.regplot(data = movie_final, y = 'domestic_gross', x = 'widest_release')

sns.regplot(data = movie_final, y = 'domestic_gross', x = 'Season')

sns.regplot(data = movie_final, y = 'domestic_gross', x = 'Scoregroup')

sns.boxplot(data = movie_final, y = 'domestic_gross', x = 'Scoregroup', hue = 'Season')

sns.boxplot(data = movie_final, y = 'domestic_gross', x = 'Season')




