#For analysing one year for one country at a time.
import pandas as pd
import statistics
df = pd.read_excel("C:/Users/Krishna Vadrevu/Desktop/Vineet_Stuff/Datasets/New_bhutan_2012-2023_peaksummer_only_daily_aggregate (3) (1).xlsx",sheet_name="2013",usecols=[1,2],nrows=64)
#print(df)
meanList=df['Fire Counts'].tolist()
mean=0
for x in meanList:
    mean+=x
mean/=df.shape[0]

li=df.iloc[:,1].tolist()
std_dev=statistics.stdev(li)
#also try modifying ddof (degrees of delta freedom)
EventCounter=0
for x in li:
    if((x-mean)/std_dev)>1.96:
        EventCounter+=1
print("There were",EventCounter," extreme events in 2013.")
