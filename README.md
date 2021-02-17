# User_Engagement_Analysis


---
![Tricks for Best User Experience Via E-commerce Data Entry Form](https://user-images.githubusercontent.com/68263684/108158546-623b5300-70a2-11eb-86ab-b8a49529b12b.jpg)

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Define](#Define)
- [Aim of the project](#AIM-OF-THE-PROJECT)
- [Discover](#Discover)
- [Task 1](#Task-1)
- [Task 2](#Task-2)
- [Task 3](#Task-3)
- [Task 4](#Task-4)
- [Databricks](#Databricks)

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
## Task 1 
#### Has user activity or engagement dropped, increased or remained stable? What is the extent of change in user activity/engagement?
- User Activity - Week wise 
 
![newplot (1)](https://user-images.githubusercontent.com/68263684/108164197-8f413300-70ad-11eb-9e0e-41262352238c.png)

 - User Activity - Month wise

![newplot (1)](https://user-images.githubusercontent.com/68263684/108164629-62d9e680-70ae-11eb-94ee-4b0961d64c7d.png)

- Change in user activity for each week

![newplot (3)](https://user-images.githubusercontent.com/68263684/108165261-7cc7f900-70af-11eb-8438-b648b326e7b1.png)

- Change in user activity for each month

![newplot (4)](https://user-images.githubusercontent.com/68263684/108165319-9c5f2180-70af-11eb-91cb-5f54f296368d.png)

#### Points to note:

-   The dataset contains informations of user activities for months between May and August
-   We can see that there is a decline is user engagement and it is subject tio follow a seasonal trend
-   We can see that the engagement dropped by almost 22% week over week in the first week of August which seems like an anomaly compared to the rest of the weeks
-   User activity remained almost stable for first three months with a slight drop in the second month
-   The extent of change was normal for the first three months while for last two months the extent of change was quite sharp
---
## Task 2
#### Are there any changes in the three stages of the emails funnel? What changes have you discovered? 

###### What is Email Funnel?
An email funnel is a representation of how a subscriber goes from prospective lead to a customer through educational and promotional email communications. For effective email funnels, marketers have to anticipate the subscriber's needs to send an email at the right time to elicit action.

- Number of user responded

![newplot (6)](https://user-images.githubusercontent.com/68263684/108167693-4be9c300-70b3-11eb-8ae6-b4004d71b23a.png)

- Funnel Conversion rate

![newplot (5)](https://user-images.githubusercontent.com/68263684/108167904-a71bb580-70b3-11eb-9e20-8cc255859158.png)

#### Points to note:

The percentage change in the change in the email funnel is seen in the table above
- The overall_conversation shows the percentage change with respect to the sent_weekly_digest while the stage_conversation shows the percentage change with respect to the previous stage of the funnel
- From the data we can say that if the email is sent to 100 people then around 35% of them opens the email while 15% of the people clicks on the links followed by 6% of the users sent the reengagement email.
- So yes there is lot of changes in the three stages of the funnel
---
## Task 3
#### Are changes in user activity/engagement associated with specific devices or hardware ( mobile phone, tablet computers, desktop computers, etc.) that customers use to read emails and interact with Zilto’s web portal?

- User activity/engagement associated with specific devices

![newplot (12)](https://user-images.githubusercontent.com/68263684/108168996-602ebf80-70b5-11eb-80d6-151e78f66b6c.png)



---
## Task 4
#### Are changes in user activity/engagement associated with specific countries or regions of the world where Zilto’s users are located?

- Most User activity/engagement associated with countries

![newplot (13)](https://user-images.githubusercontent.com/68263684/108169243-b1d74a00-70b5-11eb-983e-1148d2f3c058.png)

- Most User activity/engagement associated with countries

![newplot (11)](https://user-images.githubusercontent.com/68263684/108168778-16de7000-70b5-11eb-93a2-165168e14efa.png)

#### Points to note
- The major impact is the United States where the user engagement is the highest
- Switzerland had increased the no. of user actitivity learnierly from week 27 to 30 and then sudden decline after week 30 was seen which remained almost constant till week 35
- Neatherland and Spain had increased the number of user activities from 60 to 160
- Austria had a linear decline in the user activity at week 28 from 180 users to 30 users
- Similarly Venezuela had also seen quite decline in the number of count in the user activity
- ALl the outher contries had somewhat up and downs in the activity but overall not caused much impact and remained stable
---
## Databricks

[Click here to see the data analysis for the company in Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3839454205680965/632151243528397/573016260412799/latest.html)

---
[Back To The Top](#User_Engagement_Analysis)

