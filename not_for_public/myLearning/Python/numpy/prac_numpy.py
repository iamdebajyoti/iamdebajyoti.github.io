# %%
import numpy

# %%
a = numpy.array([1,2,3])
a
# %%
print(type(a))
print(a)
# %%
a.shape

# %%
b = numpy.array([[1],[2],[3]])
b
# %%
print(b)
print(type(b))
b.shape

# %%
c = numpy.array([["abh1", 1111],["jack", 2222],["pop",3333]])
type(c)

# %%
c
# %%
c.shape
# %%
print(c)

# %%

d = numpy.array([['abh1', 1111, 10],["jack", 2222, 20], ["pop",3333, 30], ["eric",4444, 40]])
d
# %%
d.shape
# %%
d[:, 2]
# %%
d[:, -1]
# %%
d[1:-1, 1]
# %%
d[1:3,1]
# %%
e = d[1:4,2]
e 
# %%
e.shape
# %%
e.mean()

# %%
e.max()

# %%
f = e.astype(int)

# %%
f.max()

# %%
f.mean()

# %%

f.min()
# %%
g = numpy.array([('abh1', 1111, 10),("jack", 2222, 20), ("pop",3333, 30), ("eric",4444, 40)], dtype = [('Name','U10'), ('Phone', 'i4'), ('age', 'i4')])
# %%
g.dtype
# %%
g['Name','age']
# %%
g[2, 'age']
# %%
