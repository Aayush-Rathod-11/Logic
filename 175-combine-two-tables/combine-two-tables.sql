/* Write your PL/SQL query statement below */
SELECT p.firstname, p.lastname, a.city, a.state
FROM Person p, Address a
WHERE p.personId = a.personId(+);