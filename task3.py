import json
import sys

def fill_values(tests, values):
    
    values_dict = {item['id']: item['value'] for item in values}

    
    def recurse(item):
        if isinstance(item, dict):
            
            if 'id' in item:
                test_id1 = item['id']
                if test_id1 in values_dict:
                    item['value'] = values_dict[test_id1]
            
            for key in item:
                if isinstance(item[key], (dict, list)):
                    recurse(item[key])
        elif isinstance(item, list):
            
            for elem in item:
                recurse(elem)

    recurse(tests)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    
    
    with open(values_file, 'r') as vf:
        values = json.load(vf)
    
    with open(tests_file, 'r') as tf:
        tests = json.load(tf)
    
    
    fill_values(tests, values)
    
    
    with open(report_file, 'w') as rf:
        json.dump(tests, rf, indent=4)
    
    print(f"Report generated successfully in {report_file}")
