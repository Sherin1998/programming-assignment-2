#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1
a=int(input("enter km"))
print(float(a  * 0.621))


# # 2
# x=int(input("enter temp in celcius"))
# c=((x*9)/5)+32
# print(float(c))
#     
# 

# In[20]:


# 3
import calendar
y=int(input("enter year"))
z=int(input("enter month"))
print(calendar.month(y,z))



# In[26]:


#4
import cmath 
a=int(input("enter coef(x2)"))
b=int(input("enter coef(x)"))
c=int(input("enter const"))
d=(b*b)-(4*a*c)
e= (-b + cmath.sqrt(d))/(2*a)
f=(-b - cmath.sqrt(d))/(2*a)
print("solutions are",e,",",f)


# In[27]:


#5
a=int(input("enter no1)"))
b=int(input("enter no2"))
print("before swap",a,",",b)
a,b=b,a
print("after swap",a,",",b)


# In[ ]:




