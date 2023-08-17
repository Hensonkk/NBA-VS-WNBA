# Project-Group-4

## Project Title: NBA vs WNBA

## Libraries & Tools Used
Pandas, Matplotlib, numpy, scipy.stats

## Project Overview
Base question: Why is the NBA more successful than the WNBA?

•           Do NBA players have better stats than WNBA players? (Stats: Field goals, Free throw percentage, Free throws, 2 Pointers, 3 three points, Steals, Assists, Rebounds)

•           Does the NBA receive or spend more money than the WNBA? (Sales, Marketing, player salaries)

•           Does the NBA have more viewership or attendance than the WNBA? Does the NBA have better timeslots?

•           Does the NBA have better sponsorship than the WNBA? Does team ownership have an impact on the leagues?

•           Who are the highest and lowest paid players in the NBA and WNBA? Are there any notable differences between the players?

•           Are there differences between contracts in the NBA and the WNBA?

NBA Teams: Atlanta Hawks, Chicago Bulls, Dallas Mavericks, Golden State Warriors, Indiana Pacers, Los Angeles Lakers, Minnesota Timberwolves, New York Knicks, Oklahoma City Thunder and Phoenix Suns

WNBA Teams: Atlanta Dream, Chicago Sky, Dallas Wings, Indiana Fever, Los Angeles Sparks, Las Vegas Aces, Minnesota Lynx, New York Liberty, Phoenix Mercury, Seattle Storm

## Project Intro


## Data Pre-Processing/Gathering Steps
Much of the NBA data was found on the NBA official website, ESPN, or the team websites, however information was much harder to find for the WNBA so many of us collected our own data from other sources.

### Player Stats
Infromation on player statistics for NBA & WNBA teams were gathered from NBA.com and WNBA.com. We created datasets using the statistics from 2019-2023 of 10 teams and their starting 5 or their 5 best players. Teams were decided by cities with both NBA and WNBA teams. Datasets were then cleaned and reorganized based apon different avenues of how we wanted to analyze the data. 

### Sales/Marketing
Information for sales and marketing were not publicly available and easily accessible. We generated the data by finding sources that expressed the revenues and marketing of both the NBA and WNBA. Limited amount of information about those were available online so we worked with what little data we could find. Created our own datasets and then manipulated the data to analyze. 


### Viewership/Attendance
Information on the average attendance for NBA home games and away games are organized on the ESPN website, so a dataset was created using those numbers. Since that does not exist for the WNBA, attendance numbers were pulled from the game notes of individual teams' websites (hosted by the WNBA website). Not all teams provide game notes, and not all of those notes provide the same information, so the resulting dataset wasn't as complete as the NBA data.

Since the datasets were not formed by an outside party, there was very little cleaning to do, however rows were sometimes dropped if they did not contain pertinent information.

### Sponsorship
Sponsorship information for NBA and WNBA teams is focused on the sponsorship gained from arena naming rights to more easily quantify the data. Because this information is not readily available to the public from a single source, a dataset was created for the data gathered across multiple sites. Not all sites contained the amount paid for the sponsorships, or were missing parts of other relevant data pertaining to the sponsorship in question. This made the resulting dataset not as complete as it could be if the information was readily available.

Since the datasets were formed by a outside party, much cleaning had to be done. However, rows were still dropped due to the aformentioned missing data.

### Salaries
Salary information for the NBA was gathered from NBA official website, however WNBA salary information was easier to access from spotrac.com. Two different csv files were created, one to hold NBA Salary information and another for the WNBA salary information. Each file included the top 5 best paid players for 10 different teams from the years 2019 - 2023. In order to analyze the top 10 best paid players, data cleaning had to be done to drop duplicates since those players repeat constantly. 

Although the salary information and resulting graphs provided a clear picture of the discrepancy between NBA's players' salaries and WNBA's players' salaries, a greater sample data including the least paid players would present accurate results. 

### Player Contracts
The contract information was gathered from multiple sources: ESPN.com, NBA.com, WNBA.com, Spotrac.com and various articles. Please see references. I made the files in the Contract folder which includes all csvs, Excel documents and Jupyter notebook workbook. I also found half of the statistics used in the NBA and WNBA player stats for 2021-2023. The imports I used were: matplotlib.pyplot, pandas, numpy, scipy.stats.  Much of the information I found focused on the player's salary and statistics. For my bar chart analysis, I looked at the top 5 Rookie season contracts for 2023 and the top 5 Max contracts for 2022-2023 for each league. For my regression lines, I analyzed data from the players who had the largest salaries in each league. The data I examined for both were points per game vs base salaries and steals per game vs base salaries. I wanted to do more analysis, but I was running out of time and some of the data that I needed was not available. I found stronger correlations with the women's regressions. I will continue to work on this project and see how I can improve. 

