create or replace table `hanz-hub.cosmart.session_summary` as
with
    raw_session as
        (select session_id
            ,Device_Category
            ,min(Event_Time) start_time
            ,max(Event_Time) end_time
            ,count(event_id) event_cnt
            ,count(distinct event_action_clean) event_action_unique
            ,sum(is_search_event) search_cnt
            ,sum(is_search_not_found_event) search_not_found_cnt
            ,safe_divide(sum(ifnull(is_search_not_found_event,0)),sum(ifnull(is_search_event,0))) search_not_found_rate
            ,sum(is_apply_coupon_success) success_coupon_cnt
            ,sum(is_apply_coupon_failed) failed_coupon_cnt
            
            ,string_agg(event_action_clean,'->' order by event_id) event_flows
        from `hanz-hub.cosmart.session_ga_complete`
        group by 1,2)


select * except(search_not_found_rate)
    ,1-if(search_not_found_rate>1,1,search_not_found_rate) search_found_rate
    ,safe_divide(success_coupon_cnt, success_coupon_cnt+failed_coupon_cnt) coupon_success_rate
    ,case
        when event_flows like '%ORDER_PROCESSED->ORDER_CREATED->PAYMENT_RECEIVED%' then 'order_created_paid'
        when event_flows like '%ORDER_PROCESSED->ORDER_CREATED%' and event_flows not like '%PAYMENT_RECEIVED%' then 'order_created_not_paid'
        when event_flows like '%ORDER_PROCESSED%' and event_flows not like '%ORDER_CREATED%' then 'order_processed' --> 2 session only
      else 'no order'
      end session_type
    ,datetime_diff(end_time, start_time, minute) session_duration_in_minutes
from raw_session
order by rand()


