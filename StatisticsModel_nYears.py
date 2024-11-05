import pandas as pd
import statistics
import matplotlib.pyplot as pl

file_path="C:/Users/Krishna Vadrevu/Desktop/Vineet_Stuff/datasets/firedatakpv/srilanka_2012-2023_peaksummer_only_daily_aggregate.xlsx"

#file_path="C:/Users/Krishna Vadrevu/Desktop/Vineet_Stuff/Datasets/afghanistan_2012-2023_peaksummer_only_daily_aggregate.xlsx"
#file_path="C:/Users/Krishna Vadrevu/Desktop/Vineet_Stuff/Datasets/New_bhutan_2012-2023_peaksummer_only_daily_aggregate (3) (1).xlsx"

oversum=0
country="Bangladesh"
arr=[]
arrtime=[]
choice=0
cstring=""

while(1): #user input
    choice=input("Please pick an option Fire Counts(1), or FRP Mean(2)")
    choice=int(choice)
    if(choice==1):
        choice=2
        cstring='Fire Counts'
        break
    elif(choice==2):
        choice=3
        cstring='FRP MEAN'
        break
    else:
        print("Please enter a valid option");continue


file=pd.ExcelFile(file_path) # find number of extreme events in any given year for any given country OR find the FRP Mean over the time period.
for sheet in file.sheet_names:
    print(sheet,"\n")
    df = pd.read_excel(file, sheet_name=sheet,usecols=[choice])#2
    df=df.dropna()
    print(df)
    listform=df[cstring].tolist()#Fire Counts
    mean=0
    for x in listform:
        mean+=x
    mean/=df.shape[0]
    # print(mean)
    li=df.iloc[:,0].tolist()#0
    arrtime.append(sheet)
    #print(sheet)
    std_dev=(df.std())
    std_dev=float(std_dev.iloc[0])
    EventCounter=0
    index=0
    #print("the mean is ",mean,"and the std dev is ",std_dev)
    for x in listform:
        val=(x-mean)/std_dev
        if val>=1.96:
            EventCounter+=1
            # print((x-mean)/std_dev)
    oversum+=EventCounter
    arr.append(EventCounter)
    print("There were",EventCounter,"extreme events in",sheet)


print("In total, there were",oversum,"events.")

#plot the data
dat={}
for x in range(len(arr)):
    dat[arrtime[x]]=arr[x]
dat["Total Events"]=oversum
print(dat)
dfplot = pd.DataFrame(list(dat.items()), columns=['Year', cstring])
fig, ax = pl.subplots(figsize=(1,4))
pl.title("Afghanistan",pad=35) #specifically testing Afghanistan, but can replace with var = country 
table = ax.table(cellText=dfplot.values, colLabels=dfplot.columns, cellLoc='center', loc='center')
dfplot = dfplot.T
ax.axis('off')
table.set_fontsize(20)
table.scale(0.75,0.75)
#pl.show()

dat=pd.DataFrame(dat,index=[0])
print(dat)
dat=dat.T
dat.reset_index(inplace=True)
print("-------------------------------------------------------------------")
#export data to external excel file
with pd.ExcelWriter("C:/Users/Krishna Vadrevu/Desktop/Vineet_Stuff/Datasets/InWrit.xlsx") as writer:
    dat.to_excel(writer, sheet_name="Sheet1",index=False)
