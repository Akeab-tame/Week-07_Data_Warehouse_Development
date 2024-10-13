-- Use the `ref` function to select from other models

{{config(materialized='table')}}

WITH filtered_data AS {
    SELECT *
    FROM {{source('public', 'my_table') }}
    WHERE ID > 0
}
SELECT
    Channel Title,
    Channel Username,
    ID,
    Message.
    Date,
    Media Path
FROM filtered_data