import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GS_data:
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("models\connect.json", scope)

    client = gspread.authorize(credentials)

    sheet = client.open("PZSP").sheet1  # opening the spreadsheet

    data = sheet.get_all_records()   # getting a list of all records

    def __init__(self, range=24):
        self.range = range

    def get_curr_consumption(self):
        return list(self.sheet.col_values(1)[-self.range:])  # getting values from current consumption column (%)
    def get_out_temp(self):
        return list(self.sheet.col_values(2)[-self.range:])  # getting values from temperature outside column (°C)
    def get_ins_temp(self):
        return list(self.sheet.col_values(3)[-self.range:])  # getting values from temperature inside column (°C)
    def are_wind_open(self):
        return list(self.sheet.col_values(4)[-self.range:])  # getting true if windows are open
    def is_airc_on(self):
        return list(self.sheet.col_values(5)[-self.range:])  # getting true if air conditioning launched

