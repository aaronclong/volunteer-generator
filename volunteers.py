""" Automatic Mark Down Generator for Code for Philly's Hackathon volunteers"""
import csv
import json
from urllib.request import urlopen
import yaml

class Volunteer:
    """ Simple Object for Storing and Formating Volunters for strings
    """
    def __init__(self, data):
        self.first_name = data[1]
        self.last_name = data[2]
        self.email = data[3]
        self.slack_handle = None
    def parse_slack(self, slack_list):
        """ Pass user list and match it with the user defined frome the csv
        """
        pass
    def __str__(self):
        if self.slack_handle is None:
            return
        print('{} {} \r{ {} \r}'.format(self.first_name, self.last_name, self.slack_handle))

def get_users_slack(token):
    """ Pull Slack user list from the Code for Philly list
    """
    uri = 'https://slack.com/api/users.list?token=' + token
    response = urlopen(uri)
    data = json.loads(response.read())
    if data['ok'] is True:
        pass
    else:
        raise Exception('Bad response from slack, check API token and server status')
    return False

def read_volunteers():
    """ Read all the volunters in and orchestrate their transformation
    """
    group = None # Will hold Volunteer Objects
    user_list = None # Will contain complete slack user list in JSON
    with open("volunteers.csv") as volunteers:
        reader = csv.reader(volunteers)
        group = [Volunteer(line) for line in reader]
    with open("config.yaml") as config:
        reader = yaml.load(config)
        user_list = get_users_slack(reader["slack"])
    map(lambda a: a.parse_slack(user_list), group)

if __name__ == '__main__':
    read_volunteers()
