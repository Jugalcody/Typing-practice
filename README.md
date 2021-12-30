# Typing-practice
In this project, i am trying to create a well platform for typing practice. if anyone has some additional idea ,he/she can modify it to the best.

## Aim 1
- To develop a typing platform with random characters,words,sentences,etc
- To create different levels

### Levels

- Level 1 contains simple characters 
- Level 2 contains simple random words
- Level 3 contains long range words
- Level 4 contains character with spaces
- Level 5 contains sentences with small range words
- Level 6 contains sentences with large range words

status - completed

## Aim 2

- Modify it to calculate the score of each levels and store it into a database or into a file

- After completing the last level, it would ask to the user that if mysql server is installed in the pc or not, if user enter yes, then it would ask user name
  and password of the mysql sever. At the last, all the score would be saved into the mysql database into a table.

- If users enter no(mysql sever is not installed in the pc) then the score of the user would be saved into a file with filename 'typing-score.txt'. 

status - completed

## Aim3

### Exception handling

-When computer ask to the user that if mysql sever is installed on the pc or not after completing the last level, and if user enter yes despite not having the mysql
 database installed on the pc or if mysql server is installed but the user name ,password is entered wrong or if mysql-connector is not installed or any other issue occured
 and an error would come , then unfortunately the score won't save anywhere.
 
 ### Fix
 
 - By using excetion handling, the problrm has been solved successfully.
 - Now if any error occured, then the score will automatically saved into a file named 'typing-score.txt'.
 
status- completed

## Aim 4

- To calculate the time taken by the user in completing a level
- Module used - time
- Function used- monotonic

status -completed

## Aim 5

- If the user completed the task upto level 3, and close the program and run again then the program would starts from level 1 again

- Next aim is to make the program executes from a checkpoint. Once the user completed upto some levels, then the last completed level would be recorded as a checkpoint and 
  by next time, if program runs again, instead of running from the first level, it would execute from the saved checkpoint.

 ### status(Aim 5) - incomplete
      
  * If anyone has some idea about aim 5, he/she can modify it and complete the task....
    
      
      
