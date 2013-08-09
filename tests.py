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

    def test_json_decode_error(self):
        import statsmodels.api as sm
        spector_data = sm.datasets.spector.load()
        df = pd.DataFrame(spector_data.exog, columns=['x1', 'x2', 'group'])
        df['constant'] = 1
        df['y'] = spector_data.endog

        sm = Model(df, 'clogit y x1 x2, group(group)', scalars=['N'])
        # Need to modify the scalars pulled from Stata because Stata
        # does not compute an R squared for a conditional logit,
        # otherwise we'll get a ValueError.
        result = sm.estimate()
