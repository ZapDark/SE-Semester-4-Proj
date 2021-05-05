from firebase import firebase


firebase = firebase.FirebaseApplication('https://secondtry-aa3b4-default-rtdb.firebaseio.com/', None)
data =  { 'Name': 'John Doe',
          'RollNo': 3,
          'Percentage': 70.02
          }
result = firebase.post('/Students/',data)
print(result)
