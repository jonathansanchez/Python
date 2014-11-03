from datetime import date, timedelta
import json
from django.middleware.csrf import _get_new_csrf_key
from pyquery import PyQuery as pq
from _const.messages import DATA_SAVED
from _models.con import Con
from settings import CSRF_COOKIE_NAME
from tests.integration.base_test_case import BaseTestCase
from tests.factories.con_factory import ConFactory
from tests.factories.frm_factory import FrmFactory
from tests.factories.lst_factory import LstFactory
from tests.factories.sid_factory import SidFactory
from tests.factories.usr_factory import UsrFactory
from tests.factories.const_factory import ConstFactory
from utils.web.parse_html import extract_html_form_fields


class LawFirmsTest(BaseTestCase):

    def setUp(self):
        super(LawFirmsTest, self).setUp()
        self.execute_functions_sql()
        self.oSid = SidFactory.create(sid_expires_date=date.today() + timedelta(days=1), sid_the_domain='ADM', sid_ip_address='100.0.0.0', sid_con_key=1, sid_usr_key=234, sid_frm_key=50002)
        self.client.cookies['adm_sid'] = self.oSid.sid_uuid
        self.client.cookies[CSRF_COOKIE_NAME] = _get_new_csrf_key()

    def test_search_firm(self):
        # 1. Create some firms
        x = 1
        while x <= 5:
            Frm.objects.create(frm_name="Firm %s" % x)
            x += 1

        # 2. New firm (different name)
        Frm.objects.create(frm_name="Test")

        # 3. Search for non existent
        resp = self.client.post('/pgate/llxadmin/accounts/frm_list/', {
            'q': 'I am not here',
            'action': 'global-search',
            'csrftoken': self.client.cookies[CSRF_COOKIE_NAME]})
        self.assertContains(resp, "No Records Found")

        # 4. Search for "Test" firm (1 record)
        resp = self.client.post('/pgate/llxadmin/accounts/frm_list/', {
            'q': 'Test',
            'action': 'global-search',
            'csrftoken': self.client.cookies[CSRF_COOKIE_NAME]})
        j = pq(resp.content)
        tr_list = j("table.list tbody tr")
        self.assertEqual(len(tr_list), 1)

        # 5. Search for "Firm" (5 records)
        resp = self.client.post('/pgate/llxadmin/accounts/frm_list/', {
            'q': 'firm',
            'action': 'global-search',
            'csrftoken': self.client.cookies[CSRF_COOKIE_NAME]})
        j = pq(resp.content)
        tr_list = j("table.list tbody tr")
        self.assertEqual(len(tr_list), 5)
