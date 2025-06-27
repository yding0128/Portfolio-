--Retrieve the names of the employees who work in the 'Software' department 
--more than 60% of the time, and the 'Hardware' department more than 20% of the time.
--Print the output in sorted order of name.
SELECT Emp.ename
FROM ((Emp
INNER JOIN Works ON Emp.eid = Works.eid)
INNER JOIN Dept ON Works.did = Dept.did)
WHERE Dept.dname = 'Software' AND Works.pct_time > 60

INTERSECT

SELECT Emp.ename
FROM ((Emp
INNER JOIN Works ON Emp.eid = Works.eid)
INNER JOIN Dept ON Works.did = Dept.did)
WHERE Dept.dname = 'Hardware' AND Works.pct_time > 20
ORDER BY ename;
