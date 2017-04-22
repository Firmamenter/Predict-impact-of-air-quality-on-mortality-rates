import csv
import random
test_amount = random.sample(range(1, 11834), 1833)
test_amount.sort()

# Load data
def load_data(split):
    with open(split + '.csv') as f:
        data = []
        next(f)
        for line in f.readlines():
            if split != 'test':
                Id, region, date, mortality_rate, O3, PM10, PM25, NO2, T2M = line.split(',')
                data.append([Id.strip(), region.strip(), date.strip(), mortality_rate.strip(), O3.strip(), PM10.strip(), PM25.strip(), NO2.strip(), T2M.strip()])
            else:
                Id, region, date, O3, PM10, PM25, NO2, T2M = line.split(',')
                data.append([Id.strip(), region.strip(), date.strip(), O3.strip(), PM10.strip(), PM25.strip(), NO2.strip(), T2M.strip()])
        return data
    
X = load_data('train')

print ('Length of X: ', len(X))

test_data = []

for index in test_amount:
    test_data.append(X[index])

X = [x for x in X if int(x[0]) not in test_amount]

with open('test_new.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(test_data)

print ('Length of new temp: ', len(X))    

with open('train_new.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(X)