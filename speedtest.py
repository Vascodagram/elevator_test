from cgi import print_form
import subprocess

def get_password_wifi():
    profile = subprocess.check_output('netsh wlan show profiles').decode.split('\n')
    # print(profile)

    profiles = [i.split(':')[1].strip() for i in profile if 'All User Profile' in i]
    print(profiles)
    for

get_password_wifi()
