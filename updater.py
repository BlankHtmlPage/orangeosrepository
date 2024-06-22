from time import sleep as w
from os import system as sys

w(2)
with open('updOrangeOS_Beta.exe', 'rb') as new_file:
    with open('OrangeOS_Beta.exe', 'wb') as old_file:
        old_file.write(new_file.read())
        print('Updated. Restarting...')
        sys('rm updOrangeOS_Beta.exe||del updOrangeOS_Beta.exe')
        sys('OrangeOS_Beta.exe')
        exit(666)
        
