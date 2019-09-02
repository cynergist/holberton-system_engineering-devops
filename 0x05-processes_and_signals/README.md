# 0x05. Processes and signals

## Resources
[Linux PID, LINFO.org](http://www.linfo.org/pid.html) </br >
[Linux Processes, The Geek Stuff](https://www.thegeekstuff.com/2012/03/linux-processes-environment/) </br >
[Linux Signals Fundamentals, Part I, The Geek Stuff](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/) </br >
[Linux Signals, Computer Hope](https://www.computerhope.com/unix/signals.htm) </br >

## man or help:
- `ps`
- `pgrep`
- `pkill`
- `kill`
- `exit`
- `trap`
</br >

## Learning Objectives
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

# More Info

## Shellcheck
Shellcheck is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

## Tasks

0. 0-what-is-my-pid // What is my PID: a Bash script that displays its own PID.

1. 1-list_your_processes // List your processes: a Bash script that displays a list of currently running processes.

Requirements:

- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

2. 2-show_your_bash_pid // Show your Bash PID: a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

- You cannot use pgrep
- The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

3. 3-show_your_bash_pid_made_easy // Show your Bash PID made easy:  a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

- You cannot use ps

4. 4-to_infinity_and_beyond // To infinity and beyond: a Bash script that displays To infinity and beyond indefinitely.

Requirements:

- In between each iteration of the loop, add a sleep 2

5. 5-kill_me_now // Kill me now: We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

- You must use kill

6. 6-kill_me_now_made_easy // Kill me now made easy: a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

- You cannot use kill or killall

7. 7-highlander // Highlander: a Bash script that displays:

- To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
- I am invincible!!! when receiving a SIGTERM signal

Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

8. 8-beheaded_process // Beheaded process: a Bash script that kills the process 7-highlander.