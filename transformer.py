# Connect the necessary modules
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials as sac
from converter import course


# create a function for authorization and getting values from google sheets
def gsheet_to_df(spreadsheet_name, sheet_num=0):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials_path = 'credentials.json'

    credentials = sac.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(credentials)  # authorization

    sheet = client.open(spreadsheet_name).get_worksheet(sheet_num).get_all_records()
    df = pd.DataFrame.from_dict(sheet)  # getting values
    df["Стоимость, Руб"] = [i*course if type(i) is not str else '-' for i in df["Стоимость, $"]]  # add the required column "Стоимость, Руб" to our dataframe object
    return df
