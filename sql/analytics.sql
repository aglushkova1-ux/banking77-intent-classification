SELECT COUNT(*) FROM predictions;

SELECT
    predicted_class,
    COUNT(*) as count
FROM predictions
GROUP BY predicted_class
ORDER BY count DESC;

SELECT
    AVG(inference_time_ms) as avg_time,
    MIN(inference_time_ms) as min_time,
    MAX(inference_time_ms) as max_time
FROM predictions;

SELECT
    created_at::date as date,
    COUNT(*) as count
FROM predictions
GROUP BY date
ORDER BY date;

SELECT
    LENGTH(text) as query_length,
    inference_time_ms,
    predicted_class
FROM predictions
WHERE inference_time_ms IS NOT NULL
ORDER BY query_length;

SELECT
    CASE
        WHEN LENGTH(text) < 50 THEN 'SHORT'
        WHEN LENGTH(text) <= 100 THEN 'MEDIUM'
        ELSE 'LONG'
    END AS length_category,
    AVG(inference_time_ms) as avg_time,
    COUNT(*) as count_queries
FROM predictions
WHERE inference_time_ms IS NOT NULL
GROUP BY length_category;