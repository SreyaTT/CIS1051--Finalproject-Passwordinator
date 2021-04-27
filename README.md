# CIS1051--Finalproject-Passwordinator
Final project for CIS 1051 with Professor Andrew Rosen
Link to my youtube demo: https://www.youtube.com/watch?v=Ks75m0cYQWg

## Things I achieved
I was successful in: 

-- connecting python to the mySQL server I established.

-- created functions to accept new account credentialls, reset passwords, and pull forgotten passwords.

-- created a GUI that I was sort of proud of.


## Things I didn't achieve

What I did not achieve:

-- my biggest failure was my inability to get the button widget in tkinter to return any values once the commhttps://github.com/dannydukes/CIS1051--Finalproject-Passwordinatorand ran. 
The 'command=' option for the button module would not let me return values, and was barely letting me run variables into the function subject to the command.

##Why I didn't achieve them, and how I tried to resolve it

-- I ended up utilizing the partial function to get the function to accept the reference to the entry box, and that was successful in creating a function that CLEARED the textbox.
The issue i have is that when I call the get() method for the entry widget inside the function of the button command, I couldn't store that variable to use outside of the function.

-- I tried creating a global variable inside the button command and referencing it outside. 
-- I tried turning the button command function into something that simply "clicks" and increments a variable outside of the function, and then when that variable is incremented to one i tried calling the get() command.
-- nothing I tried was beneficial, and I went through a LOT of stack overflow threads to find out where I went wrong. I still am not sure how I could change this to get it to work.

## Things I learned 
-- I feel pretty competent with SQL commands now! which is why I chose this project specifically. 
-- I learned tkinter and how to deal with new widgets (except for the button...  :/ )
-- I learned more about object oriented programming through developing my GUI. 
