t0 = 1
t1 = 2 
t2 = 3 
t3 = 3 
t4 = 3 
t5 = 3 
t6 = 3 
t7 = 3 

# stack slots
s1 = 3
s2 = 3

s3 = s1 + s2
s2 = s3

t0 = t1
t1 = t2
t3 = t2
t4 = t1

keep_alive = t0 + t1 + t2 + t3 + t4 + t5 + t6 + t7 + s1 + s2 + s3
print keep_alive
