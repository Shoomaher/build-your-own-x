from hashlib import sha256

x = 5
y = 0

#Here "proof" is zero. In Bitcoin it is called hashcash
while (sha256(str(x*y).encode()).hexdigest()[-1] != "0"):
    y+=1

print("The solution is y = {}".format(y))