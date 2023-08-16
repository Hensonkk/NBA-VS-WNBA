#!/usr/bin/env python
# coding: utf-8

# In[120]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress
#import brokenaxes


# In[121]:


NBA_2019_2020_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/NBA 2019-2020 contracts.csv"
NBA_2020_2021_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/NBA 2020-2021 contracts.csv"
NBA_2021_2022_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/NBA 2021-2022 contracts.csv"
NBA_2022_2023_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/NBA 2022-2023 contracts.csv"
NBA_player_stats_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Datasets/NBA Player Stats.csv"


WNBA_2019_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/WNBA 2019 contracts.csv"
WNBA_2020_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/WNBA 2020 contracts.csv"
WNBA_2021_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/WNBA 2021 contracts.csv"
WNBA_2022_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/WNBA 2022 contracts.csv"
WNBA_2023_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Contracts/WNBA 2023 contracts.csv"
WNBA_player_stats_path = "C:/Users/evanm/smu/NBA-VS-WNBA/Datasets/WNBA Player Stats.csv"


# In[122]:


NBA_2019_2020 = pd.read_csv(NBA_2019_2020_path)
NBA_2020_2021 = pd.read_csv(NBA_2020_2021_path)
NBA_2021_2022 = pd.read_csv(NBA_2021_2022_path)
NBA_2022_2023 = pd.read_csv(NBA_2022_2023_path)

NBA_player_stats = pd.read_csv(NBA_player_stats_path)


WNBA_2019 = pd.read_csv(WNBA_2019_path)
WNBA_2020 = pd.read_csv(WNBA_2020_path)
WNBA_2021 = pd.read_csv(WNBA_2021_path)
# Got a strange error for these three CSVs. UniDecodeError: "UTF-8". Had to save the CSVs as UTF CSVs.
WNBA_2022 = pd.read_csv(WNBA_2022_path)
WNBA_2023 = pd.read_csv(WNBA_2023_path)

WNBA_player_stats = pd.read_csv(WNBA_player_stats_path)


# In[151]:


#WNBA_player_stats


# In[124]:


NBA_data = pd.concat([NBA_2019_2020,NBA_2020_2021,NBA_2021_2022,NBA_2022_2023], axis = 1)


# In[125]:


NBA_data.fillna("", inplace = True)


# In[152]:


#NBA_2019_2021_data.T

#NBA_data.head(50)


# In[153]:


#print(NBA_data.head)


# In[128]:


WNBA_data = pd.concat([WNBA_2019,WNBA_2020,WNBA_2021,WNBA_2022,WNBA_2023], axis = 1)


# In[129]:


WNBA_data.fillna("", inplace = True)


# In[154]:


#WNBA_data.head(50)


# In[155]:


#print(WNBA_data)


# In[132]:


#NBA_data[['Player2'],['Contract2']].head(10)


# In[156]:


#NBA_player_stats.head(50)


# In[157]:


NPTS = NBA_player_stats.PTS
#NPTS


# In[158]:


#WNBA_player_stats


# In[159]:


WPTS = WNBA_player_stats.PTS
#WPTS


# In[ ]:





# In[160]:


#WNBA_data.head(50)


# In[161]:


NCT = NBA_data.Contract
#NCT.describe()


# In[162]:


WNCT = WNBA_data.Contract
#WNCT.describe()


# In[ ]:





# In[140]:


# https://www.spotrac.com/wnba/rankings/
# https://www.forbes.com/sites/justinbirnbaum/2023/06/22/2023-nba-draft-projected-contracts-for-victor-wembanyama-and-other-first-round-picks/?sh=7ca731f43a34
# https://www.nba.com/
# https://www.wnba.com/   
# www.spotrac.com
    
# Top 5 Rookie season contracts for 2023

# Victor Wembanyama 12,200,000
# Brandon Miller 10,900,000
# Scoot Henderson 9,800,000
# Amen Thompson 8,800,000
# Ausar Thompson 8,000,000

# Aliyah Boston 74,305
# Diamond Miller 74,305
# Maddy Siegrist 74,305
# Stephanie Soares 74,305
# Lou Lopez Sénéchal 71,300



# 2023 Top 5 Supermax contracts

# Stephen Curry 48,070,014 
# LeBron James 44,474,988 
# Kevin Durant 44,119,845 
# Bradley Beal 43,279,250 
# Damian Lillard 42,492,492 

# Jewell Loyd $234,936
# Arike Ogunbowale $234,936
# Diana Taurasi $234,936
# DeWanna Bonner $234,350
# Elena Delle Donne $234,350



# In[148]:



salaries1 = [12200000,10900000,9800000,8800000,8000000]
salaries2 = [74305,74305,74305,74305,71300]
salaries3 = salaries1 + salaries2
name1 = ["Victor Wembanyama","Brandon Miller", "Scoot Henderson","Amen Thompson","Ausar Thompson"]
name2 = ["Aliyah Boston", "Diamond Miller", "Maddy Siegrist", "Stephanie Soares", "Lou Lopez Sénéchal"]
name3 = name1 + name2
X_axis1 = np.arange(len(name3))
plt.bar(X_axis1 - 0.2, 0.2, facecolor = "blue", label = "NBA")
plt.bar(X_axis1 + 0.2, 0.2, facecolor = "red", label = "WNBA")
plt.bar(name1, salaries1, color = ["blue"])
plt.bar(name2, salaries2, color = ["red"])
plt.xlabel("Players")
plt.ylabel("Salary ($ tens of millions)")
plt.ylim(0,12000000)
plt.xticks(X_axis1, name3, rotation = 79)
plt.title("Top 5 Rookie season contracts for 2023")
plt.legend()
#plt.grid()
#plt.annotate()
plt.show()


# In[150]:


# Top 5 Supermax contracts for 2022-2023

# Stephen Curry 48,070,014 
# LeBron James 44,474,988 
# Kevin Durant 44,119,845 
# Bradley Beal 43,279,250 
# Damian Lillard 42,492,492 

# Jewell Loyd 234,936
# Arike Ogunbowale 234,936
# Diana Taurasi 234,936
# DeWanna Bonner 234,350
# Elena Delle Donne 234,350



salaries4 = [48070014,44474988,44119845,43279250,42492492] 
salaries5 = [234936,234936,234936,234350,234350]
salaries6 = salaries4 + salaries5
name4 = ["Stephen Curry","LeBron James", "Kevin Durant","Bradley Beal", "Damian Lillard"]
name5 = ["Jewell Loyd", "Arike Ogunbowale", "Diana Taurasi", "DeWanna Bonner", "Elena Delle Donne"]
name6 = name4 + name5
X_axis2 = np.arange(len(name6))
plt.bar(X_axis2 - 0.2, 0.2, facecolor = "blue", label = "NBA")
plt.bar(X_axis2 + 0.2, 0.2, facecolor = "red", label = "WNBA")
plt.bar(name4, salaries4, color = ["blue"])
plt.bar(name5, salaries5, color = ["red"])
plt.xlabel("Players")
plt.ylabel("Salary ($ tens of millions)")
plt.ylim(0,60000000)
plt.xticks(X_axis2, name6, rotation = 79)
plt.title("Top 5 Max contracts for 2022-2023")
plt.legend()
#plt.annotate()
plt.show()


# In[163]:


#NBA_data.head(50)


# In[164]:


#WNBA_data.head(50)


# In[ ]:





# In[26]:


PT1 = NBA_data["BS"]
Y = PT1.iloc[0:50]


# In[27]:


c_years1 = NBA_data["STPG"]
X = c_years1.iloc[0:50]


# In[28]:



plt.scatter(X, Y, color = "blue", alpha = 0.5)


plt.title("Steals & Base Salary NBA")
plt.ylabel("Salary ($)") 
plt.xlabel("Steals")
plt.ylim(0,60000000)
plt.grid(True)
plt.show()


# In[29]:


c_years2 = NBA_data["PTS"]
X2 = c_years2.iloc[0:50]


# In[30]:


PT2 = NBA_data["BS"]
Y2 = PT2.iloc[0:50]


# In[31]:


plt.scatter(X2, Y2, color = "blue", alpha = 0.5)


plt.title("Points & Base Salary NBA")
plt.ylabel("Salary ($)") 
plt.xlabel("Points")
plt.ylim(0,60000000)
plt.grid(True)
plt.show()


# In[32]:


c_years3 = NBA_data["Age"]
X3 = c_years3.iloc[0:50]


# In[33]:


PT3 = NBA_data["BS"]
Y3 = PT3.iloc[0:50]


# In[34]:


# plt.scatter(X3, Y3, color = "blue", alpha = 0.5)


# plt.title("Age & Base Salary NBA")
# plt.ylabel("Salary ($)") 
# plt.xlabel("Age")
# plt.ylim(0,60000000)
# plt.grid(True)
# plt.show()


# In[35]:


c_years4 = WNBA_data["STL"]
X4 = c_years4.iloc[0:50]


# In[36]:


PT4 = WNBA_data["BS"]
Y4 = PT4.iloc[0:50]


# In[37]:


plt.scatter(X4, Y4, color = "blue",  alpha = 0.5)


plt.title("Steals & Base Salary WNBA")
plt.ylabel("Salary ($)") 
plt.xlabel("Steals")
plt.ylim(0,250000)
plt.grid(True)
plt.show()


# In[38]:


c_years5 = WNBA_data["PTS"]
X5 = c_years5.iloc[0:50]


# In[39]:


PT5 = WNBA_data["BS"]
Y5 = PT5.iloc[0:50]


# In[40]:


plt.scatter(X5, Y5, color = "blue", alpha = 0.5)


plt.title("Points & Base Salary WNBA")
plt.ylabel("Salary ($)") 
plt.xlabel("Points")
plt.ylim(0,250000)
plt.grid(True)
plt.show()


# In[41]:


c_years6 = WNBA_data["Age"]
X6 = c_years6.iloc[0:50]


# In[42]:


PT6 = WNBA_data["BS"]
Y6 = PT6.iloc[0:50]


# In[43]:


# plt.scatter(X6, Y6, color = "blue", alpha = 0.5)


# plt.title("Age & Base Salary WNBA")
# plt.ylabel("Salary ($)") 
# plt.xlabel("Age")
# plt.ylim(0,250000)
# plt.grid(True)
# plt.show()


# In[44]:


NBA1 = NBA_2019_2020.append([NBA_2020_2021, NBA_2021_2022, NBA_2022_2023], ignore_index=True)

#  df3.set_axis(["Year", "Player","Team", "Position", "Age", "Contract", "BS", "GP", "MPG", "FG%", "FT%", "3PM", "RPG", "APG", "STPG", "BLKPG", "TOPG", "PTS"
#  ],axis = 1)

NBA1.fillna("", inplace = True)

NBA1.head(200)


# In[45]:


c_years7 = NBA1["STPG"]
STPG = c_years7.iloc[0:200]


# In[46]:


PT7 = NBA1["BS"]
BS = PT7.iloc[0:200]


# In[47]:


def LinearRegression(x_data,y_data,x_lbl,y_lbl,lbl_pos,ifig):
  
   (slope, intercept, rvalue, pvalue, stderr) = linregress(x_data, y_data)
   print(f"The r-squared is: {rvalue}")
   regress_values = x_data * slope + intercept
   equation = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

   plt.scatter(x_data,y_data)
   plt.xlabel(x_lbl)
   plt.ylabel(y_lbl)
   plt.plot(x_data,regress_values,"r-")
   plt.annotate(equation,lbl_pos,fontsize=12,color="red")
   


# In[48]:


x_lbl = "STPG" 
y_lbl = "BS"
plt.title("Steals & Base Salary NBA 2022-2023")

lbl_pos = (1,10000000)
LinearRegression(NBA_2022_2023[x_lbl],NBA_2022_2023[y_lbl],x_lbl,y_lbl,lbl_pos,5)
plt.ylim(0,60000000)
plt.xlabel("Steals per game")
plt.ylabel("Salary ($ tens of millions)") 
plt.grid()
plt.show()


