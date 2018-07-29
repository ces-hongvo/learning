SELECT 
    concat(e.firstName,' ', e.lastName) salesman, 
    e.jobTitle, 
    customerName
FROM
    employees e
        RIGHT JOIN
    customers c ON e.employeeNumber = c.salesRepEmployeeNumber
        AND e.jobTitle = 'Sales Rep'
ORDER BY customerName;
