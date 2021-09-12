import pandas as pd
import smtplib
from email.message import EmailMessage
import phonenumbers as phonenumbers
from phonenumbers import geocoder

#read csv file
df = pd.read_csv('contacts.csv')
 
#get email
print(df['email'])

my_contact = df.loc[(df['first_name'] == 'Richard') & (df['last_name'] == 'Taujenis'), ['email']]
print(my_contact)

 
 #if individiual
def individual():
   print("Individual chosen")
   print('#'*10)
   for user in df['first_name'] + ' ' + df['last_name']:
      print(user)
   print('#'*10)
   try:
      user = input('Please write the user you want to send the email to: ')
      user_name = user.split()
      first_name = user_name[0]
      last_name = user_name[1]
      print(last_name)
      if df.loc[(df['first_name'] == first_name) & (df['last_name'] == last_name), ['email']]:
         print("Chosen " + user)
      else:
         print("User not in list")
   except SystemExit:
      return
   
def bulk():
   print("bulk pressed")
      
#prompt if send email to all contact or individual
def main():
   try:
      prompt = int(input('''Do you want to send to individual contact email or all:\n For individual press 1 \n For bulk send press 2 \n>'''))
      if prompt == 1:
         individual()
      if prompt == 2:
         bulk()
      else:
         print("Only 1 or 2 is accepted. Try again...")
   except Exception:
      print("Sorry. Not accepted comand or incorrect input provided...")
      return
         
   
if __name__ == '__main__':
   runing_main = True
   main()
