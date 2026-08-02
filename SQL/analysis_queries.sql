USE REATAISALES;
GO

SELECT COUNT(*) AS TotalRows
FROM dbo.Cleaned_Superstore;

SELECT TOP 10 *
FROM dbo.Cleaned_Superstore;

select sum(Sales) as TotalSales From dbo.Cleaned_Superstore;
select top 5 * from dbo.Cleaned_Superstore;
select sum(Profit) as TotalProfit From dbo.Cleaned_Superstore
select 
count(Order_ID) as TotalOrders from dbo.Cleaned_Superstore
SELECT
    COUNT(distinct Customer_ID) AS TotalCustomers
FROM dbo.Cleaned_Superstore;

select Region,sum(Sales) as TotalSales
from dbo.Cleaned_Superstore
group by Region
order by TotalSales desc;

select top 10 Customer_Name,sum(Sales) as TotalSales from dbo.Cleaned_Superstore 
group by Customer_Name order by TotalSales desc

select top 10 Product_Name, sum(Sales) as TotalSales from dbo.Cleaned_Superstore
group by Product_Name order by TotalSales desc;

select Category,
sum(Sales) as TotalSales,
sum(Profit) as TotalProfit
from dbo.Cleaned_Superstore
group by Category
Order by TotalSales desc;

SELECT
    Sub_Category,
    SUM(Sales) AS TotalSales
FROM dbo.Cleaned_Superstore
GROUP BY Sub_Category
ORDER BY TotalSales DESC;


SELECT
    Order_Year,
    Order_Month,
    SUM(Sales) AS TotalSales
FROM dbo.Cleaned_Superstore
GROUP BY
    Order_Year,
    Order_Month,
    Order_Month_No
ORDER BY
    Order_Year,
    Order_Month_No;

SELECT
    Region,
    SUM(Sales) AS TotalSales
FROM dbo.Cleaned_Superstore
GROUP BY Region
ORDER BY TotalSales DESC;