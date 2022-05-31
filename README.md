# Kaczmarz-Cimmino

Kaczmarz and Cimmino methods are used for iterative solving of linear systems of equations:
 * **Cyclic Kaczmarz** iterates through each row.
 * **Randomized Kaczmarz** selects the row randomly by probability proportional to row's (Euclidean) norm.

      Let $ A \in \mathbb{R}^{m,n} $ the coefficient matrix and $ b \in \mathbb{R}^m $ the constant vector, $ i = k \space mod \space m $, $ k \in \mathopen[ 1,N \mathclose] $ (N = nr of iterations) then $ x^{k+1} = x^{k} + \frac{b^i-r_i^T x^k}{||r||_2^2}r_i $
                                                  
  * **Cimmino** considers all rows at once and next iteration vector represents the average value of all previously computed vectors. 
      $ x^{k+1} = x^{k} + A^T M (b-Ax^k), \space M = diag(1/(m||r_i||_2^2)) $
  
  ## Prerequisites
  
  To run the application you need to have installed the python packages from *requirements.txt*.
  
  ## Application
   Application starts by running the *gui.py* script.
   ![application screenshot](https://github.com/iodainic/Kaczmarz-Cimmino/blob/main/demo.png)
