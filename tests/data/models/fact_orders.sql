WITH orders AS (
    SELECT * FROM {{ source('raw', 'orders') }}
),

customers AS (
    SELECT * FROM {{ ref('dim_customer') }}
),

final AS (
    SELECT
        o.id AS order_id,
        o.customer_id,
        c.first_name,
        c.last_name,
        o.order_date,
        o.amount
    FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
)

SELECT * FROM final