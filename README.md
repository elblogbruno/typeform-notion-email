
# Typeform to Notion to Email

Recently we unleashed the Glassear SDK BETA users list. We needed to sent an email when a user completed the Typeform form. This is how it was born!
When you create a [Typeform form](https://www.typeform.com/), you can connect it to Notion, and this script automatically sends them a customizable email of your choice!

## How to get it working!

Clone the project

```bash
  git clone https://github.com/elblogbruno/typeform-notion-email
```

Go to the project directory

```bash
  cd typeform-notion-email
```

Install dependencies

```bash
  pip install -r requirements.txt
```

### Typeform to Notion Steps

- [Create a notion database like this template](https://glassear.notion.site/e2449f3fc7a440da81c401d980214fa5?v=57d416d7c5654987a5cef640923209a7)
- Create your typeform form. Add a screen or screens on your forms that ask for the user name and email!
- Go to connect and search for the Notion typeform integration. When asked to select a database, select the database you created. (Putting email to email property on notion, and name to name property on Notion) [Notion typeform integration](https://www.typeform.com/connect/notion/)

- [Create an integration](https://www.notion.com/my-integrations) and find the token. [→ Learn more about authorization](https://developers.notion.com/docs/authorization).

Write your notion token as a variable and database id. This will allow the script to access the database.

```bash
  export NOTION_TOKEN=<notion_token>
  export NOTION_DATABASE_ID=<notion_database_id> 

📘 Where can I find my database's ID?

Here's a quick procedure to find the database ID for a specific database in Notion:

Open the database as a full page in Notion. Use the Share menu to Copy link. Now paste the link in your text editor so you can take a closer look. The URL uses the following format:

https://www.notion.so/{workspace_name}/{database_id}?v={view_id}
Find the part that corresponds to {database_id} in the URL you pasted. It is a 36 character long string. This value is your database ID.
```

Write your email info. This is the email that will send the email to your users!

```bash
  export EMAIL_STMP_HOST=<email_stmp> #example: smtp.gmail.com
  export EMAIL_ADDRESS=<email_address> #example: demo@gmail.com
  export EMAIL_PASSWORD=<email_password> #example: very secure password
```

Start the server. Be careful emails will be sent at start! 

```bash
  python check_for_new_entries.py
```

Every 5 minutes, it will check for new users!
  
## Acknowledgements
 - [Notion API](https://www.notion.so/)
 - [Notion SDK API Python by ramnes](https://github.com/ramnes/notion-sdk-py)