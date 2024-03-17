import urllib3
import json
from datetime import datetime
import os

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

http = urllib3.PoolManager()
def monitor_ecsx_command(event, context):
    try:
        event_name = event.get("event_name", None)
        cluster_name = event.get("cluster_name", None)
        user_arn = event.get("user_arn", None)
        user_ip = event.get("user_ip", None)
        container_name = event.get("container_name", None)
        time_stamp = event.get("time_stamp", None)
        
        emoji = ':information_source:'
        
        date_format = '%Y-%m-%dT%H:%M:%S%z'
        
        date_obj = datetime.strptime(time_stamp, date_format)
        
        format = '%Y-%m-%d %H:%M %p (Beirut Time)'
        
        timestamp = date_obj.strftime(format)
        
        text = f'{emoji} *Detected an {event_name}* \n\n • *Cluster Name*: {cluster_name} \n • *Container Name*: {container_name} \n • *User ARN*: {user_arn} \n • *User IP*: {user_ip} \n • *Time Stamp*: {timestamp} \n '

        msg = {
            "channel": "aws-logins",
            "text": text,
            "icon_emoji": ""
        }
    
        encoded_msg = json.dumps(msg).encode('utf-8')
        resp = http.request('POST',SLACK_WEBHOOK_URL, body=encoded_msg)
        return resp.status
    except Exception as e:
        print(e.__traceback__)
        print(e.with_traceback)
        return e