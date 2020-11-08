# ClassroomBot

**Version 1.0.1**

Discord Bot to manage classes for remote lectures.

## Features:
The commands availible with this bot are the following ones. Only server users with the administrator permission can run these commands.
- `!newclass "class name"` creates a new class with the given name

Creating a class includes :
1. Creating a new role with the class name, so that the students with this role and only them can see the class chanels
2. Creating a new category with the class name, to englobe the following chanels
3. Creating 3 text chanels :
    1. general text chanel, where class students and teacher can write messages
    2. document text chanel, where only teacher can write messages
    3. class text chanel, for people withour a microphone to be able to speak during class without floodind the general chanel
4. Creating 1 voice chanel


- `!changeclass "old class" "new class"` transfer all students of a class from one class to another one. The second argument is facultative, and in this case all students of the class would see their role removed without being transfered to another one.

**Warning:** if the the second class (new class) was not created beforehand, the command will fail!

- `!deleteclass "class name"` delete the given class category, chanels and role (**Warning** this action is irreversible and all messages in the text chanels will be deleted)
