# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import pytest

from selenium.webdriver.edge.options import Options


@pytest.fixture
def options():
    return Options()


def test_raises_exception_with_invalid_page_load_strategy(options):
    with pytest.raises(ValueError):
        options.page_load_strategy = 'never'


def test_set_page_load_strategy(options):
    options.page_load_strategy = 'normal'
    assert options._page_load_strategy == 'normal'


def test_get_page_load_strategy(options):
    options._page_load_strategy = 'normal'
    assert options.page_load_strategy == 'normal'


def test_creates_capabilities(options):
    options.page_load_strategy = 'eager'
    caps = options.to_capabilities()
    assert caps['pageLoadStrategy'] == 'eager'


def test_starts_with_default_capabilities(options):
    from selenium.webdriver import DesiredCapabilities
    assert options._caps == DesiredCapabilities.EDGE


def test_is_a_baseoptions(options):
    from selenium.webdriver.common.options import BaseOptions
    assert isinstance(options, BaseOptions)

def test_custom_browser_name():
    options = Options(is_legacy=False)
    options.custom_browser_name = "testbrowsername"
    caps = options.to_capabilities()
    assert caps['browserName'] == "testbrowsername"
