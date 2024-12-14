import csv
import json

class CSV:
    def __init__(self, path):
        self.path = path
            
    def get_header(self):
        reader = []
        
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            
            reader = list(reader)
        
        head = reader[0]
        json_object = {"head" : head}
        
        with open('output.json', 'w') as f:
            f.write(json.dumps(json_object, indent=4))
    
    def get_data_key(self, key):
        values = []
        
        with open(self.path, 'r') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                values.append(row[key])
            
        json_object = {key : values}
        
        with open('output.json', 'w') as f:
            f.write(json.dumps(json_object, indent=4))
    
    def get_all_csv(self):
        with open(self.path, 'r') as f:
            reader = csv.DictReader(f)
            data_list = [row for row in reader]
        
        
        with open('output.json', 'w') as f:
            f.write(json.dumps(data_list, indent=4))