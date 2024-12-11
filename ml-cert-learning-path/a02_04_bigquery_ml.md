## Create a model

Make sure to create a dataset named `bqml_tutorial` in the US region.

- `species`: Species of penguin (STRING)
- `island`: Island that the penguin lives on (STRING)
- `culmen_length_mm`: Length of culmen in millimeters (FLOAT64)
- `culmen_depth_mm`: Depth of culmen in millimeters (FLOAT64)
- `flipper_length_mm`: Length of the flipper in millimeters (FLOAT64)
- `sex`: The sex of the penguin (STRING)

```sql
CREATE OR REPLACE MODEL `bqml_tutorial.penguins_model`
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['body_mass_g']) AS
SELECT
  *
FROM
  `bigquery-public-data.ml_datasets.penguins`
WHERE
  body_mass_g IS NOT NULL
```

**With enabling global explain**

```sql
-- // create
CREATE OR REPLACE MODEL bqml_tutorial.penguins_model_global
OPTIONS
  (model_type='linear_reg',
  input_label_cols=['body_mass_g'],
  enable_global_explain=TRUE) AS
SELECT
  *
FROM
  `bigquery-public-data.ml_datasets.penguins`
WHERE
  body_mass_g IS NOT NULL

-- // evaluate
SELECT
*
FROM
ML.GLOBAL_EXPLAIN(MODEL `bqml_tutorial.penguins_model_global`)
```

## Evaluate Model

```sql
SELECT
  *
FROM
  ML.EVALUATE(MODEL `bqml_tutorial.penguins_model`,
    (
    SELECT
      *
    FROM
      `bigquery-public-data.ml_datasets.penguins`
    WHERE
      body_mass_g IS NOT NULL))
```

## Predict Model

```sql
SELECT
  *
FROM
  ML.PREDICT(MODEL `bqml_tutorial.penguins_model`,
    (
    SELECT
      *
    FROM
      `bigquery-public-data.ml_datasets.penguins`
    WHERE
      body_mass_g IS NOT NULL
      AND island = "Biscoe"))
```

```sql
SELECT
  *
FROM
  ML.EXPLAIN_PREDICT(MODEL `bqml_tutorial.penguins_model`,
    (
    SELECT
      *
    FROM
      `bigquery-public-data.ml_datasets.penguins`
    WHERE
      body_mass_g IS NOT NULL
      AND island = "Biscoe"),
    STRUCT(3 as top_k_features))
```

```sql

```
