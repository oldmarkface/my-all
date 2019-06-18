import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())