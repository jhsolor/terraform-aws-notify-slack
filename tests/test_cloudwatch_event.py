import unittest, json, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/functions')
from notify_slack import *
from mock import patch, Mock
@patch('urllib.request.urlopen')

class CloudWatchEventTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['SLACK_WEBHOOK_URL'] = 'http://localhost/'
        os.environ['SLACK_CHANNEL'] = 'slack-notify-test-channel'
        os.environ['SLACK_USERNAME'] = 'slack-notify-test-user'
        os.environ['SLACK_EMOJI'] = ':aws:'

    # Basic test just makes sure the code doesn't throw an exception on the happy path.
    def test_lambda_handler_cloudwatch_alarm(self, mock_urlopen):
        a = Mock()
        a.read.side_effect = ['200 OK']
        mock_urlopen.return_value = a
        fixture = open(os.path.dirname(os.path.abspath(__file__)) + '/test_cloudwatch_alarm.json', 'r')
        test_event = json.loads(fixture.read())
        fixture.close()
        lambda_handler(test_event,"")

    # Basic test just makes sure the code doesn't throw an exception on the happy path.
    def test_lambda_handler_cloudwatch_event(self, mock_urlopen):
        a = Mock()
        a.read.side_effect = ['200 OK']
        mock_urlopen.return_value = a
        fixture = open(os.path.dirname(os.path.abspath(__file__)) + '/test_cloudwatch_event.json', 'r')
        test_event = json.loads(fixture.read())
        fixture.close()
        lambda_handler(test_event,"")

if __name__ == '__main__':
    unittest.main()