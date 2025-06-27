--Retrieve the names of the employees who work only in departments 
--with budget less than 1 million.
--Print the output in sorted order of name.
SELECT DISTINCT Emp.ename
FROM Emp
WHERE Emp.eid NOT IN (SELECT Works.eid
                  FROM Works
                  WHERE Works.did IN (
                             SELECT Dept.did
                             FROM Dept
                             WHERE Dept.budget > 1000000))
ORDER BY Emp.ename;