#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for managing HBNB data.
    """
  
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program cleanly at end of file (EOF).
        """
        print()
        return True
  
    def emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
