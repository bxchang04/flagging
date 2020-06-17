import pandas as pd
from flagging_site.data.model import reach_2_model
import pytest


def test_model_out_is_bounded(input_data: pd.DataFrame):
    # test that viewing the data renders the data between the values of 0 and 1
    df = reach_2_model(input_data)
    assert all(0 < i < 1 for i in list(df['r2_sigmoid']))

