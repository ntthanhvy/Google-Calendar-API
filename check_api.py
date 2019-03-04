from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import request as req

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def make_creds():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


# ------------getting the id of calendar or-----------------------
def get_id(service, id):
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        calendar_list_entries = calendar_list['items']

        for calendar_list_entry in calendar_list_entries:
            print(calendar_list_entry['summary'])

        if id.strip() == calendar_list_entries['id'] or id == calendar_list_entries['id']:
            return calendar_list_entry['id']
            
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    return None


# -------------the function that call on api----------------------
def get_api(api, method, id):
    service = build('calendar', 'v3', credentials=make_creds())
    request = getattr(req, api)(service)
    if method == 'list':
        method = 'list_out'
    calendarId = get_id(service, id)
    # if id.lower() == 'primary':
    #     id = 
    if not calendarId:
        print('This is not a calendar name.')
    else:
        respone = getattr(request, method)(calendarId)
        print(respone)


# if __name__ == '__main__':
#     main('event')
