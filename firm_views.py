{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;\f2\fnil\fcharset0 Menlo-Italic;
}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red133\green0\blue2;\red17\green137\blue135;
\red210\green0\blue53;\red14\green114\blue164;\red135\green136\blue117;\red135\green135\blue135;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360

\f0\b\fs24 \cf2 def
\f1\b0  
\f0\b \cf3 frm_edit_tab
\f1\b0 \cf2 (request, frm_key
\f0\b =
\f1\b0 \cf4 0\cf2 ):\
\'a0\'a0\'a0\'a0\cf5 """\cf2 \
\pard\pardeftab720\sl360
\cf5     LLX Admin module - firm tab content: handles GET & POST from all tabs\cf2 \
\cf5     """\cf2 \
\'a0\'a0\'a0\'a0usr_sess_data 
\f0\b =
\f1\b0  UserSessionData(request)\
\
\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  \cf6 int\cf2 (frm_key) 
\f0\b >
\f1\b0  \cf4 0\cf2 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b try
\f1\b0 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0oFrm 
\f0\b =
\f1\b0  Frm
\f0\b .
\f1\b0 objects
\f0\b .
\f1\b0 get(frm_key
\f0\b =
\f1\b0 frm_key)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0tModTitle 
\f0\b =
\f1\b0  \cf5 'Firm: %s'\cf2  
\f0\b %
\f1\b0  oFrm
\f0\b .
\f1\b0 frm_name\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b except
\f1\b0 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b return
\f1\b0  HttpResponse(\cf5 ''\cf2 )\
\
\'a0\'a0\'a0\'a0page 
\f0\b =
\f1\b0  request
\f0\b .
\f1\b0 GET
\f0\b .
\f1\b0 get(\cf5 'page'\cf2 , \cf4 1\cf2 )           
\f2\i \cf7 # page of the parent subject list (ex. Frm list)
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0mod_url 
\f0\b =
\f1\b0  request
\f0\b .
\f1\b0 GET
\f0\b .
\f1\b0 get(\cf5 'mod_url'\cf2 , \cf5 ''\cf2 )    
\f2\i \cf7 # mod_url of the parent subject
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0
\f2\i \cf7 #tb = request.GET.get('tb', 0)              # 0 based tab number of the address tab in parent mod page
\f1\i0 \cf2 \
\
\'a0\'a0\'a0\'a0sTemplate 
\f0\b =
\f1\b0  \cf5 'llxadmin/accounts/law_firms/tabs/general.html'\cf2 \
\'a0\'a0\'a0\'a0message 
\f0\b =
\f1\b0  \cf5 ''\cf2 \
\'a0\'a0\'a0\'a0message_class 
\f0\b =
\f1\b0  \cf5 'ui-state-error'\cf2 \
\
\'a0\'a0\'a0\'a0request
\f0\b .
\f1\b0 session[\cf5 'back_url'\cf2 ] 
\f0\b =
\f1\b0  \cf5 '/%s/llxadmin/accounts/frm_edit/%s/%s/%s/'\cf2  
\f0\b %
\f1\b0  (get_url_head(), frm_key, page, get_url_tail())\
\
\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  request
\f0\b .
\f1\b0 method 
\f0\b ==
\f1\b0  \cf5 'POST'\cf2 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0tb 
\f0\b =
\f1\b0  \cf6 int\cf2 (request
\f0\b .
\f1\b0 POST
\f0\b .
\f1\b0 get(\cf5 'jQuery-tabs-hidLastjQueryTab'\cf2 , \cf4 0\cf2 ))\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 0\cf2 :   
\f2\i \cf7 # --- TAB: General ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0sTemplate 
\f0\b =
\f1\b0  \cf5 'llxadmin/accounts/law_firms/tabs/general.html'\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0form 
\f0\b =
\f1\b0  FrmFormGeneral(request
\f0\b .
\f1\b0 POST, instance
\f0\b =
\f1\b0 oFrm, request
\f0\b =
\f1\b0 request)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  form
\f0\b .
\f1\b0 is_valid():\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0form
\f0\b .
\f1\b0 save(request
\f0\b =
\f1\b0 request)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0message 
\f0\b =
\f1\b0  DATA_SAVED\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0message_class 
\f0\b =
\f1\b0  \cf5 'ui-state-highlight'\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b else
\f1\b0 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0message 
\f0\b =
\f1\b0  VALIDATION_ERROR\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 1\cf2 :  
\f2\i \cf7 # --- TAB: Addresses ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf7 # obsolete: address are handled in common.views
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b pass
\f1\b0 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 2\cf2 :  
\f2\i \cf7 # --- TAB: Phones ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf7 # obsolete: phones are handled in common.views
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b pass
\f1\b0 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 3\cf2 :  
\f2\i \cf7 # --- TAB: Users ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0sTemplate 
\f0\b =
\f1\b0  \cf5 'llxadmin/accounts/law_firms/tabs/users.html'\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0SID 
\f0\b =
\f1\b0  usr_sess_data
\f0\b .
\f1\b0 theSID_Key\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0iUsrKey 
\f0\b =
\f1\b0  usr_sess_data
\f0\b .
\f1\b0 theUSR_Key\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 4\cf2 :  
\f2\i \cf7 # --- TAB: Billing ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0sTemplate 
\f0\b =
\f1\b0  \cf5 'llxadmin/accounts/law_firms/tabs/billing.html'\cf2 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0update_allowed 
\f0\b =
\f1\b0  \cf8 False\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  \cf5 'USR_AdminBillingPrev'\cf2  
\f0\b in
\f1\b0  request
\f0\b .
\f1\b0 session:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0update_allowed 
\f0\b =
\f1\b0  \cf6 int\cf2 (request
\f0\b .
\f1\b0 session[\cf5 'USR_AdminBillingPrev'\cf2 ])\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0show_update_button 
\f0\b =
\f1\b0  \cf4 1\cf2  
\f0\b if
\f1\b0  update_allowed 
\f0\b else
\f1\b0  \cf4 0\cf2 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  update_allowed:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0formBilling 
\f0\b =
\f1\b0  FrmFormBilling(request
\f0\b .
\f1\b0 POST, instance
\f0\b =
\f1\b0 oFrm)\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  formBilling
\f0\b .
\f1\b0 is_valid():\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0formBilling
\f0\b .
\f1\b0 save(request
\f0\b =
\f1\b0 request)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0message 
\f0\b =
\f1\b0  DATA_SAVED\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0message_class 
\f0\b =
\f1\b0  \cf5 'ui-state-highlight'\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b else
\f1\b0 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0message 
\f0\b =
\f1\b0  VALIDATION_ERROR\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b else
\f1\b0 :\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0formBilling 
\f0\b =
\f1\b0  FrmFormBilling(instance
\f0\b =
\f1\b0 oFrm)\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0show_update_button 
\f0\b =
\f1\b0  \cf4 0\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  \cf5 'USR_AdminBillingPrev'\cf2  
\f0\b in
\f1\b0  request
\f0\b .
\f1\b0 session:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0show_update_button 
\f0\b =
\f1\b0  request
\f0\b .
\f1\b0 session[\cf5 'USR_AdminBillingPrev'\cf2 ]\
\
\'a0\'a0\'a0\'a0
\f0\b else
\f1\b0 :  
\f2\i \cf7 # --------------- GET handler --------------------
\f1\i0 \cf2 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0tb 
\f0\b =
\f1\b0  \cf6 int\cf2 (request
\f0\b .
\f1\b0 GET
\f0\b .
\f1\b0 get(\cf5 'tb'\cf2 , \cf5 '0'\cf2 ))\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 0\cf2 :   
\f2\i \cf7 # --- TAB: General ---
\f1\i0 \cf2 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f2\i \cf7 # counter used on template to determine if the button "Update with latest default" is shown or not B14060
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0count_proc_req 
\f0\b =
\f1\b0  ProReq
\f0\b .
\f1\b0 objects
\f0\b .
\f1\b0 filter(pro_req_frm_key
\f0\b =
\f1\b0 oFrm
\f0\b .
\f1\b0 frm_key, pro_req_req_key 
\f0\b =
\f1\b0  
\f0\b -
\f1\b0 \cf4 1\cf2 )
\f0\b .
\f1\b0 count()\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0sTemplate 
\f0\b =
\f1\b0  \cf5 'llxadmin/accounts/law_firms/tabs/general.html'\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0form 
\f0\b =
\f1\b0  FrmFormGeneral(instance
\f0\b =
\f1\b0 oFrm, request
\f0\b =
\f1\b0 request)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0form
\f0\b .
\f1\b0 as_p()\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 1\cf2 :  
\f2\i \cf7 # --- TAB: Addresses ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b return
\f1\b0  redirect_to_url(\cf5 '/%s/common/list/add/%s/%s/?tb=%s&frm_key=%s'\cf2  
\f0\b %
\f1\b0  (get_url_head(), table_numbers
\f0\b .
\f1\b0 get_tableMapping(\cf5 'FRM'\cf2 ), oFrm
\f0\b .
\f1\b0 pk, tb, oFrm
\f0\b .
\f1\b0 pk), request)\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 2\cf2 :  
\f2\i \cf7 # --- TAB: Phones ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b return
\f1\b0  redirect_to_url(\cf5 '/%s/common/list/phn/%s/%s/?tb=%s&frm_key=%s'\cf2  
\f0\b %
\f1\b0  (get_url_head(), table_numbers
\f0\b .
\f1\b0 get_tableMapping(\cf5 'FRM'\cf2 ), oFrm
\f0\b .
\f1\b0 pk, tb, oFrm
\f0\b .
\f1\b0 pk), request)\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 3\cf2 :  
\f2\i \cf7 # --- TAB: Users ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0contacts 
\f0\b =
\f1\b0  Con
\f0\b .
\f1\b0 objects
\f0\b .
\f1\b0 get_contacts(oFrm, usr_sess_data
\f0\b .
\f1\b0 theDomain)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0sTemplate 
\f0\b =
\f1\b0  \cf5 'llxadmin/accounts/law_firms/tabs/users.html'\cf2 \
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0SID 
\f0\b =
\f1\b0  usr_sess_data
\f0\b .
\f1\b0 theSID_Key\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0iUsrKey 
\f0\b =
\f1\b0  usr_sess_data
\f0\b .
\f1\b0 theUSR_Key\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0data 
\f0\b =
\f1\b0  \cf6 locals\cf2 ()\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  \cf5 'page'\cf2  
\f0\b in
\f1\b0  data:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b del
\f1\b0  data[\cf5 'page'\cf2 ]\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b return
\f1\b0  send_html(request, sTemplate, data, queryset
\f0\b =
\f1\b0 contacts)\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b elif
\f1\b0  tb 
\f0\b ==
\f1\b0  \cf4 4\cf2 :  
\f2\i \cf7 # --- TAB: Billing ---
\f1\i0 \cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0sTemplate 
\f0\b =
\f1\b0  \cf5 'llxadmin/accounts/law_firms/tabs/billing.html'\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0formBilling 
\f0\b =
\f1\b0  FrmFormBilling(instance
\f0\b =
\f1\b0 oFrm)\
\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0show_update_button 
\f0\b =
\f1\b0  \cf4 0\cf2 \
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0
\f0\b if
\f1\b0  \cf5 'USR_AdminBillingPrev'\cf2  
\f0\b in
\f1\b0  request
\f0\b .
\f1\b0 session:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0show_update_button 
\f0\b =
\f1\b0  request
\f0\b .
\f1\b0 session[\cf5 'USR_AdminBillingPrev'\cf2 ]\
\
\'a0\'a0\'a0\'a0
\f0\b return
\f1\b0  send_html(request, sTemplate, \cf6 locals\cf2 ())\
}