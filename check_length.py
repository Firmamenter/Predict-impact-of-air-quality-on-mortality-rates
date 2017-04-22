import csv

# Load data
def load_data(split):
    with open(split + '.csv') as f:
        data = []
        for line in f.readlines():
            if split != 'test':
                Id, region, date, mortality_rate, O3, PM10, PM25, NO2, T2M = line.split(',')
                data.append([Id.strip(), region.strip(), date.strip(), mortality_rate.strip(), O3.strip(), PM10.strip(), PM25.strip(), NO2.strip(), T2M.strip()])
            else:
                Id, region, date, O3, PM10, PM25, NO2, T2M = line.split(',')
                data.append([Id.strip(), region.strip(), date.strip(), O3.strip(), PM10.strip(), PM25.strip(), NO2.strip(), T2M.strip()])
        return data
    
X = load_data('train_2k')

print ('Length of new temp: ', len(X))