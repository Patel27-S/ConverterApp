import json
import csv


def file_handling_function(file_name, file_type, file):
    
    if file_type.lower() == 'csv':

        # return json converted file object
        json_array = []

        decoded_file = file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)
      

        #convert each csv row into python dict
        for row in csv_reader: 
            #add this python dict to json array
            json_array.append(row)

        json_string = json.dumps(json_array, indent=4)

        return json_string

            

    if file_type.lower() == 'json':
        # return csv converted file object

        # decoded_file = file.read().decode('utf-8').splitlines()

        # with open(file, 'r') as json_file:
        #     jsondata = json.load(json_file)
        jsondata = file.read()

        print(jsondata)
        # Now, have to write the jsondata inside
        # of a csv.
        data_file = open('csv_file.csv', 'w', newline='')
        csv_writer = csv.writer(data_file)
        
        # writerow() is the main function
        # for writing json_data into csv_rows
        count = 0
        for data in jsondata:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())
        
        data_file.close()
        print(data_file)
        return data_file