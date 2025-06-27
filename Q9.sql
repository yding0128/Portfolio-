--Retrieve the average salary of employees for each department.
--The output should list each department id first, 
--followed by the average salary for that department.
--Print the output in sorted order of department id. 
--(Note: to compute the average salary for each department,
--simply consider all the employees who work for it.)
SELECT Works.did, AVG(Emp.salary)
FROM Emp, Works, Dept 
WHERE Works.did = Dept.did 
AND Emp.eid = Works.eid
GROUP BY Works.did
ORDER BY did;                      


