"""Example of using PandasAI with a Pandas DataFrame"""

import pandas as pd
from data.sample_dataframe import dataframe

from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

df = pd.DataFrame(dataframe)

llm = OpenAI()
pandas_ai = PandasAI(llm, verbose=True, conversational=False)
response = pandas_ai.run(df, "북아메리카 국가의 GDP 합계 계산하기")
print(response)
# Output: 20901884461056
