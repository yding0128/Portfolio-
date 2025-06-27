--Retrieve the names of the employees who work in the 'Software' department 
--more than 60% of the time.
----Print the output in sorted order of name.
SELECT DISTINCT Emp.ename
FROM ((Emp
INNER JOIN Works ON Emp.eid = Works.eid)
INNER JOIN Dept ON Works.did = Dept.did)
WHERE Dept.dname = 'Software' AND Works.pct_time > 60
ORDER BY Emp.ename;