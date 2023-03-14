-- 코드를 입력하세요
SELECT a.FLAVOR 
FROM FIRST_HALF as a
LEFT JOIN ICECREAM_INFO as b 
ON a.FLAVOR = b.FLAVOR 
where a.total_order > 3000 and b.INGREDIENT_TYPE LIKE 'fruit_based'
ORDER BY a.total_order desc