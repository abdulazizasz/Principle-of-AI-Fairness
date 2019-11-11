"""

You need to download pyreadr to read rds files effeciently

"""

import pyreadr

result = pyreadr.read_r('C:\\Users\\balat\\Downloads\\WPy64-3741\\Datset_NJ.rds') # also works for RData

df = result[None]