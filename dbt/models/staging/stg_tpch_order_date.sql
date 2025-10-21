-- stg_tpch_orders.sql
select 
    o_orderkey as order_key,
    o_orderdate as order_date
from 
    {{ source('tpch', 'orders') }}