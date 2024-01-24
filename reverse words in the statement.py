#!/usr/bin/env python
# coding: utf-8

# # Using loop

# In[7]:


s=input("Enter a statement : ")

def rev(r):
    return r[::-1] ## reverse function

word=""
new_s=""

for i in s:
    if i!=' ':
        word+=i
    else:
        new_s+=rev(word)+" "
        word=""
new_s+=rev(word)
print(new_s)


# # Using arrray

# In[46]:


def reverse_words():
    s=input("Give me a string : ")
    s1=[i for i in s.split(" ")]
    rev=lambda j:j[::-1]
    rev_l=[rev(j) for j in s1]
    return " ".join(rev_l)


# In[45]:


reverse_words()


# In[49]:


import raviraj as r


# In[50]:


r.reverse_words()


# In[ ]:




