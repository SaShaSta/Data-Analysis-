# -*- coding: utf-8 -*-
"""04 Numpy Exercises.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rYHbeluJ1hGWnba2sqKpiA2_X6fwvzP7

# NumPy Exercises

Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

#### Import NumPy as np
"""

import numpy as np

"""#### Create an array of 10 zeros"""

import numpy as np
np.zeros(10)

"""#### Create an array of 10 ones"""

import numpy as np
np.ones(10)

"""#### Create an array of 10 fives"""

import numpy as np
np.ones(10)*5

"""#### Create an array of the integers from 10 to 50"""

import numpy as np
np.arange(10,51)

"""#### Create an array of all the even integers from 10 to 50"""

import numpy as np
np.arange(10,51,2)

"""#### Create a 3x3 matrix with values ranging from 0 to 8"""

import numpy as np
np.arange(0,9).reshape(3,3)

"""#### Create a 3x3 identity matrix"""

import numpy as np
np.eye(3)

"""#### Use NumPy to generate a random number between 0 and 1"""

import numpy as np
np.random.rand(1)

"""#### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

we mentioned that the numpy.random.randn() generates samples from the **standard normal distribution**, which means it generates random numbers with a  **mean of 0 and a standard deviation of 1.**

The range of values returned by numpy.random.randn() is theoretically unbounded, but in practice, most of the generated values will be within a few standard deviations of the mean. Specifically, approximately **99.7%** of the generated values will fall within t**hree standard deviations of the mean.** (which corresponds to the range from **-3 to 3**.)
"""

import numpy as np
np.random.randn(25)

"""#### generate 20 random numbers following a normal distribution and ensure that they fall within the range of -2 to 2.

---


"""

import numpy as np
np.random.randn(20)*4+2

"""Create the following matrix (as shown below).



```
[[0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1 ]
 [0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2 ]
 [0.21 0.22 0.23 0.24 0.25 0.26 0.27 0.28 0.29 0.3 ]
 [0.31 0.32 0.33 0.34 0.35 0.36 0.37 0.38 0.39 0.4 ]
 [0.41 0.42 0.43 0.44 0.45 0.46 0.47 0.48 0.49 0.5 ]
 [0.51 0.52 0.53 0.54 0.55 0.56 0.57 0.58 0.59 0.6 ]
 [0.61 0.62 0.63 0.64 0.65 0.66 0.67 0.68 0.69 0.7 ]
 [0.71 0.72 0.73 0.74 0.75 0.76 0.77 0.78 0.79 0.8 ]
 [0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89 0.9 ]
 [0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98 0.99 1.  ]]

[[ 0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1. ]
 [ 1.1  1.2  1.3  1.4  1.5  1.6  1.7  1.8  1.9  2. ]
 [ 2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9  3. ]
 [ 3.1  3.2  3.3  3.4  3.5  3.6  3.7  3.8  3.9  4. ]
 [ 4.1  4.2  4.3  4.4  4.5  4.6  4.7  4.8  4.9  5. ]
 [ 5.1  5.2  5.3  5.4  5.5  5.6  5.7  5.8  5.9  6. ]
 [ 6.1  6.2  6.3  6.4  6.5  6.6  6.7  6.8  6.9  7. ]
 [ 7.1  7.2  7.3  7.4  7.5  7.6  7.7  7.8  7.9  8. ]
 [ 8.1  8.2  8.3  8.4  8.5  8.6  8.7  8.8  8.9  9. ]
 [ 9.1  9.2  9.3  9.4  9.5  9.6  9.7  9.8  9.9 10. ]]

[[  1   2   3   4   5   6   7   8   9  10]
 [ 11  12  13  14  15  16  17  18  19  20]
 [ 21  22  23  24  25  26  27  28  29  30]
 [ 31  32  33  34  35  36  37  38  39  40]
 [ 41  42  43  44  45  46  47  48  49  50]
 [ 51  52  53  54  55  56  57  58  59  60]
 [ 61  62  63  64  65  66  67  68  69  70]
 [ 71  72  73  74  75  76  77  78  79  80]
 [ 81  82  83  84  85  86  87  88  89  90]
 [ 91  92  93  94  95  96  97  98  99 100]]

```









"""

import numpy as np
np.arange(1,101).reshape(10,10)/100

"""#### Create an array of 20 linearly spaced points between 0 and 1:"""

import numpy as np
np.linspace(0,1,20)

"""## Numpy Indexing and Selection

Now you will be given a few matrices, and be asked to replicate the resulting matrix **outputs**:
"""

import numpy as np
mat = np.arange(1,26).reshape(5,5)
mat

# show all rows with the first and second row, and all columns without the first column
import numpy as np
mat = np.arange(1,26).reshape(5,5)
mat[1:3,1:]

# Show "20" element in the matrix
import numpy as np
mat = np.arange(1,26).reshape(5,5)
mat[3,4]

# show the second column for the top 3 rows
import numpy as np
mat = np.arange(1,26).reshape(5,5)
mat[:3,1]

# show the fifth row
import numpy as np
mat = np.arange(1,26).reshape(5,5)
mat[4]

# show all rows after the thrid row
import numpy as np
mat = np.arange(1,26).reshape(5,5)
mat[3:]

"""### Now do the following

#### Get the sum of all the values in mat
"""

import numpy as np
mat = np.arange(1,26).reshape(5,5)
np.sum(mat)

"""Get the standard deviation of the values in 'mat' (you can check what the standard deviation is, here: https://byjus.com/maths/standard-deviation/, and we will talk about these concepts in more detail)."""

import numpy as np
mat = np.arange(1,26).reshape(5,5)
np.std(mat)

"""#### Get the sum of all the columns in mat"""

import numpy as np
mat = np.arange(1,26).reshape(5,5)
np.sum(mat,axis=0)

"""# Great Job!"""