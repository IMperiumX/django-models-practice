# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BadgesBadgeitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.OneToOneField('PretixbaseItem', models.DO_NOTHING, blank=True, null=True)
    layout = models.ForeignKey('BadgesBadgelayout', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'badges_badgeitem'


class BadgesBadgelayout(models.Model):
    id = models.BigAutoField(primary_key=True)
    default = models.BooleanField()
    name = models.CharField(max_length=190)
    layout = models.TextField()
    background = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'badges_badgelayout'


class BanktransferBankimportjob(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    state = models.CharField(max_length=32)
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING, blank=True, null=True)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banktransfer_bankimportjob'


class BanktransferBanktransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=32)
    message = models.TextField()
    checksum = models.CharField(max_length=190)
    payer = models.TextField()
    reference = models.TextField()
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    date = models.CharField(max_length=50)
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING, blank=True, null=True)
    import_job = models.ForeignKey(BanktransferBankimportjob, models.DO_NOTHING)
    order = models.ForeignKey('PretixbaseOrder', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, blank=True, null=True)
    bic = models.CharField(max_length=250)
    date_parsed = models.DateField(blank=True, null=True)
    iban = models.CharField(max_length=250)
    currency = models.CharField(max_length=10, blank=True, null=True)
    external_id = models.CharField(max_length=190, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banktransfer_banktransaction'
        unique_together = (('event', 'organizer', 'checksum'),)


class BanktransferRefundexport(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    testmode = models.BooleanField()
    rows = models.TextField()
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING, blank=True, null=True)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, blank=True, null=True)
    downloaded = models.BooleanField()
    currency = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banktransfer_refundexport'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OtpStaticStaticdevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)
    throttling_failure_count = models.IntegerField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_static_staticdevice'


class OtpStaticStatictoken(models.Model):
    token = models.CharField(max_length=16)
    device = models.ForeignKey(OtpStaticStaticdevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'otp_static_statictoken'


class OtpTotpTotpdevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    key = models.CharField(max_length=80)
    step = models.SmallIntegerField()
    t0 = models.BigIntegerField()
    digits = models.SmallIntegerField()
    tolerance = models.SmallIntegerField()
    drift = models.SmallIntegerField()
    last_t = models.BigIntegerField()
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)
    throttling_failure_count = models.IntegerField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_totp_totpdevice'


