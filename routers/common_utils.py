import json

class CommonUtils:
    "common_utils"
    def writ_json(self, filename, data):
        with open(f"data/{filename}.json", 'w') as f:
            f.write(json.dumps(data))

    def read_json(self, filename):
        with open(f"data/{filename}.json", 'r') as f:
            data = json.loads(f.read())
        return data
    
    def income_formater(self, year, month, income):
        income_dict = {}
        month_dict = {}
        month_dict[month] = {"income": income}
        income_dict[year] = month_dict
        return income_dict