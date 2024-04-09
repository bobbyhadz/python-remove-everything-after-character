# Remove everything Before or After a Character in Python

my_str = 'bobby!hadz!com'

separator = '!'

result = my_str.split(separator, 1)[0]
print(result)  # 👉️ 'bobby'