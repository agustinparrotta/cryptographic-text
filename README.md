# Cryptographic Text

**Exercise:**

We have a series of encrypted messages that we want to decrypt. Thanks to our intelligence service, we know that the encryption technique used is as follows. The messages only contain characters from A to Z and spaces between words, diacritical marks (accents or tilde on the Ñ) or punctuation marks are not used. Each of these characters is assigned an integer from 0 to 26 according to the following table:

Letter A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Space
Numerical Equivalent 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Then each numerical equivalent (P) of the original message is converted to another integer (C) through the affine transformation:

$$C \equiv a P + b \quad (mod 27)$$

where 'a' and 'b' are the "keys" used. Finally, the new numbers are converted to characters using the same table. Note that the previous expression is a congruence, therefore if the resulting integer after aP + b is greater than or equal to 27 (the number of characters being worked with), the character from the table whose numerical equivalent is congruent modulo 27 with the obtained value is used. On the other hand, for each character to be encrypted to a different character, it is necessary that the integer used as key 'a' be coprime with 27, that is, its only common divisor is 1.

Create a program that accepts as arguments the name of the file with the encrypted message and the values of the keys 'a' and 'b' and prints the decrypted message on the screen.
Our spies have discovered the keys used to encrypt the message in the file message_cifrado_00.txt. You can use this message to check your algorithm. The discovered keys are

a = 7, b = 25

Assuming your program is called decrypt.py an example of its invocation could be (python corresponds to python3):

$ python decrypt.py message_cifrado_00.txt 7 25
Unfortunately, for the following messages, their encryption keys are not available. Therefore, you are asked to create an algorithm that breaches the system and discovers them. To do this, consider the following observation: since each character is always transformed into the same encrypted character, you can compare its frequency of occurrence with that of an ordinary text to find a match.

You are asked to:

Create a program that calculates the frequency of occurrence of each character in the text of a file passed as an argument and saves the calculated distribution in another file. To do this, remove diacritical marks from all letters in the text and omit punctuation marks and special characters, except for the space character, which should be included in the distribution since this character is found in encrypted messages. The program should generate a figure.

Use this program to generate the frequency distribution of letter occurrences in the Spanish language using the first chapter of the novel "Don Quijote de la Mancha", which can be found in the file quijote_es.txt.

We have received information that the encrypted texts may be in languages other than Spanish. Therefore, our agents have obtained translations of this chapter in several different languages. Generate the frequency distribution of letter occurrences for English, German, and Finnish using the text in the files quijote_en.txt, quijote_de.txt, and quijote_fi.txt, respectively. Note that these languages may have diacritical marks different from those in Spanish.

To decrypt the encrypted messages, you can correspond the most frequent characters in the encrypted text with the most frequent ones in each language.

By choosing two pairs of characters considered corresponding to each other, it is possible to find the keys 'a' and 'b' by solving the following system:

\begin{align*}C1 &\equiv a P1 + b (mod 27) \\C2 &\equiv a P2 + b (mod 27)\end{align*}

where (C1,P1) and (C2,P2) are the numerical equivalents of the chosen characters.

To verify that the message has been successfully decrypted, you can calculate the frequency of occurrence of the characters in the decrypted message and calculate its correlation with each language. You can use the Pearson correlation coefficient for this, a function that can be found in the scipy module. A value greater than 0.8 should already indicate a correct decryption. This coefficient represents how close the points are to the identity line.

You are then asked to:

Modify your first program so that, if the keys 'a' and 'b' are not specified, decrypt the message using the already generated distributions of letter occurrence in different languages. The program should:
Print the decrypted message on the screen.
Print the language that best corresponds to the decrypted message on the screen.
Make a graph comparing the most frequent characters of the encrypted message with those of the corresponding language, similar to the one shown in the second figure.
Make a graph showing the correlation between the frequency of occurrence of letters in the decrypted message and that of the corresponding language, similar to the one shown in the last figure.
Use this program to decrypt the messages mensaje_cifrado_01.txt to mensaje_cifrado_09.txt.

Extras
The intelligence center wants to be able to encrypt its own messages. You are asked to create a program that takes any normal text and encrypts it using keys 'a' and 'b' passed as arguments. The returned message must be decryptable using the program from point 1 using the same keys 'a' and 'b'.
Our spies have intercepted a very peculiar message that, although known to be in Spanish, is different from the rest of the messages. It can be found in the file message_cifrado_10.txt. Can you decrypt it?
