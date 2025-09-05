Current = []
Deleted = []
Updated = []

quit = False

def print_list(list):
        #iterates through the list passed to it as an argument and prints out the items in it
        n = len(list)
        if n == 0:
                print("Your List is empty. You're up to date!")
                return
        for i in range(n):
                list_item = i + 1
                print(str(list_item) + "." + " " + list[i])
                
def modify_list(list):
        #Adds an item to the list passed as an argument and changes the To-Do List accordingly
        try:
                list_length = len(Current)
                item_number = int(input("Choose an item number:")) - 1
                item = Current[item_number] 
                list.append(item)
                Current.pop(item_number)
        except ValueError:
                print("Invalid input. Please enter a number.")
                
        except IndexError:
                print(f"Invalid item number. Please enter a number between 1 and {list_length}")
        
        
def create_item():
        item = input("Enter an item to add to your To-Do List:")
        while item == "":
                print("Invalid list item. Please enter some text for your To-Do list item")
                item = input("Enter an item to add to your To-Do List:")
                
        Current.append(item)
        print("Your current To-Do List is now as follows:")
        print_list(Current)
        return

def run_app():
        global Current
        global Deleted
        global Updated
        global quit

        print("Enter:")
        print("'View' to view your current To-Do List:")
        print("'Remove' to remove an item from your list:")
        print("'Update' to complete an item:")
        print("'New' to create a new To-Do List item:")
        print("'Quit' to quit the application:")
   
        option = input("Choose an option:")
        option = option.strip()
        option = option.lower()
   
        valid_options = ["new", "view", "update", "remove", "quit"]
        
        if option not in valid_options:
                print("Invalid input. Please choose an option from the menu.")
                return
                    
        if option == "view":
                if len(Current) == 0:
                        print("Your To-Do List is empty. Add something to it.")
                        create_item()
                else:
                        print_list(Current)

        elif option == "new":
                create_item()

        elif option == "remove":
                if len(Current) == 0:
                        print("Your To-Do List is empty. Add something to it.")
                        create_item()
                else:
                        print("Your current list is:")
                        print_list(Current)
                        modify_list(Deleted)
                        if len(Deleted) != 0:
                                print("The following items have been deleted from your To-Do List:")
                                print_list(Deleted)
                        else:
                                return
                                                
        elif option == "update":
                if len(Current) == 0:
                        print("Your To-Do List is empty. Add something to it.")
                        create_item()
                else:
                        print("Your current list is:")
                        print_list(Current)
                        modify_list(Updated)
                        if len(Updated) != 0:
                                print("The following items have been crossed off your list:")
                                print_list(Updated)
                        else:
                                return
        else:
                print("Thank you for using the To-Do List App.")
                quit = True
           
print("Welcome to the To-Do List App!")    
   
while quit == False:
        run_app()
