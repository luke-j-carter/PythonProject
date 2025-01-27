encryptedList = []
while True:
      print("Please select your user type:\n"
      "\t1. A public user\n"
      "\t2. The owner of the keys\n"
      "\t3. Exit Program\n")
      userType = input("Enter your choice:")
      while True:
            #A public user options
            if userType == "1":
                  print("As a public user, what would you like to do?\n"
                        "\t1. Send an encrypted message\n"
                        "\t2. Authenticate a digital signature\n"
                        "\t3. Exit\n")
                  publicUserSelection = input("Enter your choice:")
                  if publicUserSelection == "1":
                        encryptedMessage = input("Enter a message:")
                        encryptedList.append(encryptedMessage)
                        print("Message encrypted and sent.")
                  elif publicUserSelection == "2":
                        print("There are no signatures to authenticate.")
                  elif publicUserSelection == "3":
                        break
                  else :
                        print("Invalid choice.")
                        quit()
            #The owner of the keys options
            elif userType == "2":
                  print("As the owner of the keys, what would you like to do?\n"
                        "\t1. Decrypt a received message\n"
                        "\t2. Digitally sign a message\n"
                        "\t3. Show the keys\n"
                        "\t4. Generate a new set of keys\n"
                        "\t5. Exit\n")
                  ownerOfTheKeysSelection = input("Enter your choice:")
                  if ownerOfTheKeysSelection == "1":
                        #Code for decrypting messages
                        print("The following messages are available:")
                        for idx, message in enumerate(encryptedList):
                              print(f"{idx+1}.\t{message}")
                        userEncryptedMessageChoice = int(input("Enter your choice:"))
                        if 1 <= userEncryptedMessageChoice <= len(encryptedList):
                              selectedMessage = encryptedList[userEncryptedMessageChoice-1]
                              print(f"You selected {userEncryptedMessageChoice}. This is the decrypted message: {selectedMessage}")
                              break
                        else :
                              break

                  if ownerOfTheKeysSelection == "2":
                        #Code to check for digital signatures
                        print("There are no signatures to authenticate.")
                  if ownerOfTheKeysSelection == "3":
                        #Display Keys
                        break
                  if ownerOfTheKeysSelection == "4":
                        #Generate a new set of keys
                        break
                  if ownerOfTheKeysSelection == "5":
                        break
                  else :
                        print("Invalid choice.")
                        quit()
            #Exit the program
            elif userType == "3":
                  quit()

            else :
                print("Invalid choice.")
                quit()
