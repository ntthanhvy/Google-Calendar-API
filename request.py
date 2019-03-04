
import datetime
import pickle


class General:
    def __init__(self, service):
        self.service = service
        self.calendar_list = self.service.calendarList().list(pageToken=None).execute()

    def get_id(self, calendar_list):
        id = input('Enter calendar name: ')
        if id in calendar_list['items']['id'] or id = calendar_list['items']['summary']:
            return id
        else:
            print('This is not a calendar.')

# ----calendarList api----------
class calendarList(General):

    def delete(self, calendarId):
        self.service.calendarList().delete(calendarId=calendarId).execute()
        print('successful')
        return self.calendar_list

    def get(self, calendarId):
        calendars = self.service.calendarList().get(calendarId=calendarId).execute()
        print(calendars['summary'])
        return calendars

    def insert(self, calendarId):
        calendar_list_entry = {
            'id': calendarId,
        }
        create_calendar_list_entry = self.service.calendarList().insert(body=calendar_list_entry).execute()
        print(create_calendar_list_entry['summary'])
        return self.calendar_list

    def list_out(self, arg):
        page_token = None
        while not page_token:
            calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(calendar_list_entry['summary'])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
        return self.calendar_list

    def patch(self, calendarId):
        # return calendar in patch 
        pass

    def update(self, calendarId):
        calendar_list_entry = self.service.calendarList().get(calendarId=calendarId).execute()
        calendar_list_entry['colorId'] = '21'

        updated_calendar_list_entry = self.service.calendarList().update(calendarId=calendar_list_entry['id'], body=calendar_list_entry).execute()

        print(updated_calendar_list_entry['etag'])
        return self.calendar_list

    def watch(self, arg):
        return self.service.calendarList().watch(body=None)


class calendars(General):

    def clear(self, calendarId):  
        # Clear primary calendar
        pass

    def delete(self, calendarId):
        # delete a seconday calendar

        self.service.calendars().delete(calendarId=calendarId).execute()
        pass

    def get(self, calendarId):
        # return metadata for a calendar
        pass

    def insert(self, calendarId):
        # Create a secondary calendar
        pass

    def patch(self, calendarId):
        # Update metadata for a calendar
        pass

    def update(self, calendarId):
        # Update metadata for calendar
        pass

    
class channels(General):

    def stop(self, calendarId):
        # stop watching resources through this channel
        pass


class colors(General):

    def get(self, calendarId):
        # Return color definitions for calendars and events
        pass


class events(General):

    def delete(self, calendarId):
        # delete an event
        pass

    def get(self, calendarId):
        # return an event
        pass

    def import_event(self, calendarId):
        # import an event (add an private copy of an existing event)
        pass

    def insert(self, calendarId):
        # create an event
        pass

    def instances(self, calendarId):
        # return instances of the specific recurring event
        pass

    def list_out(self, calendarId):
        # return an event on a specific calendar
        pass

    def move(self, calendarId):
        # move an event to another calendar
        pass

    def patch(self, calendarId):
        # update an event
        pass

    def quickAdd(self, calendarId):
        # create an event on a simple text string
        pass

    def update(self, calendarId):
        # update an event
        pass

    def watch(self, calendarId):
        # watch for change to events resources
        pass


class freebusy(General):

    def query(self, arg):
        # return free busy info for a set of calendar
        pass

    
class settings(General):

    def get(self, calendarId):
        # return a single user setting
        pass

    def list_out(self, calendarId):
        # return all user setting for the authenticated user
        pass

    def watch(self, calendarId):
        # watch for change to setting resources
        pass




# -------else api-------
def get_event(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=30, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


def get_calendar(service):
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            print (calendar_list_entry['summary'])
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break