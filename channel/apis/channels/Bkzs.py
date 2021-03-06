from utils.response import get_json_response
from django.views import View
import time


class Bkzs(View):
    def get(self, request, stu, user):
        token = stu.request('http://bkzs.hfut.edu.cn/f/ajax_get_csrfToken',
                            method='POST',
                            params={'n': '1'},
                            headers={
                                'X-Requested-With': 'XMLHttpRequest',
                                'X-Requested-Time': str(int(time.time() * 1000))
                            }).json()['data']
        data = stu.request('http://bkzs.hfut.edu.cn/f/newsCenter/ajax_article_list',
                           method='POST',
                           params={
                               'pageNo': request.GET['page'],
                               'pageSize': '20',
                               'categoryId': '833681b2bf25485cbe43bdf54b911407'
                           },
                           headers={
                               'Csrf-Token': token,
                               'X-Requested-Time': str(int(time.time() * 1000)),
                               'X-Requested-With': 'XMLHttpRequest'
                           }).json()
        response = []
        for item in data['data']['page']['list']:
            response.append({
                'id': item['id'],
                'title': item['title'],
                'url': item['url'],
                'author': item['publisher'],
                'time': time.strftime('%Y-%m-%d %H:%M', time.localtime(item['releaseDate'] / 1000)),
                'description': item['description'].strip()
            })
        return get_json_response(response)
