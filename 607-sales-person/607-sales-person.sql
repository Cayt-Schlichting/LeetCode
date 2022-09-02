# Write your MySQL query statement below
# Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".

SELECT name FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id FROM Orders 
    LEFT JOIN Company USING(com_id)
    WHERE name = 'RED');