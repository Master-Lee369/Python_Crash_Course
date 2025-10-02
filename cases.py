#Program to implement some of the python string functions and functinalities

p_name = "Sooraj"
personal_message = f"Hello {p_name}, would you like to learn some python today?"

print(personal_message)

print(p_name.upper())
print(p_name.lower())
print(p_name.title())

famous_quote = ' Albert Einstein once said "A person who never made a mistake never tried anything new"'
print(famous_quote)

author = "Albert Einstein"
quote =  "A person who never made a mistake never tried anything new"

famous_quote =  f'{author} once said "{quote}"'
print(famous_quote)

new_name = "  Ritwik  "
print("\n",new_name,"\t")
print(new_name.lstrip())
print(new_name.rstrip())
print(new_name.strip())

file_name = "python_notes.txt"

print(file_name.removesuffix(".txt"))