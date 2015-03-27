def matrix():
    m = rand_matrix(1024, 1024)
    a = inv(m)
    
    m = rand_matrix_n(1024, 1024)
    b = inv(m)
    
    z = a * b
    
    return z

