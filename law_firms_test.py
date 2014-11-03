{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;\f2\fnil\fcharset0 Menlo-Italic;
}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red67\green67\blue67;\red53\green65\blue117;
\red133\green0\blue2;\red135\green135\blue135;\red14\green114\blue164;\red17\green137\blue135;\red210\green0\blue53;
\red135\green136\blue117;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360

\f0\b\fs24 \cf2 from
\f1\b0  \cf3 datetime\cf2  
\f0\b import
\f1\b0  date, timedelta\

\f0\b import
\f1\b0  \cf3 json\cf2 \

\f0\b from
\f1\b0  \cf3 django.middleware.csrf\cf2  
\f0\b import
\f1\b0  _get_new_csrf_key\

\f0\b from
\f1\b0  \cf3 pyquery\cf2  
\f0\b import
\f1\b0  PyQuery 
\f0\b as
\f1\b0  pq\

\f0\b from
\f1\b0  \cf3 _const.messages\cf2  
\f0\b import
\f1\b0  DATA_SAVED\

\f0\b from
\f1\b0  \cf3 _models.con\cf2  
\f0\b import
\f1\b0  Con\

\f0\b from
\f1\b0  \cf3 settings\cf2  
\f0\b import
\f1\b0  CSRF_COOKIE_NAME\

\f0\b from
\f1\b0  \cf3 tests.integration.base_test_case\cf2  
\f0\b import
\f1\b0  BaseTestCase\

\f0\b from
\f1\b0  \cf3 tests.factories.con_factory\cf2  
\f0\b import
\f1\b0  ConFactory\

\f0\b from
\f1\b0  \cf3 tests.factories.frm_factory\cf2  
\f0\b import
\f1\b0  FrmFactory\

\f0\b from
\f1\b0  \cf3 tests.factories.lst_factory\cf2  
\f0\b import
\f1\b0  LstFactory\

\f0\b from
\f1\b0  \cf3 tests.factories.sid_factory\cf2  
\f0\b import
\f1\b0  SidFactory\

\f0\b from
\f1\b0  \cf3 tests.factories.usr_factory\cf2  
\f0\b import
\f1\b0  UsrFactory\

\f0\b from
\f1\b0  \cf3 tests.factories.const_factory\cf2  
\f0\b import
\f1\b0  ConstFactory\

\f0\b from
\f1\b0  \cf3 utils.web.parse_html\cf2  
\f0\b import
\f1\b0  extract_html_form_fields\
\
\

\f0\b class
\f1\b0  
\f0\b \cf4 LawFirmsTest
\f1\b0 \cf2 (BaseTestCase):\
\
\'a0\'a0\'a0\'a0
\f0\b def
\f1\b0  
\f0\b \cf5 setUp
\f1\b0 \cf2 (\cf6 self\cf2 ):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf7 super\cf2 (LawFirmsTest, \cf6 self\cf2 )
\f0\b .
\f1\b0 setUp()\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf6 self
\f0\b \cf2 .
\f1\b0 execute_functions_sql()\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf6 self
\f0\b \cf2 .
\f1\b0 oSid 
\f0\b =
\f1\b0  SidFactory
\f0\b .
\f1\b0 create(sid_expires_date
\f0\b =
\f1\b0 date
\f0\b .
\f1\b0 today() 
\f0\b +
\f1\b0  timedelta(days
\f0\b =
\f1\b0 \cf8 1\cf2 ), sid_the_domain
\f0\b =
\f1\b0 \cf9 'ADM'\cf2 , sid_ip_address
\f0\b =
\f1\b0 \cf9 '100.0.0.0'\cf2 , sid_con_key
\f0\b =
\f1\b0 \cf8 1\cf2 , sid_usr_key
\f0\b =
\f1\b0 \cf8 234\cf2 , sid_frm_key
\f0\b =
\f1\b0 \cf8 50002\cf2 )\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 cookies[\cf9 'adm_sid'\cf2 ] 
\f0\b =
\f1\b0  \cf6 self
\f0\b \cf2 .
\f1\b0 oSid
\f0\b .
\f1\b0 sid_uuid\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 cookies[CSRF_COOKIE_NAME] 
\f0\b =
\f1\b0  _get_new_csrf_key()\
\
\'a0\'a0\'a0\'a0
\f0\b def
\f1\b0  
\f0\b \cf5 test_search_firm
\f1\b0 \cf2 (\cf6 self\cf2 ):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf10 # 1. Create some firms
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0x 
\f0\b =
\f1\b0  \cf8 1\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b while
\f1\b0  x 
\f0\b <=
\f1\b0  \cf8 5\cf2 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0Frm
\f0\b .
\f1\b0 objects
\f0\b .
\f1\b0 create(frm_name
\f0\b =
\f1\b0 \cf9 "Firm %s"\cf2  
\f0\b %
\f1\b0  x)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0x 
\f0\b +=
\f1\b0  \cf8 1\cf2 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf10 # 2. New firm (different name)
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0Frm
\f0\b .
\f1\b0 objects
\f0\b .
\f1\b0 create(frm_name
\f0\b =
\f1\b0 \cf9 "Test"\cf2 )\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf10 # 3. Search for non existent
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0resp 
\f0\b =
\f1\b0  \cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 post(\cf9 '/pgate/llxadmin/accounts/frm_list/'\cf2 , \{\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'q'\cf2 : \cf9 'I am not here'\cf2 ,\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'action'\cf2 : \cf9 'global-search'\cf2 ,\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'csrftoken'\cf2 : \cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 cookies[CSRF_COOKIE_NAME]\})\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf6 self
\f0\b \cf2 .
\f1\b0 assertContains(resp, \cf9 "No Records Found"\cf2 )\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf10 # 4. Search for "Test" firm (1 record)
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0resp 
\f0\b =
\f1\b0  \cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 post(\cf9 '/pgate/llxadmin/accounts/frm_list/'\cf2 , \{\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'q'\cf2 : \cf9 'Test'\cf2 ,\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'action'\cf2 : \cf9 'global-search'\cf2 ,\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'csrftoken'\cf2 : \cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 cookies[CSRF_COOKIE_NAME]\})\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0j 
\f0\b =
\f1\b0  pq(resp
\f0\b .
\f1\b0 content)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0tr_list 
\f0\b =
\f1\b0  j(\cf9 "table.list tbody tr"\cf2 )\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf6 self
\f0\b \cf2 .
\f1\b0 assertEqual(\cf7 len\cf2 (tr_list), \cf8 1\cf2 )\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf10 # 5. Search for "Firm" (5 records)
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0resp 
\f0\b =
\f1\b0  \cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 post(\cf9 '/pgate/llxadmin/accounts/frm_list/'\cf2 , \{\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'q'\cf2 : \cf9 'firm'\cf2 ,\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'action'\cf2 : \cf9 'global-search'\cf2 ,\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf9 'csrftoken'\cf2 : \cf6 self
\f0\b \cf2 .
\f1\b0 client
\f0\b .
\f1\b0 cookies[CSRF_COOKIE_NAME]\})\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0j 
\f0\b =
\f1\b0  pq(resp
\f0\b .
\f1\b0 content)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0tr_list 
\f0\b =
\f1\b0  j(\cf9 "table.list tbody tr"\cf2 )\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf6 self
\f0\b \cf2 .
\f1\b0 assertEqual(\cf7 len\cf2 (tr_list), \cf8 5\cf2 )\
}