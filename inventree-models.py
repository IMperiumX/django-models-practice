# Loading config file : /home/inventree/data/config.yaml
# Python version 3.11.9 - /usr/local/bin/python
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'
        unique_together = (('user', 'email'),)


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BuildBuild(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.IntegerField()
    batch = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateField()
    completion_date = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    completed_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    part = models.ForeignKey('PartPart', models.DO_NOTHING)
    take_from = models.ForeignKey('StockStocklocation', models.DO_NOTHING, blank=True, null=True)
    sales_order = models.ForeignKey('OrderSalesorder', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField()
    lft = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    reference = models.CharField(unique=True, max_length=64)
    destination = models.ForeignKey('StockStocklocation', models.DO_NOTHING, related_name='buildbuild_destination_set', blank=True, null=True)
    completed = models.IntegerField()
    target_date = models.DateField(blank=True, null=True)
    issued_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='buildbuild_issued_by_set', blank=True, null=True)
    responsible = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)
    reference_int = models.BigIntegerField()
    priority = models.IntegerField()
    metadata = models.JSONField(blank=True, null=True)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    project_code = models.ForeignKey('CommonProjectcode', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_build'


class BuildBuilditem(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    stock_item = models.ForeignKey('StockStockitem', models.DO_NOTHING)
    install_into = models.ForeignKey('StockStockitem', models.DO_NOTHING, related_name='buildbuilditem_install_into_set', blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    build_line = models.ForeignKey('BuildBuildline', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_builditem'
        unique_together = (('build_line', 'stock_item', 'install_into'),)


class BuildBuildline(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    bom_item = models.ForeignKey('PartBomitem', models.DO_NOTHING)
    build = models.ForeignKey(BuildBuild, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'build_buildline'
        unique_together = (('build', 'bom_item'),)


class BuildBuildorderattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100)
    upload_date = models.DateField(blank=True, null=True)
    build = models.ForeignKey(BuildBuild, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'build_buildorderattachment'


class CommonColortheme(models.Model):
    name = models.CharField(max_length=20)
    user = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'common_colortheme'


class CommonCustomunit(models.Model):
    name = models.CharField(unique=True, max_length=50)
    symbol = models.CharField(unique=True, max_length=10)
    definition = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'common_customunit'


class CommonInventreesetting(models.Model):
    key = models.CharField(unique=True, max_length=50)
    value = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'common_inventreesetting'


class CommonInventreeusersetting(models.Model):
    value = models.CharField(max_length=2000)
    key = models.CharField(max_length=50)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_inventreeusersetting'
        unique_together = (('key', 'user'),)


class CommonNewsfeedentry(models.Model):
    feed_id = models.CharField(unique=True, max_length=250)
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    published = models.DateTimeField()
    author = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    read = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'common_newsfeedentry'


class CommonNotesimage(models.Model):
    image = models.CharField(max_length=100)
    date = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_notesimage'


class CommonNotificationentry(models.Model):
    key = models.CharField(max_length=250)
    uid = models.IntegerField()
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_notificationentry'
        unique_together = (('key', 'uid'),)


class CommonNotificationmessage(models.Model):
    target_object_id = models.IntegerField()
    source_object_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    message = models.CharField(max_length=250, blank=True, null=True)
    creation = models.DateTimeField()
    read = models.BooleanField()
    source_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    target_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, related_name='commonnotificationmessage_target_content_type_set')
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_notificationmessage'


class CommonProjectcode(models.Model):
    code = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=200)
    metadata = models.JSONField(blank=True, null=True)
    responsible = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_projectcode'


class CommonWebhookendpoint(models.Model):
    endpoint_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    token = models.CharField(max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_webhookendpoint'


class CommonWebhookmessage(models.Model):
    message_id = models.UUIDField(primary_key=True)
    host = models.CharField(max_length=255)
    header = models.CharField(max_length=255, blank=True, null=True)
    body = models.JSONField(blank=True, null=True)
    worked_on = models.BooleanField()
    endpoint = models.ForeignKey(CommonWebhookendpoint, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_webhookmessage'


class CompanyAddress(models.Model):
    title = models.CharField(max_length=100)
    primary = models.BooleanField()
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    postal_city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    shipping_notes = models.CharField(max_length=100)
    internal_shipping_notes = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    company = models.ForeignKey('CompanyCompany', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'company_address'


class CompanyCompany(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    website = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=254, blank=True, null=True)
    contact = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_customer = models.BooleanField()
    is_supplier = models.BooleanField()
    is_manufacturer = models.BooleanField()
    currency = models.CharField(max_length=3)
    metadata = models.JSONField(blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'company_company'
        unique_together = (('name', 'email'),)


class CompanyCompanyattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=100)
    upload_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(CompanyCompany, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_companyattachment'


class CompanyContact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    role = models.CharField(max_length=100)
    company = models.ForeignKey(CompanyCompany, models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_contact'


class CompanyManufacturerpart(models.Model):
    mpn = models.CharField(db_column='MPN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    manufacturer = models.ForeignKey(CompanyCompany, models.DO_NOTHING, blank=True, null=True)
    part = models.ForeignKey('PartPart', models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'company_manufacturerpart'
        unique_together = (('part', 'manufacturer', 'mpn'),)


class CompanyManufacturerpartattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=100)
    upload_date = models.DateField(blank=True, null=True)
    manufacturer_part = models.ForeignKey(CompanyManufacturerpart, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_manufacturerpartattachment'


class CompanyManufacturerpartparameter(models.Model):
    name = models.CharField(max_length=500)
    value = models.CharField(max_length=500)
    units = models.CharField(max_length=64, blank=True, null=True)
    manufacturer_part = models.ForeignKey(CompanyManufacturerpart, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'company_manufacturerpartparameter'
        unique_together = (('manufacturer_part', 'name'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoQOrmq(models.Model):
    key = models.CharField(max_length=100)
    payload = models.TextField()
    lock = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_q_ormq'


class DjangoQSchedule(models.Model):
    func = models.CharField(max_length=256)
    hook = models.CharField(max_length=256, blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    schedule_type = models.CharField(max_length=2)
    repeats = models.IntegerField()
    next_run = models.DateTimeField(blank=True, null=True)
    task = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    minutes = models.SmallIntegerField(blank=True, null=True)
    cron = models.CharField(max_length=100, blank=True, null=True)
    cluster = models.CharField(max_length=100, blank=True, null=True)
    intended_date_kwarg = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_q_schedule'


class DjangoQTask(models.Model):
    name = models.CharField(max_length=100)
    func = models.CharField(max_length=256)
    hook = models.CharField(max_length=256, blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    started = models.DateTimeField()
    stopped = models.DateTimeField()
    success = models.BooleanField()
    id = models.CharField(primary_key=True, max_length=32)
    group = models.CharField(max_length=100, blank=True, null=True)
    attempt_count = models.IntegerField()
    cluster = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_q_task'


class ErrorReportError(models.Model):
    kind = models.CharField(max_length=128, blank=True, null=True)
    info = models.TextField()
    data = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    when = models.DateTimeField()
    html = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'error_report_error'


class ExchangeExchangebackend(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    last_update = models.DateTimeField()
    base_currency = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'exchange_exchangebackend'


class ExchangeRate(models.Model):
    currency = models.CharField(max_length=3)
    value = models.DecimalField(max_digits=20, decimal_places=6)
    backend = models.ForeignKey(ExchangeExchangebackend, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exchange_rate'
        unique_together = (('currency', 'backend'),)


class FlagsFlagstate(models.Model):
    name = models.CharField(max_length=64)
    condition = models.CharField(max_length=64)
    value = models.CharField(max_length=127)
    required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'flags_flagstate'
        unique_together = (('name', 'condition', 'value'),)


class LabelBuildlinelabel(models.Model):
    metadata = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    label = models.CharField(unique=True, max_length=100)
    enabled = models.BooleanField()
    width = models.FloatField()
    height = models.FloatField()
    filename_pattern = models.CharField(max_length=100)
    filters = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'label_buildlinelabel'


class LabelLabeloutput(models.Model):
    label = models.CharField(unique=True, max_length=100)
    created = models.DateField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_labeloutput'


class LabelPartlabel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    label = models.CharField(unique=True, max_length=100)
    enabled = models.BooleanField()
    width = models.FloatField()
    height = models.FloatField()
    filename_pattern = models.CharField(max_length=100)
    filters = models.CharField(max_length=250)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_partlabel'


class LabelStockitemlabel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    label = models.CharField(unique=True, max_length=100)
    filters = models.CharField(max_length=250)
    enabled = models.BooleanField()
    height = models.FloatField()
    width = models.FloatField()
    filename_pattern = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_stockitemlabel'


class LabelStocklocationlabel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    label = models.CharField(unique=True, max_length=100)
    filters = models.CharField(max_length=250)
    enabled = models.BooleanField()
    height = models.FloatField()
    width = models.FloatField()
    filename_pattern = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_stocklocationlabel'


class MachineMachineconfig(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    machine_type = models.CharField(max_length=255)
    driver = models.CharField(max_length=255)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'machine_machineconfig'


class MachineMachinesetting(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=2000)
    config_type = models.CharField(max_length=1)
    machine_config = models.ForeignKey(MachineMachineconfig, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'machine_machinesetting'
        unique_together = (('machine_config', 'config_type', 'key'),)


class OrderPurchaseorder(models.Model):
    reference = models.CharField(unique=True, max_length=64)
    description = models.CharField(max_length=250)
    creation_date = models.DateField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey(CompanyCompany, models.DO_NOTHING, blank=True, null=True)
    link = models.CharField(max_length=200)
    status = models.IntegerField()
    complete_date = models.DateField(blank=True, null=True)
    received_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='orderpurchaseorder_received_by_set', blank=True, null=True)
    supplier_reference = models.CharField(max_length=64)
    target_date = models.DateField(blank=True, null=True)
    responsible = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)
    reference_int = models.BigIntegerField()
    metadata = models.JSONField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    total_price_currency = models.CharField(max_length=3, blank=True, null=True)
    contact = models.ForeignKey(CompanyContact, models.DO_NOTHING, blank=True, null=True)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    project_code = models.ForeignKey(CommonProjectcode, models.DO_NOTHING, blank=True, null=True)
    order_currency = models.CharField(max_length=3, blank=True, null=True)
    address = models.ForeignKey(CompanyAddress, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_purchaseorder'


class OrderPurchaseorderattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100)
    order = models.ForeignKey(OrderPurchaseorder, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_purchaseorderattachment'


class OrderPurchaseorderextraline(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    reference = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    target_date = models.DateField(blank=True, null=True)
    context = models.JSONField(blank=True, null=True)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    order = models.ForeignKey(OrderPurchaseorder, models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'order_purchaseorderextraline'


class OrderPurchaseorderlineitem(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    reference = models.CharField(max_length=100)
    received = models.DecimalField(max_digits=15, decimal_places=5)
    order = models.ForeignKey(OrderPurchaseorder, models.DO_NOTHING)
    part = models.ForeignKey('PartSupplierpart', models.DO_NOTHING, blank=True, null=True)
    notes = models.CharField(max_length=500)
    purchase_price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    purchase_price_currency = models.CharField(max_length=3, blank=True, null=True)
    destination = models.ForeignKey('StockStocklocation', models.DO_NOTHING, blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    link = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'order_purchaseorderlineitem'


class OrderReturnorder(models.Model):
    metadata = models.JSONField(blank=True, null=True)
    reference_int = models.BigIntegerField()
    description = models.CharField(max_length=250)
    link = models.CharField(max_length=200)
    creation_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reference = models.CharField(unique=True, max_length=64)
    status = models.IntegerField()
    customer_reference = models.CharField(max_length=64)
    issue_date = models.DateField(blank=True, null=True)
    complete_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(CompanyCompany, models.DO_NOTHING, blank=True, null=True)
    responsible = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)
    contact = models.ForeignKey(CompanyContact, models.DO_NOTHING, blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    total_price_currency = models.CharField(max_length=3, blank=True, null=True)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    project_code = models.ForeignKey(CommonProjectcode, models.DO_NOTHING, blank=True, null=True)
    order_currency = models.CharField(max_length=3, blank=True, null=True)
    address = models.ForeignKey(CompanyAddress, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_returnorder'


class OrderReturnorderattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=100)
    upload_date = models.DateField(blank=True, null=True)
    order = models.ForeignKey(OrderReturnorder, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_returnorderattachment'


class OrderReturnorderextraline(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    reference = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    target_date = models.DateField(blank=True, null=True)
    context = models.JSONField(blank=True, null=True)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    order = models.ForeignKey(OrderReturnorder, models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'order_returnorderextraline'


class OrderReturnorderlineitem(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    reference = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    target_date = models.DateField(blank=True, null=True)
    received_date = models.DateField(blank=True, null=True)
    outcome = models.IntegerField()
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    link = models.CharField(max_length=200)
    item = models.ForeignKey('StockStockitem', models.DO_NOTHING)
    order = models.ForeignKey(OrderReturnorder, models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_returnorderlineitem'
        unique_together = (('order', 'item'),)


class OrderSalesorder(models.Model):
    reference = models.CharField(unique=True, max_length=64)
    description = models.CharField(max_length=250)
    link = models.CharField(max_length=200)
    creation_date = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    shipment_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    customer_reference = models.CharField(max_length=64)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(CompanyCompany, models.DO_NOTHING, blank=True, null=True)
    shipped_by = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='ordersalesorder_shipped_by_set', blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    responsible = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)
    reference_int = models.BigIntegerField()
    metadata = models.JSONField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    total_price_currency = models.CharField(max_length=3, blank=True, null=True)
    contact = models.ForeignKey(CompanyContact, models.DO_NOTHING, blank=True, null=True)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    project_code = models.ForeignKey(CommonProjectcode, models.DO_NOTHING, blank=True, null=True)
    order_currency = models.CharField(max_length=3, blank=True, null=True)
    address = models.ForeignKey(CompanyAddress, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_salesorder'


class OrderSalesorderallocation(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    item = models.ForeignKey('StockStockitem', models.DO_NOTHING)
    line = models.ForeignKey('OrderSalesorderlineitem', models.DO_NOTHING)
    shipment = models.ForeignKey('OrderSalesordershipment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_salesorderallocation'


class OrderSalesorderattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100)
    order = models.ForeignKey(OrderSalesorder, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_salesorderattachment'


class OrderSalesorderextraline(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    reference = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    target_date = models.DateField(blank=True, null=True)
    context = models.JSONField(blank=True, null=True)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    order = models.ForeignKey(OrderSalesorder, models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'order_salesorderextraline'


class OrderSalesorderlineitem(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    reference = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    order = models.ForeignKey(OrderSalesorder, models.DO_NOTHING)
    part = models.ForeignKey('PartPart', models.DO_NOTHING, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    sale_price_currency = models.CharField(max_length=3, blank=True, null=True)
    shipped = models.DecimalField(max_digits=15, decimal_places=5)
    target_date = models.DateField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    link = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'order_salesorderlineitem'


class OrderSalesordershipment(models.Model):
    shipment_date = models.DateField(blank=True, null=True)
    reference = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    checked_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(OrderSalesorder, models.DO_NOTHING)
    tracking_number = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    metadata = models.JSONField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_salesordershipment'
        unique_together = (('order', 'reference'),)


class OtpStaticStaticdevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    throttling_failure_count = models.IntegerField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_totp_totpdevice'


class PartBomitem(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    overage = models.CharField(max_length=24)
    note = models.CharField(max_length=500)
    part = models.ForeignKey('PartPart', models.DO_NOTHING)
    sub_part = models.ForeignKey('PartPart', models.DO_NOTHING, related_name='partbomitem_sub_part_set')
    reference = models.CharField(max_length=5000)
    checksum = models.CharField(max_length=128)
    optional = models.BooleanField()
    inherited = models.BooleanField()
    allow_variants = models.BooleanField()
    consumable = models.BooleanField()
    validated = models.BooleanField()
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_bomitem'


class PartBomitemsubstitute(models.Model):
    bom_item = models.ForeignKey(PartBomitem, models.DO_NOTHING)
    part = models.ForeignKey('PartPart', models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_bomitemsubstitute'
        unique_together = (('part', 'bom_item'),)


class PartPart(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250, blank=True, null=True)
    ipn = models.CharField(db_column='IPN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    minimum_stock = models.DecimalField(max_digits=19, decimal_places=6)
    units = models.CharField(max_length=20, blank=True, null=True)
    trackable = models.BooleanField()
    purchaseable = models.BooleanField()
    salable = models.BooleanField()
    active = models.BooleanField()
    notes = models.TextField(blank=True, null=True)
    bom_checksum = models.CharField(max_length=128)
    bom_checked_date = models.DateField(blank=True, null=True)
    bom_checked_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('PartPartcategory', models.DO_NOTHING, blank=True, null=True)
    default_location = models.ForeignKey('StockStocklocation', models.DO_NOTHING, blank=True, null=True)
    default_supplier = models.ForeignKey('PartSupplierpart', models.DO_NOTHING, blank=True, null=True)
    is_template = models.BooleanField()
    variant_of = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    assembly = models.BooleanField()
    component = models.BooleanField()
    virtual = models.BooleanField()
    revision = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    creation_user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='partpart_creation_user_set', blank=True, null=True)
    level = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    default_expiry = models.IntegerField()
    base_cost = models.DecimalField(max_digits=19, decimal_places=6)
    multiple = models.IntegerField()
    metadata = models.JSONField(blank=True, null=True)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    last_stocktake = models.DateField(blank=True, null=True)
    responsible_owner = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_part'
        unique_together = (('name', 'ipn', 'revision'),)


class PartPartattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100)
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_partattachment'


class PartPartcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    default_keywords = models.CharField(max_length=250, blank=True, null=True)
    default_location = models.ForeignKey('StockStocklocation', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    metadata = models.JSONField(blank=True, null=True)
    pathstring = models.CharField(max_length=250)
    icon = models.CharField(max_length=100)
    structural = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'part_partcategory'


class PartPartcategoryparametertemplate(models.Model):
    default_value = models.CharField(max_length=500)
    category = models.ForeignKey(PartPartcategory, models.DO_NOTHING)
    parameter_template = models.ForeignKey('PartPartparametertemplate', models.DO_NOTHING)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_partcategoryparametertemplate'
        unique_together = (('category', 'parameter_template'),)


class PartPartcategorystar(models.Model):
    category = models.ForeignKey(PartPartcategory, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'part_partcategorystar'
        unique_together = (('category', 'user'),)


class PartPartinternalpricebreak(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_partinternalpricebreak'
        unique_together = (('part', 'quantity'),)


class PartPartparameter(models.Model):
    data = models.CharField(max_length=500)
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    template = models.ForeignKey('PartPartparametertemplate', models.DO_NOTHING)
    data_numeric = models.FloatField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_partparameter'
        unique_together = (('part', 'template'),)


class PartPartparametertemplate(models.Model):
    name = models.CharField(unique=True, max_length=100)
    units = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    metadata = models.JSONField(blank=True, null=True)
    checkbox = models.BooleanField()
    choices = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'part_partparametertemplate'


class PartPartpricing(models.Model):
    currency = models.CharField(max_length=10)
    updated = models.DateTimeField(blank=True, null=True)
    scheduled_for_update = models.BooleanField()
    bom_cost_min_currency = models.CharField(max_length=3, blank=True, null=True)
    bom_cost_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    bom_cost_max_currency = models.CharField(max_length=3, blank=True, null=True)
    bom_cost_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    purchase_cost_min_currency = models.CharField(max_length=3, blank=True, null=True)
    purchase_cost_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    purchase_cost_max_currency = models.CharField(max_length=3, blank=True, null=True)
    purchase_cost_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    internal_cost_min_currency = models.CharField(max_length=3, blank=True, null=True)
    internal_cost_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    internal_cost_max_currency = models.CharField(max_length=3, blank=True, null=True)
    internal_cost_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    supplier_price_min_currency = models.CharField(max_length=3, blank=True, null=True)
    supplier_price_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    supplier_price_max_currency = models.CharField(max_length=3, blank=True, null=True)
    supplier_price_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    variant_cost_min_currency = models.CharField(max_length=3, blank=True, null=True)
    variant_cost_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    variant_cost_max_currency = models.CharField(max_length=3, blank=True, null=True)
    variant_cost_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    overall_min_currency = models.CharField(max_length=3, blank=True, null=True)
    overall_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    overall_max_currency = models.CharField(max_length=3, blank=True, null=True)
    overall_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    sale_price_min_currency = models.CharField(max_length=3, blank=True, null=True)
    sale_price_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    sale_price_max_currency = models.CharField(max_length=3, blank=True, null=True)
    sale_price_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    sale_history_min_currency = models.CharField(max_length=3, blank=True, null=True)
    sale_history_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    sale_history_max_currency = models.CharField(max_length=3, blank=True, null=True)
    sale_history_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    part = models.OneToOneField(PartPart, models.DO_NOTHING)
    override_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    override_max_currency = models.CharField(max_length=3, blank=True, null=True)
    override_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    override_min_currency = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_partpricing'


class PartPartrelated(models.Model):
    part_1 = models.ForeignKey(PartPart, models.DO_NOTHING)
    part_2 = models.ForeignKey(PartPart, models.DO_NOTHING, related_name='partpartrelated_part_2_set')
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_partrelated'
        unique_together = (('part_1', 'part_2'),)


class PartPartsellpricebreak(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_partsellpricebreak'
        unique_together = (('part', 'quantity'),)


class PartPartstar(models.Model):
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'part_partstar'
        unique_together = (('part', 'user'),)


class PartPartstocktake(models.Model):
    quantity = models.DecimalField(max_digits=19, decimal_places=5)
    date = models.DateField()
    note = models.CharField(max_length=250)
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    cost_max = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    cost_max_currency = models.CharField(max_length=3, blank=True, null=True)
    cost_min = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    cost_min_currency = models.CharField(max_length=3, blank=True, null=True)
    item_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'part_partstocktake'


class PartPartstocktakereport(models.Model):
    date = models.DateField()
    report = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    part_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'part_partstocktakereport'


class PartParttesttemplate(models.Model):
    test_name = models.CharField(max_length=100)
    required = models.BooleanField()
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    description = models.CharField(max_length=100, blank=True, null=True)
    requires_attachment = models.BooleanField()
    requires_value = models.BooleanField()
    metadata = models.JSONField(blank=True, null=True)
    key = models.CharField(max_length=100)
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'part_parttesttemplate'


class PartSupplierpart(models.Model):
    sku = models.CharField(db_column='SKU', max_length=100)  # Field name made lowercase.
    link = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=10, decimal_places=3)
    packaging = models.CharField(max_length=50, blank=True, null=True)
    multiple = models.IntegerField()
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    supplier = models.ForeignKey(CompanyCompany, models.DO_NOTHING)
    manufacturer_part = models.ForeignKey(CompanyManufacturerpart, models.DO_NOTHING, blank=True, null=True)
    availability_updated = models.DateTimeField(blank=True, null=True)
    available = models.DecimalField(max_digits=10, decimal_places=3)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    updated = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    pack_quantity = models.CharField(max_length=25)
    pack_quantity_native = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'part_supplierpart'
        unique_together = (('part', 'supplier', 'sku'),)


class PartSupplierpricebreak(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    part = models.ForeignKey(PartSupplierpart, models.DO_NOTHING)
    price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    price_currency = models.CharField(max_length=3, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part_supplierpricebreak'
        unique_together = (('part', 'quantity'),)


class PluginNotificationusersetting(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=2000)
    method = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_notificationusersetting'
        unique_together = (('method', 'user', 'key'),)


class PluginPluginconfig(models.Model):
    key = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    metadata = models.JSONField(blank=True, null=True)
    package_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_pluginconfig'


class PluginPluginsetting(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=2000)
    plugin = models.ForeignKey(PluginPluginconfig, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'plugin_pluginsetting'
        unique_together = (('plugin', 'key'),)


class ReportBillofmaterialsreport(models.Model):
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    revision = models.IntegerField()
    enabled = models.BooleanField()
    filters = models.CharField(max_length=250)
    filename_pattern = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    landscape = models.BooleanField()
    page_size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report_billofmaterialsreport'


class ReportBuildreport(models.Model):
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    revision = models.IntegerField()
    enabled = models.BooleanField()
    filters = models.CharField(max_length=250)
    filename_pattern = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    landscape = models.BooleanField()
    page_size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report_buildreport'


class ReportPurchaseorderreport(models.Model):
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    revision = models.IntegerField()
    enabled = models.BooleanField()
    filters = models.CharField(max_length=250)
    filename_pattern = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    landscape = models.BooleanField()
    page_size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report_purchaseorderreport'


class ReportReportasset(models.Model):
    asset = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'report_reportasset'


class ReportReportsnippet(models.Model):
    snippet = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'report_reportsnippet'


class ReportReturnorderreport(models.Model):
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    revision = models.IntegerField()
    filename_pattern = models.CharField(max_length=100)
    enabled = models.BooleanField()
    filters = models.CharField(max_length=250)
    metadata = models.JSONField(blank=True, null=True)
    landscape = models.BooleanField()
    page_size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report_returnorderreport'


class ReportSalesorderreport(models.Model):
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    revision = models.IntegerField()
    enabled = models.BooleanField()
    filters = models.CharField(max_length=250)
    filename_pattern = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    landscape = models.BooleanField()
    page_size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report_salesorderreport'


class ReportStocklocationreport(models.Model):
    metadata = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    revision = models.IntegerField()
    filename_pattern = models.CharField(max_length=100)
    enabled = models.BooleanField()
    filters = models.CharField(max_length=250)
    landscape = models.BooleanField()
    page_size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report_stocklocationreport'


class ReportTestreport(models.Model):
    name = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    filters = models.CharField(max_length=250)
    enabled = models.BooleanField()
    revision = models.IntegerField()
    include_installed = models.BooleanField()
    filename_pattern = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    landscape = models.BooleanField()
    page_size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report_testreport'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=200)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.JSONField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    provider_id = models.CharField(max_length=200)
    settings = models.JSONField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class StockStockitem(models.Model):
    serial = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200)
    batch = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.DecimalField(max_digits=15, decimal_places=5)
    updated = models.DateTimeField(blank=True, null=True)
    stocktake_date = models.DateField(blank=True, null=True)
    review_needed = models.BooleanField()
    delete_on_deplete = models.BooleanField()
    status = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    belongs_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockStocklocation', models.DO_NOTHING, blank=True, null=True)
    part = models.ForeignKey(PartPart, models.DO_NOTHING)
    stocktake_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    supplier_part = models.ForeignKey(PartSupplierpart, models.DO_NOTHING, blank=True, null=True)
    purchase_order = models.ForeignKey(OrderPurchaseorder, models.DO_NOTHING, blank=True, null=True)
    build = models.ForeignKey(BuildBuild, models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField()
    lft = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='stockstockitem_parent_set', blank=True, null=True)
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    sales_order = models.ForeignKey(OrderSalesorder, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(CompanyCompany, models.DO_NOTHING, blank=True, null=True)
    is_building = models.BooleanField()
    purchase_price = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    purchase_price_currency = models.CharField(max_length=3, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)
    packaging = models.CharField(max_length=50, blank=True, null=True)
    serial_int = models.IntegerField()
    metadata = models.JSONField(blank=True, null=True)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    consumed_by = models.ForeignKey(BuildBuild, models.DO_NOTHING, related_name='stockstockitem_consumed_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_stockitem'


class StockStockitemattachment(models.Model):
    attachment = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100)
    stock_item = models.ForeignKey(StockStockitem, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_stockitemattachment'


class StockStockitemtestresult(models.Model):
    result = models.BooleanField()
    value = models.CharField(max_length=500)
    date = models.DateTimeField()
    attachment = models.CharField(max_length=100, blank=True, null=True)
    stock_item = models.ForeignKey(StockStockitem, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    notes = models.CharField(max_length=500)
    metadata = models.JSONField(blank=True, null=True)
    template = models.ForeignKey(PartParttesttemplate, models.DO_NOTHING)
    finished_datetime = models.DateTimeField(blank=True, null=True)
    started_datetime = models.DateTimeField(blank=True, null=True)
    test_station = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'stock_stockitemtestresult'


class StockStockitemtracking(models.Model):
    date = models.DateTimeField()
    notes = models.CharField(max_length=512, blank=True, null=True)
    item = models.ForeignKey(StockStockitem, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    deltas = models.JSONField(blank=True, null=True)
    tracking_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_stockitemtracking'


class StockStocklocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    owner = models.ForeignKey('UsersOwner', models.DO_NOTHING, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    pathstring = models.CharField(max_length=250)
    icon = models.CharField(max_length=100)
    barcode_data = models.CharField(max_length=500)
    barcode_hash = models.CharField(max_length=128)
    structural = models.BooleanField()
    external = models.BooleanField()
    location_type = models.ForeignKey('StockStocklocationtype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_stocklocation'


class StockStocklocationtype(models.Model):
    metadata = models.JSONField(blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    icon = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stock_stocklocationtype'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


class UserSessionsSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    user_agent = models.CharField(max_length=200, blank=True, null=True)
    last_activity = models.DateTimeField()
    ip = models.GenericIPAddressField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_sessions_session'


class UsersApitoken(models.Model):
    created = models.DateTimeField()
    key = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    expiry = models.DateField()
    revoked = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    last_seen = models.DateField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_apitoken'


class UsersOwner(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    owner_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_owner'
        unique_together = (('owner_type', 'owner_id'),)


class UsersRuleset(models.Model):
    name = models.CharField(max_length=50)
    can_view = models.BooleanField()
    can_add = models.BooleanField()
    can_change = models.BooleanField()
    can_delete = models.BooleanField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_ruleset'
        unique_together = (('name', 'group'),)