###Additional Explanations
Player Statistics​

WNBA games are 8 mins shorter than NBA games​

NBA season is twice as long as WNBA season​

30 NBA teams, but only 12 WNBA teams​

Attendance​

When not using the same venues, WNBA venues have a much smaller capacity so there is less rooms for fans to begin with​

Sponsorships​

WNBA’s Minnesota Lynx & Minnesota Timberwolves Target sponsorship has a 3-5 year annual renewal. It’s the longest running naming rights contract between a sponsor and team, having started in 1990.​

Barclays Bank WNBA’s NY Liberty was renegotiated from $400 million to $200 million in aftermath of the 2008 market crash.​

Player Contracts​

An NBA player makes between $60K and $175K on a 10 day contract. On a 7 day contract WNBA players make up to $62,825​

Average age in the NBA is between 20-25, while in the WNBA it is 27​

Average career length in the NBA is 4.5 years; in the WNBA it is 3.5 years​

Sales & Marketing​

NBA is 77 years old, WNBA is 27 years old​

NBA owned the whole WNBA until 2002​

NBA owns 50% of WNBA, other 50% is owned by the 12 WNBA teams​

50% of NBA revenue is shared with teams & players, 20% of WNBA revenue is shared with teams and players​

WNBA started fund raising in order to help increase revenue



###Major Findings
Player Statistics​

Top WNBA players perform just as well as top NBA players, and some perform better​

NBA teams outperform WNBA teams in almost every statistical metric​

Attendance​

WNBA attendance is generally lower and less predictable than NBA attendance​

Sponsorships​

2021 is the year that new naming rights sponsorships for the NBA and WNBA began the most​

The New York Knicks is one of the three(?) remaining teams without a stadium name sponsor in the NBA​

Player Contracts​

WNBA player salaries are limited by a far lower team salary than when compared to the NBA​

NBA players have better base salaries than WNBA players, despite some WNBA players performing better in certain metrics​

Years of experience make a significant impact on salary in both leagues​

Sales & Marketing​

WNBA is subsidized by NBA. The NBA sponsors the WNBA with ~$15 million dollars/year​

WNBA has never made a profit, looses ~$10 million on average​

WNBA players opted out of their CBA (Collective Bargaining Agreement) early because they want full transparency of league financials​

WNBA is expected to have ~$200 million in revenue this year, more than 3x their average revenue




###Limitations and Future Development
Player Statistics​

Difference in season length and game length creates an uneven statistical comparison​

Uneven number of teams and players between the NBA and WNBA (NBA has 15 roster spots, WNBA has 12 roster spots)​

Attendance​

Lack of accessible datasets for WNBA, uneven reporting by teams​

Lack of centralized viewership data​

Sponsorships​

Lack of publicly available NBA & WNBA financial breakdowns​

Only found ranges and estimates of sponsorship costs, no concrete data​

Salaries​

Some players were traded within the season making it hard to find a complete roster for the season and changing the player's salary​

Player Contracts​

Unable to find and read actual player contracts. Limited to generally known information and statistics​

Lack of data on certain players. Possibly due to injuries, travel, hardships, personal matters, etc.​

Multiple sources of information with similar or different sets of data​

Sales & Marketing​

Lack of publicly available NBA & WNBA revenue and financial breakdowns​

Can only find averages for WNBA revenue breakdowns, no real concrete data​

Lack of data for WNBA teams and their individual revenue and operating cost




###References 
​

https://www.espn.com/​

https://www.statista.com/​

https://www.sportsmediawatch.com/2013/03/espn-wnba-reach-new-10-year-rights-deal/​

https://www.forbes.com/?sh=7c3b2c992254​

www.spotrac.com​

https://www.forbes.com/sites/justinbirnbaum/2023/06/22/2023-nba-draft-projected-contracts-for-victor-wembanyama-and-other-first-round-picks/?sh=7ca731f43a34 ​

WNBA CBA and Salary Cap Explained | Statistics, Ranks, Game Logs and more Women's Basketball Insight from Her Hoop Stats​

WNBA Salary Cap 2023: What You Need to Know - Boardroom​

WNBA's new labor deal hikes average salary to $130,000, provides paid maternity leave - CBS News​

WNBA news: Takeaways from the WNBA salary database (highposthoops.com)​

2023 NBA salary cap tracker by team: From healthy to disastrous (sportsnaut.com)​

NBA Minimum Salaries For 2023/24 | Hoops Rumors​

Salary cap set at $112.4 million for 2021-22 season | NBA.com​

NBA Salary Cap set at $109.14 million for 2019-20 | NBA.com​

2023 NBA 10-day contract explained: How it works and salary limits | Marca​

https://www.nba.com/​

https://www.wnba.com/
