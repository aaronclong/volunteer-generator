""" Automatic Mark Down Generator for Code for Philly's Hackathon volunteers"""
import csv
import json
from urllib.request import urlopen
from trie import Trie
import yaml

class Volunteer:
    """ Simple Object for Storing and Formating Volunters for strings
    """
    def __init__(self, data):
        self.first_name = data[1]
        self.last_name = data[2]
        self.email = data[3]
        self.slack_handle = None
    def parse_slack(self, trie):
        """ Pass user list and match it with the user defined frome the csv
        """
        name = '{} {}'.format(self.first_name.lower(), self.last_name.lower())
        obj = trie.search(name)
        self.slack_handle = obj['name']
    def __str__(self):
        if self.slack_handle is None:
            return 'No handle'
        return '{} {} slack: {}'.format(self.first_name, self.last_name, self.slack_handle)

def get_users_slack(token):
    """ Pull Slack user list from the Code for Philly list
    """
    uri = 'https://slack.com/api/users.list?token=' + token
    response = urlopen(uri)
    data = json.loads(response.read())
    if data['ok'] is True:
        return data['members']
    else:
        raise Exception('Bad response from slack, check API token and server status')
    return False

def read_volunteers():
    """ Read all the volunters in and orchestrate their transformation
    """
    group = None # Will hold Volunteer Objects
    user_trie = Trie() # Will contain complete slack user list in JSON
    with open("volunteers.csv") as volunteers:
        reader = csv.reader(volunteers)
        group = [Volunteer(line) for line in reader]
    with open("config.yaml") as config:
        reader = yaml.load(config)
        user_list = get_users_slack(reader["slack"])
        for user in user_list:
            if 'real_name' not in user:
                continue
            user_trie.add(user['real_name'].lower(), user)
    map(lambda a: a.parse_slack(user_trie), group)
    for gr in group:
        print(gr)

if __name__ == '__main__':
    read_volunteers()
