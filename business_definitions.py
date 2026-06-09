# business_definitions.py

BUSINESS_DEFINITIONS = """
Revenue =
SUM(payment.amount)

Customer Count =
COUNT(DISTINCT customer.customer_id)

Rental Count =
COUNT(DISTINCT rental.rental_id)

Film Count =
COUNT(DISTINCT film.film_id)

Store Count =
COUNT(DISTINCT store.store_id)

Average Payment =
AVG(payment.amount)

Top Customers =
SUM(payment.amount)
GROUP BY customer.customer_id

Revenue By Category =
SUM(payment.amount)
GROUP BY category.name

Top Rented Films =
COUNT(rental.rental_id)
GROUP BY film.film_id
"""