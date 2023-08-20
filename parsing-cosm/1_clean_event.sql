
create or replace table `hanz-hub.cosmart.session_ga_clean` as

with
xx as
  (select *
      ,split(Event_Action,'/')[offset(0)] as event_action_focus
  from `hanz-hub.cosmart.session_ga`)

,xx2 as
  (select *
      ,replace(REGEXP_EXTRACT(replace(event_action_focus,"_"," "), 
            r'\b[A-Z]+(?:\s+[A-Z]+)*\b'),' ','_') event_action_clean
  from xx
  order by 3,2)


select 100000 + (row_number() over(order by Event_Time, Client_ID, Device_Category)) event_id
    ,cast(Client_ID as string) Client_ID
    ,* except(event_action_focus, Client_ID)
from xx2

