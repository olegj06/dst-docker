import os
import requests

# définition de l'adresse de l'API
api_address = '10.5.0.10'
# port de l'API
api_port = 8000

# requête
r1 = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

output1 = '''
============================
    scoring test v1 
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"

expected result : positive
actual result = {score}

==>  {test_status}

'''

r2 = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

output2 = '''
============================
    scoring test v1
============================

request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

expected result : negative
actual result = {score}

==>  {test_status}

'''

r3 = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

output3 = '''
============================
    scoring test v2 
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"

expected result : positive
actual result = {score}

==>  {test_status}

'''

r4 = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

output4 = '''
============================
    scoring test v2
============================

request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"

expected result : negative
actual result = {score}

==>  {test_status}

'''
# statut de la requête
sentences=["life is beautiful","that sucks"]
query_sentences=[]
scores=[]
queries= [ r1,r2,r3,r4 ]
output= [ output1,output2,output3,output4 ]

#ajout des scores dans le tableau scores
for q in queries :
   scores.append(q.json()['score'])

#ajout des phrases entrées dans le tableau query_sentences
for qs in queries :
   query_sentences.append(qs.json()['sentence'])


# affichage des résultats
for score ,out,ques in zip(scores,output,query_sentences):
    if (score > 0  and ques == sentences[0]) or (score < 0  and ques == sentences[1]):
        test_status= "SUCCESS"
    else :
    	test_status="FAILURE"
    print(out.format(score=score, test_status=test_status))
     
# impression dans un fichier

# impression dans un fichier
if os.environ.get('LOG') == '1' :
    with open('./log/api_test.log', 'a') as file:
        for score, out , ques in zip(scores, output, query_sentences) :
            if (score > 0  and ques == sentences[0]): 
                test_status = 'SUCCESS'
            elif (score < 0  and ques == sentences[1]):
                test_status = 'SUCCESS'
            else:
                test_status = 'FAILURE'
            file.write(out.format(score=score, test_status=test_status) + '\n')
