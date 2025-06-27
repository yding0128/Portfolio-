--Retrieve the dids of departments with at least two employees.
--Print the output in sorted order of did.
SELECT Dept.did
FROM Dept
INNER JOIN Works ON Dept.did = Works.did
GROUP BY Dept.did
HAVING count(Works.eid) >= 2
Order By Dept.did;

