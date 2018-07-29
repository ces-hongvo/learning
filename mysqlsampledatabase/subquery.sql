SELECT 
    lastName, firstName
FROM
    employees
WHERE
    officeCode IN (SELECT 
            officeCode
        FROM
            offices
        WHERE
            country = 'USA');

SELECT 
    customerNumber, checkNumber, amount
FROM
    payments
WHERE
    amount = (SELECT 
            MAX(amount)
        FROM
            payments);
            
SELECT 
    customerNumber, checkNumber, amount
FROM
    payments
WHERE
    amount > (SELECT 
            AVG(amount)
        FROM
            payments);

SELECT 
    customerName
FROM
    customers
WHERE
    customerNumber NOT IN (SELECT DISTINCT
            customerNumber
        FROM
            orders);
            
SELECT 
    MAX(items), MIN(items), FLOOR(AVG(items))
FROM
    (SELECT 
        orderNumber, COUNT(orderNumber) AS items
    FROM
        orderdetails
    GROUP BY orderNumber) AS lineitems;

#Correlated subquery
SELECT 
    productname, 
    buyprice
FROM
    products p1
WHERE
    buyprice > (SELECT 
            AVG(buyprice)
        FROM
            products
        WHERE
            productline = p1.productline);
            
SELECT 
    customerNumber, 
    customerName
FROM
    customers
WHERE
    EXISTS( SELECT 
            orderNumber, SUM(priceEach * quantityOrdered)
        FROM
            orderdetails
                INNER JOIN
            orders USING (orderNumber)
        WHERE
            customerNumber = customers.customerNumber
        GROUP BY orderNumber
        HAVING SUM(priceEach * quantityOrdered) > 60000);