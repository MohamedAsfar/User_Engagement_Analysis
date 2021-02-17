# User_Engagement_Analysis

[Click here to see the data analysis for the company in Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3839454205680965/632151243528397/573016260412799/latest.html)


---
![Tricks for Best User Experience Via E-commerce Data Entry Form](https://user-images.githubusercontent.com/68263684/108158546-623b5300-70a2-11eb-86ab-b8a49529b12b.jpg)

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Define](#Define)
- [Aim of the project](# AIM-OF-THE-PROJECT)
- [Preprocessing the data](#Preprocessing-the-data)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Machine Learning](#Machine-Learning)
- [SQL Integration](#SQL-Integration)
- [Business Insights in Tableau](#Business-Insights-in-Tableau)

---

## DEFINE

Zilto is a business-to-business professional services company that provides online services and products to support work of the employees of its customer companies. Many companies in diverse areas of business including, for example, manufacturers, producers, suppliers, retailers, transportation, and others are Zilto’s paid subscribers. Besides an annual subscription fee, variable charges are based on the extent of engagement with its products and services by the users (users are employees of customer companies).
The responsibility is to monitor user activity and engagement(whether engagement is stable, dropping, or increasing). For any changes in user engagement activity,possible sources or reasons for the changes should be identified and noted. The task at hand is to review the available data, do necessary analysis, interpret the findings and project visualizations for user engagement.

---
## AIM OF THE PROJECT

The project aims to answer the following questions:<br>
1. Has user activity or engagement dropped, increased or remained stable? What is the extent of change in user activity/engagement?<br>
2. Are there any changes in the three stages of the emails funnel? What changes have you discovered??<br>
3. Are changes in user activity/engagement associated with specific devices or hardware ( mobile phone, tablet computers, desktop computers, etc.)  that customers use to read emails and interact with Zilto’s  web portal?<br>
4. Are changes in user activity/engagement associated with specific countries or regions of the world where Zilto’s  users are located?<br>

---
## Preprocessing the data

The target column is "Absenteeism Time in Hours" . The irrelavant columns like "ID are removed from the table. For determining the absenteeism, the day and the month in which the employee is absent should be noted. This is calculated from the date column. There were 28 reasons for absence which will be broken down into 4 major categoeis based on their similarity. Reason 0 is for unknown cases. So this will act as the baseline and will be dropped to avoid multi collinearity. The resons were grouped as 

- Reason_1 grouped by diseases
- Reason_2 grouped by pregnancy issues
- Reason_3 grouped by poisoining
- Reason_4 grouped by general body issues

Now, lets focus on our target variable "Absenteeism Time in Hours". The meadian value in "Absenteeism Time in Hours" is 3 hours. So, we group them as 

- Moderately absent ( less than or equal to 3 hours -Class value 0)
- Excessively absent (greater than 3 hours - Class value 1)

---

## Exploratory Data Analysis
### Some of the striking features related to Absenteeism

- Months Vs Excessive Absenteeism

![EDA 1](https://user-images.githubusercontent.com/68263684/107476943-1897b900-6b34-11eb-8132-1f1520791d81.png)

- Days Vs Excessive Absenteeism

![EDA 2](https://user-images.githubusercontent.com/68263684/107477034-4a108480-6b34-11eb-9b3f-6f741d64733d.png)

- Distance to work

![EDA 3](https://user-images.githubusercontent.com/68263684/107477083-63193580-6b34-11eb-9861-94f452bc2a38.png)



### Points to note

- The rate Excessive Absenteeism is increses from January to December
- Employees were mostly absent during Mondays and Fridays
- As the Distance to work increase, Employees are prone to be absent

---

## Machine Learning

As the prediction Varible is classified as either Clas 0 or Class 1, Logistic Regression is used to create a Machine Learning model. There were nearly 46% Class 0's amn 54% Class 1's which shows that the dataset is almost balanced. Training and test sets were splitted based on the 80-20 ratio. The model created resulted in an accuracy of 78% which is above baseline. The results from the model are as follows:


| Feature name | 	Coefficient	| Odds_ratio | 
| ------------- | ------------- |------------- |
| Reason_3 | 	3.092102 | 	22.023327 | 
| 	Reason_1 | 	2.771512 | 	15.982778 | 
| Reason_2 | 	0.931688 | 	2.538791 | 
| 	Reason_4 | 	0.809059 | 	2.245794
| 	Transportation Expense | 	0.625055 | 	1.868348
| 	Children | 	0.357535 | 	1.429801
| 	Body Mass Index | 	0.288294 | 	1.334150
| 	Month Value | 	0.007812 | 	1.007843
| 	Age | 	-0.173903 | 	0.840378
| 	Education | 	-0.240816 | 	0.785986
| 	Pets | 	-0.273374 | 	0.760808
| Intercept | 	-1.609575 | 	0.199973

From the above table, it is clear that the Reason_3(poisoining), Reason_1 (disease), Reason_2 (pregnancy issues) are the major factors contributing for excessive absenteeism.

---
## SQL Integration

SQL is intergrated with Jupyter Notebook using the library pymysql. As an analyst, when we deal with huge amount of data, it is always better to use SQL for data manupulation rather than working in the same Jupyter Notebook where the Machine Learning model is created. The databease and a table named "predicted_outputs" is created in MYSQL workbench and the the data predicted from the machine learning model are imported via Jupyter Notebook. The table created contains all the columns including the reasons, probabilities and predicted values. These values are saved as a csv file which will be visualized in Tableau. 

![Screenshot (86)](https://user-images.githubusercontent.com/68263684/107481349-43394000-6b3b-11eb-8471-046611d8237b.png)



## Business Insights in Tableau

[Click here to see the Visualization's in Tableau](https://public.tableau.com/profile/mohamed.asfar.babul.hussain#!/vizhome/Portfolio2_16128568419720/ReasonsVSProbabilty)


---
[Back To The Top](#Employee_Absenteeism)

