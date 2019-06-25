
# coding: utf-8

# In[ ]:


def add(a,b):
    return a+b

def wrongadd(a,b):
    return a-b

def test(fun):
    i = 1
    j = 1
    assert fun(i,j) == 2
    return 'pass!'

print(test(add))
print(test(wrongadd))

