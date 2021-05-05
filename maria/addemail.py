from firebase import firebase 



enteraddress = input("Enter email address to add to database: ")

firebase = firebase.FirebaseApplication('https://email-48310-default-rtdb.firebaseio.com/', None)  
data =  { 'address': enteraddress  
            
          }  
result = firebase.post('email-48310-default-rtdb/emailstosend',data)  
print("email added.")  