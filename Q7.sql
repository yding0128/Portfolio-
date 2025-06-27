--Retrieve the names of the employees who work in all departments 
--with budget greater than 12 million.
--Print the output in sorted order of name.
SELECT DISTINCT Emp.ename
FROM ((Emp
INNER JOIN Works ON Emp.eid = Works.eid)
INNER JOIN Dept ON Works.did = Dept.did)
WHERE Dept.budget > 12000000
GROUP BY Emp.ename
HAVING COUNT(DISTINCT Works.did) = (SELECT COUNT(DISTINCT Dept.did)
                                    FROM Dept
                                    WHERE Dept.budget > 12000000)    
ORDER BY Emp.ename;


