from email_handler import send_email_to_user
from notion_client import Client,  APIErrorCode, APIResponseError
import time
import os

notion = Client(auth=os.environ["NOTION_TOKEN"])
                
def change_check_property_notion(user_block_id, email_sent=True):
    database = notion.pages.update(
            **{
                "page_id": user_block_id,
                "properties": {
                    'Email Sent': {
                        "checkbox": email_sent,
                    },
                },
            }
    )

def check_users_and_send_email(emails, names, ids):
    if emails and names:
        for email, name, id in zip(emails, names, ids):
            change_check_property_notion(id)
            send_email_to_user(email, name)
    else:
        print("All users have been sent an email!")

def query_emails_and_name():
    try:
        #it gets all users that have not been sent an email!
        database = notion.databases.query(
            **{
                "database_id": str(os.environ["NOTION_DATABASE_ID"]),
                "filter": {
                    "property": "Email Sent",
                    "checkbox": {
                        "equals": False,
                    },
                },
            }
        ).get("results")

        emails = [email["properties"]['Email']['email'] for email in database]
        names = [name["properties"]['Name']['title'][0]['plain_text'] for name in database]
        ids = [name["id"] for name in database]

        return emails, names, ids
        
    except APIResponseError as error:
        print(str(error))
        return None, None, None

if __name__ == '__main__':
    while True:
        emails, names, ids = query_emails_and_name()
        check_users_and_send_email(emails, names, ids)
        print("Sleeping for 5 minutes")
        time.sleep(300)
