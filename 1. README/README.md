# P3_Property Finder

## Executive Summary
- DML develops a Property Finder application for customers to Rent or Buy property, utilising cryptocurrency accepted transactions
- Additional goals: Connecting various learning modules learnt in course

## Main Concept
Simply pay with Cryptocurrency without additional third party involvements
Additional goals: Connecting various learning modules together learnt in course
Breakdown of tasks and roles
Administrative & Data gathering : All
Pyviz : Mark
Remix : Daniel
Streamlit : Lucis

## PyViz Charts & Data

[![image](https://raw.githubusercontent.com/Lucis-1/P3_Tokenize/main/3.%20Pyviz/Median%20Sales%20Data.png)
[![image](https://raw.githubusercontent.com/Lucis-1/P3_Tokenize/main/3.%20Pyviz/PyViz%20Plot.png)
[![image](https://raw.githubusercontent.com/aliquid-novi/HW-Projects/master/Scatter%20Median%20ppsf.png)
[![image](https://raw.githubusercontent.com/Lucis-1/P3_Tokenize/main/3.%20Pyviz/Map.png)

### Data Techniques 

**Data Source**
Variety of Real Estate Data Bases, such as private (Zillow) and public government sources. Most databases were in CSV form but however had to deal with a new type of file for larger databases called a GZ file which an unzipper was needed.

**Reason for data selection**
These data sources had the most accurate information aswell as a large variety of it.

**Collection, exploration and cleaning process**
Longest part was finding and filtering through the numerous excel, csv and gz zip files to find relevant data for the project. Once finding relevant data, converting GZ files (very large zip files, most of them 1gb +) to CSV files was the next step.
Cleaning the CSV files to find relevant data was the next part - this was the largest books I've cleaned, some books having 500,000 + rows.

## Challenges (Streamlit)
- Streamlit date time slider wouldn’t work
- Could only add one date
- Fix was to simply add the calendar, and then use
a dropdown for number of days, which is not ideal
[![image](https://github.com/Lucis-1/P3_Tokenize/blob/main/5.%20Presentation/Images/Picture1.png)

## Remix/Solidity
Use of Remix IDE
Use of a timelock with the withdraw function
This is to improve security
If time allowed would have used the 
Ownable library, which helps with exploitation
and owner attacks
[![image](https://github.com/Lucis-1/P3_Tokenize/blob/main/5.%20Presentation/Images/timelock.png)

## Streamlit
**Technologies Utilised:
- Additional Streamlit modules
- Ganache
- ABI connecting code
- testing/troubleshooting

## Successes:
- Completed Initial working prototype

