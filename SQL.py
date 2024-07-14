#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql')


# In[2]:


get_ipython().system('pip install mysql-connector-python')


# In[1]:


import mysql.connector


# In[2]:


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sai@1112'
)
print(mydb)


# In[5]:


mycursor=mydb.cursor()


# In[6]:


mycursor.execute('SHOW DATABASES')
for i in mycursor:
    print(i)


# In[ ]:


mycursor.execute('CREATE DATABASE database1')


# In[19]:


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sai@1112',
    database='database1'
)

mycursor=mydb.cursor()


# In[ ]:


mycursor.execute


# In[3]:


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sai@1112',
    database='capstone'
)

mycursor=mydb.cursor()


# In[4]:


mycursor.execute('SHOW TABLES')


# In[5]:


for i in mycursor:
    print(i)


# 3.1	        Insert records from 42_District_wise_crimes_committed_against_women_2001_2012.csv into a table.

# In[11]:


mycursor.execute('SELECT * from capstone.district_women')


# In[12]:


mycursor.fetchall()


# 3.2	Write SQL query to find the highest number of rapes & Kidnappings that happened in which state, District, and year.
# 
# 

# In[17]:


while mycursor.nextset():
    mycursor.fetchall()
sql = """
    SELECT state, DISTRICT, Year, MAX(Rape) AS max_rapes, MAX(kidnap_abduction) AS max_kidnappings 
    FROM capstone.district_women 
    WHERE DISTRICT <> 'TOTAL' and DISTRICT <> 'DELHi UT TOTAL' 
    GROUP BY state, DISTRICT, year 
    ORDER BY max_rapes DESC, max_kidnappings DESC 
    LIMIT 5;
"""
mycursor.execute(sql)
result = mycursor.fetchall()
for items in result:
    print(items)


# 3.3	Write SQL query to find All the lowest number of rapes & Kidnappings that happened in which state, District, and year.
# 
# 

# In[20]:


while mycursor.nextset():
    mycursor.fetchall()
sql = """
    SELECT state, DISTRICT, Year, MAX(Rape) AS max_rapes, MAX(kidnap_abduction) AS max_kidnappings 
    FROM capstone.district_women 
    WHERE DISTRICT <> 'TOTAL' and DISTRICT <> 'DELHi UT TOTAL' 
    GROUP BY state, DISTRICT, year 
    ORDER BY max_rapes, max_kidnappings
    LIMIT 10;
"""
mycursor.execute(sql)
result = mycursor.fetchall()
for items in result:
    print(items)


# 3.4	Insert records from 02_District_wise_crimes_committed_against_ST_2001_2012.csv into a new table

# In[24]:


mycursor.execute('SELECT * from capstone.crimes_againest_st')


# In[25]:


mycursor.fetchall()


# 3.5	Write SQL query to find the highest number of dacoity/robbery in which district.

# In[29]:


sql = '''
SELECT STATE_UT, DISTRICT, MAX(Year) AS max_year, MAX(Dacoity) AS max_dacoity, MAX(Robbery) AS max_robbery
FROM capstone.crimes_againest_st
WHERE DISTRICT <> 'TOTAL' AND DISTRICT <> 'DELHI UT TOTAL'
GROUP BY STATE_UT, DISTRICT
ORDER BY max_dacoity DESC, max_robbery DESC
LIMIT 5;
'''

mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)


# 3.6	Write SQL query to find in which districts(All) the lowest number of murders happened.

# In[30]:


sql = '''
SELECT STATE_UT, DISTRICT, MIN(Murder) AS min_Murder
FROM capstone.crimes_againest_st
WHERE DISTRICT <> 'TOTAL' AND DISTRICT <> 'DELHI UT TOTAL'
GROUP BY STATE_UT, DISTRICT
ORDER BY min_Murder DESC

'''

mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)


# 3.7	Write SQL query to find the number of murders in ascending order in district and year wise.

# In[34]:


