# Write your MySQL query statement below

SELECT 
    user_id, 
    name, 
    mail
FROM Users
WHERE REGEXP_like (mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$', 'c');

-- SELECT user_id, name, mail
-- FROM Users
-- WHERE mail LIKE '[a-zA-Z]%@leetcode.com'
--   AND mail NOT LIKE '%[^a-zA-Z0-9_.@-]%'
--   AND LEN(mail) - LEN(REPLACE(mail, '@', '')) = 1;