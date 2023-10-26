from controller.import_files import ImportFiles
from controller.grouping import Grouping
from controller.cleansing import Cleansing
import openpyxl
import xlrd


def cleanse_learning_data():
    #  import excel files
    learning_df = ImportFiles.import_excel_files(
        "./files/Training History IT_9010.XLSX"
    )

    # cleanse weird chars from column "Course Name"
    learning_df["Course Name"] = Cleansing.remove_all_non_ascii_code_from_column(
        dataframe=learning_df, column_to_cleanse="Course Name"
    )

    # cleanse unwanted chars: ":" and "." from column "Course Name"
    learning_df["Course Name"] = Cleansing.remove_characters_from_column(
        dataframe=learning_df,
        column_to_cleanse="Course Name",
        chars_to_remove=[":", "."],
    )

    # cleanse duplicate data refers to "Personnel Number"
    learning_df = Cleansing.remove_duplicates_from_column(
        dataframe=learning_df,
        column_to_drop="Personnel Number",
        sort_first=True,
        sort_by_column=["Personnel Number"],
        keep_type="last",
    )

    # save the result as excel
    learning_df.to_excel("./files/Result.xlsx")


cleanse_learning_data()
