import os
import requests

# définition de l'adresse de l'API
api_address = '10.5.0.10'
# port de l'API
api_port = 8000

# requête
r1 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)

output1 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="wonderland"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''

r2 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)

output2 = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="bob"
| password="builder"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''

r3 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'mandarine'
    }
)

output3 =  '''
============================
    Authentication test
============================

request done at "/permissions"
| username="alice"
| password="mandarine"

expected result = 403
actual result = {status_code}

==>  {test_status}

'''

r4 = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'clementine'
    }
)

output4 =  '''
============================
    Authentication test
============================

request done at "/permissions"
| username="bob"
| password="clementine"

expected result = 403
actual result = {status_code}

==>  {test_status}

'''



# statut de la requête
expected_code = [ 200,200,403,403]
status_code = []
queries= [ r1,r2,r3,r4 ]
output= [ output1,output2,output3,output4 ]

for r in queries:
  status_code.append(r.status_code)

# affichage des résultats
for code,expcode, out in zip(status_code,expected_code,output) :
   if  code == expcode :
      test_status= 'SUCCESS'
   else:
      test_status = 'FAILURE'
   print(out.format(status_code=code, test_status=test_status))
      
# impression dans un fichier

if os.environ.get('LOG') == '1' :
    with open('./log/api_test.log', 'a') as file:
        for code,expcode, out in zip(status_code,expected_code,output):
            if  code == expcode :
            	test_status = 'SUCCESS'
            else:
                test_status = 'FAILURE'
            file.write(out.format(status_code=code, test_status=test_status) + '\n')
