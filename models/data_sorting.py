from models.gs_sync import GS_data


class DataSort:
    def get_circle_chart_data(self, list):
        yes = 0
        no = 0
        for value in list:
            if value == "TRUE":
                yes += 1
            elif value == "FALSE":
                no += 1
        return yes, no

