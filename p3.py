# wapf to accept as input three numbers
# and return their sum and product

def compute(n1, n2, n3):
	r1 = n1+ n2 + n3
	r2 = n1 * n2 * n3
	return r1, r2

m1 = float(input(" enter first number "))
m2 = float(input(" enter second number "))
m3 = float(input(" enter third number "))

a1, a2 = compute(m1, m2, m3)
print("sum = ", a1)
print(" product = ",a2)