import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Caeser_Cipher
def caeser(direction, plain_text, shift_amount):
  cipher_text= ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == 'encode':
        new_positon = position + shift
      elif direction == 'decode':
        new_positon = position - shift

      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. start_text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      new_letter = alphabet[new_positon]
      cipher_text += new_letter
    else:
      cipher_text += letter

  print(f"The {direction}d text is {cipher_text}")


print(art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
to_continue = True
while to_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift% 26
  caeser(direction, text, shift)

reset = input("Do you want to try again? Type 'Yes' or 'No':\n").lower()
if reset=='no':
  to_continue = False
  print("Good Bye")