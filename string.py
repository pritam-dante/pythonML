### Split###
# split --->  spliting a string to list

msg = "Pay attention to everyting I say"
words = msg.split()  # seperated everything based on space
# print(words)

msg = "Pay ,attention ,to ,everyting ,I ,say"
words = msg.split(', ')  # seperated everything based on comma and space
# print(words)

msg = """\ 
Pay attention \
to \
everything I
have to
say"""
# \ ignoring the new line
# words = msg.splitlines() #first method
words = msg.split('\n')
# print(words)

