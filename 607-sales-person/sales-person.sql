# Write your MySQL query statement below
select name from SalesPerson where sales_id not in ( select sales_id from Company natural join Orders where name = 'red');