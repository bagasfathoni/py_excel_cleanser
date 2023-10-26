import pandas
import openpyxl
import xlrd


class ImportFiles:
    @classmethod
    def import_excel_files(cls, files_loc: str):
        try:
            df = pandas.read_excel(files_loc)
            print(
                "---\n IMPORTED EXCEL FILES '{}' WITH DETAILS: \n{}\n{}\n---".format(
                    files_loc, df.columns, df.index
                )
            )
            print("---\nSHOWING SAMPLE FROM EXCEL DATA: \n{}\n---".format(df.head(3)))
        except Exception as e:
            print("ERROR ON READING EXCEL FILES: ", e)
        return df

    @classmethod
    def import_csv_files(cls, files_loc: str):
        try:
            df = pandas.read_csv(files_loc)
            print("IMPORTED CSV FILES WITH DETAILS: \n", df.info)
            print("SHOWING SAMPLE FROM CSV DATA: \n", df.head(3))
        except Exception as e:
            print("ERROR ON READING CSV FILES: ", e)
        return df
