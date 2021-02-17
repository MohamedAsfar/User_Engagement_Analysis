# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ##Project for a B2B professional services company 

# COMMAND ----------

# MAGIC %md ## Task 1
# MAGIC #### Has user activity or engagement dropped, increased or remained stable? What is the extent of change in user activity/engagement?

# COMMAND ----------

# MAGIC %md 
# MAGIC ##### First let us check the duration of the dataset

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT min(occurred_at), max(occurred_at) FROM events

# COMMAND ----------

# MAGIC %md ##### Since the data is for four months (from May to August), let us plot total user engagement per day, week and month for the entire dataset

# COMMAND ----------

# MAGIC %sql
# MAGIC -- by day
# MAGIC SELECT
# MAGIC    to_date(occurred_at) as date,
# MAGIC    COUNT (*) as total_engagement 
# MAGIC FROM
# MAGIC    events
# MAGIC WHERE
# MAGIC    event_type = 'engagement' 
# MAGIC GROUP BY
# MAGIC    to_date(occurred_at) 
# MAGIC ORDER BY
# MAGIC    to_date(occurred_at)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- by week
# MAGIC SELECT
# MAGIC    EXTRACT(week from occurred_at) as week,
# MAGIC    COUNT (*) as total_engagement 
# MAGIC FROM
# MAGIC    events
# MAGIC WHERE
# MAGIC    event_type = 'engagement' 
# MAGIC GROUP BY
# MAGIC    week 
# MAGIC ORDER BY
# MAGIC    week

# COMMAND ----------

# MAGIC %sql
# MAGIC -- by month
# MAGIC SELECT
# MAGIC    EXTRACT(month from occurred_at) as month,
# MAGIC    COUNT (*) as total_engagement 
# MAGIC FROM
# MAGIC    events 
# MAGIC WHERE
# MAGIC    event_type = 'engagement' 
# MAGIC GROUP BY
# MAGIC    month 
# MAGIC ORDER BY
# MAGIC    month

# COMMAND ----------

# MAGIC %md #### Few Initial Observations
# MAGIC   - We can see that there is a decline is user engagement over the weekends, which is expected because very few people would be working over the weekend
# MAGIC   - We also see a visible decline in user engagement starting from August

# COMMAND ----------

# MAGIC %md #### Given the above obervations, let us analyze the engagement difference week over week and month over month

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Analyzing engagement difference by week
# MAGIC WITH weekly_engagement AS 
# MAGIC (
# MAGIC    SELECT
# MAGIC       EXTRACT(week from occurred_at) AS week,
# MAGIC       COUNT (*) as total_engagement 
# MAGIC    FROM
# MAGIC       events
# MAGIC    WHERE
# MAGIC       event_type = 'engagement' 
# MAGIC      AND occurred_at > '2014-05-05' 
# MAGIC    GROUP BY
# MAGIC       1 
# MAGIC    ORDER BY
# MAGIC       1
# MAGIC ),
# MAGIC engagement_previous AS 
# MAGIC (
# MAGIC    SELECT
# MAGIC       week,
# MAGIC       total_engagement,
# MAGIC       LAG(total_engagement, 1) OVER ( 
# MAGIC    ORDER BY
# MAGIC       week ) previous_week_engagement 
# MAGIC    FROM
# MAGIC       weekly_engagement 
# MAGIC )
# MAGIC SELECT
# MAGIC    week,
# MAGIC    total_engagement,
# MAGIC    CASE WHEN previous_week_engagement IS NULL THEN 0 ELSE 100*(total_engagement - previous_week_engagement) / previous_week_engagement END as engagement_difference 
# MAGIC FROM
# MAGIC    engagement_previous

# COMMAND ----------

# MAGIC %md - We can see that the engagement dropped by almost 22% week over week in the first week of August which seems like an anomaly compared to the rest of the weeks

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Analyzing engagement difference month over month
# MAGIC WITH monthly_engagement AS 
# MAGIC (
# MAGIC    SELECT
# MAGIC       EXTRACT(month from occurred_at) AS month,
# MAGIC       COUNT (*) as total_engagement 
# MAGIC    FROM
# MAGIC       events 
# MAGIC    WHERE
# MAGIC       event_type = 'engagement'  
# MAGIC    GROUP BY
# MAGIC       1 
# MAGIC    ORDER BY
# MAGIC       1
# MAGIC ),
# MAGIC engagement_previous AS 
# MAGIC (
# MAGIC    SELECT
# MAGIC       month,
# MAGIC       total_engagement,
# MAGIC       LAG(total_engagement, 1) OVER ( 
# MAGIC    ORDER BY
# MAGIC       month ) previous_month_engagement 
# MAGIC    FROM
# MAGIC       monthly_engagement 
# MAGIC )
# MAGIC SELECT
# MAGIC    month,
# MAGIC    total_engagement,
# MAGIC    CASE WHEN previous_month_engagement IS NULL THEN 0 ELSE 100*(total_engagement - previous_month_engagement) / previous_month_engagement END as engagement_difference 
# MAGIC FROM
# MAGIC    engagement_previous

# COMMAND ----------

# MAGIC %md #### Final Findings
# MAGIC 
# MAGIC - User activity saw a sharp decline in the month of August (by almost 25%)
# MAGIC - User activity remained almost stable for first three months with a slight drop in the second month
# MAGIC - The extent of change was normal for the first three months while for last two months the extent of change was quite sharp

# COMMAND ----------

# MAGIC %md ## Task 2
# MAGIC #### Are there any changes in the three stages of the emails funnel? What changes have you discovered? (Please search online for terms such as sales funnel, marketing funnel to understand the funnel concept).

# COMMAND ----------

# MAGIC %md #### ANSWER FOR TASK 2
# MAGIC ##### First let us plot the count of each email action

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC    action,
# MAGIC    COUNT(*) as num_events 
# MAGIC FROM
# MAGIC    emails 
# MAGIC GROUP BY
# MAGIC    action 
# MAGIC ORDER BY
# MAGIC    num_events DESC

# COMMAND ----------

# MAGIC %md ##### Now, let us analyze the drop in user actions for each funnel

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH email_actions AS 
# MAGIC (
# MAGIC    SELECT
# MAGIC       action,
# MAGIC       COUNT(*) as num_events 
# MAGIC    FROM
# MAGIC       emails 
# MAGIC    GROUP BY
# MAGIC       action 
# MAGIC    ORDER BY
# MAGIC       num_events DESC 
# MAGIC )
# MAGIC ,
# MAGIC funnel AS 
# MAGIC (
# MAGIC    SELECT
# MAGIC       action,
# MAGIC       num_events,
# MAGIC       LAG(num_events, 1) OVER ( 
# MAGIC    ORDER BY
# MAGIC       num_events DESC) previous_action_events 
# MAGIC    FROM
# MAGIC       email_actions 
# MAGIC )
# MAGIC SELECT
# MAGIC    action,
# MAGIC    num_events,
# MAGIC    100*num_events / (
# MAGIC    SELECT
# MAGIC       MAX(num_events) 
# MAGIC    FROM
# MAGIC       funnel) AS overall_conversion,
# MAGIC       100*(num_events) / previous_action_events AS stage_conversion 
# MAGIC    FROM
# MAGIC       funnel

# COMMAND ----------

# MAGIC %md #### Findings
# MAGIC - The percentage change in the change in the email funnel is seen in the table above
# MAGIC - The overall_conversation shows the percentage change with respect to the sent_weekly_digest while the stage_conversation shows the percentage change with respect to the previous stage of the funnel
# MAGIC - From the data we can say that if the email is sent to 100 people then around 35% of them opens the email while 15% of the people clicks on the links followed by 6% of the users sent the reengagement email. 
# MAGIC - So yes there is lot of changes in the three stages of the funnel

# COMMAND ----------

# MAGIC %md ## Task 3
# MAGIC 
# MAGIC #### Are changes in user activity/engagement associated with specific devices or hardware ( mobile phone, tablet computers, desktop computers, etc.)  that customers use to read emails and interact with Zilto’sweb portal?

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH emails AS
# MAGIC (
# MAGIC    SELECT
# MAGIC       *,
# MAGIC       to_date(occurred_at) AS date,
# MAGIC       EXTRACT(month FROM occurred_at) AS month 
# MAGIC    FROM
# MAGIC       emails emails
# MAGIC )
# MAGIC ,
# MAGIC events AS
# MAGIC (
# MAGIC    SELECT
# MAGIC       user_id,
# MAGIC       to_date(occurred_at) AS date,
# MAGIC       device,
# MAGIC       EXTRACT(month FROM occurred_at) AS month 
# MAGIC    FROM
# MAGIC       events
# MAGIC    ORDER BY
# MAGIC       user_id ASC
# MAGIC )
# MAGIC SELECT
# MAGIC    CASE
# MAGIC       WHEN
# MAGIC          device IN 
# MAGIC          (
# MAGIC             'amazon fire phone',
# MAGIC             'nexus 10',
# MAGIC             'iphone 5',
# MAGIC             'nexus 7',
# MAGIC             'iphone 5s',
# MAGIC             'nexus 5',
# MAGIC             'htc one',
# MAGIC             'iphone 4s',
# MAGIC             'samsung galaxy note',
# MAGIC             'nokia lumia 635',
# MAGIC             'samsung galaxy s4'
# MAGIC          )
# MAGIC       THEN
# MAGIC          'Mobile' 
# MAGIC       WHEN
# MAGIC          device IN 
# MAGIC          (
# MAGIC             'ipad mini', 'samsung galaxy tablet', 'kindle fire', 'ipad air'
# MAGIC          )
# MAGIC       THEN
# MAGIC          'Tablet' 
# MAGIC       WHEN
# MAGIC          device IN 
# MAGIC          (
# MAGIC             'dell inspiron notebook', 'macbook pro', 'asus chromebook', 'windows surface', 'macbook air', 'lenovo thinkpad', 'mac mini', 'acer aspire notebook'
# MAGIC          )
# MAGIC       THEN
# MAGIC          'Laptops' 
# MAGIC       WHEN
# MAGIC          device IN 
# MAGIC          (
# MAGIC             'dell inspiron desktop', 'acer aspire desktop', 'hp pavilion desktop'
# MAGIC          )
# MAGIC       THEN
# MAGIC          'Desktops' 
# MAGIC       ELSE
# MAGIC          'Unknown' 
# MAGIC    END
# MAGIC    AS device_type, 
# MAGIC    emails.month, 
# MAGIC    count(emails.user_id) 
# MAGIC FROM
# MAGIC    emails 
# MAGIC    LEFT JOIN
# MAGIC       events 
# MAGIC       ON emails.user_id = events.user_id 
# MAGIC       AND emails.date = events.date 
# MAGIC WHERE
# MAGIC    action = 'email_clickthrough' 
# MAGIC GROUP BY
# MAGIC    1, 2
# MAGIC ORDER BY
# MAGIC    1, 2

# COMMAND ----------

# MAGIC %md #### Findings

# COMMAND ----------

# MAGIC %md ##### Findings : 
# MAGIC - From the graph we can say that the

# COMMAND ----------

# MAGIC %md ## Task 4
# MAGIC #### Are changes in user activity/engagement associated with specific countries or regions of the world where Zilto’s  users are located?

# COMMAND ----------

# MAGIC %md #### ANSWER FOR TASK 4
# MAGIC ##### First let us analyze the number of countries/location present in the data

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(DISTINCT(location)) FROM events

# COMMAND ----------

# MAGIC %md ##### Let us plot the top 20 countries which have highest engagement overall

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT location, COUNT(*) as engagement_count FROM events GROUP BY location ORDER BY engagement_count DESC LIMIT 20

# COMMAND ----------

# MAGIC %md ### Final Findings
# MAGIC - From the bar graph we can see the top 20 countries where the user engagement is highest
# MAGIC - We can say that the user engagement is hightest in the USA which is more than 40k
# MAGIC - Following by Japan and Germany which contributes only around 1/3rd of the US users
# MAGIC - So yes we can say that the activity/engagement is accociated with the country

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT location, COUNT(*) as engagement_count FROM events GROUP BY location ORDER BY engagement_count ASC LIMIT 27

# COMMAND ----------

# MAGIC %md ### Findings
# MAGIC - In the above graph we can see the 27 countries where the user engagement was the lowest
# MAGIC - We can say that Portugal has the least user engagement followed by pakistan and Iraq

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT location, EXTRACT(week from occurred_at) AS week, COUNT (*) AS engagement_count FROM events
# MAGIC WHERE event_type = 'engagement' AND occurred_at > '2014-06-30'
# MAGIC GROUP BY 1, 2
# MAGIC ORDER BY engagement_count DESC

# COMMAND ----------

# MAGIC %md ##### Findings
# MAGIC - The major impact is the United States where the user engagement is the highest
# MAGIC - Switzerland had increased the no. of user actitivity learnierly from week 27 to 30 and then sudden decline after week 30 was seen which remained almost constant till week 35
# MAGIC - Neatherland and Spain had increased the number of user activities from 60 to 160 
# MAGIC - Austria had a linear decline in the user activity at week 28 from 180 users to 30 users
# MAGIC - Similarly Venezuela had also seen quite decline in the number of count in the user activity
# MAGIC - ALl the outher contries had somewhat up and downs in the activity but overall not caused much impact and remained stable

# COMMAND ----------

# MAGIC %md ### Business Insights from the data set. 
# MAGIC 
# MAGIC 
# MAGIC - Now that we have analyzed drop of engagement in august but we don't know what was the reason behind this drop
# MAGIC - Drop of the user engagement activity can be due to various reason such as lost of interest of the users, New better subcription avaiable at loewr cost and more benefits
# MAGIC - Changes in the agreement with respect to the subcribers of a particular country

# COMMAND ----------

# MAGIC %md ### Additional Task 
# MAGIC #### Do the answers to any of the initial questions lead you to additional questions or possibilities that should be investigated? If so, what are they and how will you address them?
# MAGIC ##### ANSWER
# MAGIC - Yes the intial questions lead to additional questions and possibility that should be investigated such as whay few countries had so less user engagement
# MAGIC - Was there a drop in the user engagement during the weekends and rise in the engagement during the week to understand this we can make two graphs and see the user engagement on weekend Vs Weekdays
# MAGIC - We can also investigate in deep why the user activity dropped in the month of August and see what are the most affecting factors associated with this drop 
# MAGIC - We can also investigate the which days are affecting the drop in the user activities in the particular country (Might be because of public holidays)
# MAGIC - We can also investigate further if the user engagement depends on the culture or language of english speaking users in that particular country
