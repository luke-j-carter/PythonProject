def clientInterface():
    encryptedList = []
    generateKeys()

    while True:
        userType = getUserType()

        if userType == "1":  # Public user
            handlePublicUser(encryptedList)
        elif userType == "2":  # Owner of keys
            handleOwnerOfKeys(encryptedList)
        elif userType == "3":  # Exit program
            print("Bye for now!")
            break
        else:
            print("Invalid choice.")


def getUserType():
    print("Please select your user type:\n"
          "\t1. A public user\n"
          "\t2. The owner of the keys\n"
          "\t3. Exit Program\n")
    return input("Enter your choice:")


def handlePublicUser(encryptedList):
    while True:
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
        else:
            print("Invalid choice.")


def handleOwnerOfKeys(encryptedList):
    while True:
        print("As the owner of the keys, what would you like to do?\n"
              "\t1. Decrypt a received message\n"
              "\t2. Digitally sign a message\n"
              "\t3. Show the keys\n"
              "\t4. Generate a new set of keys\n"
              "\t5. Exit\n")
        ownerSelection = input("Enter your choice:")

        if ownerSelection == "1":
            decryptMessage(encryptedList)
        elif ownerSelection == "2":
            print("There are no signatures to authenticate.")
        elif ownerSelection == "3":
            showKeys()
        elif ownerSelection == "4":
            generateNewKeys()
        elif ownerSelection == "5":
            break
        else:
            print("Invalid choice.")


def decryptMessage(encryptedList):
    if not encryptedList:
        print("No messages to decrypt.")
        return
    print("The following messages are available:")
    displayOptions(encryptedList)
    userEncryptedMessageChoice = int(input("Enter your choice:"))

    if 1 <= userEncryptedMessageChoice <= len(encryptedList):
        selectedMessage = encryptedList[userEncryptedMessageChoice - 1]
        print(f"You selected {userEncryptedMessageChoice}. This is the decrypted message: {selectedMessage}")
    else:
        print("Invalid choice.")


def showKeys():
    # Implement key display logic here (update the `keys` list accordingly)
    keys = ["Public Key", "Private Key"]  # Example keys
    displayOptions(keys)


def generateNewKeys():
    print("Generating a new set of keys...")
    generateKeys()


def displayOptions(options):
    for idx, option in enumerate(options):
        print(f"{idx + 1}.\t{option}")


def generateKeys():
    # Add the actual key generation logic here.
    print("Generating keys...")


clientInterface()
