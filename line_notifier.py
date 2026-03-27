import requests

class LineNotifier:
    def __init__(self, access_token):
        self.access_token = access_token

    def send_alert(self, message):
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'messages': [{'type': 'text', 'text': message}]
        }
        response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=data)
        return response.status_code == 200

# Example usage:
if __name__ == '__main__':
    notifier = LineNotifier('YOUR_ACCESS_TOKEN')
    success = notifier.send_alert('This is a test alert!')
    print('Alert sent!' if success else 'Failed to send alert')