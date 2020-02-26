import pandas as pd
import matplotlib.pyplot as plot 
import os
from sklearn import preprocessing


os.chdir("D:\Chris_Personal\challange\cainthus_data_science_challenge")
print(os.getcwd())

data = "feed_data.csv"
col_names = ['barn', 'localtime', 'feed_level', 'feed_position']
feed_data = pd.read_csv(data, header=True, names=col_names)


feed_data = pd.read_csv("feed_data.csv")
feed_dataframe = pd.DataFrame(feed_data)
feed_delivery = pd.read_csv("feed_delivery_times.csv")
cow_detection_data = pd.read_csv("cow_detection_data.csv")


Normalize_columns

barn_norm = feed_dataframe[['feed_level']].values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(barn_norm)
feedllevel_normalized = pd.DataFrame(x_scaled)


feedposition_norm = feed_dataframe[['feed_position']].values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
y_scaled = min_max_scaler.fit_transform(barn_norm)
feedposition_normalized = pd.DataFrame(y_scaled)


barn_norm.plot(kind='scatter',x='feed_level',y='feed_position',color='red')

plot.scatter(feed_data.localtime,feed_data.feed_level,feed_data.feed_position)

#plot.scatter(feedllevel_normalized,feedposition_normalized)
#plot.xlabel('feedlleve')
#plot.ylabel('feedposition')
#plot.title('MOvement of Cows')


#barn_norm.plot(kind='scatter',x='feed_level',color='red')
