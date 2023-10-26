import pandas
import numpy


class Grouping:
    @classmethod
    def group_by_a_column(cls, dataframe: pandas.DataFrame, column_name: list):
        grp = dataframe.groupby(column_name)
        return grp
