import unittest
import pandas as pd
from df_utils import check_dataframe_na


class TestDfUtils(unittest.TestCase):
    def test_check_dataframe_na(self):
        df = pd.DataFrame({'a': [0,1,2], 'b': [1,1,1]})
        self.assertFalse(check_dataframe_na(df))

        df = pd.DataFrame({'a': [0,1,float('nan')], 'b': [1,1,float('nan')]})
        self.assertTrue(check_dataframe_na(df))

if __name__ == '__main__':
    unittest.main()

