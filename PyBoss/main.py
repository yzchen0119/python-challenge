import os
import csv 
from datetime import datetime

csvpath = os.path.join('..', 'PyBoss', 'employee_data.csv')

#state abbr dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# empty lists to store data
emp_id = []
first_name = []
last_name = []
dob =[]
ssn = []
state = []

with open(csvpath, newline='') as csvfile:  
    csvreader = csv.reader(csvfile)
    next(csvreader)
    
    # append information to empty lists 
    for row in csvreader:
        emp_id.append(row[0])
        first_name.append(row[1].split(" ")[0])
        last_name.append(row[1].split(" ")[1])
        dob.append(datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
        ssn.append(f"***-**-{row[3].split('-')[2]}")
        state.append(us_state_abbrev[row[4]])
        
# zip lists 
result = zip(emp_id, first_name, last_name, dob, ssn, state)

output_path = os.path.join('..', 'PyBoss', 'result.csv')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ",")
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    csvwriter.writerows(result)