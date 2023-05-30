


my_tuppy = (1,2,5,8)

my_tuppy[2] = 6


# In[ ]:


S = [['him', 'sell'], [90, 28, 43]]

print(S[0][1][1])


# In[ ]:


y = [(2, 4), (7, 8), (1, 5, 9)]
x=y[1][-1]
print(x)


# In[ ]:


import pandas as pd

df = pd.read_csv(
    "https://github.com/HamoyeHQ/HDSC-Introduction-to-Python-for-machine-learning",
    encoding="latin-1",
)

uni = df.area.unique()

print(uni)

