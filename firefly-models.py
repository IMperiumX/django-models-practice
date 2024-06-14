# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TwoFaTokens(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    expires_at = models.DateTimeField()
    token = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = '2fa_tokens'


class AccountBalances(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    account = models.ForeignKey('Accounts', models.DO_NOTHING)
    transaction_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)
    transaction_journal = models.ForeignKey('TransactionJournals', models.DO_NOTHING, blank=True, null=True)
    balance = models.DecimalField(max_digits=32, decimal_places=12)

    class Meta:
        managed = False
        db_table = 'account_balances'
        unique_together = (('account', 'transaction_currency', 'transaction_journal', 'date', 'title'),)


class AccountMeta(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey('Accounts', models.DO_NOTHING)
    name = models.CharField(max_length=191)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'account_meta'


class AccountTypes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'account_types'


class Accounts(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    account_type = models.ForeignKey(AccountTypes, models.DO_NOTHING)
    name = models.CharField(max_length=1024)
    virtual_balance = models.DecimalField(max_digits=32, decimal_places=12, blank=True, null=True)
    iban = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    encrypted = models.IntegerField()
    order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'accounts'


class Attachments(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    attachable_id = models.PositiveIntegerField()
    attachable_type = models.CharField(max_length=255)
    md5 = models.CharField(max_length=128)
    filename = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mime = models.CharField(max_length=1024)
    size = models.PositiveIntegerField()
    uploaded = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attachments'


class AuditLogEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    auditable_id = models.PositiveIntegerField()
    auditable_type = models.CharField(max_length=191)
    changer_id = models.PositiveIntegerField()
    changer_type = models.CharField(max_length=191)
    action = models.CharField(max_length=255)
    before = models.TextField(blank=True, null=True)
    after = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log_entries'


class AutoBudgets(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    budget = models.ForeignKey('Budgets', models.DO_NOTHING)
    transaction_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING)
    auto_budget_type = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=32, decimal_places=12)
    period = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'auto_budgets'


class AvailableBudgets(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    transaction_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=32, decimal_places=12)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'available_budgets'


class Bills(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    transaction_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=1024)
    match = models.CharField(max_length=1024)
    amount_min = models.DecimalField(max_digits=32, decimal_places=12)
    amount_max = models.DecimalField(max_digits=32, decimal_places=12)
    date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    extension_date = models.DateField(blank=True, null=True)
    repeat_freq = models.CharField(max_length=30)
    skip = models.PositiveSmallIntegerField()
    automatch = models.IntegerField()
    active = models.IntegerField()
    name_encrypted = models.IntegerField()
    match_encrypted = models.IntegerField()
    order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bills'


class BudgetLimits(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    budget = models.ForeignKey('Budgets', models.DO_NOTHING)
    transaction_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=32, decimal_places=12)
    period = models.CharField(max_length=12, blank=True, null=True)
    generated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'budget_limits'


class BudgetTransaction(models.Model):
    budget = models.ForeignKey('Budgets', models.DO_NOTHING)
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'budget_transaction'


class BudgetTransactionJournal(models.Model):
    budget = models.ForeignKey('Budgets', models.DO_NOTHING)
    budget_limit = models.ForeignKey(BudgetLimits, models.DO_NOTHING, blank=True, null=True)
    transaction_journal = models.ForeignKey('TransactionJournals', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'budget_transaction_journal'


class Budgets(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=1024)
    active = models.IntegerField()
    encrypted = models.IntegerField()
    order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'budgets'


class Categories(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=1024)
    encrypted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories'


class CategoryTransaction(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'category_transaction'


class CategoryTransactionJournal(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    transaction_journal = models.ForeignKey('TransactionJournals', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'category_transaction_journal'


class Configuration(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'configuration'


class CurrencyExchangeRates(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    from_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING)
    to_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING, related_name='currencyexchangerates_to_currency_set')
    date = models.DateField()
    rate = models.DecimalField(max_digits=32, decimal_places=12)
    user_rate = models.DecimalField(max_digits=32, decimal_places=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_exchange_rates'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=191)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class GroupJournals(models.Model):
    transaction_group = models.ForeignKey('TransactionGroups', models.DO_NOTHING)
    transaction_journal = models.ForeignKey('TransactionJournals', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_journals'
        unique_together = (('transaction_group', 'transaction_journal'),)


class GroupMemberships(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING)
    user_role = models.ForeignKey('UserRoles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_memberships'
        unique_together = (('user', 'user_group', 'user_role'),)


class InvitedUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    email = models.CharField(max_length=255)
    invite_code = models.CharField(max_length=64)
    expires = models.DateTimeField()
    redeemed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invited_users'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=191)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class JournalLinks(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    link_type = models.ForeignKey('LinkTypes', models.DO_NOTHING)
    source = models.ForeignKey('TransactionJournals', models.DO_NOTHING)
    destination = models.ForeignKey('TransactionJournals', models.DO_NOTHING, related_name='journallinks_destination_set')
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_links'
        unique_together = (('link_type', 'source', 'destination'),)


class JournalMeta(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    transaction_journal = models.ForeignKey('TransactionJournals', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    data = models.TextField()
    hash = models.CharField(max_length=64)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_meta'


class LimitRepetitions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    budget_limit = models.ForeignKey(BudgetLimits, models.DO_NOTHING)
    startdate = models.DateField()
    enddate = models.DateField()
    amount = models.DecimalField(max_digits=32, decimal_places=12)

    class Meta:
        managed = False
        db_table = 'limit_repetitions'


class LinkTypes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=191)
    outward = models.CharField(max_length=191)
    inward = models.CharField(max_length=191)
    editable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'link_types'
        unique_together = (('name', 'outward', 'inward'),)


class Locations(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    locatable_id = models.PositiveIntegerField()
    locatable_type = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    zoom_level = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Notes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    noteable_id = models.PositiveIntegerField()
    noteable_type = models.CharField(max_length=191)
    title = models.CharField(max_length=191, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


class Notifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=191)
    notifiable_type = models.CharField(max_length=191)
    notifiable_id = models.PositiveBigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField()
    client_id = models.IntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    secret = models.CharField(max_length=100, blank=True, null=True)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class ObjectGroupables(models.Model):
    object_group_id = models.IntegerField()
    object_groupable_id = models.PositiveIntegerField()
    object_groupable_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'object_groupables'


class ObjectGroups(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'object_groups'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PermissionRole(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)  # The composite primary key (permission_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permission_role'
        unique_together = (('permission', 'role'),)


class Permissions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=191)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=191)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class PiggyBankEvents(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    piggy_bank = models.ForeignKey('PiggyBanks', models.DO_NOTHING)
    transaction_journal = models.ForeignKey('TransactionJournals', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=32, decimal_places=12)

    class Meta:
        managed = False
        db_table = 'piggy_bank_events'


class PiggyBankRepetitions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    piggy_bank = models.ForeignKey('PiggyBanks', models.DO_NOTHING)
    startdate = models.DateField(blank=True, null=True)
    targetdate = models.DateField(blank=True, null=True)
    currentamount = models.DecimalField(max_digits=32, decimal_places=12)

    class Meta:
        managed = False
        db_table = 'piggy_bank_repetitions'


class PiggyBanks(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(Accounts, models.DO_NOTHING)
    name = models.CharField(max_length=1024)
    targetamount = models.DecimalField(max_digits=32, decimal_places=12)
    startdate = models.DateField(blank=True, null=True)
    targetdate = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField()
    active = models.IntegerField()
    encrypted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'piggy_banks'


class Preferences(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=1024)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preferences'


class Recurrences(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    transaction_type = models.ForeignKey('TransactionTypes', models.DO_NOTHING)
    title = models.CharField(max_length=1024)
    description = models.TextField()
    first_date = models.DateField()
    repeat_until = models.DateField(blank=True, null=True)
    latest_date = models.DateField(blank=True, null=True)
    repetitions = models.PositiveSmallIntegerField()
    apply_rules = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recurrences'


class RecurrencesMeta(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    recurrence = models.ForeignKey(Recurrences, models.DO_NOTHING)
    name = models.CharField(max_length=50)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'recurrences_meta'


class RecurrencesRepetitions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    recurrence = models.ForeignKey(Recurrences, models.DO_NOTHING)
    repetition_type = models.CharField(max_length=50)
    repetition_moment = models.CharField(max_length=50)
    repetition_skip = models.PositiveSmallIntegerField()
    weekend = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'recurrences_repetitions'


class RecurrencesTransactions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    recurrence = models.ForeignKey(Recurrences, models.DO_NOTHING)
    transaction_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING)
    transaction_type = models.ForeignKey('TransactionTypes', models.DO_NOTHING, blank=True, null=True)
    foreign_currency = models.ForeignKey('TransactionCurrencies', models.DO_NOTHING, related_name='recurrencestransactions_foreign_currency_set', blank=True, null=True)
    source = models.ForeignKey(Accounts, models.DO_NOTHING)
    destination = models.ForeignKey(Accounts, models.DO_NOTHING, related_name='recurrencestransactions_destination_set')
    amount = models.DecimalField(max_digits=32, decimal_places=12)
    foreign_amount = models.DecimalField(max_digits=32, decimal_places=12, blank=True, null=True)
    description = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'recurrences_transactions'


class RoleUser(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_user'
        unique_together = (('user', 'role'),)


class Roles(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=191)
    display_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class RtMeta(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    rt = models.ForeignKey(RecurrencesTransactions, models.DO_NOTHING)
    name = models.CharField(max_length=50)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'rt_meta'


class RuleActions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rule = models.ForeignKey('Rules', models.DO_NOTHING)
    action_type = models.CharField(max_length=50)
    action_value = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    active = models.IntegerField()
    stop_processing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule_actions'


class RuleGroups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()
    active = models.IntegerField()
    stop_processing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule_groups'


class RuleTriggers(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rule = models.ForeignKey('Rules', models.DO_NOTHING)
    trigger_type = models.CharField(max_length=50)
    trigger_value = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    active = models.IntegerField()
    stop_processing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule_triggers'


class Rules(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    rule_group = models.ForeignKey(RuleGroups, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()
    active = models.IntegerField()
    stop_processing = models.IntegerField()
    strict = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rules'


class Sessions(models.Model):
    id = models.CharField(unique=True, max_length=191)
    user_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class TagTransactionJournal(models.Model):
    tag = models.ForeignKey('Tags', models.DO_NOTHING)
    transaction_journal = models.ForeignKey('TransactionJournals', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tag_transaction_journal'
        unique_together = (('tag', 'transaction_journal'),)


class Tags(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    tag = models.CharField(max_length=1024)
    tagmode = models.CharField(db_column='tagMode', max_length=1024)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    zoomlevel = models.PositiveSmallIntegerField(db_column='zoomLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tags'


class TransactionCurrencies(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField()
    code = models.CharField(unique=True, max_length=51)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=51)
    decimal_places = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_currencies'


class TransactionCurrencyUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    transaction_currency = models.ForeignKey(TransactionCurrencies, models.DO_NOTHING)
    user_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_currency_user'
        unique_together = (('user', 'transaction_currency'),)


class TransactionCurrencyUserGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING)
    transaction_currency = models.ForeignKey(TransactionCurrencies, models.DO_NOTHING)
    group_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_currency_user_group'
        unique_together = (('user_group', 'transaction_currency'),)


class TransactionGroups(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_groups'


class TransactionJournals(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    user_group = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    transaction_type = models.ForeignKey('TransactionTypes', models.DO_NOTHING)
    transaction_group = models.ForeignKey(TransactionGroups, models.DO_NOTHING, blank=True, null=True)
    bill = models.ForeignKey(Bills, models.DO_NOTHING, blank=True, null=True)
    transaction_currency = models.ForeignKey(TransactionCurrencies, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=1024)
    date = models.DateTimeField()
    interest_date = models.DateField(blank=True, null=True)
    book_date = models.DateField(blank=True, null=True)
    process_date = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField()
    tag_count = models.PositiveIntegerField()
    encrypted = models.IntegerField()
    completed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_journals'


class TransactionTypes(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'transaction_types'


class Transactions(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    reconciled = models.IntegerField()
    account = models.ForeignKey(Accounts, models.DO_NOTHING)
    transaction_journal = models.ForeignKey(TransactionJournals, models.DO_NOTHING)
    description = models.CharField(max_length=1024, blank=True, null=True)
    transaction_currency = models.ForeignKey(TransactionCurrencies, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=32, decimal_places=12)
    foreign_amount = models.DecimalField(max_digits=32, decimal_places=12, blank=True, null=True)
    foreign_currency = models.ForeignKey(TransactionCurrencies, models.DO_NOTHING, related_name='transactions_foreign_currency_set', blank=True, null=True)
    identifier = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'transactions'


class UserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'user_groups'


class UserRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    objectguid = models.CharField(max_length=36, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    reset = models.CharField(max_length=32, blank=True, null=True)
    blocked = models.PositiveIntegerField()
    blocked_code = models.CharField(max_length=25, blank=True, null=True)
    mfa_secret = models.CharField(max_length=50, blank=True, null=True)
    domain = models.CharField(max_length=191, blank=True, null=True)
    user_group = models.ForeignKey(UserGroups, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WebhookAttempts(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    webhook_message = models.ForeignKey('WebhookMessages', models.DO_NOTHING)
    status_code = models.PositiveSmallIntegerField()
    logs = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webhook_attempts'


class WebhookMessages(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    sent = models.IntegerField()
    errored = models.IntegerField()
    webhook = models.ForeignKey('Webhooks', models.DO_NOTHING)
    uuid = models.CharField(max_length=64)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'webhook_messages'


class Webhooks(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    user_group = models.ForeignKey(UserGroups, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    secret = models.CharField(max_length=32)
    active = models.IntegerField()
    trigger = models.PositiveSmallIntegerField()
    response = models.PositiveSmallIntegerField()
    delivery = models.PositiveSmallIntegerField()
    url = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'webhooks'
