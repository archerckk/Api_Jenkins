import requests
import allure
import logging

@allure.feature('企业微信接口测试')
class TestWeWork:
    session = requests.Session()

    def setup(self):
        params = {
            "corpid": "ww5df43357194e9ba6",
            "corpsecret": "NUZ-NHi5wvrgYNp9NgnTbBezimNV5sBiWqxs3KdNLgk"
        }
        res = self.session.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)

        self.session.params.update({"access_token": res.json()['access_token']})
        print(self.session.params)

    @allure.story('测试添加成员')
    def test_add_member(self):
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "13800000001",
            "department": [1],
        }
        res = self.session.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create',
                                json=data)
        logging.info(f'接口返回结果为：{res.json()}' )
        assert res.json()["errmsg"] == 'created'

    @allure.story('测试获取成员')
    def test_get_member(self):
        params = {
            'userid': 'zhangsan'
        }
        res = self.session.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get', params=params)

        logging.info(f'接口返回结果为：{res.json()}' )
        assert res.json()['errmsg'] == 'ok'
        assert res.json()['userid'] == 'zhangsan'

    @allure.story('测试修改成员资料')
    def test_update_member(self):
        data = {
            'userid': 'zhangsan',
            'name': '王五'
        }
        res = self.session.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update',
                                json=data)

        logging.info(f'接口返回结果为：{res.json()}' )
        assert res.json()["errmsg"] == 'updated'

    @allure.story('测试删除成员')
    def test_delete_member(self):
        params = {
            'userid': 'zhangsan'
        }
        res = self.session.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete', params=params)
        logging.info(f'接口返回结果为：{res.json()}' )
        assert res.json()["errmsg"] == 'deleted'
