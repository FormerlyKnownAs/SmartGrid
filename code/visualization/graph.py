import matplotlib.pyplot as plt 
import numpy as np 

totalPrice = [[0, 4378],[1, 7845], [2, 7438], [3, 9854], [4, 7611], [5, 5673], [6, 4133], [7, 9841], [8, 6739], [9, 4020], [10, 6743], [11, 8932], [12, 5722]]
lowestPrice = [[0, 4378], [1, 4378], [2, 4378], [3, 4378], [4, 4378], [5, 4378], [6, 4133], [7, 4133], [8, 4133], [9, 4020], [10, 4020], [11, 4020], [12, 4020]]

plt.title("RandomV?")
plt.axis([0, 15, 0, 10000])

totalArray = np.array(totalPrice)
lowestArray = np.array(lowestPrice)

plt.plot(*totalArray.T, 'r-')
plt.plot(*lowestArray.T, 'b:')

plt.show()