email = input('What is your email address?: ')
start = email.index('@')+1
stop = email.rindex('.')
print(email[start:stop])
