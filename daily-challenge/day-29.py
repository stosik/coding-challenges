# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.

class RunLenghtCoder:
  @staticmethod
  def encode(message):
    if message == None or not message or len(message) == 1:
      return message

    count = 1
    encoded_message = ''

    for i in range(1, len(message)):
      if(message[i] == message[i - 1]):
        count += 1
      else:
        if count > 1:
          encoded_message += str(count)
        encoded_message += message[i - 1]
        count = 1
    
    if count > 1:
      encoded_message += str(count)
    encoded_message += message[i - 1]

    return encoded_message

  @staticmethod
  def decode(message):
    decode = ''
    count = ''
    for char in message:
      if char.isdigit():
        count += char
      else:
        decode += char * int(count)
        count = ''
    return decode


def solution(message):
  encoded_message = RunLenghtCoder.encode(message)
  print(encoded_message)
  decoded_message = RunLenghtCoder.decode(encoded_message)
  print(decoded_message)

print(solution('AAAABBBCCDAA'))