# Write your MySQL query statement below

# Write an SQL query that reports the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

# product_id | product_name | unit_price |

SELECT product_id, product_name FROM Product
WHERE product_id NOT IN (
SELECT product_id FROM Sales
WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31')
    AND product_id IN (SELECT product_id FROM sales);
