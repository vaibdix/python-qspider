# import re
#
# s = "good day"
#
# x=re.match('g', s)
# print(x)
# print(x.start())
# print(x.end())
# print(x.group())
#
# x = re.fullmatch("good day", s)
# print(x)
#
# x = re.search("g", s)
# print(x)
#
# x = re.sub("o", '@', s, count=4)
# print(x)
#
# x = re.subn("o", '@', s, count=4)
# print(x)
#
# x = re.split("o", s, 1)
# print(x)
#
# s = "good day tHis is"
#
# x = re.findall('[A-Z]', s)
# print(x)
#
#
#
# import re
#
# # 1. Matches any number between 0-9
# a1 = "The cost of the book is Rs.100"
# digits = re.findall(r'\d', a1)
# print("Digits:", digits)
#
#
#
# # 2. Matches only lowercase letters and uppercase letters
# b2 = "hello HOW ARE YOU"
# letters = re.findall(r'[a-zA-Z]', b2)
# print("Letters:", letters)
#
#
#
# # 3. Count the number of white spaces in a given string
# c3 = "HELLO world welcome to python Hi how are you. Hi how are you"
# whitespace_count = len(re.findall(r'\s', c3))
# print("Whitespace count:", whitespace_count)
#
#
# #4
# word4 = "PYTHON12nREG567exp2"
# numbers = re.findall(r'\d+', word4)
# total_sum = sum(int(number) for number in numbers)
# print(total_sum)
#
#
#
#
#
#
# # 5. Matches everything apart from numbers between 0-9
# a5 = "The cost of the book is Rs.100"
# non_digits = re.findall(r'\D', a5)
# print("Non-digits:", ''.join(non_digits))
#
#
#
# #6.matches everything apart from "a","b","c","d"
#
# b = "abcdefghijklmnop"
# pattern = r"[^abcd]"
# matches = re.findall(pattern, b)
# print(matches)
#
#
#
#
# # 7. Matches only those characters that are digits
# word7 = "@hello12world34welcome!123"
# digits_only = re.findall(r'\d', word7)
# print("Digits only:", ''.join(digits_only))
#
#
# # 9. Extract only pincode
# s9 = "Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
# pincode = re.findall(r'\b\d{6}\b', s9)
# print("Pincode:", pincode)
#
#
# # 10.wap to print the AADHAR CARD numbers
# s="my aadhar number is 1234-4567-8910"
# pattern = r'\d{4}-\d{4}-\d{4}'
# adhar_card_numbers = re.findall(pattern, s)
# print(adhar_card_numbers)
#
#
# # 11.wap to print the pan card number
# a = "my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
# pattern = r'\b[A-Z]{5}\d{4}[A-Z]\b'
# pan_numbers = re.findall(pattern, a)
# print(pan_numbers)
#
#
#
#
# # 12.How to fetch the protocols
a="https://www.google.com"
#
# # o/p--->['https', 'www', 'google', 'com'] (i want first output like this )
# # o/p--->['https://www.google.com']        (second output)
#
re1 = re.findall('.+', a)
print(re1)
#
#
# a = "https://www.google.com"
pattern = r'(\w+)://(?:www\.)?([a-z]+)\.([a-z]+)\.([a-z]+)'
match = re.search(pattern, a)
print(match, a)
#
#
#
#
# file_format = [
#     "Graphic Interchange Format",
#     "Advanced Audio Coding",
#     "HyperText Markup Language",
#     "Content Management System",
#     "Windows Media,Audio",
#     "Comma Separated values"
# ]
#



import re
emails = ["test.user@company.gov","test_user@company.edu","123test-T.user@company.in","testing@company","pspider@company.in"]

matched_emails = [email for email in emails if re.match(r'\w+@\w+\.\w+', email)]
print(matched_emails)


phonenumbers = ["123-345-0987","456-9832-098","800-987-4756","080-1029384727","123-345-12","900-938-0987"]
matched_numbers = [phone for phone in phonenumbers if re.match(r'\d{3}-\d{3}-\d{4}', phone)]
print(matched_numbers)



s = "helloworld welcome to python"
s_new = s.replace(" ", "\n")
print(s_new)


s = "hello 123 mic testing 123 123"
s_new = re.sub(r'\d', '**', s)
print(s_new)


