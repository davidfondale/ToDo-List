
# To-Do List Application #

The To Do List Application is a console application which tracks items on a basic To Do list.
It allows the user to track items to do, items completed from the to do list, and items removed
from the list without doing them. This last category allows the user to distinguish between items
on the list which the user may ultimately decide need not be done, re-assigns to an assistant or
associate, or otherwise chooses to delegate to someone else. 

The application is enabled with basic Create, Read, Update, and Delete (CRUD) functionality. The command
line interface, (CLI) displays an option menu as follows:

##### Enter:  
##### 'View' to view your current To-Do List:  
##### 'Remove' to remove an item from your list:  
##### 'Update' to complete an item:  
##### 'New' to create a new To-Do List item:  
##### 'Quit' to quit the application:  

The application will promp the user to choose an option. Depending on the option the user chooses, the app
may prompt the user for aditional information, such as the text for an item to add to the list, the number
of an item to remove from the list, etc. In every case, the app provides immediate feedback as to the current
state of all lists; To Do, Updated, or Deleted, as the case may be. 

The app will also provide immediate feedback concerning errors the user may have made in typing any information
into the interface, such as the number of a list item which doen't exist, trying to view an empty list, etc. After
displaying the relavent error message, the app will immediately return the user back to the main menu where the
user can correct his mistake and continue using the application. Please note that when making choices, the 
application is completely IN-sensitive to case and space characters. In other words additional spaces, capital
and or lowercase, or even mixed case letters will be ignored. Spaces and case are NOT ignored in list items. 
Though, as expected, they only effect the display of text and in no other way affect the operation of the application.

Typing "Quit" at the choose an option: prompt will immediately close the application.

Welcome and enjoy using the To-Do List Application!
