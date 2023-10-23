import time
from decimal import Decimal, getcontext

# Set the precision to a high value to handle large results
getcontext().prec = 5000

startTime = time.time()
product = Decimal(1)

for i in range(1, 100001):
    product *= Decimal(i)

endTime = time.time()

# print('Product is %s' % (product))
print('The result is %s digits long.' % (len(str(product))))
print('Took %s seconds to calculate.' % (endTime - startTime))
