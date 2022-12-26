
import numpy

recipient = numpy.array(["James","David","Steve","Susan","Michael"])
buyer = numpy.array(["James","David","Steve","Susan","Michael"])
numpy.random.shuffle(buyer)

print(buyer[:]," buys for ",recipient[:])
