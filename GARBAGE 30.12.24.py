import sys
a=[1,2,3]
ref_count=sys.getrefcount(a)

print("reference Count: ",ref_count)

#
import sys
a=[]
b=a
c=b
print("referencecount is: ",sys.getrefcount(a))
#
import gc
collected=gc.collect()
print("garbage collected is:", collected)
#
import gc
gc.enable()
gc.disable()
l1=[1,2,3]
d1={'a':1,'b':2}
s1='garbage collection'
del l1
del d1
del s1
gc.set_threshold(1,2,2)
print('Current threshold is',gc.get_threshold())
collected=gc.collect()
print("garbage collection: ",collected)
