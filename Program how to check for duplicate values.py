#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=[1,2,3,4,1,2,3,4,4,4,44,4,4]
# x=['aaditya','crismon','brad','aaditya','c']
x.sort()
print(x)
length=len(x)
for i in range(1,length):
    try:
        no=x[i-1]
        prev=x[i]
        if no==prev:
            print("Common. The common datapoint is ",no,prev)
            x.remove(no)
            print("The new list is ", x)

        else:
            print("False")
    except:
        print(x)


# In[ ]:


#perfectioned

