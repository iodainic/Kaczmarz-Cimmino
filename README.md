# Kaczmarz-Cimmino

Kaczmarz and Cimmino methods are used for iterative solving of linear systems of equations:
  **Cyclic Kaczmarz iterates through each row in the matrix.
  **Randomized Kaczmarz selects the rows randomly by probability proportional to row's (Euclidean) norm.
               Let $ A \in \mathbb{R}^{m,n} the coefficient matrix and  b \in \mathbb{R}^m the constant vector, 
               i = k mod m , k \in 1..N (nr of iterations),
                                                  x^{k} = x^{k+1} + \frac{b^i-r_i^T x^k}{||r||_2^2}*r_i  $
  **Cimmino considers all rows at once and next iteration vector represents the average value of all previously computed vectors. 
  

