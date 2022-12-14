
"""
-*- coding: utf-8 -*-

Copyright ©2020 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# A sample script for using an incoming webhook for Hangouts chat rooms.
# [START hangouts_python_webhook]
from json import dumps

from httplib2 import Http


def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/7D8la4AAAAE/messages?key=' \
          'AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=' \
          'HulDviWFMz6R5FW-GwlO4INCW1cZGDDExuWVaEbbr_g%3D'
    bot_message = {
        'text': 'Hello from a Python script!'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)


if __name__ == '__main__':
    main()
# [END hangouts_python_webhook]
