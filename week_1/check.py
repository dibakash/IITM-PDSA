import modules
from performance import Performance

a = Performance()

a.start()
for i in range(100000):
    ...
a.stop()
print(a.performance)
