USE bank_full;

SELECT * FROM bank_full;
SELECT COUNT(*) FROM bank_full;

-- Y --
SELECT y, COUNT(*)  
FROM bank_full
GROUP BY y;

SELECT y, COUNT(*) AS total, ROUND(100*COUNT(*) / (SELECT COUNT(*) FROM bank_full),2) AS percentage
FROM bank_full
GROUP BY y;

-- ----------------------------------------------------------------------
SELECT * FROM campaign;

-- Contact --
SELECT contact, COUNT(*)
FROM campaign
GROUP BY contact;

SELECT contact, COUNT(*) AS total
FROM campaign 
GROUP BY contact
ORDER BY total DESC;

-- Day --
SELECT day, COUNT(*)  
FROM campaign
GROUP BY day;

-- Month --
SELECT month, COUNT(*)  
FROM campaign
GROUP BY month
ORDER BY month ASC;

-- Duration --
SELECT duration, COUNT(*)  
FROM campaign
GROUP BY duration;

-- Number of contacts --
SELECT number_of_contacts, COUNT(*)  
FROM campaign
GROUP BY number_of_contacts;

SELECT AVG(number_of_contacts) AS avg_contacts FROM campaign;

-- Pdays --
SELECT pdays, COUNT(*)  
FROM campaign
GROUP BY pdays;

-- Previous --
SELECT previous, COUNT(*)  
FROM campaign
GROUP BY previous;

-- Poutcome --
SELECT poutcome, COUNT(*)  
FROM campaign
GROUP BY poutcome;