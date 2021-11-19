import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("firebase_sdk.json")
firebase_admin.initialize_app(cred)

# user= auth.create_user(
#         email='user@example.com22333',
#         email_verified=False,
#         phone_number='+15554550100',
#         password='secretPassword',
#         display_name='John Doe',
#         photo_url='http://www.example.com/12345678/photo.png',
#         disabled=False
#         )
# print('Sucessfully created new user: {0}'.format(user.uid))

decoded_token = auth.verify_id_token("eyJhbGciOiJSUzI1NiIsImtpZCI6ImY1NWUyOTRlZWRjMTY3Y2Q5N2JiNWE4MTliYmY3OTA2MzZmMTIzN2UiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbXVhaG8tMzk0ZDIiLCJhdWQiOiJtdWFoby0zOTRkMiIsImF1dGhfdGltZSI6MTYzNzI5NTgxMCwidXNlcl9pZCI6IkVKSXR5a3VEQWdPMEVWTE5SdkhhVXZjd0hVdDIiLCJzdWIiOiJFSkl0eWt1REFnTzBFVkxOUnZIYVV2Y3dIVXQyIiwiaWF0IjoxNjM3Mjk1ODExLCJleHAiOjE2MzcyOTk0MTEsImVtYWlsIjoicGh1YzFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInBodWMxQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.XREcjHgv7NCNG7gAYZGmqnepzIMGUmaZi2Jy4ntnWAE2gn5983feRnpYdLy088oXlrS4xt7f0ZYiAXPLRyJneUugorIhCx6WPYWD-QuRoXjMvQz0YnRipT4IUHnDqvhis8tzQRWFr9q_ZLYwkspd8lYS5epCGnWMZfPvEnxj-gQ5LRedJ6dQpkD0AkkNABfu29TIJE3wDDEqKtHCXQvCDBlUmLjYxyqNyaBrdBACuUZb98XclslQk-cSkc1c1o3FQNMAVQYeFjy6eTrr4-pgs-Uey1Iqi7kEt4lmWfBShW7xdwBZUU4m2lfRNi5mQYOVRYmGrPLGL52RvsJLs7y_og")
uid = decoded_token['uid']
print(decoded_token)
print(uid)

