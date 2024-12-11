```sql
SELECT
  date
  , airline
  , departure_airport
  , departure_schedule
  , arrival_airport
  , arrival_delay
FROM
  `bigquery-samples.airline_ontime_data.flights`
WHERE
  -- // one in 100 rows
  MOD(ABS(FARM_FINGERPRINT(date)), 100) = 0
  AND
  -- ignore 50% (500/1000=50%)
  MOD(ABS(FARM_FINGERPRINT(date)), 1000) >= 500
  AND
  -- ignore another 25% (1000-500)/2+500=750
  MOD(ABS(FARM_FINGERPRINT(date)), 1000) < 750
```
