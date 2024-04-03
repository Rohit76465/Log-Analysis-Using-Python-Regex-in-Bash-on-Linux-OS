#GUIDE:-
#.........

#1)To give executable permission to the Python script ticky_check.py.

  chmod +x ticky_check.py

#2)Run the ticky_check.py by using the following command:

  ./ticky_check.py

#3)To visualize the data in the error_message.csv and user_statistics file, you have to generate a webpage that'll be served by the webserver running on the machine.The script csv_to_html.py            takes in two arguments, the CSV file, and location i.e directory that would host the HTML page generated.

#- Give write permission to this location that would host that HTML page:

  sudo chmod +x csv_to_html.py

#- Give executable permission to the script file csv_to_html.py.

  sudo chmod o+w /var/www/html


#4)Executing ticky_check.py will generate two report file error_message.csv and user_statistics.csv.You can now visualize the error_message.csv and user_statistics.csv by converting them to HTML pages. To do this, pass the files one by one to the script csv_to_html.py file, like we did in the previous section.

#- To convert the error_message.csv into HTML file run the following command:

  ./csv_to_html.py error_message.csv /var/www/html/Write_Any_Name_of_Your_Choice.html

#- To convert user_statistics.csv into HTML file, run the following command:

  ./csv_to_html.py user_statistics.csv /var/www/html/Write_Any_Name_of_Your_Choice.html

#5)Now, To view these HTML pages, open any web-browser and enter the following URL in the search bar.

  #[External IP address]/[html-filename].html

  #Note - External IP address was provided to me by Qwiklabs on Coursera.