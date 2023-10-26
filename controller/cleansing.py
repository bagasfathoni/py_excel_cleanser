import pandas
import numpy


class Cleansing:
    @classmethod
    def remove_characters_from_column(
        cls,
        dataframe: pandas.DataFrame,
        column_to_cleanse: str | list,
        chars_to_remove: list,
    ):
        try:
            temp = dataframe[column_to_cleanse]
            for char in chars_to_remove:
                temp = temp.apply(lambda x: str(x).replace(char, ""))
            return temp
        except Exception as e:
            print("ERROR WHEN REMOVING CHARACTERS: ", e)
            return

    @classmethod
    def remove_all_non_ascii_code_from_column(
        cls, dataframe: pandas.DataFrame, column_to_cleanse: str | list
    ):
        try:
            return (
                dataframe[column_to_cleanse]
                .str.encode("ascii", "ignore")
                .str.decode("ascii")
            )
        except Exception as e:
            print("ERROR WHEN REMOVING NON ASCII CODE: ", e)
            return

    @classmethod
    def remove_duplicates_from_column(
        cls,
        dataframe: pandas.DataFrame,
        column_to_drop: str | list,
        sort_first: bool,
        sort_by_column: list,
        keep_type: str,
    ):
        try:
            if sort_first:
                sorted_df = dataframe.sort_values(by=sort_by_column).reset_index(
                    drop=True
                )
                result = sorted_df.drop_duplicates(
                    subset=column_to_drop, keep=keep_type
                ).reset_index(drop=True)
                return result
            else:
                return dataframe.drop_duplicates(
                    subset=column_to_drop, keep=keep_type
                ).reset_index(drop=True)
        except Exception as e:
            print("ERROR WHEN REMOVING DUPLICATE: ", e)
            return

    @classmethod
    def remove_na_from_column(
        cls,
        dataframe: pandas.DataFrame,
        column_to_drop: str | list,
        sort_first: bool,
        sort_by_column: list,
        remove_type: str,
    ):
        try:
            if sort_first:
                sorted_df = dataframe.sort_values(by=sort_by_column).reset_index(
                    drop=True
                )
                result = sorted_df.dropna(
                    subset=column_to_drop, how=remove_type
                ).reset_index(drop=True)
                return result
            else:
                return dataframe.dropna(
                    subset=column_to_drop, how=remove_type
                ).reset_index(drop=True)
        except Exception as e:
            print("ERROR WHEN REMOVING N/A: ", e)
            return