class PaypalReferencedpaypalobject(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference = models.CharField(unique=True, max_length=190)
    order = models.ForeignKey('PretixbaseOrder', models.DO_NOTHING)
    payment = models.ForeignKey('PretixbaseOrderpayment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_referencedpaypalobject'


class PretixapiApicall(models.Model):
    id = models.BigAutoField(primary_key=True)
    idempotency_key = models.CharField(max_length=190)
    auth_hash = models.CharField(max_length=190)
    created = models.DateTimeField()
    locked = models.DateTimeField(blank=True, null=True)
    request_method = models.CharField(max_length=20)
    request_path = models.CharField(max_length=255)
    response_code = models.IntegerField()
    response_headers = models.TextField()
    response_body = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'pretixapi_apicall'
        unique_together = (('idempotency_key', 'auth_hash'),)


class PretixapiOauthaccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey('PretixapiOauthapplication', models.DO_NOTHING, blank=True, null=True)
    source_refresh_token = models.OneToOneField('PretixapiOauthrefreshtoken', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING, blank=True, null=True)
    id_token = models.OneToOneField('PretixapiOauthidtoken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthaccesstoken'


class PretixapiOauthaccesstokenOrganizers(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauthaccesstoken = models.ForeignKey(PretixapiOauthaccesstoken, models.DO_NOTHING)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthaccesstoken_organizers'
        unique_together = (('oauthaccesstoken', 'organizer'),)


class PretixapiOauthapplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    skip_authorization = models.BooleanField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    name = models.CharField(max_length=255)
    redirect_uris = models.TextField()
    client_id = models.CharField(unique=True, max_length=100)
    client_secret = models.CharField(max_length=255)
    active = models.BooleanField()
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING, blank=True, null=True)
    algorithm = models.CharField(max_length=5)
    post_logout_redirect_uris = models.TextField()

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthapplication'


class PretixapiOauthgrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=2500)
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey(PretixapiOauthapplication, models.DO_NOTHING)
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)
    claims = models.TextField()
    code_challenge = models.CharField(max_length=128)
    code_challenge_method = models.CharField(max_length=10)
    nonce = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthgrant'


class PretixapiOauthgrantOrganizers(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauthgrant = models.ForeignKey(PretixapiOauthgrant, models.DO_NOTHING)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthgrant_organizers'
        unique_together = (('oauthgrant', 'organizer'),)


class PretixapiOauthidtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    jti = models.UUIDField(unique=True)
    expires = models.DateTimeField()
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey(PretixapiOauthapplication, models.DO_NOTHING)
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthidtoken'


class PretixapiOauthidtokenOrganizers(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauthidtoken = models.ForeignKey(PretixapiOauthidtoken, models.DO_NOTHING)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthidtoken_organizers'
        unique_together = (('oauthidtoken', 'organizer'),)


class PretixapiOauthrefreshtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    revoked = models.DateTimeField(blank=True, null=True)
    access_token = models.OneToOneField(PretixapiOauthaccesstoken, models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(PretixapiOauthapplication, models.DO_NOTHING)
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixapi_oauthrefreshtoken'
        unique_together = (('token', 'revoked'),)


class PretixapiWebhook(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    target_url = models.CharField(max_length=255)
    all_events = models.BooleanField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixapi_webhook'


class PretixapiWebhookLimitEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    webhook = models.ForeignKey(PretixapiWebhook, models.DO_NOTHING)
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixapi_webhook_limit_events'
        unique_together = (('webhook', 'event'),)


class PretixapiWebhookcall(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    target_url = models.CharField(max_length=255)
    is_retry = models.BooleanField()
    execution_time = models.FloatField(blank=True, null=True)
    return_code = models.IntegerField()
    payload = models.TextField()
    response_body = models.TextField()
    webhook = models.ForeignKey(PretixapiWebhook, models.DO_NOTHING)
    success = models.BooleanField()
    action_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pretixapi_webhookcall'


class PretixapiWebhookcallretry(models.Model):
    id = models.BigAutoField(primary_key=True)
    retry_not_before = models.DateTimeField()
    retry_count = models.IntegerField()
    action_type = models.CharField(max_length=255)
    logentry = models.ForeignKey('PretixbaseLogentry', models.DO_NOTHING)
    webhook = models.ForeignKey(PretixapiWebhook, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixapi_webhookcallretry'
        unique_together = (('webhook', 'logentry'),)


class PretixapiWebhookeventlistener(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_type = models.CharField(max_length=255)
    webhook = models.ForeignKey(PretixapiWebhook, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixapi_webhookeventlistener'


class PretixbaseAttendeeprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    attendee_name_cached = models.CharField(max_length=255, blank=True, null=True)
    attendee_name_parts = models.JSONField()
    attendee_email = models.CharField(max_length=254, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    answers = models.JSONField()
    customer = models.ForeignKey('PretixbaseCustomer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_attendeeprofile'


class PretixbaseBlockedticketsecret(models.Model):
    id = models.BigAutoField(primary_key=True)
    secret = models.TextField()
    blocked = models.BooleanField()
    updated = models.DateTimeField()
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING)
    position = models.ForeignKey('PretixbaseOrderposition', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_blockedticketsecret'
        unique_together = (('event', 'secret'),)


class PretixbaseCachedcombinedticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    file = models.CharField(max_length=255, blank=True, null=True)
    order = models.ForeignKey('PretixbaseOrder', models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pretixbase_cachedcombinedticket'


class PretixbaseCachedfile(models.Model):
    id = models.UUIDField(primary_key=True)
    expires = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    filename = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    file = models.CharField(max_length=255, blank=True, null=True)
    session_key = models.TextField(blank=True, null=True)
    web_download = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_cachedfile'


class PretixbaseCachedticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=255)
    order_position = models.ForeignKey('PretixbaseOrderposition', models.DO_NOTHING)
    extension = models.CharField(max_length=255)
    file = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pretixbase_cachedticket'


class PretixbaseCancellationrequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    cancellation_fee = models.DecimalField(max_digits=13, decimal_places=2)
    refund_as_giftcard = models.BooleanField()
    order = models.ForeignKey('PretixbaseOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_cancellationrequest'


class PretixbaseCartposition(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    attendee_name_cached = models.CharField(max_length=255, blank=True, null=True)
    cart_id = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField()
    expires = models.DateTimeField()
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING)
    item = models.ForeignKey('PretixbaseItem', models.DO_NOTHING)
    variation = models.ForeignKey('PretixbaseItemvariation', models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey('PretixbaseVoucher', models.DO_NOTHING, blank=True, null=True)
    attendee_email = models.CharField(max_length=254, blank=True, null=True)
    addon_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    meta_info = models.TextField(blank=True, null=True)
    subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)
    attendee_name_parts = models.JSONField()
    is_bundled = models.BooleanField()
    seat = models.ForeignKey('PretixbaseSeat', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    used_membership = models.ForeignKey('PretixbaseMembership', models.DO_NOTHING, blank=True, null=True)
    custom_price_input = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    custom_price_input_is_net = models.BooleanField()
    line_price_gross = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    listed_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    price_after_voucher = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.ForeignKey('PretixbaseDiscount', models.DO_NOTHING, blank=True, null=True)
    requested_valid_from = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_cartposition'


class PretixbaseCheckin(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    position = models.ForeignKey('PretixbaseOrderposition', models.DO_NOTHING, blank=True, null=True)
    nonce = models.CharField(max_length=190, blank=True, null=True)
    list = models.ForeignKey('PretixbaseCheckinlist', models.DO_NOTHING)
    auto_checked_in = models.BooleanField()
    device = models.ForeignKey('PretixbaseDevice', models.DO_NOTHING, blank=True, null=True)
    forced = models.BooleanField()
    type = models.CharField(max_length=100)
    gate = models.ForeignKey('PretixbaseGate', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    error_explanation = models.TextField(blank=True, null=True)
    error_reason = models.CharField(max_length=100, blank=True, null=True)
    raw_barcode = models.TextField(blank=True, null=True)
    raw_item = models.ForeignKey('PretixbaseItem', models.DO_NOTHING, blank=True, null=True)
    raw_subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)
    raw_variation = models.ForeignKey('PretixbaseItemvariation', models.DO_NOTHING, blank=True, null=True)
    successful = models.BooleanField()
    force_sent = models.BooleanField(blank=True, null=True)
    raw_source_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_checkin'


class PretixbaseCheckinlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    all_products = models.BooleanField()
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING)
    subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)
    include_pending = models.BooleanField()
    auto_checkin_sales_channels = models.TextField()
    allow_entry_after_exit = models.BooleanField()
    allow_multiple_entries = models.BooleanField()
    rules = models.JSONField()
    exit_all_at = models.DateTimeField(blank=True, null=True)
    addon_match = models.BooleanField()
    consider_tickets_used = models.BooleanField()
    ignore_in_statistics = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_checkinlist'


class PretixbaseCheckinlistGates(models.Model):
    id = models.BigAutoField(primary_key=True)
    checkinlist = models.ForeignKey(PretixbaseCheckinlist, models.DO_NOTHING)
    gate = models.ForeignKey('PretixbaseGate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_checkinlist_gates'
        unique_together = (('checkinlist', 'gate'),)


class PretixbaseCheckinlistLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    checkinlist = models.ForeignKey(PretixbaseCheckinlist, models.DO_NOTHING)
    item = models.ForeignKey('PretixbaseItem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_checkinlist_limit_products'
        unique_together = (('checkinlist', 'item'),)


class PretixbaseCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    identifier = models.CharField(max_length=190)
    email = models.CharField(max_length=190, blank=True, null=True)
    password = models.CharField(max_length=128)
    name_cached = models.CharField(max_length=255)
    name_parts = models.JSONField()
    is_active = models.BooleanField()
    is_verified = models.BooleanField()
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField()
    locale = models.CharField(max_length=50)
    last_modified = models.DateTimeField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    phone = models.CharField(max_length=128, blank=True, null=True)
    external_identifier = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    provider = models.ForeignKey('PretixbaseCustomerssoprovider', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_customer'
        unique_together = (('organizer', 'email'), ('organizer', 'identifier'),)


class PretixbaseCustomerssoaccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_code = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    client = models.ForeignKey('PretixbaseCustomerssoclient', models.DO_NOTHING)
    customer = models.ForeignKey(PretixbaseCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_customerssoaccesstoken'


class PretixbaseCustomerssoclient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField()
    client_id = models.CharField(unique=True, max_length=100)
    client_secret = models.CharField(max_length=255)
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    redirect_uris = models.TextField()
    allowed_scopes = models.TextField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_customerssoclient'


class PretixbaseCustomerssogrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    nonce = models.CharField(max_length=255, blank=True, null=True)
    auth_time = models.IntegerField()
    expires = models.DateTimeField()
    redirect_uri = models.TextField()
    scope = models.TextField()
    client = models.ForeignKey(PretixbaseCustomerssoclient, models.DO_NOTHING)
    customer = models.ForeignKey(PretixbaseCustomer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_customerssogrant'


class PretixbaseCustomerssoprovider(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    is_active = models.BooleanField()
    button_label = models.TextField()
    method = models.CharField(max_length=190)
    configuration = models.JSONField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_customerssoprovider'


class PretixbaseDevice(models.Model):
    id = models.BigAutoField(primary_key=True)
    device_id = models.IntegerField()
    unique_serial = models.CharField(unique=True, max_length=190)
    initialization_token = models.CharField(unique=True, max_length=190)
    api_token = models.CharField(unique=True, max_length=190, blank=True, null=True)
    all_events = models.BooleanField()
    name = models.CharField(max_length=190)
    created = models.DateTimeField()
    initialized = models.DateTimeField(blank=True, null=True)
    hardware_brand = models.CharField(max_length=190, blank=True, null=True)
    hardware_model = models.CharField(max_length=190, blank=True, null=True)
    software_brand = models.CharField(max_length=190, blank=True, null=True)
    software_version = models.CharField(max_length=190, blank=True, null=True)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    revoked = models.BooleanField()
    security_profile = models.CharField(max_length=190, blank=True, null=True)
    gate = models.ForeignKey('PretixbaseGate', models.DO_NOTHING, blank=True, null=True)
    info = models.JSONField(blank=True, null=True)
    os_name = models.CharField(max_length=190, blank=True, null=True)
    os_version = models.CharField(max_length=190, blank=True, null=True)
    rsa_pubkey = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_device'
        unique_together = (('organizer', 'device_id'),)


class PretixbaseDeviceLimitEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    device = models.ForeignKey(PretixbaseDevice, models.DO_NOTHING)
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_device_limit_events'
        unique_together = (('device', 'event'),)


class PretixbaseDiscount(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField()
    internal_name = models.CharField(max_length=255)
    position = models.IntegerField()
    sales_channels = models.TextField()
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)
    subevent_mode = models.CharField(max_length=50)
    condition_all_products = models.BooleanField()
    condition_min_count = models.IntegerField()
    condition_min_value = models.DecimalField(max_digits=13, decimal_places=2)
    benefit_discount_matching_percent = models.DecimalField(max_digits=10, decimal_places=2)
    benefit_only_apply_to_cheapest_n_matches = models.IntegerField(blank=True, null=True)
    condition_apply_to_addons = models.BooleanField()
    event = models.ForeignKey('PretixbaseEvent', models.DO_NOTHING)
    condition_ignore_voucher_discounted = models.BooleanField()
    benefit_apply_to_addons = models.BooleanField()
    benefit_ignore_voucher_discounted = models.BooleanField()
    benefit_same_products = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_discount'


class PretixbaseDiscountBenefitLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    discount = models.ForeignKey(PretixbaseDiscount, models.DO_NOTHING)
    item = models.ForeignKey('PretixbaseItem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_discount_benefit_limit_products'
        unique_together = (('discount', 'item'),)


class PretixbaseDiscountConditionLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    discount = models.ForeignKey(PretixbaseDiscount, models.DO_NOTHING)
    item = models.ForeignKey('PretixbaseItem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_discount_condition_limit_products'
        unique_together = (('discount', 'item'),)


class PretixbaseEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    slug = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField()
    presale_end = models.DateTimeField(blank=True, null=True)
    presale_start = models.DateTimeField(blank=True, null=True)
    plugins = models.TextField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    live = models.BooleanField()
    location = models.TextField(blank=True, null=True)
    date_admission = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    has_subevents = models.BooleanField()
    testmode = models.BooleanField()
    seating_plan = models.ForeignKey('PretixbaseSeatingplan', models.DO_NOTHING, blank=True, null=True)
    geo_lat = models.FloatField(blank=True, null=True)
    geo_lon = models.FloatField(blank=True, null=True)
    sales_channels = models.TextField()
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pretixbase_event'
        unique_together = (('organizer', 'slug'),)


class PretixbaseEventSettingsstore(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField()
    object = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_event_settingsstore'


class PretixbaseEventfooterlink(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.TextField()
    url = models.CharField(max_length=200)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_eventfooterlink'


class PretixbaseEventlock(models.Model):
    event = models.CharField(primary_key=True, max_length=36)
    date = models.DateTimeField()
    token = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'pretixbase_eventlock'


class PretixbaseEventmetaproperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    default = models.TextField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    protected = models.BooleanField()
    required = models.BooleanField()
    filter_allowed = models.BooleanField()
    filter_public = models.BooleanField()
    public_label = models.TextField(blank=True, null=True)
    position = models.IntegerField()
    choices = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_eventmetaproperty'


class PretixbaseEventmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    property = models.ForeignKey(PretixbaseEventmetaproperty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_eventmetavalue'
        unique_together = (('event', 'property'),)


class PretixbaseExchangerate(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.CharField(max_length=100)
    source_date = models.DateField()
    updated = models.DateTimeField()
    source_currency = models.CharField(max_length=3)
    other_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=16, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'pretixbase_exchangerate'
        unique_together = (('source', 'source_currency', 'other_currency'),)


class PretixbaseGate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    identifier = models.CharField(max_length=190)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_gate'


class PretixbaseGiftcard(models.Model):
    id = models.BigAutoField(primary_key=True)
    issuance = models.DateTimeField()
    secret = models.CharField(max_length=190)
    currency = models.CharField(max_length=10)
    issued_in = models.ForeignKey('PretixbaseOrderposition', models.DO_NOTHING, blank=True, null=True)
    issuer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    testmode = models.BooleanField()
    conditions = models.TextField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    owner_ticket = models.ForeignKey('PretixbaseOrderposition', models.DO_NOTHING, related_name='pretixbasegiftcard_owner_ticket_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_giftcard'
        unique_together = (('secret', 'issuer'),)


class PretixbaseGiftcardacceptance(models.Model):
    id = models.BigAutoField(primary_key=True)
    acceptor = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    issuer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, related_name='pretixbasegiftcardacceptance_issuer_set')
    active = models.BooleanField()
    reusable_media = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_giftcardacceptance'
        unique_together = (('issuer', 'acceptor'),)


class PretixbaseGiftcardtransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=13, decimal_places=2)
    card = models.ForeignKey(PretixbaseGiftcard, models.DO_NOTHING)
    order = models.ForeignKey('PretixbaseOrder', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('PretixbaseOrderpayment', models.DO_NOTHING, blank=True, null=True)
    refund = models.ForeignKey('PretixbaseOrderrefund', models.DO_NOTHING, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    acceptor = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, blank=True, null=True)
    info = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_giftcardtransaction'


class PretixbaseGlobalsettingsobjectSettingsstore(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'pretixbase_globalsettingsobject_settingsstore'


class PretixbaseInvoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_from = models.TextField()
    invoice_to = models.TextField()
    date = models.DateField()
    file = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    order = models.ForeignKey('PretixbaseOrder', models.DO_NOTHING)
    locale = models.CharField(max_length=50)
    additional_text = models.TextField()
    is_cancellation = models.BooleanField()
    refers = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    invoice_no = models.CharField(max_length=19)
    footer_text = models.TextField()
    introductory_text = models.TextField()
    payment_provider_text = models.TextField()
    prefix = models.CharField(max_length=160)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)
    foreign_currency_display = models.CharField(max_length=50, blank=True, null=True)
    foreign_currency_rate = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    foreign_currency_rate_date = models.DateField(blank=True, null=True)
    internal_reference = models.TextField()
    full_invoice_no = models.CharField(max_length=190)
    shredded = models.BooleanField()
    invoice_from_city = models.CharField(max_length=190, blank=True, null=True)
    invoice_from_country = models.CharField(max_length=2, blank=True, null=True)
    invoice_from_name = models.CharField(max_length=190, blank=True, null=True)
    invoice_from_tax_id = models.CharField(max_length=190, blank=True, null=True)
    invoice_from_vat_id = models.CharField(max_length=190, blank=True, null=True)
    invoice_from_zipcode = models.CharField(max_length=190, blank=True, null=True)
    invoice_to_city = models.TextField(blank=True, null=True)
    invoice_to_company = models.TextField(blank=True, null=True)
    invoice_to_country = models.CharField(max_length=2, blank=True, null=True)
    invoice_to_name = models.TextField(blank=True, null=True)
    invoice_to_street = models.TextField(blank=True, null=True)
    invoice_to_vat_id = models.TextField(blank=True, null=True)
    invoice_to_zipcode = models.CharField(max_length=190, blank=True, null=True)
    reverse_charge = models.BooleanField()
    invoice_to_beneficiary = models.TextField(blank=True, null=True)
    invoice_to_state = models.CharField(max_length=190, blank=True, null=True)
    custom_field = models.CharField(max_length=255, blank=True, null=True)
    sent_to_organizer = models.BooleanField(blank=True, null=True)
    sent_to_customer = models.DateTimeField(blank=True, null=True)
    payment_provider_stamp = models.CharField(max_length=100, blank=True, null=True)
    foreign_currency_source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_invoice'
        unique_together = (('organizer', 'prefix', 'invoice_no'),)


class PretixbaseInvoiceaddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_modified = models.DateTimeField()
    company = models.CharField(max_length=255)
    name_cached = models.CharField(max_length=255)
    street = models.TextField()
    zipcode = models.CharField(max_length=30)
    city = models.CharField(max_length=255)
    country_old = models.CharField(max_length=255)
    vat_id = models.CharField(max_length=255)
    order = models.OneToOneField('PretixbaseOrder', models.DO_NOTHING, blank=True, null=True)
    country = models.CharField(max_length=2)
    is_business = models.BooleanField()
    vat_id_validated = models.BooleanField()
    internal_reference = models.TextField()
    name_parts = models.JSONField()
    beneficiary = models.TextField()
    state = models.CharField(max_length=255)
    custom_field = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(PretixbaseCustomer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_invoiceaddress'


class PretixbaseInvoiceline(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    gross_value = models.DecimalField(max_digits=13, decimal_places=2)
    tax_value = models.DecimalField(max_digits=13, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    invoice = models.ForeignKey(PretixbaseInvoice, models.DO_NOTHING)
    tax_name = models.CharField(max_length=190)
    position = models.IntegerField()
    event_date_from = models.DateTimeField(blank=True, null=True)
    subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)
    attendee_name = models.TextField(blank=True, null=True)
    event_date_to = models.DateTimeField(blank=True, null=True)
    item = models.ForeignKey('PretixbaseItem', models.DO_NOTHING, blank=True, null=True)
    variation = models.ForeignKey('PretixbaseItemvariation', models.DO_NOTHING, blank=True, null=True)
    fee_internal_type = models.CharField(max_length=190, blank=True, null=True)
    fee_type = models.CharField(max_length=190, blank=True, null=True)
    event_location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_invoiceline'


class PretixbaseItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    active = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    default_price = models.DecimalField(max_digits=13, decimal_places=2)
    admission = models.BooleanField()
    position = models.IntegerField()
    picture = models.CharField(max_length=255, blank=True, null=True)
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('PretixbaseItemcategory', models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    free_price = models.BooleanField()
    hide_without_voucher = models.BooleanField()
    require_voucher = models.BooleanField()
    allow_cancel = models.BooleanField()
    max_per_order = models.IntegerField(blank=True, null=True)
    min_per_order = models.IntegerField(blank=True, null=True)
    tax_rule = models.ForeignKey('PretixbaseTaxrule', models.DO_NOTHING, blank=True, null=True)
    checkin_attention = models.BooleanField()
    internal_name = models.CharField(max_length=255, blank=True, null=True)
    original_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    require_approval = models.BooleanField()
    sales_channels = models.TextField()
    generate_tickets = models.BooleanField(blank=True, null=True)
    require_bundling = models.BooleanField()
    show_quota_left = models.BooleanField(blank=True, null=True)
    hidden_if_available = models.ForeignKey('PretixbaseQuota', models.DO_NOTHING, blank=True, null=True)
    allow_waitinglist = models.BooleanField()
    issue_giftcard = models.BooleanField()
    grant_membership_duration_days = models.IntegerField()
    grant_membership_duration_like_event = models.BooleanField()
    grant_membership_duration_months = models.IntegerField()
    require_membership = models.BooleanField()
    grant_membership_type = models.ForeignKey('PretixbaseMembershiptype', models.DO_NOTHING, blank=True, null=True)
    require_membership_hidden = models.BooleanField()
    personalized = models.BooleanField()
    validity_dynamic_duration_days = models.IntegerField(blank=True, null=True)
    validity_dynamic_duration_hours = models.IntegerField(blank=True, null=True)
    validity_dynamic_duration_minutes = models.IntegerField(blank=True, null=True)
    validity_dynamic_duration_months = models.IntegerField(blank=True, null=True)
    validity_dynamic_start_choice = models.BooleanField()
    validity_dynamic_start_choice_day_limit = models.IntegerField(blank=True, null=True)
    validity_fixed_from = models.DateTimeField(blank=True, null=True)
    validity_fixed_until = models.DateTimeField(blank=True, null=True)
    validity_mode = models.CharField(max_length=16, blank=True, null=True)
    media_policy = models.CharField(max_length=16, blank=True, null=True)
    media_type = models.CharField(max_length=100, blank=True, null=True)
    free_price_suggestion = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    hidden_if_item_available = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    checkin_text = models.TextField(blank=True, null=True)
    available_from_mode = models.CharField(max_length=16)
    available_until_mode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'pretixbase_item'


class PretixbaseItemRequireMembershipTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    membershiptype = models.ForeignKey('PretixbaseMembershiptype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_item_require_membership_types'
        unique_together = (('item', 'membershiptype'),)


class PretixbaseItemaddon(models.Model):
    id = models.BigAutoField(primary_key=True)
    min_count = models.IntegerField()
    max_count = models.IntegerField()
    addon_category = models.ForeignKey('PretixbaseItemcategory', models.DO_NOTHING)
    base_item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    position = models.IntegerField()
    price_included = models.BooleanField()
    multi_allowed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_itemaddon'
        unique_together = (('base_item', 'addon_category'),)


class PretixbaseItembundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField()
    designated_price = models.DecimalField(max_digits=13, decimal_places=2)
    base_item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    bundled_item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING, related_name='pretixbaseitembundle_bundled_item_set')
    bundled_variation = models.ForeignKey('PretixbaseItemvariation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_itembundle'


class PretixbaseItemcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    position = models.IntegerField()
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    description = models.TextField()
    is_addon = models.BooleanField()
    internal_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_itemcategory'


class PretixbaseItemmetaproperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    default = models.TextField()
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    allowed_values = models.TextField(blank=True, null=True)
    required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_itemmetaproperty'


class PretixbaseItemmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    property = models.ForeignKey(PretixbaseItemmetaproperty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_itemmetavalue'
        unique_together = (('item', 'property'),)


class PretixbaseItemvariation(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    active = models.BooleanField()
    position = models.IntegerField()
    default_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    original_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    require_membership = models.BooleanField()
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)
    hide_without_voucher = models.BooleanField()
    sales_channels = models.TextField()
    require_membership_hidden = models.BooleanField()
    require_approval = models.BooleanField()
    checkin_attention = models.BooleanField()
    free_price_suggestion = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    checkin_text = models.TextField(blank=True, null=True)
    available_from_mode = models.CharField(max_length=16)
    available_until_mode = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'pretixbase_itemvariation'


class PretixbaseItemvariationRequireMembershipTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemvariation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING)
    membershiptype = models.ForeignKey('PretixbaseMembershiptype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_itemvariation_require_membership_types'
        unique_together = (('itemvariation', 'membershiptype'),)


class PretixbaseItemvariationmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    property = models.ForeignKey(PretixbaseItemmetaproperty, models.DO_NOTHING)
    variation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_itemvariationmetavalue'
        unique_together = (('variation', 'property'),)


class PretixbaseLogentry(models.Model):
    id = models.BigAutoField(primary_key=True)
    object_id = models.IntegerField()
    datetime = models.DateTimeField()
    action_type = models.CharField(max_length=255)
    data = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING, blank=True, null=True)
    api_token = models.ForeignKey('PretixbaseTeamapitoken', models.DO_NOTHING, blank=True, null=True)
    visible = models.BooleanField()
    shredded = models.BooleanField()
    oauth_application = models.ForeignKey(PretixapiOauthapplication, models.DO_NOTHING, blank=True, null=True)
    device = models.ForeignKey(PretixbaseDevice, models.DO_NOTHING, blank=True, null=True)
    organizer_link = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_logentry'


class PretixbaseMediumkeyset(models.Model):
    id = models.BigAutoField(primary_key=True)
    public_id = models.BigIntegerField(unique=True)
    media_type = models.CharField(max_length=100)
    active = models.BooleanField()
    uid_key = models.BinaryField()
    diversification_key = models.BinaryField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_mediumkeyset'
        unique_together = (('organizer', 'media_type'),)


class PretixbaseMembership(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    attendee_name_parts = models.JSONField(blank=True, null=True)
    customer = models.ForeignKey(PretixbaseCustomer, models.DO_NOTHING)
    granted_in = models.ForeignKey('PretixbaseOrderposition', models.DO_NOTHING, blank=True, null=True)
    membership_type = models.ForeignKey('PretixbaseMembershiptype', models.DO_NOTHING)
    testmode = models.BooleanField()
    canceled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_membership'


class PretixbaseMembershiptype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    transferable = models.BooleanField()
    allow_parallel_usage = models.BooleanField()
    max_usages = models.IntegerField(blank=True, null=True)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_membershiptype'


class PretixbaseNotificationsetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_type = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_notificationsetting'
        unique_together = (('user', 'action_type', 'event', 'method'),)


class PretixbaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=16)
    status = models.CharField(max_length=3)
    email = models.CharField(max_length=254, blank=True, null=True)
    locale = models.CharField(max_length=32, blank=True, null=True)
    secret = models.CharField(max_length=32)
    datetime = models.DateTimeField()
    expires = models.DateTimeField()
    total = models.DecimalField(max_digits=13, decimal_places=2)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    comment = models.TextField()
    expiry_reminder_sent = models.BooleanField()
    meta_info = models.TextField(blank=True, null=True)
    download_reminder_sent = models.BooleanField()
    checkin_attention = models.BooleanField()
    last_modified = models.DateTimeField()
    require_approval = models.BooleanField()
    sales_channel = models.CharField(max_length=190)
    testmode = models.BooleanField()
    email_known_to_work = models.BooleanField()
    cancellation_date = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    customer = models.ForeignKey(PretixbaseCustomer, models.DO_NOTHING, blank=True, null=True)
    custom_followup_at = models.DateField(blank=True, null=True)
    valid_if_pending = models.BooleanField()
    invoice_dirty = models.BooleanField()
    checkin_text = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, blank=True, null=True)
    internal_secret = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_order'
        unique_together = (('organizer', 'code'),)


class PretixbaseOrderfee(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.DecimalField(max_digits=13, decimal_places=2)
    description = models.CharField(max_length=190)
    internal_type = models.CharField(max_length=255)
    fee_type = models.CharField(max_length=100)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    tax_value = models.DecimalField(max_digits=13, decimal_places=2)
    order = models.ForeignKey(PretixbaseOrder, models.DO_NOTHING)
    tax_rule = models.ForeignKey('PretixbaseTaxrule', models.DO_NOTHING, blank=True, null=True)
    canceled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_orderfee'


class PretixbaseOrderpayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    local_id = models.IntegerField()
    state = models.CharField(max_length=190)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    created = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    migrated = models.BooleanField()
    fee = models.ForeignKey(PretixbaseOrderfee, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(PretixbaseOrder, models.DO_NOTHING)
    process_initiated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_orderpayment'


class PretixbaseOrderposition(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    attendee_name_cached = models.CharField(max_length=255, blank=True, null=True)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    order = models.ForeignKey(PretixbaseOrder, models.DO_NOTHING)
    variation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey('PretixbaseVoucher', models.DO_NOTHING, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    tax_value = models.DecimalField(max_digits=13, decimal_places=2)
    secret = models.CharField(max_length=255)
    positionid = models.IntegerField()
    attendee_email = models.CharField(max_length=254, blank=True, null=True)
    addon_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    meta_info = models.TextField(blank=True, null=True)
    subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)
    tax_rule = models.ForeignKey('PretixbaseTaxrule', models.DO_NOTHING, blank=True, null=True)
    pseudonymization_id = models.CharField(unique=True, max_length=16)
    attendee_name_parts = models.JSONField()
    canceled = models.BooleanField()
    web_secret = models.CharField(max_length=32)
    seat = models.ForeignKey('PretixbaseSeat', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    used_membership = models.ForeignKey(PretixbaseMembership, models.DO_NOTHING, blank=True, null=True)
    is_bundled = models.BooleanField()
    discount = models.ForeignKey(PretixbaseDiscount, models.DO_NOTHING, blank=True, null=True)
    voucher_budget_use = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    blocked = models.JSONField(blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    ignore_from_quota_while_blocked = models.BooleanField()
    organizer = models.ForeignKey('PretixbaseOrganizer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_orderposition'
        unique_together = (('organizer', 'secret'),)


class PretixbaseOrderrefund(models.Model):
    id = models.BigAutoField(primary_key=True)
    local_id = models.IntegerField()
    state = models.CharField(max_length=190)
    source = models.CharField(max_length=190)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    created = models.DateTimeField()
    execution_date = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    order = models.ForeignKey(PretixbaseOrder, models.DO_NOTHING)
    payment = models.ForeignKey(PretixbaseOrderpayment, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_orderrefund'


class PretixbaseOrganizer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'pretixbase_organizer'


class PretixbaseOrganizerSettingsstore(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField()
    object = models.ForeignKey(PretixbaseOrganizer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_organizer_settingsstore'


class PretixbaseOrganizerfooterlink(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.TextField()
    url = models.CharField(max_length=200)
    organizer = models.ForeignKey(PretixbaseOrganizer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_organizerfooterlink'


class PretixbaseQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField()
    type = models.CharField(max_length=5)
    required = models.BooleanField()
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    position = models.IntegerField()
    help_text = models.TextField(blank=True, null=True)
    ask_during_checkin = models.BooleanField()
    identifier = models.CharField(max_length=190)
    dependency_question = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    dependency_values = models.TextField()
    hidden = models.BooleanField()
    print_on_invoice = models.BooleanField()
    valid_date_max = models.DateField(blank=True, null=True)
    valid_date_min = models.DateField(blank=True, null=True)
    valid_datetime_max = models.DateTimeField(blank=True, null=True)
    valid_datetime_min = models.DateTimeField(blank=True, null=True)
    valid_number_max = models.DecimalField(max_digits=16, decimal_places=6, blank=True, null=True)
    valid_number_min = models.DecimalField(max_digits=16, decimal_places=6, blank=True, null=True)
    valid_file_portrait = models.BooleanField()
    valid_string_length_max = models.IntegerField(blank=True, null=True)
    show_during_checkin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_question'
        unique_together = (('event', 'identifier'),)


class PretixbaseQuestionItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(PretixbaseQuestion, models.DO_NOTHING)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_question_items'
        unique_together = (('question', 'item'),)


class PretixbaseQuestionanswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.TextField()
    cartposition = models.ForeignKey(PretixbaseCartposition, models.DO_NOTHING, blank=True, null=True)
    orderposition = models.ForeignKey(PretixbaseOrderposition, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey(PretixbaseQuestion, models.DO_NOTHING)
    file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_questionanswer'
        unique_together = (('cartposition', 'question'), ('orderposition', 'question'),)


class PretixbaseQuestionanswerOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionanswer = models.ForeignKey(PretixbaseQuestionanswer, models.DO_NOTHING)
    questionoption = models.ForeignKey('PretixbaseQuestionoption', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_questionanswer_options'
        unique_together = (('questionanswer', 'questionoption'),)


class PretixbaseQuestionoption(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.TextField()
    question = models.ForeignKey(PretixbaseQuestion, models.DO_NOTHING)
    position = models.IntegerField()
    identifier = models.CharField(max_length=190)

    class Meta:
        managed = False
        db_table = 'pretixbase_questionoption'


class PretixbaseQuota(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    size = models.IntegerField(blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)
    close_when_sold_out = models.BooleanField()
    closed = models.BooleanField()
    release_after_exit = models.BooleanField()
    ignore_for_event_availability = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_quota'


class PretixbaseQuotaItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    quota = models.ForeignKey(PretixbaseQuota, models.DO_NOTHING)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_quota_items'
        unique_together = (('quota', 'item'),)


class PretixbaseQuotaVariations(models.Model):
    id = models.BigAutoField(primary_key=True)
    quota = models.ForeignKey(PretixbaseQuota, models.DO_NOTHING)
    itemvariation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_quota_variations'
        unique_together = (('quota', 'itemvariation'),)


class PretixbaseReusablemedium(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    type = models.CharField(max_length=100)
    identifier = models.CharField(max_length=200)
    active = models.BooleanField()
    expires = models.DateTimeField(blank=True, null=True)
    info = models.JSONField()
    notes = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(PretixbaseCustomer, models.DO_NOTHING, blank=True, null=True)
    linked_giftcard = models.ForeignKey(PretixbaseGiftcard, models.DO_NOTHING, blank=True, null=True)
    linked_orderposition = models.ForeignKey(PretixbaseOrderposition, models.DO_NOTHING, blank=True, null=True)
    organizer = models.ForeignKey(PretixbaseOrganizer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_reusablemedium'
        unique_together = (('identifier', 'type', 'organizer'),)


class PretixbaseRevokedticketsecret(models.Model):
    id = models.BigAutoField(primary_key=True)
    secret = models.TextField()
    created = models.DateTimeField()
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    position = models.ForeignKey(PretixbaseOrderposition, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_revokedticketsecret'


class PretixbaseScheduledeventexport(models.Model):
    id = models.BigAutoField(primary_key=True)
    export_identifier = models.CharField(max_length=190)
    export_form_data = models.JSONField()
    locale = models.CharField(max_length=250)
    mail_additional_recipients = models.TextField()
    mail_additional_recipients_cc = models.TextField()
    mail_additional_recipients_bcc = models.TextField()
    mail_subject = models.CharField(max_length=250)
    mail_template = models.TextField()
    schedule_rrule = models.TextField(blank=True, null=True)
    schedule_rrule_time = models.TimeField()
    schedule_next_run = models.DateTimeField(blank=True, null=True)
    error_counter = models.IntegerField()
    error_last_message = models.TextField(blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    owner = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_scheduledeventexport'


class PretixbaseScheduledorganizerexport(models.Model):
    id = models.BigAutoField(primary_key=True)
    export_identifier = models.CharField(max_length=190)
    export_form_data = models.JSONField()
    locale = models.CharField(max_length=250)
    mail_additional_recipients = models.TextField()
    mail_additional_recipients_cc = models.TextField()
    mail_additional_recipients_bcc = models.TextField()
    mail_subject = models.CharField(max_length=250)
    mail_template = models.TextField()
    schedule_rrule = models.TextField(blank=True, null=True)
    schedule_rrule_time = models.TimeField()
    schedule_next_run = models.DateTimeField(blank=True, null=True)
    error_counter = models.IntegerField()
    error_last_message = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=100)
    organizer = models.ForeignKey(PretixbaseOrganizer, models.DO_NOTHING)
    owner = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_scheduledorganizerexport'


class PretixbaseSeat(models.Model):
    id = models.BigAutoField(primary_key=True)
    blocked = models.BooleanField()
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    product = models.ForeignKey(PretixbaseItem, models.DO_NOTHING, blank=True, null=True)
    subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)
    seat_guid = models.CharField(max_length=190)
    row_name = models.CharField(max_length=190)
    seat_number = models.CharField(max_length=190)
    zone_name = models.CharField(max_length=190)
    sorting_rank = models.BigIntegerField()
    row_label = models.CharField(max_length=190, blank=True, null=True)
    seat_label = models.CharField(max_length=190, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_seat'


class PretixbaseSeatcategorymapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    layout_category = models.CharField(max_length=190)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    product = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    subevent = models.ForeignKey('PretixbaseSubevent', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_seatcategorymapping'


class PretixbaseSeatingplan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    layout = models.TextField()
    organizer = models.ForeignKey(PretixbaseOrganizer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_seatingplan'


class PretixbaseStaffsession(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(blank=True, null=True)
    session_key = models.CharField(max_length=255)
    comment = models.TextField()
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_staffsession'


class PretixbaseStaffsessionauditlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    url = models.CharField(max_length=255)
    session = models.ForeignKey(PretixbaseStaffsession, models.DO_NOTHING)
    impersonating = models.ForeignKey('PretixbaseUser', models.DO_NOTHING, blank=True, null=True)
    method = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pretixbase_staffsessionauditlog'


class PretixbaseSubevent(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField()
    name = models.TextField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(blank=True, null=True)
    date_admission = models.DateTimeField(blank=True, null=True)
    presale_end = models.DateTimeField(blank=True, null=True)
    presale_start = models.DateTimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    frontpage_text = models.TextField(blank=True, null=True)
    is_public = models.BooleanField()
    seating_plan = models.ForeignKey(PretixbaseSeatingplan, models.DO_NOTHING, blank=True, null=True)
    geo_lat = models.FloatField(blank=True, null=True)
    geo_lon = models.FloatField(blank=True, null=True)
    last_modified = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_subevent'


class PretixbaseSubeventitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING)
    disabled = models.BooleanField()
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_subeventitem'


class PretixbaseSubeventitemvariation(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING)
    variation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING)
    disabled = models.BooleanField()
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_subeventitemvariation'


class PretixbaseSubeventmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    property = models.ForeignKey(PretixbaseEventmetaproperty, models.DO_NOTHING)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_subeventmetavalue'
        unique_together = (('subevent', 'property'),)


class PretixbaseTaxrule(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    price_includes_tax = models.BooleanField()
    eu_reverse_charge = models.BooleanField()
    home_country = models.CharField(max_length=2)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    custom_rules = models.TextField(blank=True, null=True)
    internal_name = models.CharField(max_length=190, blank=True, null=True)
    keep_gross_if_rate_changes = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_taxrule'


class PretixbaseTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    all_events = models.BooleanField()
    can_create_events = models.BooleanField()
    can_change_teams = models.BooleanField()
    can_change_organizer_settings = models.BooleanField()
    can_change_event_settings = models.BooleanField()
    can_change_items = models.BooleanField()
    can_view_orders = models.BooleanField()
    can_change_orders = models.BooleanField()
    can_view_vouchers = models.BooleanField()
    can_change_vouchers = models.BooleanField()
    organizer = models.ForeignKey(PretixbaseOrganizer, models.DO_NOTHING)
    can_manage_gift_cards = models.BooleanField()
    can_checkin_orders = models.BooleanField()
    can_manage_customers = models.BooleanField()
    can_manage_reusable_media = models.BooleanField()
    require_2fa = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_team'


class PretixbaseTeamLimitEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey(PretixbaseTeam, models.DO_NOTHING)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_team_limit_events'
        unique_together = (('team', 'event'),)


class PretixbaseTeamMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey(PretixbaseTeam, models.DO_NOTHING)
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_team_members'
        unique_together = (('team', 'user'),)


class PretixbaseTeamapitoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    active = models.BooleanField()
    token = models.CharField(max_length=64)
    team = models.ForeignKey(PretixbaseTeam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_teamapitoken'


class PretixbaseTeaminvite(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    team = models.ForeignKey(PretixbaseTeam, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_teaminvite'


class PretixbaseTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    datetime = models.DateTimeField()
    migrated = models.BooleanField()
    positionid = models.IntegerField(blank=True, null=True)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    tax_value = models.DecimalField(max_digits=13, decimal_places=2)
    fee_type = models.CharField(max_length=100, blank=True, null=True)
    internal_type = models.CharField(max_length=255, blank=True, null=True)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(PretixbaseOrder, models.DO_NOTHING)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING, blank=True, null=True)
    tax_rule = models.ForeignKey(PretixbaseTaxrule, models.DO_NOTHING, blank=True, null=True)
    variation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_transaction'


class PretixbaseU2Fdevice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    json_data = models.TextField()
    user = models.ForeignKey('PretixbaseUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_u2fdevice'


class PretixbaseUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=190, blank=True, null=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    date_joined = models.DateTimeField()
    locale = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    require_2fa = models.BooleanField()
    fullname = models.CharField(max_length=255, blank=True, null=True)
    notifications_send = models.BooleanField()
    notifications_token = models.CharField(max_length=255)
    auth_backend = models.CharField(max_length=255)
    session_token = models.CharField(max_length=32)
    needs_password_change = models.BooleanField()
    auth_backend_identifier = models.CharField(max_length=190, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_user'
        unique_together = (('auth_backend', 'auth_backend_identifier'),)


class PretixbaseUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(PretixbaseUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_user_groups'
        unique_together = (('user', 'group'),)


class PretixbaseUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(PretixbaseUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_user_user_permissions'
        unique_together = (('user', 'permission'),)


class PretixbaseUserknownloginsource(models.Model):
    id = models.BigAutoField(primary_key=True)
    agent_type = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    last_seen = models.DateTimeField()
    user = models.ForeignKey(PretixbaseUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_userknownloginsource'


class PretixbaseVoucher(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    valid_until = models.DateTimeField(blank=True, null=True)
    block_quota = models.BooleanField()
    allow_ignore_quota = models.BooleanField()
    value = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING, blank=True, null=True)
    redeemed = models.IntegerField()
    variation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING, blank=True, null=True)
    quota = models.ForeignKey(PretixbaseQuota, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()
    tag = models.CharField(max_length=255)
    max_usages = models.IntegerField()
    price_mode = models.CharField(max_length=100)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING, blank=True, null=True)
    show_hidden_items = models.BooleanField()
    seat = models.ForeignKey(PretixbaseSeat, models.DO_NOTHING, blank=True, null=True)
    budget = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    min_usages = models.IntegerField()
    all_addons_included = models.BooleanField()
    all_bundles_included = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pretixbase_voucher'
        unique_together = (('event', 'code'),)


class PretixbaseWaitinglistentry(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    email = models.CharField(max_length=254)
    locale = models.CharField(max_length=190)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)
    variation = models.ForeignKey(PretixbaseItemvariation, models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey(PretixbaseVoucher, models.DO_NOTHING, blank=True, null=True)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField()
    name_cached = models.CharField(max_length=255, blank=True, null=True)
    name_parts = models.JSONField()
    phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixbase_waitinglistentry'


class PretixbaseWebauthndevice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    credential_id = models.CharField(max_length=255, blank=True, null=True)
    rp_id = models.CharField(max_length=255, blank=True, null=True)
    icon_url = models.CharField(max_length=255, blank=True, null=True)
    ukey = models.TextField(blank=True, null=True)
    pub_key = models.TextField(blank=True, null=True)
    sign_count = models.IntegerField()
    user = models.ForeignKey(PretixbaseUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pretixbase_webauthndevice'


class PretixhelpersThumbnail(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixhelpers_thumbnail'
        unique_together = (('source', 'size'),)


class PretixmultidomainKnowndomain(models.Model):
    domainname = models.CharField(primary_key=True, max_length=255)
    organizer = models.ForeignKey(PretixbaseOrganizer, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pretixmultidomain_knowndomain'


class SendmailRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.TextField()
    template = models.TextField()
    all_products = models.BooleanField()
    send_date = models.DateTimeField(blank=True, null=True)
    send_offset_days = models.IntegerField(blank=True, null=True)
    send_offset_time = models.TimeField(blank=True, null=True)
    date_is_absolute = models.BooleanField()
    offset_to_event_end = models.BooleanField()
    offset_is_after = models.BooleanField()
    send_to = models.CharField(max_length=10)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    enabled = models.BooleanField()
    attach_ical = models.BooleanField()
    restrict_to_status = models.TextField()
    checked_in_status = models.CharField(max_length=10, blank=True, null=True)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sendmail_rule'


class SendmailRuleLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    rule = models.ForeignKey(SendmailRule, models.DO_NOTHING)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sendmail_rule_limit_products'
        unique_together = (('rule', 'item'),)


class SendmailScheduledmail(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_computed = models.DateTimeField()
    computed_datetime = models.DateTimeField()
    state = models.CharField(max_length=100)
    last_successful_order_id = models.BigIntegerField(blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)
    rule = models.ForeignKey(SendmailRule, models.DO_NOTHING)
    subevent = models.ForeignKey(PretixbaseSubevent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sendmail_scheduledmail'
        unique_together = (('rule', 'subevent'),)


class StripeReferencedstripeobject(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference = models.CharField(unique=True, max_length=190)
    order = models.ForeignKey(PretixbaseOrder, models.DO_NOTHING)
    payment = models.ForeignKey(PretixbaseOrderpayment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stripe_referencedstripeobject'


class StripeRegisteredapplepaydomain(models.Model):
    id = models.BigAutoField(primary_key=True)
    domain = models.CharField(max_length=190)
    account = models.CharField(max_length=190)

    class Meta:
        managed = False
        db_table = 'stripe_registeredapplepaydomain'


class TicketoutputpdfTicketlayout(models.Model):
    id = models.BigAutoField(primary_key=True)
    default = models.BooleanField()
    name = models.CharField(max_length=190)
    layout = models.TextField()
    background = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey(PretixbaseEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ticketoutputpdf_ticketlayout'


class TicketoutputpdfTicketlayoutitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(PretixbaseItem, models.DO_NOTHING, blank=True, null=True)
    layout = models.ForeignKey(TicketoutputpdfTicketlayout, models.DO_NOTHING)
    sales_channel = models.CharField(max_length=190)

    class Meta:
        managed = False
        db_table = 'ticketoutputpdf_ticketlayoutitem'
        unique_together = (('item', 'layout', 'sales_channel'),)
