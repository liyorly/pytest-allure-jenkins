import os

import pytest
import requests

from pytestJenkins.yaml_util import ReadYaml


class TestPytestJenkins:


    @pytest.mark.parametrize('args',ReadYaml(os.getcwd()+'/pytestJenkins/test01.yaml').readYaml())
    def test_01(self,args):
        url=args['request']['url']
        params=args['request']['params']
        res = requests.get(url,params=params)
        print('响应结果：'+res.text)