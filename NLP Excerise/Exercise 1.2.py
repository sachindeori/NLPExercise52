#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1
total_seconds = 42 * 60 + 42
print("Total Seconds:", total_seconds)


# In[2]:


# Question 2
total_miles = 10 / 1.61
print("Total Miles:", total_miles)


# In[3]:


#question 3

total_seconds = 42 * 60 + 42
total_miles = 10 / 1.61
pace_in_seconds = total_seconds / total_miles
average_pace_minutes = int(pace_in_seconds // 60)
average_pace_seconds = int(pace_in_seconds % 60)

print(f"Average Pace: {average_pace_minutes} minutes {average_pace_seconds} seconds per mile")

# Convert pace to hours
total_hours = total_seconds / 3600
average_speed = total_miles / total_hours
print(f"Average Speed: {average_speed} miles per hour")


# In[ ]:




