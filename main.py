import csv
import json
import click

class CSV:
    def __init__(self, path):
        self.path = path
    
    def get_header(self):
        reader = []
        
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            reader = list(reader)
        
        head = reader[0]
        json_object = {"head": head}
        
        with open('output.json', 'w') as f:
            f.write(json.dumps(json_object, indent=4))
        
        return head
    
    def get_data_key(self, key):
        values = []
        
        with open(self.path, 'r') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                values.append(row[key])
            
        json_object = {key: values}
        
        with open('output.json', 'w') as f:
            f.write(json.dumps(json_object, indent=4))
        
        return values
    
    def get_all_csv(self):
        with open(self.path, 'r') as f:
            reader = csv.DictReader(f)
            data_list = [row for row in reader]
        
        with open('output.json', 'w') as f:
            f.write(json.dumps(data_list, indent=4))
        
        return data_list

@click.command()
@click.argument('file')
@click.option('--header', is_flag=True, help='Get the header of the CSV file.')
@click.option('--key', help='Get data by key.')
def cli(file, header, key):
    csv_file = CSV(file)
    
    if header:
        click.echo(f"Header: {csv_file.get_header()}")
    elif key:
        click.echo(f"Data for key '{key}': {csv_file.get_data_key(key)}")
    else:
        click.echo(f"All CSV data: {csv_file.get_all_csv()}")

if __name__ == '__main__':
    cli()