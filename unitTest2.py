import pandas as pd
from pandas.testing import assert_frame_equal
import unittest

class UnitTestDF(unittest.TestCase):
    def __init__(self, df, expected):
        self.df = pd.read_csv(df)
        self.expected = pd.read_csv(expected)


class Identify_Less_Than_1Mb(UnitTestDF):
    def image_less_then_1Mb(self):
        # act
        actual = self.df[self.df['File Size(in Mb)'].apply(lambda x: x < 1)].reset_index(drop=True)

        actual = actual.loc[:, ~actual.columns.str.match("Unnamed")]
        self.expected = self.expected.loc[:, ~self.expected.columns.str.match("Unnamed")]

        # assert
        assert_frame_equal(actual, self.expected, check_dtype=False)
        print(self.expected)
        return "Test Successfully Completed"


print(Identify_Less_Than_1Mb('Test1.csv', 'Test2.csv').image_less_then_1Mb())

