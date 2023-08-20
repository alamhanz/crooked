create or replace table `hanz-hub.cosmart.session_id_list` as
with
    raw_event as
        (select event_id
            ,Event_Time
            ,Client_ID
            ,Device_Category
            ,lag(Event_Time) over(partition by Client_ID, Device_Category order by event_id) Event_Time_before
        from `hanz-hub.cosmart.session_ga_clean`)

    ,raw_event_diff as
        (select *
            -- ,Event_Time
            ,datetime_diff(Event_Time, Event_Time_before, minute) time_diff_in_minutes
            ,if(datetime_diff(Event_Time, Event_Time_before, minute)>90,1,0) new_session
            ,MD5(Client_ID) client_id_md5
        from raw_event)

    ,session_temp as
        (select *
            ,sum(new_session) over(partition by Client_ID, Device_Category order by event_id) session_temp_id
        from raw_event_diff
        )

select event_id
    ,case 
        when Device_Category = 'mobile' then concat(cast(session_temp_id + 5123 as string),'+',TO_BASE64(client_id_md5))
        when Device_Category = 'desktop' then concat(cast(session_temp_id + 7432 as string),'+',TO_BASE64(client_id_md5))
        when Device_Category = 'tablet' then concat(cast(session_temp_id + 9751 as string),'+',TO_BASE64(client_id_md5))
        else concat(cast(session_temp_id + 3112 as string),'+',TO_BASE64(client_id_md5))
    end session_id
from session_temp
order by rand()