sql = '''
SELECT STATE_UT, DISTRICT,Year,MIN(Murder
) as murders
FROM capstone.crimes_againest_st
WHERE DISTRICT <> 'TOTAL' AND DISTRICT <> 'DELHI UT TOTAL'
GROUP BY STATE_UT, DISTRICT,Year
ORDER BY DISTRICT,Year,murders

'''

mycursor.execute(sql)
result = mycursor.fetchall()
for i in result:
    print(i)
  


# 3.8.1	Insert records of STATE/UT, DISTRICT, YEAR, MURDER, ATTEMPT TO MURDER, and RAPE columns only from 01_District_wise_crimes_committed_IPC_2001_2012.csv into a new table.
# 
# 

# In[38]:


import pandas as pd
df = pd.read_csv('Book.csv', usecols=['STATE/UT', 'DISTRICT', 'YEAR', 'MURDER', 'ATTEMPT TO MURDER'])


# In[40]:


df.columns=['STATE_UT', 'DISTRICT', 'YEAR', 'MURDER', 'ATTEMPT_TO_MURDER']


# In[41]:


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sai@1112',
    database='capstone'
)

mycursor=mydb.cursor()


# In[45]:


create_table_sql = """
CREATE TABLE new_crimes_table (
    STATE_UT VARCHAR(255),
    DISTRICT VARCHAR(255),
    YEAR INT,
    MURDER INT,
    ATTEMPT_TO_MURDER INT,
    RAPE INT
);
"""

mycursor.execute(create_table_sql)


# In[65]:


insert_sql='''
INSERT INTO new_crimes_table('STATE_UT', 'DISTRICT', 'YEAR', 'MURDER', 'ATTEMPT_TO_MURDER')
VALUES (%s,%s,%s,%s,%s) '''


# In[66]:


# Insert data into the new table
for i, row in df.iterrows():
    try:
        print(tuple(row))  # Debug: Print the row to be inserted
        mycursor.execute(insert_sql, tuple(row))
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print(f"Row causing error: {tuple(row)}")
        continue  # Skip the row that caused the error and continue with the next

# Commit the transaction
conn.commit()

# Close the connection
mycursor.close()
conn.close()


# In[61]:


df=pd.read_csv(r"csv")


# In[62]:


df


# In[53]:


import re


# In[64]:


test=re.sub(" ","_",text)


# In[60]:


print(test)


# 3.8.1	Insert records of STATE/UT, DISTRICT, YEAR, MURDER, ATTEMPT TO MURDER, and RAPE columns only from 01_District_wise_crimes_committed_IPC_2001_2012.csv into a new table.

# In[7]:


mycursor.execute('SELECT * FROM capstone.crimes_ipc')


# In[8]:


mycursor.fetchall()


# 3.8.2	Write SQL query to find which District in each state/UT has the highest number of murders year wise. Your output should show STATE/UT, YEAR, DISTRICT, and MURDERS.

# In[13]:


sql='''

 SELECT `STATE/UT`, `YEAR`, `DISTRICT`, `MURDER`
FROM (
    SELECT `STATE/UT`, `YEAR`, `DISTRICT`, `MURDER`,
           RANK() OVER (PARTITION BY `STATE/UT`, `YEAR` ORDER BY `MURDER` DESC) murder_rank
    FROM `crimes_ipc`
) tmp
WHERE murder_rank = 1;
'''


# In[14]:


mycursor.execute(sql)


# In[15]:


result=mycursor.fetchall()


# In[17]:


result


# 3.8.3	Store the above data (the result of 3.2) in DataFrame and analyze districts that appear 3 or more than 3 years and print the corresponding state/UT, district, murders, and year in descending order.

# In[26]:


sql='''select * from crimes_ipc;
SELECT STATE/UT, DISTRICT, MURDER, YEAR
FROM crimes_ipc
WHERE DISTRICT IN (
    SELECT DISTRICT
    FROM crimes_ipc
    GROUP BY DISTRICT
    HAVING COUNT(DISTRICT) >= 3
)
ORDER BY YEAR DESC; 
'''


# In[ ]:





# In[27]:


mycursor.execute(sql)
result=mycursor.fetchall()
result

