import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import random
df=pd.read_csv(r'G:\DJ Sanghvi\NOTES\PYTHON\DHRUV\PYTHON_prj\most_subscribed_youtube_channels.csv')
print(df)
# null values
df.isnull()
df = df.dropna()
print(df)

fig, axs = plt.subplots(2,1, figsize=(10, 10))

''' Most viewed category on the basis of views '''
# data for pie chart
category = df['category']
df2 = pd.DataFrame(category)
print(df2)
views = df['views']
df3 = pd.DataFrame(views)
print(df3)

combined_list = zip(category, views)
# Use a dictionary comprehension to create the dictionary
category_views = {key: value for key, value in combined_list}
# Create a list to store the categories with less than 2 counts
less_than_two = []
# Iterate through the category_views dictionary and check for categories with less than 2 counts
for category, views in category_views.items():
    #if category_views[category] < 2:
    if len(category) < 2:
        less_than_two.append(category)
# Combine the views and category for categories with less than 2 counts
for category in less_than_two:
    if "Other" in category_views:
        category_views["Other"] += category_views.pop(category)
    else:
        category_views["Other"] = category_views.pop(category)
# Display the pie chart using the category_views dictionary
labels = list(category_views.keys())
sizes = list(category_views.values())
sizes = [int(size.replace(',','')) if isinstance(size, str) else size for size in sizes]
wedgeprops = {'linewidth': 2, 'edgecolor':'black'}
axs[0].pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90,textprops={'color':'white'} , wedgeprops=wedgeprops)
axs[0].set_title('Total Views on the basis of Category')
axs[0].axis('equal')  
axs[0].legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0.)


''' Dual axis for subscribers and views of youtubers '''
df = df.head(10)
# Data for the line chart
df['subscribers'] = df['subscribers'].str.replace(',','').astype(float)
df['views'] = df['views'].str.replace(',','').astype(float)
Youtuber = df['Youtuber']
subscribers = df['subscribers']
views = df['views']
print(Youtuber)
print(subscribers)
print(views)
# create figure and axes
# plot bar chart
axs[1].bar(Youtuber, subscribers, color='r', width=0.4)
axs[1].set_ylabel('Subscribers (in million)')
# create second y-axis
ax2 = axs[1].twinx()
# plot line chart
ax2.plot(Youtuber, views, '-o')
#ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
ax2.set_title('Average Views and Subscribers count of TOP 10 youtubers')
ax2.set_ylabel('Views (in hundred Billion)')

plt.tight_layout()
plt.show()
