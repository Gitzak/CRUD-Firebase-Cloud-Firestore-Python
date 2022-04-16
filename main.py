
from cgitb import reset
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create Data

# create collection and document with auto ID
# collection can create if not exist
# db.collection('personnes').add(
#     {
#         'name': 'zak be',
#         'age': 55
#     }
# )

# add to collection document with auto ID
# db.collection('projects').add(
#     {
#         'title': 'p 7',
#         'description': 'description 7'
#     }
# )

# set document with knowm ID
# db.collection('personnes').document('1').set(
#     {
#         'name': 'zaaak',
#         'age': 29
#     }
# )

# set document with auto ID
# db.collection('personnes').document().set(
#     {
#         'name': 'Hamza',
#         'age': 28
#     }
# )

# merging with data exist and replace
# db.collection('personnes').document('1').set(
#     {
#         'age' : 40
#     },
#     merge = True
# )

# set collection in document
# db.collection('personnes').document('1').collection('groups').add(
#     {
#         'name' : 'group 1',
#         'description' : 'description group 1'
#     }
# )

# db.collection('personnes').document('1').collection('groups').document('GR-2').set(
#     {
#         'name' : 'group 2',
#         'description' : 'description group 2'
#     }
# )

# Read Data
# where ID
# result = db.collection('personnes').document('1').get()
# if result.exists:
#     print(result.to_dict())

# get all documment in collection
# docs = db.collection('personnes').get()
# if len(docs):
#     for doc in docs:
#         print(doc.to_dict())

# querying
# == <= >= < > != array_contains in
# docs = db.collection('personnes').where('age', '==', 28).get()
# if len(docs):
#     for doc in docs:
#         print(doc.to_dict())

# docs = db.collection('personnes').where('age', 'in', [28, 40]).get()
# if len(docs):
#     for doc in docs:
#         print(doc.to_dict())

# Update Data - Known key
# db.collection('personnes').document('1').update({
#     'age' : firestore.Increment(1),
#     'name' : "Zakaria"
# })

# db.collection('personnes').document('1').update({
#     'address' : "Address 1"
# })

# db.collection('personnes').document('1').update({
#     'social_network' :{
#         '#facebook',
#         '#linkedin',
#         '#instagram',
#     }
# })

# db.collection('personnes').document('1').update({
#     'social_network' : firestore.ArrayRemove(['#instagram'])
# })

# db.collection('personnes').document('1').update({
#     'social_network' : firestore.ArrayUnion(['#instagram'])
# })

# Update Data - unknown key
# docs = db.collection('personnes').get()
# for doc in docs:
#     if doc.to_dict()['age'] >= 29:
#         db.collection('personnes').document(doc.id).update({
#             'age_group': 'Chooooraf'
#         })

# docs = db.collection('personnes').where('age', '>=', 29).get()
# for doc in docs:
#     db.collection('personnes').document(doc.id).update({
#         'age_group': 'Chooooraf w'
#     })

# Delete Data - known ID
# db.collection('personnes').document('OzuftEk28LaoldBl4Etq').delete()

# Delete Data - known ID => field
# db.collection('personnes').document('1').update({
#     'social_network' : firestore.DELETE_FIELD
# })

# Delete data one by one - unknown ID (First way)
docs = db.collection('personnes').get()
for doc in docs:
    key = doc.id
    db.collection('personnes').document(key).delete()
