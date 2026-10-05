import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate 10 random integers from 1 to 100
data = np.random.randint(1, 101, 10)

# Create Pandas Series
s = pd.Series(data)

# Print result
print(s)
```[cite: 9, 10]