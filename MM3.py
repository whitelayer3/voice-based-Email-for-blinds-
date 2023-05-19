import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import time
import smtplib
import re
import imaplib
import email

#fuNctioNs........................................................................................................
def cw(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

def correct_email(email):
    # Check if email contains common mistakes and correct them using regular expressions
    email = re.sub(r'\s+at\s+|\s+@\s+', '@', email)  # Replace "at" or "@" surrounded by spaces with "@"
    email = re.sub(r'\s+dot\s+|\s+\.\s+', '.', email)  # Replace "dot" or "." surrounded by spaces with "."
    email = re.sub(r'\s+', '', email)  # Remove any remaining whitespace
    return email.lower()  # Convert email to lowercase




def speak(word):
    tts = gTTS(text=word, lang="en")
    filename = "voi.mp3"
    os.remove('voi.mp3')
    tts.save(filename)
    time.sleep(1)
    playsound.playsound(filename)

 #read mail thiNgs
yo = ''
paa = ''
def rea():
    r = sr.Recognizer()
    with sr.Microphone() as source:

            print("Speak now...")
            speak("you can Speak now...")
            audio = r.listen(source)
            try:
                # recognize speech using Google Speech Recognition
                text = r.recognize_google(audio)
                print("You said: ", text)
                paa = text
                #print(paa)
                speak('you said' + text)

            except sr.UnknownValueError:
                print("Sorry, could not understand audio")
                pass
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                pass


    return paa

def semt():
    print('composimg')
    speak('Ready to compose your mail')
    while True:
        speak('say receiver address')
        addd = rea()
        print(addd)
        che_addd = correct_email(addd)
        print(che_addd)
        speak(che_addd + 'is that curect')
        res = rea()
        if cw(res, 'yes'):
            break
        elif cw(res, 'okay'):
            break

    while True:
        speak('what is the subject of the mail')
        suBB = rea()
        print(suBB)
        speak(suBB + 'is that curect')
        res = rea()
        if cw(res, 'yes'):
            break
        elif cw(res, 'okay'):
            break
        elif cw(res, 'YES'):
            break
        elif cw(res, 'YES'):
            break

    while True:
        speak('what is the matter of the mail')
        matt = rea()
        print(matt)
        speak(matt + 'is that you said')
        res = rea()
        if cw(res, 'yes'):
            break
        elif cw(res, 'okay'):
            break
        elif cw(res, 'YES'):
            break
        elif cw(res, 'YES'):
            break
    receiver_email = che_addd
    # password = "jmhcndupygyyuwvv"
    subject = suBB
    body = matt

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(username, receiver_email, message)


#actual code...........................................................................................................

def read():
    matt = ''
    text = ''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Speak now...")
            speak('your Now at main page what do you want to do now')

            audio = r.listen(source)
            try:
                # recognize speech using Google Speech Recognition
                text = r.recognize_google(audio)
                #text = input('mmmm')
                print("You said: ", text)
                # paa = text.replace(" ", "")
                # print(paa)


            except sr.UnknownValueError:
                print("Sorry, could not understand audio")
                pass
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                pass

            if cw(text,'compose'):
                semt()


            elif cw(text,'write'):
                semt()


            elif cw(text,'Write'):
                semt()


            elif cw(text,'read'):
                read_f()


            elif cw(text,'logout'):
                break
            elif cw(text,'log'):
                break
            elif cw(text,'out'):
                break
            else:
                print('try agaim')
    return text



def read_f():
    # IMAP settings for Gmail
    imap_host = 'imap.gmail.com'
    imap_port = 993
    #username = 'projectgroup5cem@gmail.com'
    #password = 'jmhcndupygyyuwvv'

    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_host, imap_port)
    mail.login(username, password)
    mail.select('inbox')

    # Search for unread messages
    status, response = mail.search(None, 'UNSEEN')
    unread_msg_nums = response[0].split()

    urmsg = f'Total Unread Messages: {len(unread_msg_nums)}'
    print(urmsg)
    print('you have' + urmsg + 'unreaded messages')
    speak(urmsg + 'unreaded messages')
    if len(unread_msg_nums) > 0:
        while True:
            print('do you want me to read one by one ,or read user name and subject of the mail')
            speak('do you want me to read one by one ,or read user name and subject of the mail')
            res = input()
            if cw(res, 'one'):
                for msg_num in unread_msg_nums:
                    # Fetch the email message by ID
                    status, email_data = mail.fetch(msg_num, '(RFC822)')
                    email_message = email.message_from_bytes(email_data[0][1])

                    # Get the email sender, subject, and body
                    sender = email_message['From']
                    subject = email_message['Subject']
                    body = None
                    for part in email_message.walk():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload(decode=True).decode('utf-8')
                            break

                    print(f"From: {sender}")
                    speak(f"From: {sender}")
                    print(f"Subject: {subject}")
                    speak(f"Subject: {subject}")
                    print(f"Body: {body}")
                    speak(f"Body: {body}")
                    print('-----------------------------')
            elif cw(res, 'user'):
                for msg_num in unread_msg_nums:
                    # Fetch the email message by ID
                    status, email_data = mail.fetch(msg_num, '(RFC822)')
                    email_message = email.message_from_bytes(email_data[0][1])

                    # Get the email sender, subject, and body
                    sender = email_message['From']
                    subject = email_message['Subject']
                    body = None
                    for part in email_message.walk():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload(decode=True).decode('utf-8')
                            break

                    s_m = f"From: {sender}"
                    print(f"From: {sender}")
                    speak(f"From: {sender}")

                    print(f"Subject: {subject}")
                    speak(f"Subject: {subject}")
                    print('do you want to read')
                    speak('do you want to read')
                    res = input()
                    if cw(res, 'yes'):
                        print(f"Body: {body}")
                        speak(f"Body: {body}")
                        print('-----------------------------')
                    else:
                        pass
            else:
                break

    else:
        wish = ''
        print('do you want to search mail or exit')
        speak('do you want to search mail or exit')
        wish = input()
        if cw(wish, 'search'):
            # Search for messages matching the subject or sender id
            subject = input('sub')
            sender = input('example_sender@example.com')
            search_query = f'(SUBJECT "{subject}") (FROM "{sender}")'
            status, search_results = mail.search(None, search_query)

            # Iterate through the message ids
            for msg_id in search_results[0].split():
                # Fetch the message data
                status, msg_data = mail.fetch(msg_id, '(RFC822)')

                # Parse the message data into an email message object
                msg = email.message_from_bytes(msg_data[0][1])

                body = None
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8')
                        break

                # Print the message subject and sender
                print(f'Subject: {msg["Subject"]}')
                speak(f'Subject: {msg["Subject"]}')
                print(f'Sender: {msg["From"]}')
                speak(f'Sender: {msg["From"]}')
                print(f"Body: {body}")
                speak(f"Body: {body}")
                print('-----------------------------')




        elif cw(wish, 'exit'):
            pass

            # Logout from the email account
            mail.logout()
    # anandhumanu143@gmail.com

    # Close the mailbox and logout from the IMAP server
    mail.close()
    mail.logout()



paa = ''
print('email id')
username = "projectgroup5cem@gmail.com"
#correct_email(username)
print('password')
password = "jmhcndupygyyuwvv"
#sender_email = email_id
smtp_server = 'smtp.gmail.com'
smtp_port = 587
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    print('Login successful!')
    read()
    server.quit()
except Exception as e:
    print('Login failed:', e)



#print(m)









