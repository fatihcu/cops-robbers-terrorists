
# Importing libraries
import pandas as pd
import numpy as np
from gmplot import gmplot
import matplotlib.pyplot as plt
import seaborn as sns

# Api key in order to use google maps.
api_key="MY-API-KEY"
# Reading dataset, available with additional information provided url. I made another dataframe for Cold War Era by subtracting years from 1992 to 2016
terror=pd.read_csv(r'path.csv')
cw=terror[terror["iyear"]<1993]
# Create a dataframe for plotting heatmap on google maps and then plotting them intended parameters like radius or opacity of points.
field=cw[['latitude','longitude']]
field=field.dropna(how='all',axis=0)
gmap = gmplot.GoogleMapPlotter(apikey=api_key,center_lat=0,center_lng=0,zoom=1.5)
gmap.heatmap(threshold=0,radius=15,opacity=0.8,lats=field["latitude"],lngs=field["longitude"])
# Gmap accepts only html format, after creating the format, I took a screenshot and used it.
gmap.draw("m.html")

# Firstly I grouped dataframe by terrorist group names and then made a barplot
groups=cw.gname.value_counts().reset_index().sort_values(by='gname',ascending=False)
groups.columns=['Terrorist Group Name','Counts']
groups=groups.iloc[1:,:]
group_top_15=groups.iloc[:15,:]
sns.set_palette('Spectral')
sns.set_style('whitegrid')
sns.barplot(x=group_top_15['Terrorist Group Name'],y=group_top_15['Counts'],color='Black')
plt.xticks(rotation=90)
plt.title('Cold War Era Top 15 Active Terrorist Groups')
plt.figure(figsize(8,8))

# After the groups, I made a dataframe for country groups and plotted.
country=cw.groupby('country_txt')['country_txt'].count().sort_values(ascending=False)
country=country.rename('Counts')
country_top_15=country[:15]
sns.set_style('whitegrid')
sns.barplot(x=country_top_15.index,y=country_top_15,color='DarkGreen')
plt.xticks(rotation=90)
plt.title('Cold War Era Top 15 Country with Terror Attacks')
plt.figure(figsize(8,8))

# Then looked at the years and made a line plot with points
years=pd.DataFrame(cw.groupby(['iyear'])['Unnamed: 0'].count())
years["index"]=list(years.index)
sns.set_style('whitegrid')
sns.pointplot(x="index",y="iyear",data = years)
plt.title("Number of Terror Incidents Across the World Wide through 1970 to 1992")
plt.xlabel("Years")
plt.ylabel("Number of Terror Incidents")

# Lastly, I used attacking type for describing data.
attack_count=cw.groupby('attacktype1_txt')['Unnamed: 0'].count().reset_index()
attack=cw.groupby(['iyear','attacktype1_txt'])['Unnamed: 0'].count().reset_index()
attack=attack[attack['attacktype1_txt']!='Unknown']
attack_top3=attack_count.iloc[:3,:]
attack=attack[attack['attacktype1_txt'].isin(attack_top3['attacktype1_txt'])]
attack.columns=["Years","Types","Counts"]
sns.pointplot(x="Years",y="Counts",data=attack,hue="Types")
plt.title("Most 3 Attacking Types from 1970 to 1992")







