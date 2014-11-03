def frm_edit_tab(request, frm_key=0):
    """
    LLX Admin module - firm tab content: handles GET & POST from all tabs
    """
    usr_sess_data = UserSessionData(request)

    if int(frm_key) > 0:
        try:
            oFrm = Frm.objects.get(frm_key=frm_key)
            tModTitle = 'Firm: %s' % oFrm.frm_name
        except:
            return HttpResponse('')

    page = request.GET.get('page', 1)           # page of the parent subject list (ex. Frm list)
    mod_url = request.GET.get('mod_url', '')    # mod_url of the parent subject
    #tb = request.GET.get('tb', 0)              # 0 based tab number of the address tab in parent mod page

    sTemplate = 'llxadmin/accounts/law_firms/tabs/general.html'
    message = ''
    message_class = 'ui-state-error'

    request.session['back_url'] = '/%s/llxadmin/accounts/frm_edit/%s/%s/%s/' % (get_url_head(), frm_key, page, get_url_tail())

    if request.method == 'POST':
        tb = int(request.POST.get('jQuery-tabs-hidLastjQueryTab', 0))

        if tb == 0:   # --- TAB: General ---
            sTemplate = 'llxadmin/accounts/law_firms/tabs/general.html'
            form = FrmFormGeneral(request.POST, instance=oFrm, request=request)
            if form.is_valid():
                form.save(request=request)
                message = DATA_SAVED
                message_class = 'ui-state-highlight'
            else:
                message = VALIDATION_ERROR

        elif tb == 1:  # --- TAB: Addresses ---
            # obsolete: address are handled in common.views
            pass

        elif tb == 2:  # --- TAB: Phones ---
            # obsolete: phones are handled in common.views
            pass

        elif tb == 3:  # --- TAB: Users ---
            sTemplate = 'llxadmin/accounts/law_firms/tabs/users.html'
            SID = usr_sess_data.theSID_Key
            iUsrKey = usr_sess_data.theUSR_Key

        elif tb == 4:  # --- TAB: Billing ---
            sTemplate = 'llxadmin/accounts/law_firms/tabs/billing.html'

            update_allowed = False
            if 'USR_AdminBillingPrev' in request.session:
                update_allowed = int(request.session['USR_AdminBillingPrev'])

            show_update_button = 1 if update_allowed else 0

            if update_allowed:
                formBilling = FrmFormBilling(request.POST, instance=oFrm)

                if formBilling.is_valid():
                    formBilling.save(request=request)
                    message = DATA_SAVED
                    message_class = 'ui-state-highlight'
                else:
                    message = VALIDATION_ERROR

            else:
                formBilling = FrmFormBilling(instance=oFrm)

                show_update_button = 0
                if 'USR_AdminBillingPrev' in request.session:
                    show_update_button = request.session['USR_AdminBillingPrev']

    else:  # --------------- GET handler --------------------

        tb = int(request.GET.get('tb', '0'))

        if tb == 0:   # --- TAB: General ---

            # counter used on template to determine if the button "Update with latest default" is shown or not B14060
            count_proc_req = ProReq.objects.filter(pro_req_frm_key=oFrm.frm_key, pro_req_req_key = -1).count()

            sTemplate = 'llxadmin/accounts/law_firms/tabs/general.html'
            form = FrmFormGeneral(instance=oFrm, request=request)
            form.as_p()

        elif tb == 1:  # --- TAB: Addresses ---
            return redirect_to_url('/%s/common/list/add/%s/%s/?tb=%s&frm_key=%s' % (get_url_head(), table_numbers.get_tableMapping('FRM'), oFrm.pk, tb, oFrm.pk), request)

        elif tb == 2:  # --- TAB: Phones ---
            return redirect_to_url('/%s/common/list/phn/%s/%s/?tb=%s&frm_key=%s' % (get_url_head(), table_numbers.get_tableMapping('FRM'), oFrm.pk, tb, oFrm.pk), request)

        elif tb == 3:  # --- TAB: Users ---
            contacts = Con.objects.get_contacts(oFrm, usr_sess_data.theDomain)
            sTemplate = 'llxadmin/accounts/law_firms/tabs/users.html'

            SID = usr_sess_data.theSID_Key
            iUsrKey = usr_sess_data.theUSR_Key

            data = locals()
            if 'page' in data:
                del data['page']

            return send_html(request, sTemplate, data, queryset=contacts)

        elif tb == 4:  # --- TAB: Billing ---
            sTemplate = 'llxadmin/accounts/law_firms/tabs/billing.html'
            formBilling = FrmFormBilling(instance=oFrm)

            show_update_button = 0
            if 'USR_AdminBillingPrev' in request.session:
                show_update_button = request.session['USR_AdminBillingPrev']

    return send_html(request, sTemplate, locals())
