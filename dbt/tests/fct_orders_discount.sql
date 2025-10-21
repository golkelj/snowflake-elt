select 
    * 
from 
    {{ ref('fct_orders') }} 
where 
    items_discount_amount > 0 