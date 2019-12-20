import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GS_data:
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("PZSP-ef8954300654.json", scope)

    client = gspread.authorize(credentials)

    sheet = client.open("PZSP").sheet1  # opening the spreadsheet

    data = sheet.get_all_records()   # getting a list of all records

    def get_curr_consumption(self, range=10):
        return sheet.col_values(1)[-range:]  # getting values from current consumption column (%)
    def get_out_temp(self, range=10):
        return sheet.col_values(2)[-range:]  # getting values from temperature outside column (°C)
    def get_ins_temp(self, range=10):
        return sheet.col_values(3)[-range:]  # getting values from temperature inside column (°C)
    def are_wind_open(self, range=10):
        return sheet.col_values(4)[-range:]  # getting true if windows are open
    def is_airc_on(self, range=10):
        return sheet.col_values(5)[-range:]  # getting true if air conditioning launched

