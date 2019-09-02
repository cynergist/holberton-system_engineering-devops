# 0x04. Loops, conditions and parsing

## Resources
[Loops sample](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html) </br >
[Variable assignment and arithmetic](http://tldp.org/LDP/abs/html/ops.html) </br >
[Comparison operators](http://tldp.org/LDP/abs/html/ops.html) </br >
[File test operators](http://tldp.org/LDP/abs/html/comparison-ops.html) </br >
[Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html) </br >

## man or help:
- `env`
- `cut`
- `for`
- `while`
- `until`
- `if`
</br >

## Learning Objectives
- How to create SSH keys
- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
- How to use while, until and for loops
- How to use if, else, elif and case condition statements
- How to use the cut command
- What are files and other comparison operators, and how to use them

# More Info

## Shellcheck
Shellcheck is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

## Tasks

0. 0-RSA_public_key.pub // Create a SSH RSA key pair: Read for this task:

Linux and Mac OS users
Windows users
man: ssh-keygen

You will soon have to manage your own servers hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

- Share your public key in your answer file 0-RSA_public_key.pub
- Fill the SSH public key field of your intranet profile with the public key you just generated
- Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
- If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.

1. 1-for_holberton_school // For Holberton School loop: a Bash script that displays Holberton School 10 times.

Requirement:

- You must use the for loop (while and until are forbidden)

2. 2-while_holberton_school // While Holberton School loop: a Bash script that displays Holberton School 10 times.

Requirements:

- You must use the while loop (for and until are forbidden)

3. 3-until_holberton_school // Until Holberton School loop: a Bash script that displays Holberton School 10 times.

Requirements:

- You must use the until loop (for and while are forbidden)

4. 4-if_9_say_hi // If 9, say Hi!: a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.

Requirements:

- You must use the while loop (for and until are forbidden)
- You must use the if statement

5. 5-4_bad_luck_8_is_your_chance // 4 bad luck, 8 is your chance: a Bash script that loops from 1 to 10 and:

- displays bad luck for the 4th loop iteration
- displays good luck for the 8th loop iteration
- displays Holberton School for the other iterations

Requirements:

- You must use the while loop (for and until are forbidden)
- You must use the if, elif and else statements

6. 6-superstitious_numbers // Superstitious numbers: a Bash script that displays numbers from 1 to 20 and:

- displays 4 and then bad luck from China for the 4th loop iteration
- displays 9 and then bad luck from Japan for the 9th loop iteration
- displays 17 and then bad luck from Italy for the 17th loop iteration

Requirements:

- You must use the while loop (for and until are forbidden)
- You must use the case statement

7. 7-clock // Clock: a Bash script that displays the time for 12 hours and 59 minutes:

- display hours from 0 to 12
- display minutes from 1 to 59

Requirements:

- You must use the while loop (for and until are forbidden)

Note that in this example, we only display the first 70 lines using the head command.

8. 8-for_ls // For ls: a Bash script that displays:

- The content of the current directory
- In a list format
- Where only the part of the name after the first dash is displayed (refer to the example)

Requirements:

- You must use the for loop (while and until are forbidden)
- Do not display hidden files

9. 9-to_file_or_not_to_file // To file, or not to file: a Bash script that gives you information about the holbertonschool file.

Requirements:

- You must use if and, else (case is forbidden)
- Your Bash script should check if the file exists and print:
-- if the file exists: holbertonschool file exists
-- if the file does not exist: holbertonschool file does not exist
- If the file exists, print:
-- if the file is empty: holbertonschool file is empty
-- if the file is not empty: holbertonschool file is not empty
-- if the file is a regular file: holbertonschool is a regular file
-- if the file is not a regular file: (nothing)

10. 10-fizzbuzz // FizzBuzz: a Bash script that displays numbers from 1 to 100.

Requirements:

- Displays FizzBuzz when the number is a multiple of 3 and 5
- Displays Fizz when the number is multiple of 3
- Displays Buzz when the number is a multiple of 5
- Otherwise, displays the number
- In a list format