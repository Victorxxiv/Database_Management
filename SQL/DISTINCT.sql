 SELECT DISTINCT cFirstName, cLastName, prodName
        FROM customers 
          NATURAL JOIN orders
          NATURAL JOIN orderlines
          NATURAL JOIN products
        WHERE cFirstName = 'Alvaro' AND cLastName = 'Monge'
        ORDER BY prodName;