#  Copyright (c) 2022 https://reportportal.io .
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def test_report_portal_logging():
    """An example test with shows how to use standard python logger."""
    logger.info("Standard logger logs to Report Portal")
    assert True


def test_launch_url_get(rp_logger, rp_launch_id, rp_endpoint, rp_project):
    """
    This is a test which gets Launch ID, Report Portal endpoint and Project
    Name from fixtures in `conftest.py` and prints the result in logs, both: in
    console and on Report Portal
    """
    rp_logger.info("Got launch ID: %s", rp_launch_id)
    rp_logger.info("Launch URL: %s/ui/#%s/launches/all/%s", rp_endpoint,
                   rp_project, rp_launch_id)
    assert True


def test_attachment_logging(rp_logger):
    """This is a test which logs an image as byte array."""
    rp_logger.info("Log as byte array", attachment={
        "name": 'lucky_pug.jpg',
        "data": open('res/pug/lucky.jpg', 'rb').read(),
        "mime": 'image/jpeg',
    })
    assert True
