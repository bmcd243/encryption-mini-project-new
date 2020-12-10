### vernam cipher

message_to_encrypt = "hello"

key = '@456'

message_binary = ''.join(format(ord(i), 'b') for i in message_to_encrypt)
key_binary = ''.join(format(ord(i), 'b') for i in key)

encrypted_binary = message_binary + key_binary

print (encrypted_binary)



n = 8

split_strings = []

for i in range(0, len(encrypted_binary), n):
	split_strings.append(encrypted_binary[i : i + n])


print (split_strings)

encrypted_message = []

for i in range(len(split_strings)):
	int(split_strings[i], 2)
	current = chr(int(split_strings[i], 2))
	encrypted_message.append(current)

print (encrypted_message)