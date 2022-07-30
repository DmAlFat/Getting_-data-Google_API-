import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials as sac
from converter import course


def gsheet_to_df(spreadsheet_name, sheet_num=0):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials_path = 'credentials.json'

    credentials = sac.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(credentials)

    sheet = client.open(spreadsheet_name).get_worksheet(sheet_num).get_all_records()
    df = pd.DataFrame.from_dict(sheet)
    df["Стоимость, Руб"] = [i*course if type(i) is not str else '-' for i in df["Стоимость, $"]]
    return df
