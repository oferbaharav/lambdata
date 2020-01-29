import pandas as pd
import numpy as np

#giberish from Aaron Gallant

TEST_DF = pd.DataFrame([1,2,3])

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))


#check dataframe for nulls
def check_dataframe_na(df):
    result = df.isnull().any().any()
    return result


