OBJECTIVE :-

  The main purpose of the project “LIBRARY MANAGEMENT SYSTEM” is to manage all the details of books and members of the library etc. The objective of this project is to   reduce the manual work for the Librarian. It tracks all the details about the issues, returns, books present in the library and members of the library and keeps all
  data safe and secure.

LANGUAGES USED :-

  Front End : Python 3.7
  Back End : Mysql 5.7
  
MODULES USED :-

The program uses ‘tkinter’ module for GUI development, ‘pickle’ module for binary data file handling and ‘mysql.connector’ module for back end (mysql) connectivity.

FUNCTIONS OF LIBRARY MANAGEMENT SYSTEM :- 

● Add Book : This module allows librarian to add various details of the books available in the library i.e Book ID, Book Name, ISBN No., Publisher, Edition, Price and Pages of the book. Insert button inserts the details of the book provided by the librarian. Delete button deletes the record of the given book id. Clear button clears all entries. Close button closes the add book window.

● Add Student : This module allows librarian to add various details of the students i.e, Student ID, Student Name, Father Name, Course, Branch, Year and Semester of the student. Insert button inserts the details of the student provided by the librarian. Delete button deletes the record of the given student id. Clear button clears all entries. Close button closes the add student window.

● Issue Book : This module allows librarian to add various details of the book issued by the student i.e Book ID, Student ID, Book Name, Student Name, Course, Branch, Year and Date of Issue. Insert button inserts the details of the issued book provided by the librarian. Delete button deletes the record of the given book id. Clear button clears all entries. Close button closes the issue book window.

● Return Book : This module allows librarian to add various details of the book returned by the student i.e Book ID, Student ID, Book Name, Student Name Insert button inserts the details of the returned book provided by the librarian. Delete button deletes the record of the given book id. Clear button clears all entries. Close button closes the return book window.

● Statistics : This module allows librarian to view the details of the books present in the library, details of the students, details of previous and current issued and returned books. Close button closes the statistics window.

● Settings : This module has two buttons (functions) :-
 I. Change Password : This module allows the administrator (librarian) to change the login password for the program.
II. About : This module allows the client to view the details of the program i.e the purpose and current version of the program. Close button closes the settings window.

HIGHLIGHTED FEATURE :-

Security : This program makes the data secure and safe with its login password security feature. With this feature private data of students can be kept secure. This feature also allows the administrator (librarian) to change the password. By default there is no password and the username is ‘admin’. Password can be changed by clicking the ‘change password’ button under the ‘settings’ option. It will ask for the current password, if the current password matches then the client can set a new password and then confirm it. After setting a new password, the program reruns and login page appears. The password and username are saved in separate binary files so that it can be kept encrypted and secure.
