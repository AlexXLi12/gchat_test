from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

# Specify required scopes.
SCOPES = ['https://www.googleapis.com/auth/chat.bot']

# Specify service account details.
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    'total-scion-371119-ae8844b5e838.json', SCOPES)

# Build the URI and authenticate with the service account.
chat = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))

users_list = chat.spaces().members().list(parent='spaces/AAAA7nyhBxg').execute()
# Create a Chat message.
# result = chat.spaces().messages().create(

#     # The space to create the message in.
#     #
#     # Replace SPACE_NAME with a space name.
#     # Obtain the space name from the spaces resource of Chat API,
#     # or from a space's URL.
#     parent='spaces/AAAA7nyhBxg',

#     # The message to create.
#     body={'text': 'Hello from the authenticated service account!'}

# ).execute()


# print(result)
print([user['member']['displayName'] for user in users_list['memberships']])