# In[49]:


c_years8 = NBA1["PTS"]
PTS = c_years8.iloc[0:200]


# In[50]:


PT8 = NBA1["BS"]
BS = PT8.iloc[0:200]


# In[51]:


def LinearRegression(x_data,y_data,x_lbl,y_lbl,lbl_pos,ifig):
  
   (slope, intercept, rvalue, pvalue, stderr) = linregress(x_data, y_data)
   print(f"The r-squared is: {rvalue}")
   regress_values = x_data * slope + intercept
   equation = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

   plt.scatter(x_data,y_data)
   plt.xlabel(x_lbl)
   plt.ylabel(y_lbl)
   plt.plot(x_data,regress_values,"r-")
   plt.annotate(equation,lbl_pos,fontsize=12,color="red")


# In[52]:


x_lbl = "PTS"
y_lbl = "BS"
plt.title("Points & Base Salary NBA 2022-2023")

lbl_pos = (12,10000000)
LinearRegression(NBA_2022_2023[x_lbl],NBA_2022_2023[y_lbl],x_lbl,y_lbl,lbl_pos,5)
plt.ylim(0,60000000)
plt.xlabel("Points per game")
plt.ylabel("Salary ($ tens of millions)") 
plt.grid()
plt.show()


# In[165]:


WNBA1 = WNBA_2019.append([WNBA_2020, WNBA_2021, WNBA_2022, WNBA_2023], ignore_index=True)

WNBA1.fillna("", inplace = True)

#WNBA1.head(250)


# In[54]:


c_years9 = WNBA1["PTS"]
PTS = c_years9.iloc[0:250]


# In[55]:


PT9 = WNBA1["BS"]
BS = PT9.iloc[0:200]


# In[56]:


def LinearRegression(x_data,y_data,x_lbl,y_lbl,lbl_pos,ifig):
  
   (slope, intercept, rvalue, pvalue, stderr) = linregress(x_data, y_data)
   print(f"The r-squared is: {rvalue}")
   regress_values = x_data * slope + intercept
   equation = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

   plt.scatter(x_data,y_data)
   plt.xlabel(x_lbl)
   plt.ylabel(y_lbl)
   plt.plot(x_data,regress_values,"r-")
   plt.annotate(equation,lbl_pos,fontsize=12,color="red")


# In[57]:


x_lbl = "PTS"
y_lbl = "BS"
plt.title("Points & Base Salary WNBA 2023")

lbl_pos = (6,70000)
LinearRegression(WNBA_2023[x_lbl],WNBA_2023[y_lbl],x_lbl,y_lbl,lbl_pos,5)
plt.ylim(0,350000)
plt.xlabel("Points per game")
plt.ylabel("Salary ($ hundreds of thousands)") 
plt.grid()
plt.show()


# In[58]:


c_years9 = WNBA1["STL"]
PTS = c_years9.iloc[0:250]


# In[59]:


PT9 = WNBA1["BS"]
BS = PT9.iloc[0:200]


# In[60]:


def LinearRegression(x_data,y_data,x_lbl,y_lbl,lbl_pos,ifig):
  
   (slope, intercept, rvalue, pvalue, stderr) = linregress(x_data, y_data)
   print(f"The r-squared is: {rvalue}")
   regress_values = x_data * slope + intercept
   equation = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

   plt.scatter(x_data,y_data)
   plt.xlabel(x_lbl)
   plt.ylabel(y_lbl)
   plt.plot(x_data,regress_values,"r-")
   plt.annotate(equation,lbl_pos,fontsize=12,color="red")


# In[61]:


x_lbl = "STL"
y_lbl = "BS"
plt.title("Steals & Base Salary WNBA 2023")

lbl_pos = (0.5,100000)
LinearRegression(WNBA_2023[x_lbl],WNBA_2023[y_lbl],x_lbl,y_lbl,lbl_pos,5)
plt.ylim(0,350000)
plt.xlabel("Steals per game")
plt.ylabel("Salary ($ hundreds of thousands)") 
plt.grid()
plt.show()

