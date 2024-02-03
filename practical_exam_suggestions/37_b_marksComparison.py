from matplotlib import pyplot as plt
import numpy as np

s1 = np.random.randint(7,10, size = 6)
s2 = np.random.randint(7,10, size = 6)
x = ['Bengali', 'English', 'Math','Physics','Chemisry','Computer']

plt.plot(x,s1, color = 'red', linewidth = 1.5, linestyle='dotted')
plt.plot(x,s2, color = 'green', linewidth = 1.5)
plt.title("Student Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()



'''
np->Package : Class, Variables
    random->Class: Methods, Variables, Contructors
        randint-> Method

matplotlib->Package
    Pyplot->Class 
        plot-> Method : It plots the graph 
        title->Method : It will provide a title for the graph
        xlabel->Method : It will provide the label for x axis
        ylabel->Method
        show->Method : It will display the plotted graph on the screen
'''
