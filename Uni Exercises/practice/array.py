import array
import timeit
list=range(1000000)

t = timeit.Timer(""list+1"")
print t.timeit(1)
