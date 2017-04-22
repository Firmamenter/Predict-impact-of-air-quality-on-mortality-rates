import csv
import random

# Load data
def load_data(split):
    with open(split + '.csv') as f:
        data = []
        for line in f.readlines():
            Id, region, date, mortality_rate, O3, PM10, PM25, NO2, T2M = line.split(',')
            data.append([Id.strip(), region.strip(), date.strip(), mortality_rate.strip(), O3.strip(), PM10.strip(), PM25.strip(), NO2.strip(), T2M.strip()])
        return data
    
X = load_data('train_4k')

for i in range(2000):
    X.pop(random.randint(0, 4000 - i))

print ('Length of new temp: ', len(X))    

with open('train_2k.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(X)