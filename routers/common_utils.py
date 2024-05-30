import json

class CommonUtils:
    "common_utils"
    def writ_json(self, filename, data):
        with open(filename, 'w') as f:
            f.write(json.dumps(data))