from unittest import TestCase
import pandas as pd
from stata import Model

class TestStata(TestCase):

    def test_model(self):
        df = pd.DataFrame({'y': [1, 2, 3, 4], 'x': [0, 1, 0, 1]})
        sm = Model(df, 'regress y x, robust')
        result = sm.estimate()
        expected = {
            'cmdline': 'regress y x, robust',
            'V': [
                [2, -1],
                [-1, 1]
            ],
            'b': [[1, 2]],
            'r2': 0.2,
            'N': 4.0
        }
        self.assertEquals(result, expected)
