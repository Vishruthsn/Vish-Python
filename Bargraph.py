import matplotlib.pyplot as plt 
left=[1,2,3,4,5]
height=[10,33,45,22,18]
tic_label = ['One','Two','Three','Four','Five']
plt.bar(left,height,tick_label=tick_label,width=0.8,colour=['red','green'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

