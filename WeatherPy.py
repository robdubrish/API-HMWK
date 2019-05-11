#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# ### Analysis
# * As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.
# * There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.
# * There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.
# 
# ---
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[3]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Import API key
from api_keys import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[4]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# In[5]:



coor_df = pd.DataFrame ({"lats": lats, "lngs":lngs})


# In[6]:



#create empty lists
city = []
country = []
weather = []


for index, row in coor_df.iterrows():
    city_lat=(row["lats"])
    city_lng=(row["lngs"])
    city_name = citipy.nearest_city(city_lat, city_lng).city_name
    country_code = citipy.nearest_city(city_lat, city_lng).country_code
    city.append(city_name)
    country.append(country_code)
    
city_df= pd.DataFrame ({"city": city, "country": country})
city_df.drop_duplicates(["city", "country"])
city_df.head()


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[3]:


url = "http://api.openweathermap.org/data/2.5/weather?"
row_count = 1

for index, row in city_df.iterrows():
    act_city = row["City"]
    act_url = url + "appid=" + api_key + "&units=IMPERIAL" + "&q=" + target_city.replace(" ","+")
    print(act_url)
    city_df = requests.get(target_url).json()
  

    else:
        #clean_cities_df.set_value(index, "City", city_data["name"])
        
        Cities_data.set_value(index, "Temperature (F)", city_data["main"]["temp"])
        Cities_data.set_value(index, "Latitude", city_data["coord"]["lat"])
        Cities_data.set_value(index, "Longitude", city_data["coord"]["lon"])
        Cities_data.set_value(index, "Humidity (%)", city_data["main"]["humidity"])
        Cities_data.set_value(index, "Cloudiness (%)", city_data["clouds"]["all"])
        Cities_data.set_value(index, "Wind Speed (mph)", city_data["wind"]["speed"])


# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[4]:





# In[5]:





# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[6]:





# #### Latitude vs. Humidity Plot

# In[7]:





# #### Latitude vs. Cloudiness Plot

# In[8]:





# #### Latitude vs. Wind Speed Plot

# In[9]:





# In[ ]:




