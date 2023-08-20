create or replace table `hanz-hub.cosmart.session_ga_complete` as
select A.*
    ,B.session_id
    -- ,if(event_action_clean like '%SEARCH%',split(Event_Label,':')[offset(0)],'-')
    ,if(event_action_clean like '%SEARCH%',
        ifnull(REGEXP_EXTRACT(
                    REGEXP_EXTRACT(Event_Label,r'\:(.*)'),
                r'(.*)Not Found'),
                        REGEXP_EXTRACT(Event_Label,
                            r'\:(.*)')), null) search_keyword

    ,if(event_action_clean like '%APPLY_COUPON%', REGEXP_EXTRACT(Event_Label,
                            r'\:(.*)'),null) coupon_code

    ,if(event_action_clean = 'SEARCH',1,0) is_search_event
    ,if(event_action_clean = 'SEARCH_NOT_FOUND',1,0) is_search_not_found_event
    ,if(event_action_clean = 'APPLY_COUPON_SUCCESS',1,0) is_apply_coupon_success
    ,if(event_action_clean = 'APPLY_COUPON_FAILED',1,0) is_apply_coupon_failed

from `hanz-hub.cosmart.session_ga_clean` A
left join `hanz-hub.cosmart.session_id_list` B
    on A.event_id = B.event_id
order by rand()