# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Badgeitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.OneToOneField('Item', models.DO_NOTHING, blank=True, null=True)
    layout = models.ForeignKey('Badgelayout', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Badgelayout(models.Model):
    id = models.BigAutoField(primary_key=True)
    default = models.BooleanField()
    name = models.CharField(max_length=190)
    layout = models.TextField()
    background = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey('Event', models.DO_NOTHING)

    class Meta:
        managed = True


class Bankimportjob(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    state = models.CharField(max_length=32)
    event = models.ForeignKey('Event', models.DO_NOTHING, blank=True, null=True)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True


class Banktransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=32)
    message = models.TextField()
    checksum = models.CharField(max_length=190)
    payer = models.TextField()
    reference = models.TextField()
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    date = models.CharField(max_length=50)
    event = models.ForeignKey('Event', models.DO_NOTHING, blank=True, null=True)
    import_job = models.ForeignKey(Bankimportjob, models.DO_NOTHING)
    order = models.ForeignKey('Order', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)
    bic = models.CharField(max_length=250)
    date_parsed = models.DateField(blank=True, null=True)
    iban = models.CharField(max_length=250)
    currency = models.CharField(max_length=10, blank=True, null=True)
    external_id = models.CharField(max_length=190, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('event', 'organizer', 'checksum'),)


class Refundexport(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    testmode = models.BooleanField()
    rows = models.TextField()
    event = models.ForeignKey('Event', models.DO_NOTHING, blank=True, null=True)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)
    downloaded = models.BooleanField()
    currency = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True


class Staticdevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    throttling_failure_count = models.IntegerField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True


class Statictoken(models.Model):
    token = models.CharField(max_length=16)
    device = models.ForeignKey(Staticdevice, models.DO_NOTHING)

    class Meta:
        managed = True


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
    user = models.ForeignKey('User', models.DO_NOTHING)
    throttling_failure_count = models.IntegerField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True


class Referencedpaypalobject(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference = models.CharField(unique=True, max_length=190)
    order = models.ForeignKey('Order', models.DO_NOTHING)
    payment = models.ForeignKey('Orderpayment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Apicall(models.Model):
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
        managed = True
        unique_together = (('idempotency_key', 'auth_hash'),)


class Oauthaccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey('Oauthapplication', models.DO_NOTHING, blank=True, null=True)
    source_refresh_token = models.OneToOneField('Oauthrefreshtoken', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    id_token = models.OneToOneField('Oauthidtoken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class OauthaccesstokenOrganizers(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauthaccesstoken = models.ForeignKey(Oauthaccesstoken, models.DO_NOTHING)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('oauthaccesstoken', 'organizer'),)


class Oauthapplication(models.Model):
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
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    algorithm = models.CharField(max_length=5)
    post_logout_redirect_uris = models.TextField()

    class Meta:
        managed = True


class Oauthgrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.CharField(max_length=2500)
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey(Oauthapplication, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    claims = models.TextField()
    code_challenge = models.CharField(max_length=128)
    code_challenge_method = models.CharField(max_length=10)
    nonce = models.CharField(max_length=255)

    class Meta:
        managed = True


class OauthgrantOrganizers(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauthgrant = models.ForeignKey(Oauthgrant, models.DO_NOTHING)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('oauthgrant', 'organizer'),)


class Oauthidtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    jti = models.UUIDField(unique=True)
    expires = models.DateTimeField()
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey(Oauthapplication, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class OauthidtokenOrganizers(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauthidtoken = models.ForeignKey(Oauthidtoken, models.DO_NOTHING)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('oauthidtoken', 'organizer'),)


class Oauthrefreshtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    revoked = models.DateTimeField(blank=True, null=True)
    access_token = models.OneToOneField(Oauthaccesstoken, models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(Oauthapplication, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('token', 'revoked'),)


class Webhook(models.Model):
    id = models.BigAutoField(primary_key=True)
    enabled = models.BooleanField()
    target_url = models.CharField(max_length=255)
    all_events = models.BooleanField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True


class WebhookLimitEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    webhook = models.ForeignKey(Webhook, models.DO_NOTHING)
    event = models.ForeignKey('Event', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('webhook', 'event'),)


class Webhookcall(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    target_url = models.CharField(max_length=255)
    is_retry = models.BooleanField()
    execution_time = models.FloatField(blank=True, null=True)
    return_code = models.IntegerField()
    payload = models.TextField()
    response_body = models.TextField()
    webhook = models.ForeignKey(Webhook, models.DO_NOTHING)
    success = models.BooleanField()
    action_type = models.CharField(max_length=255)

    class Meta:
        managed = True


class Webhookcallretry(models.Model):
    id = models.BigAutoField(primary_key=True)
    retry_not_before = models.DateTimeField()
    retry_count = models.IntegerField()
    action_type = models.CharField(max_length=255)
    logentry = models.ForeignKey('Logentry', models.DO_NOTHING)
    webhook = models.ForeignKey(Webhook, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('webhook', 'logentry'),)


class Webhookeventlistener(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_type = models.CharField(max_length=255)
    webhook = models.ForeignKey(Webhook, models.DO_NOTHING)

    class Meta:
        managed = True


class Attendeeprofile(models.Model):
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
    customer = models.ForeignKey('Customer', models.DO_NOTHING)

    class Meta:
        managed = True


class Blockedticketsecret(models.Model):
    id = models.BigAutoField(primary_key=True)
    secret = models.TextField()
    blocked = models.BooleanField()
    updated = models.DateTimeField()
    event = models.ForeignKey('Event', models.DO_NOTHING)
    position = models.ForeignKey('Orderposition', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('event', 'secret'),)


class Cachedcombinedticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    file = models.CharField(max_length=255, blank=True, null=True)
    order = models.ForeignKey('Order', models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = True


class Cachedfile(models.Model):
    id = models.UUIDField(primary_key=True)
    expires = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    filename = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    file = models.CharField(max_length=255, blank=True, null=True)
    session_key = models.TextField(blank=True, null=True)
    web_download = models.BooleanField()

    class Meta:
        managed = True


class Cachedticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=255)
    order_position = models.ForeignKey('Orderposition', models.DO_NOTHING)
    extension = models.CharField(max_length=255)
    file = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    created = models.DateTimeField()

    class Meta:
        managed = True


class Cancellationrequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    cancellation_fee = models.DecimalField(max_digits=13, decimal_places=2)
    refund_as_giftcard = models.BooleanField()
    order = models.ForeignKey('Order', models.DO_NOTHING)

    class Meta:
        managed = True


class Cartposition(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    attendee_name_cached = models.CharField(max_length=255, blank=True, null=True)
    cart_id = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField()
    expires = models.DateTimeField()
    event = models.ForeignKey('Event', models.DO_NOTHING)
    item = models.ForeignKey('Item', models.DO_NOTHING)
    variation = models.ForeignKey('Itemvariation', models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey('Voucher', models.DO_NOTHING, blank=True, null=True)
    attendee_email = models.CharField(max_length=254, blank=True, null=True)
    addon_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    meta_info = models.TextField(blank=True, null=True)
    subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)
    attendee_name_parts = models.JSONField()
    is_bundled = models.BooleanField()
    seat = models.ForeignKey('Seat', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    used_membership = models.ForeignKey('Membership', models.DO_NOTHING, blank=True, null=True)
    custom_price_input = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    custom_price_input_is_net = models.BooleanField()
    line_price_gross = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    listed_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    price_after_voucher = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.ForeignKey('Discount', models.DO_NOTHING, blank=True, null=True)
    requested_valid_from = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True


class Checkin(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    position = models.ForeignKey('Orderposition', models.DO_NOTHING, blank=True, null=True)
    nonce = models.CharField(max_length=190, blank=True, null=True)
    list = models.ForeignKey('Checkinlist', models.DO_NOTHING)
    auto_checked_in = models.BooleanField()
    device = models.ForeignKey('Device', models.DO_NOTHING, blank=True, null=True)
    forced = models.BooleanField()
    type = models.CharField(max_length=100)
    gate = models.ForeignKey('Gate', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    error_explanation = models.TextField(blank=True, null=True)
    error_reason = models.CharField(max_length=100, blank=True, null=True)
    raw_barcode = models.TextField(blank=True, null=True)
    raw_item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)
    raw_subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)
    raw_variation = models.ForeignKey('Itemvariation', models.DO_NOTHING, blank=True, null=True)
    successful = models.BooleanField()
    force_sent = models.BooleanField(blank=True, null=True)
    raw_source_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True


class Checkinlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    all_products = models.BooleanField()
    event = models.ForeignKey('Event', models.DO_NOTHING)
    subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)
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
        managed = True


class CheckinlistGates(models.Model):
    id = models.BigAutoField(primary_key=True)
    checkinlist = models.ForeignKey(Checkinlist, models.DO_NOTHING)
    gate = models.ForeignKey('Gate', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('checkinlist', 'gate'),)


class CheckinlistLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    checkinlist = models.ForeignKey(Checkinlist, models.DO_NOTHING)
    item = models.ForeignKey('Item', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('checkinlist', 'item'),)


class Customer(models.Model):
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
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)
    phone = models.CharField(max_length=128, blank=True, null=True)
    external_identifier = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    provider = models.ForeignKey('Customerssoprovider', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('organizer', 'email'), ('organizer', 'identifier'),)


class Customerssoaccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_code = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    client = models.ForeignKey('Customerssoclient', models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = True


class Customerssoclient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField()
    client_id = models.CharField(unique=True, max_length=100)
    client_secret = models.CharField(max_length=255)
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    redirect_uris = models.TextField()
    allowed_scopes = models.TextField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True


class Customerssogrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    nonce = models.CharField(max_length=255, blank=True, null=True)
    auth_time = models.IntegerField()
    expires = models.DateTimeField()
    redirect_uri = models.TextField()
    scope = models.TextField()
    client = models.ForeignKey(Customerssoclient, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = True


class Customerssoprovider(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    is_active = models.BooleanField()
    button_label = models.TextField()
    method = models.CharField(max_length=190)
    configuration = models.JSONField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True


class Device(models.Model):
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
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)
    revoked = models.BooleanField()
    security_profile = models.CharField(max_length=190, blank=True, null=True)
    gate = models.ForeignKey('Gate', models.DO_NOTHING, blank=True, null=True)
    info = models.JSONField(blank=True, null=True)
    os_name = models.CharField(max_length=190, blank=True, null=True)
    os_version = models.CharField(max_length=190, blank=True, null=True)
    rsa_pubkey = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('organizer', 'device_id'),)


class DeviceLimitEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    device = models.ForeignKey(Device, models.DO_NOTHING)
    event = models.ForeignKey('Event', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('device', 'event'),)


class Discount(models.Model):
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
    event = models.ForeignKey('Event', models.DO_NOTHING)
    condition_ignore_voucher_discounted = models.BooleanField()
    benefit_apply_to_addons = models.BooleanField()
    benefit_ignore_voucher_discounted = models.BooleanField()
    benefit_same_products = models.BooleanField()

    class Meta:
        managed = True


class DiscountBenefitLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    discount = models.ForeignKey(Discount, models.DO_NOTHING)
    item = models.ForeignKey('Item', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('discount', 'item'),)


class DiscountConditionLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    discount = models.ForeignKey(Discount, models.DO_NOTHING)
    item = models.ForeignKey('Item', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('discount', 'item'),)


class Event(models.Model):
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
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)
    live = models.BooleanField()
    location = models.TextField(blank=True, null=True)
    date_admission = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    has_subevents = models.BooleanField()
    testmode = models.BooleanField()
    seating_plan = models.ForeignKey('Seatingplan', models.DO_NOTHING, blank=True, null=True)
    geo_lat = models.FloatField(blank=True, null=True)
    geo_lon = models.FloatField(blank=True, null=True)
    sales_channels = models.TextField()
    last_modified = models.DateTimeField()

    class Meta:
        managed = True
        unique_together = (('organizer', 'slug'),)


class EventSettingsstore(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField()
    object = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = True


class Eventfooterlink(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.TextField()
    url = models.CharField(max_length=200)
    event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = True


class Eventlock(models.Model):
    event = models.CharField(primary_key=True, max_length=36)
    date = models.DateTimeField()
    token = models.UUIDField()

    class Meta:
        managed = True


class Eventmetaproperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    default = models.TextField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)
    protected = models.BooleanField()
    required = models.BooleanField()
    filter_allowed = models.BooleanField()
    filter_public = models.BooleanField()
    public_label = models.TextField(blank=True, null=True)
    position = models.IntegerField()
    choices = models.JSONField(blank=True, null=True)

    class Meta:
        managed = True


class Eventmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
    property = models.ForeignKey(Eventmetaproperty, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('event', 'property'),)


class Exchangerate(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.CharField(max_length=100)
    source_date = models.DateField()
    updated = models.DateTimeField()
    source_currency = models.CharField(max_length=3)
    other_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=16, decimal_places=6)

    class Meta:
        managed = True
        unique_together = (('source', 'source_currency', 'other_currency'),)


class Gate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    identifier = models.CharField(max_length=190)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True


class Giftcard(models.Model):
    id = models.BigAutoField(primary_key=True)
    issuance = models.DateTimeField()
    secret = models.CharField(max_length=190)
    currency = models.CharField(max_length=10)
    issued_in = models.ForeignKey('Orderposition', models.DO_NOTHING, blank=True, null=True)
    issuer = models.ForeignKey('Organizer', models.DO_NOTHING)
    testmode = models.BooleanField()
    conditions = models.TextField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    owner_ticket = models.ForeignKey('Orderposition', models.DO_NOTHING, related_name='giftcard_owner_ticket_set', blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('secret', 'issuer'),)


class Giftcardacceptance(models.Model):
    id = models.BigAutoField(primary_key=True)
    acceptor = models.ForeignKey('Organizer', models.DO_NOTHING)
    issuer = models.ForeignKey('Organizer', models.DO_NOTHING, related_name='giftcardacceptance_issuer_set')
    active = models.BooleanField()
    reusable_media = models.BooleanField()

    class Meta:
        managed = True
        unique_together = (('issuer', 'acceptor'),)


class Giftcardtransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=13, decimal_places=2)
    card = models.ForeignKey(Giftcard, models.DO_NOTHING)
    order = models.ForeignKey('Order', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('Orderpayment', models.DO_NOTHING, blank=True, null=True)
    refund = models.ForeignKey('Orderrefund', models.DO_NOTHING, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    acceptor = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)
    info = models.JSONField(blank=True, null=True)

    class Meta:
        managed = True


class GlobalsettingsobjectSettingsstore(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = True


class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_from = models.TextField()
    invoice_to = models.TextField()
    date = models.DateField()
    file = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    order = models.ForeignKey('Order', models.DO_NOTHING)
    locale = models.CharField(max_length=50)
    additional_text = models.TextField()
    is_cancellation = models.BooleanField()
    refers = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    invoice_no = models.CharField(max_length=19)
    footer_text = models.TextField()
    introductory_text = models.TextField()
    payment_provider_text = models.TextField()
    prefix = models.CharField(max_length=160)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)
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
        managed = True
        unique_together = (('organizer', 'prefix', 'invoice_no'),)


class Invoiceaddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_modified = models.DateTimeField()
    company = models.CharField(max_length=255)
    name_cached = models.CharField(max_length=255)
    street = models.TextField()
    zipcode = models.CharField(max_length=30)
    city = models.CharField(max_length=255)
    country_old = models.CharField(max_length=255)
    vat_id = models.CharField(max_length=255)
    order = models.OneToOneField('Order', models.DO_NOTHING, blank=True, null=True)
    country = models.CharField(max_length=2)
    is_business = models.BooleanField()
    vat_id_validated = models.BooleanField()
    internal_reference = models.TextField()
    name_parts = models.JSONField()
    beneficiary = models.TextField()
    state = models.CharField(max_length=255)
    custom_field = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Invoiceline(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    gross_value = models.DecimalField(max_digits=13, decimal_places=2)
    tax_value = models.DecimalField(max_digits=13, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    tax_name = models.CharField(max_length=190)
    position = models.IntegerField()
    event_date_from = models.DateTimeField(blank=True, null=True)
    subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)
    attendee_name = models.TextField(blank=True, null=True)
    event_date_to = models.DateTimeField(blank=True, null=True)
    item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)
    variation = models.ForeignKey('Itemvariation', models.DO_NOTHING, blank=True, null=True)
    fee_internal_type = models.CharField(max_length=190, blank=True, null=True)
    fee_type = models.CharField(max_length=190, blank=True, null=True)
    event_location = models.TextField(blank=True, null=True)

    class Meta:
        managed = True


class Item(models.Model):
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
    category = models.ForeignKey('Itemcategory', models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    free_price = models.BooleanField()
    hide_without_voucher = models.BooleanField()
    require_voucher = models.BooleanField()
    allow_cancel = models.BooleanField()
    max_per_order = models.IntegerField(blank=True, null=True)
    min_per_order = models.IntegerField(blank=True, null=True)
    tax_rule = models.ForeignKey('Taxrule', models.DO_NOTHING, blank=True, null=True)
    checkin_attention = models.BooleanField()
    internal_name = models.CharField(max_length=255, blank=True, null=True)
    original_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    require_approval = models.BooleanField()
    sales_channels = models.TextField()
    generate_tickets = models.BooleanField(blank=True, null=True)
    require_bundling = models.BooleanField()
    show_quota_left = models.BooleanField(blank=True, null=True)
    hidden_if_available = models.ForeignKey('Quota', models.DO_NOTHING, blank=True, null=True)
    allow_waitinglist = models.BooleanField()
    issue_giftcard = models.BooleanField()
    grant_membership_duration_days = models.IntegerField()
    grant_membership_duration_like_event = models.BooleanField()
    grant_membership_duration_months = models.IntegerField()
    require_membership = models.BooleanField()
    grant_membership_type = models.ForeignKey('Membershiptype', models.DO_NOTHING, blank=True, null=True)
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
        managed = True


class ItemRequireMembershipTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    membershiptype = models.ForeignKey('Membershiptype', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('item', 'membershiptype'),)


class Itemaddon(models.Model):
    id = models.BigAutoField(primary_key=True)
    min_count = models.IntegerField()
    max_count = models.IntegerField()
    addon_category = models.ForeignKey('Itemcategory', models.DO_NOTHING)
    base_item = models.ForeignKey(Item, models.DO_NOTHING)
    position = models.IntegerField()
    price_included = models.BooleanField()
    multi_allowed = models.BooleanField()

    class Meta:
        managed = True
        unique_together = (('base_item', 'addon_category'),)


class Itembundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField()
    designated_price = models.DecimalField(max_digits=13, decimal_places=2)
    base_item = models.ForeignKey(Item, models.DO_NOTHING)
    bundled_item = models.ForeignKey(Item, models.DO_NOTHING, related_name='itembundle_bundled_item_set')
    bundled_variation = models.ForeignKey('Itemvariation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Itemcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    position = models.IntegerField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
    description = models.TextField()
    is_addon = models.BooleanField()
    internal_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True


class Itemmetaproperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    default = models.TextField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
    allowed_values = models.TextField(blank=True, null=True)
    required = models.BooleanField()

    class Meta:
        managed = True


class Itemmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    item = models.ForeignKey(Item, models.DO_NOTHING)
    property = models.ForeignKey(Itemmetaproperty, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('item', 'property'),)


class Itemvariation(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    active = models.BooleanField()
    position = models.IntegerField()
    default_price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
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
        managed = True


class ItemvariationRequireMembershipTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemvariation = models.ForeignKey(Itemvariation, models.DO_NOTHING)
    membershiptype = models.ForeignKey('Membershiptype', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('itemvariation', 'membershiptype'),)


class Itemvariationmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    property = models.ForeignKey(Itemmetaproperty, models.DO_NOTHING)
    variation = models.ForeignKey(Itemvariation, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('variation', 'property'),)


class Logentry(models.Model):
    id = models.BigAutoField(primary_key=True)
    object_id = models.IntegerField()
    datetime = models.DateTimeField()
    action_type = models.CharField(max_length=255)
    data = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    api_token = models.ForeignKey('Teamapitoken', models.DO_NOTHING, blank=True, null=True)
    visible = models.BooleanField()
    shredded = models.BooleanField()
    oauth_application = models.ForeignKey(Oauthapplication, models.DO_NOTHING, blank=True, null=True)
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=True, null=True)
    organizer_link = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Mediumkeyset(models.Model):
    id = models.BigAutoField(primary_key=True)
    public_id = models.BigIntegerField(unique=True)
    media_type = models.CharField(max_length=100)
    active = models.BooleanField()
    uid_key = models.BinaryField()
    diversification_key = models.BinaryField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('organizer', 'media_type'),)


class Membership(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    attendee_name_parts = models.JSONField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    granted_in = models.ForeignKey('Orderposition', models.DO_NOTHING, blank=True, null=True)
    membership_type = models.ForeignKey('Membershiptype', models.DO_NOTHING)
    testmode = models.BooleanField()
    canceled = models.BooleanField()

    class Meta:
        managed = True


class Membershiptype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    transferable = models.BooleanField()
    allow_parallel_usage = models.BooleanField()
    max_usages = models.IntegerField(blank=True, null=True)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING)

    class Meta:
        managed = True


class Notificationsetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_type = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    enabled = models.BooleanField()

    class Meta:
        managed = True
        unique_together = (('user', 'action_type', 'event', 'method'),)


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=16)
    status = models.CharField(max_length=3)
    email = models.CharField(max_length=254, blank=True, null=True)
    locale = models.CharField(max_length=32, blank=True, null=True)
    secret = models.CharField(max_length=32)
    datetime = models.DateTimeField()
    expires = models.DateTimeField()
    total = models.DecimalField(max_digits=13, decimal_places=2)
    event = models.ForeignKey(Event, models.DO_NOTHING)
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
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    custom_followup_at = models.DateField(blank=True, null=True)
    valid_if_pending = models.BooleanField()
    invoice_dirty = models.BooleanField()
    checkin_text = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)
    internal_secret = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('organizer', 'code'),)


class Orderfee(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.DecimalField(max_digits=13, decimal_places=2)
    description = models.CharField(max_length=190)
    internal_type = models.CharField(max_length=255)
    fee_type = models.CharField(max_length=100)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    tax_value = models.DecimalField(max_digits=13, decimal_places=2)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    tax_rule = models.ForeignKey('Taxrule', models.DO_NOTHING, blank=True, null=True)
    canceled = models.BooleanField()

    class Meta:
        managed = True


class Orderpayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    local_id = models.IntegerField()
    state = models.CharField(max_length=190)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    created = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    migrated = models.BooleanField()
    fee = models.ForeignKey(Orderfee, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    process_initiated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True


class Orderposition(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    attendee_name_cached = models.CharField(max_length=255, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    variation = models.ForeignKey(Itemvariation, models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey('Voucher', models.DO_NOTHING, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=7, decimal_places=2)
    tax_value = models.DecimalField(max_digits=13, decimal_places=2)
    secret = models.CharField(max_length=255)
    positionid = models.IntegerField()
    attendee_email = models.CharField(max_length=254, blank=True, null=True)
    addon_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    meta_info = models.TextField(blank=True, null=True)
    subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)
    tax_rule = models.ForeignKey('Taxrule', models.DO_NOTHING, blank=True, null=True)
    pseudonymization_id = models.CharField(unique=True, max_length=16)
    attendee_name_parts = models.JSONField()
    canceled = models.BooleanField()
    web_secret = models.CharField(max_length=32)
    seat = models.ForeignKey('Seat', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    used_membership = models.ForeignKey(Membership, models.DO_NOTHING, blank=True, null=True)
    is_bundled = models.BooleanField()
    discount = models.ForeignKey(Discount, models.DO_NOTHING, blank=True, null=True)
    voucher_budget_use = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    blocked = models.JSONField(blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)
    ignore_from_quota_while_blocked = models.BooleanField()
    organizer = models.ForeignKey('Organizer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('organizer', 'secret'),)


class Orderrefund(models.Model):
    id = models.BigAutoField(primary_key=True)
    local_id = models.IntegerField()
    state = models.CharField(max_length=190)
    source = models.CharField(max_length=190)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    created = models.DateTimeField()
    execution_date = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    payment = models.ForeignKey(Orderpayment, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True


class Organizer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = True


class OrganizerSettingsstore(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField()
    object = models.ForeignKey(Organizer, models.DO_NOTHING)

    class Meta:
        managed = True


class Organizerfooterlink(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.TextField()
    url = models.CharField(max_length=200)
    organizer = models.ForeignKey(Organizer, models.DO_NOTHING)

    class Meta:
        managed = True


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField()
    type = models.CharField(max_length=5)
    required = models.BooleanField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
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
        managed = True
        unique_together = (('event', 'identifier'),)


class QuestionItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(Question, models.DO_NOTHING)
    item = models.ForeignKey(Item, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('question', 'item'),)


class Questionanswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.TextField()
    cartposition = models.ForeignKey(Cartposition, models.DO_NOTHING, blank=True, null=True)
    orderposition = models.ForeignKey(Orderposition, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey(Question, models.DO_NOTHING)
    file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('cartposition', 'question'), ('orderposition', 'question'),)


class QuestionanswerOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionanswer = models.ForeignKey(Questionanswer, models.DO_NOTHING)
    questionoption = models.ForeignKey('Questionoption', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('questionanswer', 'questionoption'),)


class Questionoption(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.TextField()
    question = models.ForeignKey(Question, models.DO_NOTHING)
    position = models.IntegerField()
    identifier = models.CharField(max_length=190)

    class Meta:
        managed = True


class Quota(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    size = models.IntegerField(blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)
    close_when_sold_out = models.BooleanField()
    closed = models.BooleanField()
    release_after_exit = models.BooleanField()
    ignore_for_event_availability = models.BooleanField()

    class Meta:
        managed = True


class QuotaItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    quota = models.ForeignKey(Quota, models.DO_NOTHING)
    item = models.ForeignKey(Item, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('quota', 'item'),)


class QuotaVariations(models.Model):
    id = models.BigAutoField(primary_key=True)
    quota = models.ForeignKey(Quota, models.DO_NOTHING)
    itemvariation = models.ForeignKey(Itemvariation, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('quota', 'itemvariation'),)


class Reusablemedium(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    type = models.CharField(max_length=100)
    identifier = models.CharField(max_length=200)
    active = models.BooleanField()
    expires = models.DateTimeField(blank=True, null=True)
    info = models.JSONField()
    notes = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    linked_giftcard = models.ForeignKey(Giftcard, models.DO_NOTHING, blank=True, null=True)
    linked_orderposition = models.ForeignKey(Orderposition, models.DO_NOTHING, blank=True, null=True)
    organizer = models.ForeignKey(Organizer, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('identifier', 'type', 'organizer'),)


class Revokedticketsecret(models.Model):
    id = models.BigAutoField(primary_key=True)
    secret = models.TextField()
    created = models.DateTimeField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
    position = models.ForeignKey(Orderposition, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Scheduledeventexport(models.Model):
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
    event = models.ForeignKey(Event, models.DO_NOTHING)
    owner = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = True


class Scheduledorganizerexport(models.Model):
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
    organizer = models.ForeignKey(Organizer, models.DO_NOTHING)
    owner = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = True


class Seat(models.Model):
    id = models.BigAutoField(primary_key=True)
    blocked = models.BooleanField()
    event = models.ForeignKey(Event, models.DO_NOTHING)
    product = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)
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
        managed = True


class Seatcategorymapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    layout_category = models.CharField(max_length=190)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    product = models.ForeignKey(Item, models.DO_NOTHING)
    subevent = models.ForeignKey('Subevent', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Seatingplan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    layout = models.TextField()
    organizer = models.ForeignKey(Organizer, models.DO_NOTHING)

    class Meta:
        managed = True


class Staffsession(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(blank=True, null=True)
    session_key = models.CharField(max_length=255)
    comment = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = True


class Staffsessionauditlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField()
    url = models.CharField(max_length=255)
    session = models.ForeignKey(Staffsession, models.DO_NOTHING)
    impersonating = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    method = models.CharField(max_length=255)

    class Meta:
        managed = True


class Subevent(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField()
    name = models.TextField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(blank=True, null=True)
    date_admission = models.DateTimeField(blank=True, null=True)
    presale_end = models.DateTimeField(blank=True, null=True)
    presale_start = models.DateTimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    frontpage_text = models.TextField(blank=True, null=True)
    is_public = models.BooleanField()
    seating_plan = models.ForeignKey(Seatingplan, models.DO_NOTHING, blank=True, null=True)
    geo_lat = models.FloatField(blank=True, null=True)
    geo_lon = models.FloatField(blank=True, null=True)
    last_modified = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True


class Subeventitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING)
    disabled = models.BooleanField()
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True


class Subeventitemvariation(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING)
    variation = models.ForeignKey(Itemvariation, models.DO_NOTHING)
    disabled = models.BooleanField()
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True


class Subeventmetavalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    property = models.ForeignKey(Eventmetaproperty, models.DO_NOTHING)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('subevent', 'property'),)


class Taxrule(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    price_includes_tax = models.BooleanField()
    eu_reverse_charge = models.BooleanField()
    home_country = models.CharField(max_length=2)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    custom_rules = models.TextField(blank=True, null=True)
    internal_name = models.CharField(max_length=190, blank=True, null=True)
    keep_gross_if_rate_changes = models.BooleanField()

    class Meta:
        managed = True


class Team(models.Model):
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
    organizer = models.ForeignKey(Organizer, models.DO_NOTHING)
    can_manage_gift_cards = models.BooleanField()
    can_checkin_orders = models.BooleanField()
    can_manage_customers = models.BooleanField()
    can_manage_reusable_media = models.BooleanField()
    require_2fa = models.BooleanField()

    class Meta:
        managed = True


class TeamLimitEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('team', 'event'),)


class TeamMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('team', 'user'),)


class Teamapitoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=190)
    active = models.BooleanField()
    token = models.CharField(max_length=64)
    team = models.ForeignKey(Team, models.DO_NOTHING)

    class Meta:
        managed = True


class Teaminvite(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    team = models.ForeignKey(Team, models.DO_NOTHING)

    class Meta:
        managed = True


class Transaction(models.Model):
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
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING, blank=True, null=True)
    tax_rule = models.ForeignKey(Taxrule, models.DO_NOTHING, blank=True, null=True)
    variation = models.ForeignKey(Itemvariation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class U2Fdevice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    json_data = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = True


class User(models.Model):
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
        managed = True
        unique_together = (('auth_backend', 'auth_backend_identifier'),)


class UserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('user', 'permission'),)


class Userknownloginsource(models.Model):
    id = models.BigAutoField(primary_key=True)
    agent_type = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    last_seen = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = True


class Voucher(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    valid_until = models.DateTimeField(blank=True, null=True)
    block_quota = models.BooleanField()
    allow_ignore_quota = models.BooleanField()
    value = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    redeemed = models.IntegerField()
    variation = models.ForeignKey(Itemvariation, models.DO_NOTHING, blank=True, null=True)
    quota = models.ForeignKey(Quota, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()
    tag = models.CharField(max_length=255)
    max_usages = models.IntegerField()
    price_mode = models.CharField(max_length=100)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING, blank=True, null=True)
    show_hidden_items = models.BooleanField()
    seat = models.ForeignKey(Seat, models.DO_NOTHING, blank=True, null=True)
    budget = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    min_usages = models.IntegerField()
    all_addons_included = models.BooleanField()
    all_bundles_included = models.BooleanField()

    class Meta:
        managed = True
        unique_together = (('event', 'code'),)


class Waitinglistentry(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    email = models.CharField(max_length=254)
    locale = models.CharField(max_length=190)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    variation = models.ForeignKey(Itemvariation, models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey(Voucher, models.DO_NOTHING, blank=True, null=True)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField()
    name_cached = models.CharField(max_length=255, blank=True, null=True)
    name_parts = models.JSONField()
    phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True


class Webauthndevice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    credential_id = models.CharField(max_length=255, blank=True, null=True)
    rp_id = models.CharField(max_length=255, blank=True, null=True)
    icon_url = models.CharField(max_length=255, blank=True, null=True)
    ukey = models.TextField(blank=True, null=True)
    pub_key = models.TextField(blank=True, null=True)
    sign_count = models.IntegerField()
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = True


class Thumbnail(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    thumb = models.CharField(max_length=255)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('source', 'size'),)


class Knowndomain(models.Model):
    domainname = models.CharField(primary_key=True, max_length=255)
    organizer = models.ForeignKey(Organizer, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


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
    event = models.ForeignKey(Event, models.DO_NOTHING)
    enabled = models.BooleanField()
    attach_ical = models.BooleanField()
    restrict_to_status = models.TextField()
    checked_in_status = models.CharField(max_length=10, blank=True, null=True)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class SendmailRuleLimitProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    rule = models.ForeignKey(SendmailRule, models.DO_NOTHING)
    item = models.ForeignKey(Item, models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = (('rule', 'item'),)


class SendmailScheduledmail(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_computed = models.DateTimeField()
    computed_datetime = models.DateTimeField()
    state = models.CharField(max_length=100)
    last_successful_order_id = models.BigIntegerField(blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    rule = models.ForeignKey(SendmailRule, models.DO_NOTHING)
    subevent = models.ForeignKey(Subevent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        unique_together = (('rule', 'subevent'),)


class StripeReferencedstripeobject(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference = models.CharField(unique=True, max_length=190)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    payment = models.ForeignKey(Orderpayment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class StripeRegisteredapplepaydomain(models.Model):
    id = models.BigAutoField(primary_key=True)
    domain = models.CharField(max_length=190)
    account = models.CharField(max_length=190)

    class Meta:
        managed = True


class TicketoutputpdfTicketlayout(models.Model):
    id = models.BigAutoField(primary_key=True)
    default = models.BooleanField()
    name = models.CharField(max_length=190)
    layout = models.TextField()
    background = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = True


class TicketoutputpdfTicketlayoutitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    layout = models.ForeignKey(TicketoutputpdfTicketlayout, models.DO_NOTHING)
    sales_channel = models.CharField(max_length=190)

    class Meta:
        managed = True
        unique_together = (('item', 'layout', 'sales_channel'),)
