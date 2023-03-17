-- 1. 주문량 3000 초과
-- 2. 주성분 과일
-- 3. 총 주문량 큰 순서대로
SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
WHERE (A.TOTAL_ORDER > 3000) AND (B.INGREDIENT_TYPE = 'fruit_based')
ORDER BY A.TOTAL_ORDER DESC;
