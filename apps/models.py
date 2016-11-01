from __future__ import unicode_literals

from django.db import models


class AccountAccount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    internal_type = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    deprecated = models.NullBooleanField()
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=64)
    write_date = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_user_type")
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountAccountTag(models.Model):
    account_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_account_account")
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_account_account_tag")

    class Meta:
        managed = False
        db_table = 'account_account_account_tag'
        unique_together = (('account_account', 'account_account_tag'),)


class AccountAccountFinancialReport(models.Model):
    report_line = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_report_line")
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account")

    class Meta:
        managed = False
        db_table = 'account_account_financial_report'
        unique_together = (('report_line', 'account'),)


class AccountAccountFinancialReportType(models.Model):
    report = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING,
                               related_name="%(app_label)s_%(class)s_report")
    account_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_account_type")

    class Meta:
        managed = False
        db_table = 'account_account_financial_report_type'
        unique_together = (('report', 'account_type'),)


class AccountAccountTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    applicability = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_tag'


class AccountAccountTagAccountTaxTemplateRel(models.Model):
    account_tax_template = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_account_tax_template")
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_account_account_tag")

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_tax_template_rel'
        unique_together = (('account_tax_template', 'account_account_tag'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account")
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_chart_template", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    nocreate = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_user_type")
    reconcile = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateAccountTag(models.Model):
    account_account_template = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                 related_name="%(app_label)s_%(class)s_account_account_template")
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_account_account_tag")

    class Meta:
        managed = False
        db_table = 'account_account_template_account_tag'
        unique_together = (('account_account_template', 'account_account_tag'),)


class AccountAccountTemplateTaxRel(models.Model):
    account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_account")
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    include_initial_balance = models.NullBooleanField()
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_account_type'


class AccountAccountTypeRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account")

    class Meta:
        managed = False
        db_table = 'account_account_type_rel'
        unique_together = (('journal', 'account'),)


class AccountAgedTrialBalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    period_length = models.IntegerField()
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance'


class AccountAgedTrialBalanceAccountJournalRel(models.Model):
    account_aged_trial_balance = models.ForeignKey('AccountAgedTrialBalance', models.DO_NOTHING,
                                                   related_name="%(app_label)s_%(class)s_account_aged_trial_balance")
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_account_journal")

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance_account_journal_rel'
        unique_together = (('account_aged_trial_balance', 'account_journal'),)


class AccountAnalyticAccount(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(max_length=255)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    use_tasks = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticAccountTagRel(models.Model):
    account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_account")
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tag")

    class Meta:
        managed = False
        db_table = 'account_analytic_account_tag_rel'
        unique_together = (('account', 'tag'),)


class AccountAnalyticChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_chart'


class AccountAnalyticLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_account")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    date = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet",
                                blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=8, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    general_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_general_account", blank=True, null=True)
    move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move",
                             blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    so_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_so_line",
                                db_column='so_line', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAnalyticLineTagRel(models.Model):
    line = models.ForeignKey('AccountAnalyticLine', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_line")
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tag")

    class Meta:
        managed = False
        db_table = 'account_analytic_line_tag_rel'
        unique_together = (('line', 'tag'),)


class AccountAnalyticTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag'


class AccountBalanceReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_account = models.CharField(max_length=255)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_balance_report'


class AccountBalanceReportJournalRel(models.Model):
    account = models.ForeignKey('AccountBalanceReport', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_account")
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")

    class Meta:
        managed = False
        db_table = 'account_balance_report_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountBankAccountsWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('WizardMultiChartsAccounts', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_bank_account")
    acc_name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_accounts_wizard'


class AccountBankStatement(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    state = models.CharField(max_length=255)
    cashbox_start = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_cashbox_start", blank=True, null=True)
    cashbox_end = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_cashbox_end", blank=True, null=True)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pos_session = models.ForeignKey('PosSession', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_pos_session",
                                    blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementCashbox(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_cashbox'


class AccountBankStatementClosebalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_closebalance'


class AccountBankStatementImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    data_file = models.BinaryField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_import'


class AccountBankStatementImportJournalCreation(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_import_journal_creation'


class AccountBankStatementLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey('AccountBankStatement', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_statement")
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal",
                                blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_bank_account", blank=True, null=True)
    date = models.DateField()
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account",
                                blank=True, null=True)
    unique_import_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pos_statement = models.ForeignKey('PosOrder', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_pos_statement", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashboxLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    cashbox = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_cashbox", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    coin_value = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'account_cashbox_line'


class AccountChartTemplate(models.Model):
    bank_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    visible = models.NullBooleanField()
    property_account_receivable = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                    related_name="%(app_label)s_%(class)s_property_account_receivable",
                                                    blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                         related_name="%(app_label)s_%(class)s_property_stock_valuation_acount",
                                                         blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    complete_tax_set = models.NullBooleanField()
    property_stock_account_output_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                            related_name="%(app_label)s_%(class)s_property_stock_account_output_categ",
                                                            blank=True, null=True)
    transfer_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_transfer_account")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                          related_name="%(app_label)s_%(class)s_expense_currency_exchange_account",
                                                          blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    property_account_income_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                      related_name="%(app_label)s_%(class)s_property_account_income_categ",
                                                      blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                           related_name="%(app_label)s_%(class)s_property_stock_account_input_categ",
                                                           blank=True, null=True)
    property_account_income = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_property_account_income",
                                                blank=True, null=True)
    property_account_expense_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                       related_name="%(app_label)s_%(class)s_property_account_expense_categ",
                                                       blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_anglo_saxon = models.NullBooleanField()
    code_digits = models.IntegerField()
    name = models.CharField(max_length=255)
    property_account_expense = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                 related_name="%(app_label)s_%(class)s_property_account_expense",
                                                 blank=True, null=True)
    property_account_payable = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                 related_name="%(app_label)s_%(class)s_property_account_payable",
                                                 blank=True, null=True)
    income_currency_exchange_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                         related_name="%(app_label)s_%(class)s_income_currency_exchange_account",
                                                         blank=True, null=True)
    spoken_languages = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountCommonAccountReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_account = models.CharField(max_length=255)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_common_account_report'


class AccountCommonAccountReportAccountJournalRel(models.Model):
    account_common_account_report = models.ForeignKey('AccountCommonAccountReport', models.DO_NOTHING,
                                                      related_name="%(app_label)s_%(class)s_account_common_account_report")
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_account_journal")

    class Meta:
        managed = False
        db_table = 'account_common_account_report_account_journal_rel'
        unique_together = (('account_common_account_report', 'account_journal'),)


class AccountCommonPartnerReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report'


class AccountCommonPartnerReportAccountJournalRel(models.Model):
    account_common_partner_report = models.ForeignKey('AccountCommonPartnerReport', models.DO_NOTHING,
                                                      related_name="%(app_label)s_%(class)s_account_common_partner_report")
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_account_journal")

    class Meta:
        managed = False
        db_table = 'account_common_partner_report_account_journal_rel'
        unique_together = (('account_common_partner_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.ForeignKey('AccountCommonReport', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_account_common_report")
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_account_journal")

    class Meta:
        managed = False
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountConfigSettings(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    module_account_asset = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    module_account_accountant = models.NullBooleanField()
    module_account_plaid = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    complete_tax_set = models.NullBooleanField()
    template_transfer_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                                  related_name="%(app_label)s_%(class)s_template_transfer_account",
                                                  blank=True, null=True)
    module_account_bank_statement_import_qif = models.NullBooleanField()
    module_account_budget = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    group_multi_currency = models.NullBooleanField()
    group_proforma_invoices = models.NullBooleanField()
    has_chart_of_accounts = models.NullBooleanField()
    has_default_company = models.NullBooleanField()
    purchase_tax_rate = models.FloatField(blank=True, null=True)
    module_account_bank_statement_import_ofx = models.NullBooleanField()
    default_purchase_tax = models.ForeignKey('AccountTax', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_default_purchase_tax", blank=True,
                                             null=True)
    group_analytic_accounting = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    sale_tax_rate = models.FloatField(blank=True, null=True)
    module_account_batch_deposit = models.NullBooleanField()
    module_account_yodlee = models.NullBooleanField()
    module_account_tax_cash_basis = models.NullBooleanField()
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_chart_template", blank=True, null=True)
    default_sale_tax = models.ForeignKey('AccountTax', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_default_sale_tax", blank=True, null=True)
    sale_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_sale_tax", blank=True, null=True)
    module_account_sepa = models.NullBooleanField()
    module_account_reports = models.NullBooleanField()
    module_l10n_us_check_printing = models.NullBooleanField()
    module_account_reports_followup = models.NullBooleanField()
    purchase_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_purchase_tax", blank=True, null=True)
    module_payment_paypal = models.NullBooleanField()
    module_payment_buckaroo = models.NullBooleanField()
    module_payment_adyen = models.NullBooleanField()
    module_payment_ogone = models.NullBooleanField()
    module_payment_transfer = models.NullBooleanField()
    group_analytic_account_for_sales = models.NullBooleanField()
    default_acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_default_acquirer",
                                         db_column='default_acquirer', blank=True, null=True)
    group_analytic_account_for_purchases = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_config_settings'


class AccountFinancialReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    style_overwrite = models.IntegerField(blank=True, null=True)
    sign = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_report = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account_report",
                                       blank=True, null=True)
    display_detail = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_report'


class AccountFiscalPosition(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_country_group", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    zip_to = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country",
                                blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    auto_apply = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    zip_from = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    vat_required = models.NullBooleanField()
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_position")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    account_dest = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_account_dest")
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_account_src")

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_position")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    account_dest = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_account_dest")
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_account_src")

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionPosConfigRel(models.Model):
    pos_config = models.ForeignKey('PosConfig', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_pos_config")
    account_fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_position")

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_pos_config_rel'
        unique_together = (('pos_config', 'account_fiscal_position'),)


class AccountFiscalPositionResCountryStateRel(models.Model):
    account_fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_position")
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_res_country_state")

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_country_state_rel'
        unique_together = (('account_fiscal_position', 'res_country_state'),)


class AccountFiscalPositionTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_position")
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax_src")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax_dest",
                                 blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_position")
    tax_src = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax_src")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    tax_dest = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_tax_dest", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_chart_template")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFullReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_full_reconcile'


class AccountInvoice(models.Model):
    comment = models.TextField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    reference_type = models.CharField(max_length=255)
    number = models.CharField(max_length=255, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    amount_total_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_partner_bank", blank=True, null=True)
    residual_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_fiscal_position", blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    sent = models.NullBooleanField()
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account")
    reconciled = models.NullBooleanField()
    origin = models.CharField(max_length=255, blank=True, null=True)
    residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    move_name = models.CharField(max_length=255, blank=True, null=True)
    date_invoice = models.DateField(blank=True, null=True)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_payment_term", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move", blank=True,
                             null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_commercial_partner", blank=True,
                                           null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    incoterms = models.ForeignKey('StockIncoterms', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_incoterms",
                                  blank=True, null=True)
    purchase = models.ForeignKey('PurchaseOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_purchase",
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice'
        unique_together = (('number', 'company', 'journal', 'type'),)


class AccountInvoiceAccountMoveLineRel(models.Model):
    account_invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_account_invoice")
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_account_move_line")

    class Meta:
        managed = False
        db_table = 'account_invoice_account_move_line_rel'
        unique_together = (('account_invoice', 'account_move_line'),)


class AccountInvoiceCancel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_cancel'


class AccountInvoiceConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_confirm'


class AccountInvoiceLine(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uom", blank=True,
                            null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    account_analytic = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_account_analytic", blank=True, null=True)
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account")
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_subtotal_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.TextField()
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_invoice",
                                blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_purchase_line", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_line'


class AccountInvoiceLineTax(models.Model):
    invoice_line = models.ForeignKey('AccountInvoiceLine', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_invoice_line")
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'account_invoice_line_tax'
        unique_together = (('invoice_line', 'tax'),)


class AccountInvoicePaymentRel(models.Model):
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_payment")
    invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_invoice")

    class Meta:
        managed = False
        db_table = 'account_invoice_payment_rel'
        unique_together = (('payment', 'invoice'),)


class AccountInvoiceRefund(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    filter_refund = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    date_invoice = models.DateField()
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_refund'


class AccountInvoiceTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account")
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_invoice",
                                blank=True, null=True)
    manual = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_analytic = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_account_analytic", blank=True, null=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax", blank=True,
                            null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_tax'


class AccountJournal(models.Model):
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    at_least_one_inbound = models.NullBooleanField()
    bank_statements_source = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    group_invoice_lines = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_bank_account", blank=True, null=True)
    profit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_profit_account", blank=True, null=True)
    display_on_footer = models.NullBooleanField()
    type = models.CharField(max_length=255)
    default_debit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_default_debit_account", blank=True,
                                              null=True)
    show_on_dashboard = models.NullBooleanField()
    default_credit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_default_credit_account",
                                               blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    refund_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_refund_sequence", blank=True, null=True)
    loss_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_loss_account", blank=True, null=True)
    update_posted = models.NullBooleanField()
    name = models.CharField(max_length=255)
    at_least_one_outbound = models.NullBooleanField()
    amount_authorized_diff = models.FloatField(blank=True, null=True)
    journal_user = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('code', 'name', 'company'),)


class AccountJournalAccountingReportRel(models.Model):
    accounting_report = models.ForeignKey('AccountingReport', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_accounting_report")
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_journal")

    class Meta:
        managed = False
        db_table = 'account_journal_accounting_report_rel'
        unique_together = (('accounting_report', 'account_journal'),)


class AccountJournalInboundPaymentMethodRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    inbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_inbound_payment_method",
                                               db_column='inbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_inbound_payment_method_rel'
        unique_together = (('journal', 'inbound_payment_method'),)


class AccountJournalOutboundPaymentMethodRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    outbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_outbound_payment_method",
                                                db_column='outbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_outbound_payment_method_rel'
        unique_together = (('journal', 'outbound_payment_method'),)


class AccountJournalTypeRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_type")

    class Meta:
        managed = False
        db_table = 'account_journal_type_rel'
        unique_together = (('journal', 'type'),)


class AccountMove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    statement_line = models.ForeignKey('AccountBankStatementLine', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_statement_line", blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    state = models.CharField(max_length=255)
    rate_diff_partial_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_rate_diff_partial_rec", blank=True,
                                              null=True)
    matched_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_move'


class AccountMoveLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey('AccountBankStatement', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_statement", blank=True, null=True)
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    date_maturity = models.DateField()
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_user_type", blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    blocked = models.NullBooleanField()
    analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_analytic_account", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    debit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reconciled = models.NullBooleanField()
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move")
    name = models.CharField(max_length=255)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_payment",
                                blank=True, null=True)
    company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_compane_currency", blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_invoice",
                                blank=True, null=True)
    tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax_line",
                                 blank=True, null=True)
    credit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uom",
                                    blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_reconcile = models.ForeignKey('AccountFullReconcile', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_full_reconcile", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineAccountTaxRel(models.Model):
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_account_move_line")
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'account_move_line_account_tax_rel'
        unique_together = (('account_move_line', 'account_tax'),)


class AccountMoveLineReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trans_nbr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile'


class AccountMoveLineReconcileWriteoff(models.Model):
    comment = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff_acc = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_writeoff_acc")
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    analytic = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_analytic", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_p = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile_writeoff'


class AccountMoveReversal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'account_move_reversal'


class AccountOperationTemplate(models.Model):
    second_analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_second_analytic_account",
                                                blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField()
    second_amount_type = models.CharField(max_length=255)
    second_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_second_journal", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_analytic_account", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    second_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_second_tax",
                                   blank=True, null=True)
    has_second_line = models.NullBooleanField()
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal",
                                blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    second_label = models.CharField(max_length=255, blank=True, null=True)
    second_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_second_account", blank=True, null=True)
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account",
                                blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_date = models.DateTimeField(blank=True, null=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax", blank=True,
                            null=True)
    amount_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    second_amount = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'account_operation_template'


class AccountPartialReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    credit_move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_credit_move")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_debit_move")
    write_date = models.DateTimeField(blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    full_reconcile = models.ForeignKey('AccountFullReconcile', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_full_reconcile", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partial_reconcile'


class AccountPayment(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    communication = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_payment_method")
    payment_date = models.DateField()
    payment_difference_handling = models.CharField(max_length=255, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    state = models.CharField(max_length=255, blank=True, null=True)
    writeoff_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_writeoff_account", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    partner_type = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    destination_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_destination_journal", blank=True,
                                            null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    payment_type = models.CharField(max_length=255)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment'


class AccountPaymentMethod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    payment_type = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method'


class AccountPaymentTerm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    payment = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_payment")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    option = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    days = models.IntegerField()
    value = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountRegisterPayments(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateField()
    communication = models.CharField(max_length=255, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    partner_type = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    payment_type = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_payment_method")

    class Meta:
        managed = False
        db_table = 'account_register_payments'


class AccountReportGeneralLedger(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    initial_balance = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    display_account = models.CharField(max_length=255)
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    sortby = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger'


class AccountReportGeneralLedgerJournalRel(models.Model):
    account = models.ForeignKey('AccountReportGeneralLedger', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_account")
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountTax(models.Model):
    amount_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField()
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_tax_group")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    type_tax_use = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    analytic = models.NullBooleanField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    include_base_amount = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    price_include = models.NullBooleanField()
    active = models.NullBooleanField()
    refund_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_refund_account", blank=True, null=True)
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company', 'type_tax_use'),)


class AccountTaxAccountTag(models.Model):
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_account_account_tag")

    class Meta:
        managed = False
        db_table = 'account_tax_account_tag'
        unique_together = (('account_tax', 'account_account_tag'),)


class AccountTaxFiliationRel(models.Model):
    parent_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent_tax",
                                   db_column='parent_tax')
    child_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_child_tax",
                                  db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_group'


class AccountTaxPosOrderLineRel(models.Model):
    pos_order_line = models.ForeignKey('PosOrderLine', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_pos_order_line")
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'account_tax_pos_order_line_rel'
        unique_together = (('pos_order_line', 'account_tax'),)


class AccountTaxPurchaseOrderLineRel(models.Model):
    purchase_order_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_purchase_order_line")
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'account_tax_purchase_order_line_rel'
        unique_together = (('purchase_order_line', 'account_tax'),)


class AccountTaxSaleAdvancePaymentInvRel(models.Model):
    sale_advance_payment_inv = models.ForeignKey('SaleAdvancePaymentInv', models.DO_NOTHING,
                                                 related_name="%(app_label)s_%(class)s_sale_advance_payment_inv")
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'account_tax_sale_advance_payment_inv_rel'
        unique_together = (('sale_advance_payment_inv', 'account_tax'),)


class AccountTaxSaleOrderLineRel(models.Model):
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_sale_order_line")
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_account_tax")

    class Meta:
        managed = False
        db_table = 'account_tax_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_tax'),)


class AccountTaxTemplate(models.Model):
    amount_type = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField()
    price_include = models.NullBooleanField()
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_chart_template")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    type_tax_use = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    analytic = models.NullBooleanField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    include_base_amount = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    refund_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_refund_account", blank=True, null=True)
    account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_account", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_template'
        unique_together = (('name', 'company', 'type_tax_use'),)


class AccountTaxTemplateFiliationRel(models.Model):
    parent_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_parent_tax", db_column='parent_tax')
    child_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_child_tax", db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_template_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class AccountingReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    filter_cmp = models.CharField(max_length=255)
    date_from = models.DateField(blank=True, null=True)
    enable_filter = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    date_to_cmp = models.DateField(blank=True, null=True)
    date_from_cmp = models.DateField(blank=True, null=True)
    label_filter = models.CharField(max_length=255, blank=True, null=True)
    debit_credit = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    account_report = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_account_report")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'accounting_report'


class BadgeUnlockedDefinitionRel(models.Model):
    gamification_badge = models.ForeignKey('GamificationBadge', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_gamification_badge")
    gamification_goal_definition = models.ForeignKey('GamificationGoalDefinition', models.DO_NOTHING,
                                                     related_name="%(app_label)s_%(class)s_gamification_goal_definition")

    class Meta:
        managed = False
        db_table = 'badge_unlocked_definition_rel'
        unique_together = (('gamification_badge', 'gamification_goal_definition'),)


class BarcodeNomenclature(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=32)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    upc_ean_conv = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'barcode_nomenclature'


class BarcodeRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=32)
    sequence = models.IntegerField(blank=True, null=True)
    pattern = models.CharField(max_length=32)
    encoding = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    alias = models.CharField(max_length=32)
    write_date = models.DateTimeField(blank=True, null=True)
    barcode_nomenclature = models.ForeignKey('BarcodeNomenclature', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_barcode_nomenclature", blank=True,
                                             null=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'barcode_rule'


class BaseActionRule(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    filter_pre = models.ForeignKey('IrFilters', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_filter_pre",
                                   blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    trg_date_range_type = models.CharField(max_length=255, blank=True, null=True)
    trg_date_range = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    filter_pre_domain = models.CharField(max_length=255, blank=True, null=True)
    on_change_fields = models.CharField(max_length=255, blank=True, null=True)
    filter = models.ForeignKey('IrFilters', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_filter",
                               blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model")
    trg_date = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_trg_date",
                                 blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    kind = models.CharField(max_length=255, blank=True, null=True)
    filter_domain = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    act_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                                 null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    trg_date_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_trg_date_calendar", blank=True,
                                          null=True)

    class Meta:
        managed = False
        db_table = 'base_action_rule'


class BaseActionRuleIrActServerRel(models.Model):
    base_action_rule = models.ForeignKey('BaseActionRule', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_base_action_rule")
    ir_act_server = models.ForeignKey('IrActServer', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_ir_act_server")

    class Meta:
        managed = False
        db_table = 'base_action_rule_ir_act_server_rel'
        unique_together = (('base_action_rule', 'ir_act_server'),)


class BaseActionRuleLeadTest(models.Model):
    customer = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    name = models.CharField(max_length=255)
    date_action_last = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_action_rule_lead_test'


class BaseActionRuleLineTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    lead = models.ForeignKey('BaseActionRuleLeadTest', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lead",
                             blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_action_rule_line_test'


class BaseActionRuleResPartnerRel(models.Model):
    base_action_rule = models.ForeignKey('BaseActionRule', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_base_action_rule")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'base_action_rule_res_partner_rel'
        unique_together = (('base_action_rule', 'res_partner'),)


class BaseConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    group_light_multi_company = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    module_google_drive = models.NullBooleanField()
    module_inter_company_rules = models.NullBooleanField()
    module_base_import = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    module_portal = models.NullBooleanField()
    module_google_calendar = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    module_share = models.NullBooleanField()
    module_auth_oauth = models.NullBooleanField()
    company_share_partner = models.NullBooleanField()
    fail_counter = models.IntegerField(blank=True, null=True)
    alias_domain = models.CharField(max_length=255, blank=True, null=True)
    auth_signup_reset_password = models.NullBooleanField()
    auth_signup_uninvited = models.NullBooleanField()
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                                  related_name="%(app_label)s_%(class)s_user", blank=True, null=True)
    company_share_product = models.NullBooleanField()
    group_product_variant = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_config_settings'


class BaseImportImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    res_model = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportTestsModelsChar(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsM2O(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING,
                              related_name="%(app_label)s_%(class)s_value", db_column='value', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING,
                              related_name="%(app_label)s_%(class)s_value", db_column='value')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('BaseImportTestsModelsO2M', models.DO_NOTHING,
                               related_name="%(app_label)s_%(class)s_parent", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    othervalue = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    somevalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    lang = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    format = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    data = models.BinaryField()
    overwrite = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    overwrite = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseLanguageInstallWebsiteRel(models.Model):
    base_language_install = models.ForeignKey('BaseLanguageInstall', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_base_language_install")
    website = models.ForeignKey('Website', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_website")

    class Meta:
        managed = False
        db_table = 'base_language_install_website_rel'
        unique_together = (('base_language_install', 'website'),)


class BaseModuleConfiguration(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_configuration'


class BaseModuleUpdate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BasePartnerMergeAutomaticWizard(models.Model):
    exclude_journal_item = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    current_line = models.ForeignKey('BasePartnerMergeLine', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_current_line", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    group_by_name = models.NullBooleanField()
    group_by_vat = models.NullBooleanField()
    group_by_parent_id = models.NullBooleanField()
    exclude_contact = models.NullBooleanField()
    group_by_is_company = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=255)
    maximum_group = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    number_group = models.IntegerField(blank=True, null=True)
    group_by_email = models.NullBooleanField()
    dst_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                    blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    base_partner_merge_automatic_wizard = models.ForeignKey('BasePartnerMergeAutomaticWizard', models.DO_NOTHING,
                                                            related_name="%(app_label)s_%(class)s_base_partner_merge_automatic_wizard")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        unique_together = (('base_partner_merge_automatic_wizard', 'res_partner'),)


class BasePartnerMergeLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    aggr_ids = models.CharField(max_length=255)
    wizard = models.ForeignKey('BasePartnerMergeAutomaticWizard', models.DO_NOTHING,
                               related_name="%(app_label)s_%(class)s_wizard", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    min_id = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_line'


class BaseSetupTerminology(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'base_setup_terminology'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BlogBlog(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_blog'


class BlogPost(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    website_published = models.NullBooleanField()
    blog = models.ForeignKey('BlogBlog', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_blog")
    visits = models.IntegerField(blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    cover_properties = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_author",
                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_post'


class BlogPostBlogTagRel(models.Model):
    blog_tag = models.ForeignKey('BlogTag', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_blog_tag")
    blog_post = models.ForeignKey('BlogPost', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_blog_post")

    class Meta:
        managed = False
        db_table = 'blog_post_blog_tag_rel'
        unique_together = (('blog_tag', 'blog_post'),)


class BlogTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_tag'


class BoardCreate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    menu_parent = models.ForeignKey('IrUiMenu', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_menu_parent")

    class Meta:
        managed = False
        db_table = 'board_create'


class BusBus(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class BusPresence(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", unique=True)
    last_poll = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    interval = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField()
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.ForeignKey('CalendarEvent', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_calendar_event")
    calendar_alarm = models.ForeignKey('CalendarAlarm', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_calendar_alarm")

    class Meta:
        managed = False
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    cn = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey('CalendarEvent', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event",
                              blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    availability = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_attendee'


class CalendarContacts(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")

    class Meta:
        managed = False
        db_table = 'calendar_contacts'


class CalendarEvent(models.Model):
    allday = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    display_start = models.CharField(max_length=255, blank=True, null=True)
    recurrency = models.NullBooleanField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    month_by = models.CharField(max_length=255, blank=True, null=True)
    rrule = models.CharField(max_length=255, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    tu = models.NullBooleanField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    week_list = models.CharField(max_length=255, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField()
    state = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    th = models.NullBooleanField()
    start_date = models.DateField(blank=True, null=True)
    fr = models.NullBooleanField()
    recurrent_id_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    stop = models.DateTimeField()
    stop_datetime = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    byday = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    end_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    we = models.NullBooleanField()
    mo = models.NullBooleanField()
    interval = models.IntegerField(blank=True, null=True)
    su = models.NullBooleanField()
    recurrent_id = models.IntegerField(blank=True, null=True)
    sa = models.NullBooleanField()
    rrule_type = models.CharField(max_length=255, blank=True, null=True)
    show_as = models.CharField(max_length=255, blank=True, null=True)
    opportunity = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_opportunity",
                                    blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    calendar_event = models.ForeignKey('CalendarEvent', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_calendar_event")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('calendar_event', 'res_partner'),)


class CalendarEventType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event_type'


class CashBoxIn(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_in'


class CashBoxOut(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_out'


class ChangePasswordUser(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user_login = models.CharField(max_length=255, blank=True, null=True)
    new_passwd = models.CharField(max_length=255, blank=True, null=True)
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wizard")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class ChangeProductionQty(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'change_production_qty'


class CrmActivity(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    activity_2 = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_activity_2",
                                   blank=True, null=True)
    activity_3 = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_activity_3",
                                   blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_subtype")
    write_date = models.DateTimeField(blank=True, null=True)
    activity_1 = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_activity_1",
                                   blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_activity'


class CrmLead(models.Model):
    date_closed = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country",
                                blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_action_last = models.DateTimeField(blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_campaign",
                                 blank=True, null=True)
    day_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    day_open = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    contact_name = models.CharField(max_length=64, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    date_action_next = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    date_conversion = models.DateTimeField(blank=True, null=True)
    opt_out = models.NullBooleanField()
    date_open = models.DateTimeField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_title",
                              db_column='title', blank=True, null=True)
    partner_name = models.CharField(max_length=64, blank=True, null=True)
    planned_revenue = models.FloatField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    next_activity = models.ForeignKey('CrmActivity', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_next_activity", blank=True, null=True)
    email_cc = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255)
    function = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    title_action = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_lost_reason", db_column='lost_reason',
                                    blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    date_action = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255)
    stage = models.ForeignKey('CrmStage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_stage", blank=True,
                              null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_medium",
                               blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    last_activity = models.ForeignKey('CrmActivity', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_last_activity", blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_source",
                               blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_state",
                              blank=True, null=True)
    email_from = models.CharField(max_length=128, blank=True, null=True)
    referred = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead'


class CrmLead2OpportunityPartner(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    name = models.CharField(max_length=255)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner'


class CrmLead2OpportunityPartnerMass(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    deduplicate = models.NullBooleanField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    name = models.CharField(max_length=255)
    force_assignation = models.NullBooleanField()
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass'


class CrmLead2OpportunityPartnerMassResUsersRel(models.Model):
    crm_lead2opportunity_partner_mass = models.ForeignKey('CrmLead2OpportunityPartnerMass', models.DO_NOTHING,
                                                          related_name="%(app_label)s_%(class)s_crm_lead2opportunity_partner_mass")
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_res_users")

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass_res_users_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'res_users'),)


class CrmLeadCrmLead2OpportunityPartnerMassRel(models.Model):
    crm_lead2opportunity_partner_mass = models.ForeignKey('CrmLead2OpportunityPartnerMass', models.DO_NOTHING,
                                                          related_name="%(app_label)s_%(class)s_crm_lead2opportunity_partner_mass")
    crm_lead = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_crm_lead")

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_mass_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmLeadCrmLead2OpportunityPartnerRel(models.Model):
    crm_lead2opportunity_partner = models.ForeignKey('CrmLead2OpportunityPartner', models.DO_NOTHING,
                                                     related_name="%(app_label)s_%(class)s_crm_lead2opportunity_partner")
    crm_lead = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_crm_lead")

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_rel'
        unique_together = (('crm_lead2opportunity_partner', 'crm_lead'),)


class CrmLeadLost(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    lead = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lead")
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_lost_reason", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_lost'


class CrmLeadTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_tag'


class CrmLeadTagRel(models.Model):
    lead = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lead")
    tag = models.ForeignKey('CrmLeadTag', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tag")

    class Meta:
        managed = False
        db_table = 'crm_lead_tag_rel'
        unique_together = (('lead', 'tag'),)


class CrmLostReason(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'crm_lost_reason'


class CrmMergeOpportunity(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_merge_opportunity'


class CrmPartnerBinding(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_partner_binding'


class CrmStage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    probability = models.FloatField()
    sequence = models.IntegerField(blank=True, null=True)
    on_change = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    fold = models.NullBooleanField()
    legend_priority = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crm_stage'


class CrmTeam(models.Model):
    code = models.CharField(unique=True, max_length=8, blank=True, null=True)
    working_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=64)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    reply_to = models.CharField(max_length=64, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_alias")
    use_leads = models.NullBooleanField()
    use_opportunities = models.NullBooleanField()
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_calendar", blank=True, null=True)
    use_quotations = models.NullBooleanField()
    invoiced_target = models.IntegerField(blank=True, null=True)
    use_invoices = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'crm_team'


class CrmTeamStageRel(models.Model):
    stage = models.ForeignKey('CrmStage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_stage")
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team")

    class Meta:
        managed = False
        db_table = 'crm_team_stage_rel'
        unique_together = (('stage', 'team'),)


class DecimalPrecision(models.Model):
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DecimalPrecisionTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    float_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    float_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision_test'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


# see error here table name was pg_gti710

class EmailTemplateAttachmentRel(models.Model):
    email_template = models.ForeignKey('MailTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_email_template")
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_attachment")

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmailTemplatePreview(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sub_object",
                                   db_column='sub_object', blank=True, null=True)
    auto_delete = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_mail_server", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    partner_to = models.CharField(max_length=255, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_ref_ir_act_window",
                                          db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_report_template",
                                        db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey('IrValues', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_ref_ir_value",
                                     db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.NullBooleanField()
    null_value = models.CharField(max_length=255, blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model", blank=True,
                              null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_sub_model_object_field",
                                               db_column='sub_model_object_field', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    copyvalue = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_model_object_field",
                                           db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=255, blank=True, null=True)
    use_default_to = models.NullBooleanField()
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_preview'


class EmailTemplatePreviewResPartnerRel(models.Model):
    email_template_preview = models.ForeignKey('EmailTemplatePreview', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_email_template_preview")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'email_template_preview_res_partner_rel'
        unique_together = (('email_template_preview', 'res_partner'),)


class EventConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    auto_confirmation = models.IntegerField(blank=True, null=True)
    group_email_scheduling = models.IntegerField(blank=True, null=True)
    module_website_event_questions = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_event_sale = models.IntegerField(blank=True, null=True)
    module_website_event_track = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_config_settings'


class EventConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_confirm'


class EventEvent(models.Model):
    badge_innerleft = models.TextField(blank=True, null=True)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_address",
                                blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    date_begin = models.DateTimeField()
    seats_availability = models.CharField(max_length=255)
    seats_reserved = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country",
                                blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    state = models.CharField(max_length=255)
    event_logo = models.TextField(blank=True, null=True)
    badge_back = models.TextField(blank=True, null=True)
    date_tz = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event_type = models.ForeignKey('EventType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event_type",
                                   blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    seats_max = models.IntegerField(blank=True, null=True)
    badge_front = models.TextField(blank=True, null=True)
    seats_used = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    seats_available = models.IntegerField(blank=True, null=True)
    seats_min = models.IntegerField(blank=True, null=True)
    badge_innerright = models.TextField(blank=True, null=True)
    seats_unconfirmed = models.IntegerField(blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    organizer = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_organizer",
                                  blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    website_published = models.NullBooleanField()
    show_menu = models.NullBooleanField()
    menu = models.ForeignKey('WebsiteMenu', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_menu", blank=True,
                             null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    twitter_hashtag = models.CharField(max_length=255, blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_event'


class EventEventTicket(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    name = models.CharField(max_length=255)
    seats_availability = models.CharField(max_length=255)
    seats_reserved = models.IntegerField(blank=True, null=True)
    event = models.ForeignKey('EventEvent', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event")
    seats_available = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    seats_used = models.IntegerField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    seats_unconfirmed = models.IntegerField(blank=True, null=True)
    seats_max = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")

    class Meta:
        managed = False
        db_table = 'event_event_ticket'


class EventMail(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    event = models.ForeignKey('EventEvent', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event")
    interval_type = models.CharField(max_length=255)
    interval_nbr = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    interval_unit = models.CharField(max_length=255)
    done = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    mail_sent = models.NullBooleanField()
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_template")

    class Meta:
        managed = False
        db_table = 'event_mail'


class EventMailRegistration(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    registration = models.ForeignKey('EventRegistration', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_registration")
    create_date = models.DateTimeField(blank=True, null=True)
    scheduler = models.ForeignKey('EventMail', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_scheduler")
    scheduled_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mail_sent = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'event_mail_registration'


class EventRegistration(models.Model):
    date_closed = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    event = models.ForeignKey('EventEvent', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event")
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_sale_order_line", blank=True, null=True)
    event_ticket = models.ForeignKey('EventEventTicket', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_event_ticket", blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sale_order",
                                   blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_registration'


class EventType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    default_reply_to = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    default_registration_max = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    default_registration_min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_type'


class FetchmailConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_config_settings'


class FetchmailServer(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    port = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=255, blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_object", blank=True,
                               null=True)
    priority = models.IntegerField(blank=True, null=True)
    attach = models.NullBooleanField()
    state = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    action = models.ForeignKey('IrActServer', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_action",
                               blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    is_ssl = models.NullBooleanField()
    server = models.CharField(max_length=255, blank=True, null=True)
    original = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class ForumForum(models.Model):
    karma_close_all = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    karma_moderate = models.IntegerField(blank=True, null=True)
    karma_comment_unlink_all = models.IntegerField(blank=True, null=True)
    karma_edit_all = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    karma_edit_own = models.IntegerField(blank=True, null=True)
    karma_answer = models.IntegerField(blank=True, null=True)
    relevancy_post_vote = models.FloatField(blank=True, null=True)
    karma_gen_answer_flagged = models.IntegerField(blank=True, null=True)
    relevancy_time_decay = models.FloatField(blank=True, null=True)
    karma_downvote = models.IntegerField(blank=True, null=True)
    karma_comment_all = models.IntegerField(blank=True, null=True)
    allow_link = models.NullBooleanField()
    karma_ask = models.IntegerField(blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    karma_gen_question_upvote = models.IntegerField(blank=True, null=True)
    karma_comment_convert_all = models.IntegerField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    karma_gen_answer_downvote = models.IntegerField(blank=True, null=True)
    karma_user_bio = models.IntegerField(blank=True, null=True)
    karma_unlink_all = models.IntegerField(blank=True, null=True)
    karma_flag = models.IntegerField(blank=True, null=True)
    karma_unlink_own = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    faq = models.TextField(blank=True, null=True)
    karma_gen_answer_accept = models.IntegerField(blank=True, null=True)
    karma_retag = models.IntegerField(blank=True, null=True)
    karma_gen_question_downvote = models.IntegerField(blank=True, null=True)
    allow_question = models.NullBooleanField()
    allow_share = models.NullBooleanField()
    website_meta_description = models.TextField(blank=True, null=True)
    karma_answer_accept_all = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    karma_comment_unlink_own = models.IntegerField(blank=True, null=True)
    karma_close_own = models.IntegerField(blank=True, null=True)
    karma_comment_own = models.IntegerField(blank=True, null=True)
    karma_gen_answer_accepted = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    karma_upvote = models.IntegerField(blank=True, null=True)
    default_order = models.CharField(max_length=255)
    karma_editor = models.IntegerField(blank=True, null=True)
    allow_discussion = models.NullBooleanField()
    karma_post = models.IntegerField(blank=True, null=True)
    karma_gen_answer_upvote = models.IntegerField(blank=True, null=True)
    default_post_type = models.CharField(max_length=255)
    karma_comment_convert_own = models.IntegerField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    karma_answer_accept_own = models.IntegerField(blank=True, null=True)
    allow_bump = models.NullBooleanField()
    karma_dofollow = models.IntegerField(blank=True, null=True)
    karma_gen_question_new = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_forum'


class ForumPost(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    closed_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_closed_uid",
                                   db_column='closed_uid', blank=True, null=True)
    plain_content = models.TextField(blank=True, null=True)
    is_correct = models.NullBooleanField()
    post_type = models.CharField(max_length=255)
    moderator = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_moderator",
                                  blank=True, null=True)
    self_reply = models.NullBooleanField()
    vote_count = models.IntegerField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    relevancy = models.FloatField(blank=True, null=True)
    bump_date = models.DateTimeField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    closed_reason = models.ForeignKey('ForumPostReason', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_closed_reason", blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    child_count = models.IntegerField(blank=True, null=True)
    favourite_count = models.IntegerField(blank=True, null=True)
    has_validated_answer = models.NullBooleanField()
    views = models.IntegerField(blank=True, null=True)
    forum = models.ForeignKey('ForumForum', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_forum")
    content_link = models.CharField(max_length=255, blank=True, null=True)
    flag_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user",
                                  blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_post'


class ForumPostReason(models.Model):
    reason_type = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_post_reason'


class ForumPostResUsersRel(models.Model):
    forum_post = models.ForeignKey('ForumPost', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_forum_post")
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_res_users")

    class Meta:
        managed = False
        db_table = 'forum_post_res_users_rel'
        unique_together = (('forum_post', 'res_users'),)


class ForumPostVote(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    forum = models.ForeignKey('ForumForum', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_forum", blank=True,
                              null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    post = models.ForeignKey('ForumPost', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_post")
    recipient = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_recipient",
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    vote = models.CharField(max_length=255)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")

    class Meta:
        managed = False
        db_table = 'forum_post_vote'


class ForumTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    forum = models.ForeignKey('ForumForum', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_forum")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    posts_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_tag'
        unique_together = (('name', 'forum'),)


class ForumTagRel(models.Model):
    forum = models.ForeignKey('ForumPost', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_forum")
    forum_tag = models.ForeignKey('ForumTag', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_forum_tag")

    class Meta:
        managed = False
        db_table = 'forum_tag_rel'
        unique_together = (('forum', 'forum_tag'),)


class GamificationBadge(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rule_max_number = models.IntegerField(blank=True, null=True)
    rule_max = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    name = models.CharField(max_length=255)
    rule_auth = models.CharField(max_length=255)
    level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_badge'


class GamificationBadgeRuleBadgeRel(models.Model):
    badge1 = models.ForeignKey('GamificationBadge', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_badge1")
    badge2 = models.ForeignKey('GamificationBadge', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_badge2")

    class Meta:
        managed = False
        db_table = 'gamification_badge_rule_badge_rel'
        unique_together = (('badge1', 'badge2'),)


class GamificationBadgeUser(models.Model):
    comment = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    challenge = models.ForeignKey('GamificationChallenge', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_challenge", blank=True, null=True)
    sender = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sender", blank=True,
                               null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    badge = models.ForeignKey('GamificationBadge', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_badge")
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_badge_user'


class GamificationBadgeUserWizard(models.Model):
    comment = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    badge = models.ForeignKey('GamificationBadge', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_badge")
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)

    class Meta:
        managed = False
        db_table = 'gamification_badge_user_wizard'


class GamificationChallenge(models.Model):
    reward_failure = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    reward_realtime = models.NullBooleanField()
    next_report_date = models.DateField(blank=True, null=True)
    reward_second = models.ForeignKey('GamificationBadge', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_reward_second", blank=True, null=True)
    period = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    last_report_date = models.DateField(blank=True, null=True)
    report_template = models.ForeignKey('MailTemplate', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_report_template")
    remind_update_delay = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255)
    report_message_frequency = models.CharField(max_length=255)
    message_last_post = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255)
    manager = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_manager",
                                blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    reward = models.ForeignKey('GamificationBadge', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_reward",
                               blank=True, null=True)
    reward_third = models.ForeignKey('GamificationBadge', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_reward_third", blank=True, null=True)
    user_domain = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    reward_first = models.ForeignKey('GamificationBadge', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_reward_first", blank=True, null=True)
    visibility_mode = models.CharField(max_length=255)
    report_message_group = models.ForeignKey('MailChannel', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_report_message_group", blank=True,
                                             null=True)

    class Meta:
        managed = False
        db_table = 'gamification_challenge'


class GamificationChallengeLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    challenge = models.ForeignKey('GamificationChallenge', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_challenge")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    definition = models.ForeignKey('GamificationGoalDefinition', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_definition")
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    target_goal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'gamification_challenge_line'


class GamificationChallengeUsersRel(models.Model):
    gamification_challenge = models.ForeignKey('GamificationChallenge', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_gamification_challenge")
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_res_users")

    class Meta:
        managed = False
        db_table = 'gamification_challenge_users_rel'
        unique_together = (('gamification_challenge', 'res_users'),)


class GamificationGoal(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    target_goal = models.FloatField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    remind_update_delay = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    last_update = models.DateField(blank=True, null=True)
    current = models.FloatField()
    state = models.CharField(max_length=255)
    closed = models.NullBooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    challenge = models.ForeignKey('GamificationChallenge', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_challenge", blank=True, null=True)
    to_update = models.NullBooleanField()
    line = models.ForeignKey('GamificationChallengeLine', models.DO_NOTHING,
                             related_name="%(app_label)s_%(class)s_line", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    definition = models.ForeignKey('GamificationGoalDefinition', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_definition")

    class Meta:
        managed = False
        db_table = 'gamification_goal'


class GamificationGoalDefinition(models.Model):
    domain = models.CharField(max_length=255)
    res_id_field = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    compute_code = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    computation_mode = models.CharField(max_length=255)
    display_mode = models.CharField(max_length=255)
    action = models.ForeignKey('IrActWindow', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_action",
                               blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model", blank=True,
                              null=True)
    description = models.TextField(blank=True, null=True)
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_field",
                              blank=True, null=True)
    monetary = models.NullBooleanField()
    batch_user_expression = models.CharField(max_length=255, blank=True, null=True)
    batch_mode = models.NullBooleanField()
    batch_distinctive_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_batch_distinctive_field",
                                                db_column='batch_distinctive_field', blank=True, null=True)
    condition = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    field_date = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_field_date", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_goal_definition'


class GamificationGoalWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    goal = models.ForeignKey('GamificationGoal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_goal")
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_goal_wizard'


class GamificationInvitedUserIdsRel(models.Model):
    gamification_challenge = models.ForeignKey('GamificationChallenge', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_gamification_challenge")
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_res_users")

    class Meta:
        managed = False
        db_table = 'gamification_invited_user_ids_rel'
        unique_together = (('gamification_challenge', 'res_users'),)


class ImLivechatChannel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    default_message = models.CharField(max_length=255, blank=True, null=True)
    input_placeholder = models.CharField(max_length=255, blank=True, null=True)
    button_text = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_livechat_channel'


class ImLivechatChannelCountryRel(models.Model):
    channel = models.ForeignKey('ImLivechatChannelRule', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_channel")
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country")

    class Meta:
        managed = False
        db_table = 'im_livechat_channel_country_rel'
        unique_together = (('channel', 'country'),)


class ImLivechatChannelImUser(models.Model):
    channel = models.ForeignKey('ImLivechatChannel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_channel")
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")

    class Meta:
        managed = False
        db_table = 'im_livechat_channel_im_user'
        unique_together = (('channel', 'user'),)


class ImLivechatChannelRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    channel = models.ForeignKey('ImLivechatChannel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_channel",
                                blank=True, null=True)
    regex_url = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255)
    auto_popup_timer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_livechat_channel_rule'


class IrActClient(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    res_model = models.CharField(max_length=255, blank=True, null=True)
    params_store = models.BinaryField(blank=True, null=True)
    tag = models.CharField(max_length=255)
    context = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    parser = models.CharField(max_length=255, blank=True, null=True)
    header = models.NullBooleanField()
    report_type = models.CharField(max_length=255)
    ir_values = models.ForeignKey('IrValues', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_ir_values",
                                  blank=True, null=True)
    attachment = models.CharField(max_length=255, blank=True, null=True)
    report_sxw_content_data = models.BinaryField(blank=True, null=True)
    report_xml = models.CharField(max_length=255, blank=True, null=True)
    report_rml_content_data = models.BinaryField(blank=True, null=True)
    auto = models.NullBooleanField()
    report_file = models.CharField(max_length=255, blank=True, null=True)
    multi = models.NullBooleanField()
    report_xsl = models.CharField(max_length=255, blank=True, null=True)
    report_rml = models.CharField(max_length=255, blank=True, null=True)
    report_name = models.CharField(max_length=255)
    attachment_use = models.NullBooleanField()
    model = models.CharField(max_length=255)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_paperformat", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    code = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_crud_model",
                                   blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)
    ref_object = models.CharField(max_length=128, blank=True, null=True)
    id_object = models.CharField(max_length=128, blank=True, null=True)
    crud_model_name = models.CharField(max_length=255, blank=True, null=True)
    use_relational_model = models.CharField(max_length=255)
    use_create = models.CharField(max_length=255)
    wkf_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wkf_field",
                                  blank=True, null=True)
    wkf_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wkf_model",
                                  blank=True, null=True)
    state = models.CharField(max_length=255)
    id_value = models.CharField(max_length=255, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model")
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_sub_model_object_field",
                                               db_column='sub_model_object_field', blank=True, null=True)
    link_new_record = models.NullBooleanField()
    wkf_transition = models.ForeignKey('WkfTransition', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_wkf_transition", blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sub_object",
                                   db_column='sub_object', blank=True, null=True)
    use_write = models.CharField(max_length=255)
    wkf_model_name = models.CharField(max_length=255, blank=True, null=True)
    copyvalue = models.CharField(max_length=255, blank=True, null=True)
    write_expression = models.CharField(max_length=255, blank=True, null=True)
    menu_ir_values = models.ForeignKey('IrValues', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_menu_ir_values", blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_model_object_field",
                                           db_column='model_object_field', blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_link_field", blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_template",
                                 blank=True, null=True)
    website_published = models.NullBooleanField()
    website_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActUrl(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True, null=True)
    res_model = models.CharField(max_length=255)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_search_view",
                                    blank=True, null=True)
    view_type = models.CharField(max_length=255)
    src_model = models.CharField(max_length=255, blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_view", blank=True,
                             null=True)
    auto_refresh = models.IntegerField(blank=True, null=True)
    view_mode = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True, null=True)
    multi = models.NullBooleanField()
    auto_search = models.NullBooleanField()
    res_id = models.IntegerField(blank=True, null=True)
    filter = models.NullBooleanField()
    limit = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.ForeignKey('IrActWindow', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_act")
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_gid", db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    multi = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_view", blank=True,
                             null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    view_mode = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_act_window",
                                   blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255)
    action_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    res_model = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    res_name = models.CharField(max_length=255, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255)
    public = models.NullBooleanField()
    store_fname = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    res_field = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=1024, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=40, blank=True, null=True)
    datas_fname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrAutovacuum(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_autovacuum'


class IrConfigParameter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value = models.TextField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    key = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrConfigParameterGroupsRel(models.Model):
    icp = models.ForeignKey('IrConfigParameter', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_icp")
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group")

    class Meta:
        managed = False
        db_table = 'ir_config_parameter_groups_rel'
        unique_together = (('icp', 'group'),)


class IrCron(models.Model):
    function = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    name = models.CharField(max_length=255)
    interval_type = models.CharField(max_length=255, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    nextcall = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    doall = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrExports(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    resource = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    export = models.ForeignKey('IrExports', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_export",
                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    sort = models.TextField()
    model_id = models.CharField(max_length=255)
    domain = models.TextField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    is_default = models.NullBooleanField()
    context = models.TextField()
    active = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_filters'


class IrLogging(models.Model):
    create_uid = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, blank=True, null=True)
    line = models.CharField(max_length=255)
    dbname = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    func = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_logging'


class IrMailServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    smtp_encryption = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    smtp_port = models.IntegerField()
    smtp_host = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    smtp_pass = models.CharField(max_length=64, blank=True, null=True)
    smtp_debug = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    smtp_user = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    model = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    transient = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model")
    perm_read = models.NullBooleanField()
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    perm_unlink = models.NullBooleanField()
    perm_write = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    perm_create = models.NullBooleanField()
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group", blank=True,
                              null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_module",
                               db_column='module')
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model",
                              db_column='model')
    type = models.CharField(max_length=1)
    definition = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    noupdate = models.NullBooleanField()
    name = models.CharField(max_length=255)
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    model = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    field_description = models.CharField(max_length=255)
    help = models.TextField(blank=True, null=True)
    ttype = models.CharField(max_length=255)
    relation = models.CharField(max_length=255, blank=True, null=True)
    relation_field = models.CharField(max_length=255, blank=True, null=True)
    index = models.NullBooleanField()
    copy = models.NullBooleanField()
    related = models.CharField(max_length=255, blank=True, null=True)
    readonly = models.NullBooleanField()
    required = models.NullBooleanField()
    selectable = models.NullBooleanField()
    translate = models.NullBooleanField()
    serialization_field = models.ForeignKey('self', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_serialization_field", blank=True,
                                            null=True)
    relation_table = models.CharField(max_length=255, blank=True, null=True)
    column1 = models.CharField(max_length=255, blank=True, null=True)
    column2 = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    selection = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    on_delete = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    depends = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    compute = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields'


class IrModelFieldsGroupRel(models.Model):
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_field")
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group")

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelRelation(models.Model):
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_module",
                               db_column='module')
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model",
                              db_column='model')
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    visible = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    latest_version = models.CharField(max_length=255, blank=True, null=True)
    shortdesc = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey('IrModuleCategory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_category",
                                 blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.NullBooleanField()
    demo = models.NullBooleanField()
    web = models.NullBooleanField()
    license = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.NullBooleanField()
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    maintainer = models.CharField(max_length=255, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_module",
                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrProperty(models.Model):
    value_text = models.TextField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    type = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    fields = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_fields")
    value_datetime = models.DateTimeField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_reference = models.CharField(max_length=255, blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    res_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_property'


class IrRule(models.Model):
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model")
    domain_force = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    perm_read = models.NullBooleanField()
    perm_unlink = models.NullBooleanField()
    perm_write = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    perm_create = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_rule'


class IrSequence(models.Model):
    padding = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    number_next = models.IntegerField()
    implementation = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    use_date_range = models.NullBooleanField()
    number_increment = models.IntegerField()
    prefix = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    suffix = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence'


class IrSequenceDateRange(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    number_next = models.IntegerField()
    date_from = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sequence")
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField()

    class Meta:
        managed = False
        db_table = 'ir_sequence_date_range'


class IrServerObjectLines(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    server = models.ForeignKey('IrActServer', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_server",
                               blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.TextField()
    col1 = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_col1",
                             db_column='col1')
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ir_server_object_lines'


class IrTranslation(models.Model):
    lang = models.ForeignKey('ResLang', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lang",
                             db_column='lang', blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_translation'


class IrUiMenu(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    web_icon = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.ForeignKey('IrUiMenu', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_menu")
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_gid", db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiView(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    field_parent = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    model_data = models.ForeignKey('IrModelData', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model_data",
                                   blank=True, null=True)
    priority = models.IntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    arch_db = models.TextField(blank=True, null=True)
    inherit = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_inherit", blank=True,
                                null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    active = models.NullBooleanField()
    arch_fs = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    mode = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True, null=True)
    website = models.ForeignKey('Website', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_website",
                                blank=True, null=True)
    customize_show = models.NullBooleanField()
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    page = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    ref = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_ref")
    arch = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.ForeignKey('IrUiView', models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class IrValues(models.Model):
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model", blank=True,
                              null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    key2 = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    key = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_values'


class LinkTracker(models.Model):
    count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_medium",
                               blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_campaign",
                                 blank=True, null=True)
    favicon = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_source",
                               blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_mass_mailing_campaign", blank=True,
                                              null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mass_mailing", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_tracker'


class LinkTrackerClick(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country",
                                blank=True, null=True)
    link = models.ForeignKey('LinkTracker', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_link")
    write_date = models.DateTimeField(blank=True, null=True)
    click_date = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    mail_stat = models.ForeignKey('MailMailStatistics', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_mail_stat", blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_mass_mailing_campaign", blank=True,
                                              null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mass_mailing", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_tracker_click'


class LinkTrackerCode(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    link = models.ForeignKey('LinkTracker', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_link")

    class Meta:
        managed = False
        db_table = 'link_tracker_code'


class MailAlias(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    alias_defaults = models.TextField()
    alias_contact = models.CharField(max_length=255)
    alias_parent_model = models.ForeignKey('IrModel', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_alias_parent_model", blank=True,
                                           null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    alias_force_thread_id = models.IntegerField(blank=True, null=True)
    alias_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_alias_model")
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    alias_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user",
                                   blank=True, null=True)
    alias_name = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailChannel(models.Model):
    create_date = models.DateTimeField()
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_alias")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    public = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    group_public = models.ForeignKey('ResGroups', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_group_public", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    channel_type = models.CharField(max_length=255, blank=True, null=True)
    email_send = models.NullBooleanField()
    anonymous_name = models.CharField(max_length=255, blank=True, null=True)
    livechat_channel = models.ForeignKey('ImLivechatChannel', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_livechat_channel", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel'


class MailChannelMailWizardInviteRel(models.Model):
    mail_wizard_invite = models.ForeignKey('MailWizardInvite', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_mail_wizard_invite")
    mail_channel = models.ForeignKey('MailChannel', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_channel")

    class Meta:
        managed = False
        db_table = 'mail_channel_mail_wizard_invite_rel'
        unique_together = (('mail_wizard_invite', 'mail_channel'),)


class MailChannelPartner(models.Model):
    seen_message = models.ForeignKey('MailMessage', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_seen_message", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_minimized = models.NullBooleanField()
    is_pinned = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    channel = models.ForeignKey('MailChannel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_channel",
                                blank=True, null=True)
    fold_state = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_partner'


class MailChannelResGroupRel(models.Model):
    mail_channel = models.ForeignKey('MailChannel', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_channel")
    groups = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_groups")

    class Meta:
        managed = False
        db_table = 'mail_channel_res_group_rel'
        unique_together = (('mail_channel', 'groups'),)


class MailComposeMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    no_auto_thread = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_mail_server", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    notify = models.NullBooleanField()
    active_domain = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    composition_mode = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    is_log = models.NullBooleanField()
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent",
                               blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_subtype",
                                blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    record_name = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    use_active_domain = models.NullBooleanField()
    email_from = models.CharField(max_length=255, blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_author",
                               blank=True, null=True)
    message_type = models.CharField(max_length=255)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_template",
                                 blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_mass_mailing_campaign", blank=True,
                                              null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mass_mailing", blank=True, null=True)
    mass_mailing_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.ForeignKey('MailComposeMessage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wizard")
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_attachment")

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageMailMassMailingListRel(models.Model):
    mail_compose_message = models.ForeignKey('MailComposeMessage', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_mail_compose_message")
    mail_mass_mailing_list = models.ForeignKey('MailMassMailingList', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_mail_mass_mailing_list")

    class Meta:
        managed = False
        db_table = 'mail_compose_message_mail_mass_mailing_list_rel'
        unique_together = (('mail_compose_message', 'mail_mass_mailing_list'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.ForeignKey('MailComposeMessage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wizard")
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    channel = models.ForeignKey('MailChannel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_channel",
                                blank=True, null=True)
    res_model = models.CharField(max_length=255)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'partner'), ('res_model', 'res_id', 'channel'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.ForeignKey('MailFollowers', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_mail_followers")
    mail_message_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_mail_message_subtype")

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_message")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    notification = models.NullBooleanField()
    auto_delete = models.NullBooleanField()
    body_html = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    email_to = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    fetchmail_server = models.ForeignKey('FetchmailServer', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_fetchmail_server", blank=True, null=True)
    mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_mailing",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.ForeignKey('MailMail', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_mail_mail")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMailStatistics(models.Model):
    replied = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    state_update = models.DateTimeField(blank=True, null=True)
    mail_mail = models.ForeignKey('MailMail', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_mail_mail",
                                  blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_mass_mailing_campaign", blank=True,
                                              null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mass_mailing", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    opened = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    sent = models.DateTimeField(blank=True, null=True)
    scheduled = models.DateTimeField(blank=True, null=True)
    mail_mail_id_int = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    exception = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    bounced = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail_statistics'


class MailMassMailing(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_campaign",
                                 blank=True, null=True)
    mass_mailing_campaign = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_mass_mailing_campaign", blank=True,
                                              null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    contact_ab_pc = models.IntegerField(blank=True, null=True)
    mailing_model = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    mailing_domain = models.CharField(max_length=255, blank=True, null=True)
    keep_archives = models.NullBooleanField()
    sent_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=255)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_medium",
                               blank=True, null=True)
    reply_to_mode = models.CharField(max_length=255)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_source",
                               blank=True, null=True)
    email_from = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing'


class MailMassMailingCampaign(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_campaign")
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    unique_ab_testing = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    stage = models.ForeignKey('MailMassMailingStage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_stage")
    name = models.CharField(max_length=255)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_medium",
                               blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_source",
                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_campaign'


class MailMassMailingContact(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    opt_out = models.NullBooleanField()
    unsubscription_date = models.DateTimeField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    list = models.ForeignKey('MailMassMailingList', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_list")
    message_bounce = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_contact'


class MailMassMailingList(models.Model):
    popup_redirect_url = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    popup_content = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_list'


class MailMassMailingListRel(models.Model):
    mail_mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_mail_mass_mailing")
    mail_mass_mailing_list = models.ForeignKey('MailMassMailingList', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_mail_mass_mailing_list")

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_list_rel'
        unique_together = (('mail_mass_mailing', 'mail_mass_mailing_list'),)


class MailMassMailingStage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_stage'


class MailMassMailingTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_tag'


class MailMassMailingTagRel(models.Model):
    tag = models.ForeignKey('MailMassMailingCampaign', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tag")
    campaign = models.ForeignKey('MailMassMailingTag', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_campaign")

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_tag_rel'
        unique_together = (('tag', 'campaign'),)


class MailMassMailingTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    email_to = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mass_mailing")

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_test'


class MailMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_mail_server", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_subtype",
                                blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    record_name = models.CharField(max_length=255, blank=True, null=True)
    no_auto_thread = models.NullBooleanField()
    date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_author",
                               blank=True, null=True)
    message_type = models.CharField(max_length=255)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    website_published = models.NullBooleanField()
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message'


class MailMessageMailChannelRel(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_message")
    mail_channel = models.ForeignKey('MailChannel', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_channel")

    class Meta:
        managed = False
        db_table = 'mail_message_mail_channel_rel'
        unique_together = (('mail_message', 'mail_channel'),)


class MailMessageResPartnerNeedactionRel(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_message")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_needaction_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerRel(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_message")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerStarredRel(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_message")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_starred_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSubtype(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    default = models.NullBooleanField()
    res_model = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    internal = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    relation_field = models.CharField(max_length=255, blank=True, null=True)
    hidden = models.NullBooleanField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'


class MailShortcode(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    source = models.CharField(max_length=255)
    shortcode_type = models.CharField(max_length=255)
    substitution = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_shortcode'


class MailTemplate(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    auto_delete = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_mail_server", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    partner_to = models.CharField(max_length=255, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_ref_ir_act_window",
                                          db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_report_template",
                                        db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey('IrValues', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_ref_ir_value",
                                     db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.NullBooleanField()
    null_value = models.CharField(max_length=255, blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_model", blank=True,
                              null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                               related_name="%(app_label)s_%(class)s_sub_model_object_field",
                                               db_column='sub_model_object_field', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=255, blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sub_object",
                                   db_column='sub_object', blank=True, null=True)
    copyvalue = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_model_object_field",
                                           db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=255, blank=True, null=True)
    use_default_to = models.NullBooleanField()
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template'


class MailTrackingValue(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    field_type = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    old_value_datetime = models.DateTimeField(blank=True, null=True)
    old_value_monetary = models.FloatField(blank=True, null=True)
    new_value_monetary = models.FloatField(blank=True, null=True)
    field_desc = models.CharField(max_length=255)
    old_value_char = models.CharField(max_length=255, blank=True, null=True)
    old_value_float = models.FloatField(blank=True, null=True)
    new_value_text = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    new_value_float = models.FloatField(blank=True, null=True)
    field = models.CharField(max_length=255)
    old_value_text = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    new_value_char = models.CharField(max_length=255, blank=True, null=True)
    new_value_datetime = models.DateTimeField(blank=True, null=True)
    old_value_integer = models.IntegerField(blank=True, null=True)
    new_value_integer = models.IntegerField(blank=True, null=True)
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mail_message")

    class Meta:
        managed = False
        db_table = 'mail_tracking_value'


class MailWizardInvite(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    res_model = models.CharField(max_length=255)
    send_mail = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.ForeignKey('MailWizardInvite', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_mail_wizard_invite")
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner")

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MakeProcurement(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    date_planned = models.DateField()
    res_model = models.CharField(max_length=255, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl")
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uom")
    write_date = models.DateTimeField(blank=True, null=True)
    qty = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'make_procurement'


class MakeProcurementStockLocationRouteRel(models.Model):
    make_procurement = models.ForeignKey('MakeProcurement', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_make_procurement")
    stock_location_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_stock_location_route")

    class Meta:
        managed = False
        db_table = 'make_procurement_stock_location_route_rel'
        unique_together = (('make_procurement', 'stock_location_route'),)


class MarketingConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    module_marketing_campaign = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_config_settings'


class MassMailingConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    group_website_popup_on_exit = models.IntegerField(blank=True, null=True)
    module_mass_mailing_themes = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    group_mass_mailing_campaign = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mass_mailing_config_settings'


class MassMailingIrAttachmentsRel(models.Model):
    mass_mailing = models.ForeignKey('MailMassMailing', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mass_mailing")
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_attachment")

    class Meta:
        managed = False
        db_table = 'mass_mailing_ir_attachments_rel'
        unique_together = (('mass_mailing', 'attachment'),)


class MeetingCategoryRel(models.Model):
    event = models.ForeignKey('CalendarEvent', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event")
    type = models.ForeignKey('CalendarEventType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_type")

    class Meta:
        managed = False
        db_table = 'meeting_category_rel'
        unique_together = (('event', 'type'),)


class MergeOpportunityRel(models.Model):
    merge = models.ForeignKey('CrmMergeOpportunity', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_merge")
    opportunity = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_opportunity")

    class Meta:
        managed = False
        db_table = 'merge_opportunity_rel'
        unique_together = (('merge', 'opportunity'),)


class MessageAttachmentRel(models.Model):
    message = models.ForeignKey('MailMessage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_message")
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_attachment")

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class MrpBom(models.Model):
    date_stop = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=16, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    sequence = models.IntegerField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl")
    routing = models.ForeignKey('MrpRouting', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_routing",
                                blank=True, null=True)
    type = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    product_efficiency = models.FloatField()
    product_rounding = models.FloatField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_bom'


class MrpBomLine(models.Model):
    product_rounding = models.FloatField(blank=True, null=True)
    date_stop = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    sequence = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    bom = models.ForeignKey('MrpBom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_bom")
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    routing = models.ForeignKey('MrpRouting', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_routing",
                                blank=True, null=True)
    product_efficiency = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mrp_bom_line'


class MrpBomLineMrpPropertyRel(models.Model):
    mrp_bom_line = models.ForeignKey('MrpBomLine', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mrp_bom_line")
    mrp_property = models.ForeignKey('MrpProperty', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mrp_property")

    class Meta:
        managed = False
        db_table = 'mrp_bom_line_mrp_property_rel'
        unique_together = (('mrp_bom_line', 'mrp_property'),)


class MrpBomLineProductAttributeValueRel(models.Model):
    mrp_bom_line = models.ForeignKey('MrpBomLine', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mrp_bom_line")
    product_attribute_value = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_product_attribute_value")

    class Meta:
        managed = False
        db_table = 'mrp_bom_line_product_attribute_value_rel'
        unique_together = (('mrp_bom_line', 'product_attribute_value'),)


class MrpBomMrpPropertyRel(models.Model):
    mrp_bom = models.ForeignKey('MrpBom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_mrp_bom")
    mrp_property = models.ForeignKey('MrpProperty', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_mrp_property")

    class Meta:
        managed = False
        db_table = 'mrp_bom_mrp_property_rel'
        unique_together = (('mrp_bom', 'mrp_property'),)


class MrpConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    group_product_variant = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    module_mrp_byproduct = models.IntegerField(blank=True, null=True)
    group_rounding_efficiency = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_mrp_operations = models.IntegerField(blank=True, null=True)
    group_mrp_routings = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_config_settings'


class MrpProductProduce(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    mode = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_product_produce'


class MrpProductProduceLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    produce = models.ForeignKey('MrpProductProduce', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_produce",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_product_produce_line'


class MrpProduction(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    priority = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    location_src = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_location_src")
    cycle_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    state = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    bom = models.ForeignKey('MrpBom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_bom", blank=True,
                            null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    date_planned = models.DateTimeField()
    move_prod = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move_prod",
                                  blank=True, null=True)
    routing = models.ForeignKey('MrpRouting', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_routing",
                                blank=True, null=True)
    ready_production = models.NullBooleanField()
    hour_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_dest")

    class Meta:
        managed = False
        db_table = 'mrp_production'
        unique_together = (('name', 'company'),)


class MrpProductionProductLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    production = models.ForeignKey('MrpProduction', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_production", blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")

    class Meta:
        managed = False
        db_table = 'mrp_production_product_line'


class MrpProductionWorkcenterLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    hour = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    production = models.ForeignKey('MrpProduction', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_production")
    sequence = models.IntegerField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    workcenter = models.ForeignKey('MrpWorkcenter', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_workcenter")
    cycle = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_production_workcenter_line'


class MrpProperty(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    group = models.ForeignKey('MrpPropertyGroup', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group")
    composition = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_property'


class MrpPropertyGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mrp_property_group'


class MrpRepair(models.Model):
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_address",
                                blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    internal_notes = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)
    quotation_notes = models.TextField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    invoiced = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pricelist", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_invoice = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_partner_invoice", blank=True, null=True)
    move = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move", blank=True,
                             null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    guarantee_limit = models.DateField(blank=True, null=True)
    invoice_method = models.CharField(max_length=255)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_dest")
    invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_invoice",
                                blank=True, null=True)
    repaired = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mrp_repair'


class MrpRepairCancel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_repair_cancel'


class MrpRepairFee(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    repair = models.ForeignKey('MrpRepair', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_repair")
    invoice_line = models.ForeignKey('AccountInvoiceLine', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_invoice_line", blank=True, null=True)
    price_unit = models.FloatField()
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    to_invoice = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    invoiced = models.NullBooleanField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mrp_repair_fee'


class MrpRepairLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    invoiced = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    state = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    invoice_line = models.ForeignKey('AccountInvoiceLine', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_invoice_line", blank=True, null=True)
    repair = models.ForeignKey('MrpRepair', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_repair",
                               blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    move = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move", blank=True,
                             null=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    to_invoice = models.NullBooleanField()
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_dest")

    class Meta:
        managed = False
        db_table = 'mrp_repair_line'


class MrpRepairMakeInvoice(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    group = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_repair_make_invoice'


class MrpRouting(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location",
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_routing'


class MrpRoutingWorkcenter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    cycle_nbr = models.FloatField()
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    workcenter = models.ForeignKey('MrpWorkcenter', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_workcenter")
    routing = models.ForeignKey('MrpRouting', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_routing",
                                blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    hour_nbr = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mrp_routing_workcenter'


class MrpWorkcenter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    capacity_per_cycle = models.FloatField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    time_stop = models.FloatField(blank=True, null=True)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_resource")
    costs_hour = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    costs_general_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_costs_general_account", blank=True,
                                              null=True)
    costs_hour_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_costs_hour_account", blank=True,
                                           null=True)
    costs_cycle_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_costs_cycle_account", blank=True,
                                            null=True)
    costs_cycle = models.FloatField(blank=True, null=True)
    time_start = models.FloatField(blank=True, null=True)
    time_cycle = models.FloatField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter'


class NoteNote(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    date_done = models.DateField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    open = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'note_note'


class NoteStage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    fold = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_stage'


class NoteStageRel(models.Model):
    note = models.ForeignKey('NoteNote', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_note")
    stage = models.ForeignKey('NoteStage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_stage")

    class Meta:
        managed = False
        db_table = 'note_stage_rel'
        unique_together = (('note', 'stage'),)


class NoteTag(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_tag'


class NoteTagsRel(models.Model):
    note = models.ForeignKey('NoteNote', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_note")
    tag = models.ForeignKey('NoteTag', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tag")

    class Meta:
        managed = False
        db_table = 'note_tags_rel'
        unique_together = (('note', 'tag'),)


class PaymentAcquirer(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fees_active = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    cancel_msg = models.TextField(blank=True, null=True)
    registration_view_template = models.ForeignKey('IrUiView', models.DO_NOTHING,
                                                   related_name="%(app_label)s_%(class)s_registration_view_template",
                                                   blank=True, null=True)
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    environment = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255)
    website_published = models.NullBooleanField()
    auto_confirm = models.CharField(max_length=255)
    pending_msg = models.TextField(blank=True, null=True)
    post_msg = models.TextField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    done_msg = models.TextField(blank=True, null=True)
    pre_msg = models.TextField(blank=True, null=True)
    error_msg = models.TextField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    view_template = models.ForeignKey('IrUiView', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_view_template")

    class Meta:
        managed = False
        db_table = 'payment_acquirer'


class PaymentMethod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    acquirer_ref = models.CharField(max_length=255)
    acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_acquirer")
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")

    class Meta:
        managed = False
        db_table = 'payment_method'


class PaymentTransaction(models.Model):
    state_message = models.TextField(blank=True, null=True)
    callback_eval = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_acquirer")
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_payment_method", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    partner_phone = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_partner_country")
    acquirer_reference = models.CharField(max_length=255, blank=True, null=True)
    partner_address = models.CharField(max_length=255, blank=True, null=True)
    partner_email = models.CharField(max_length=255, blank=True, null=True)
    partner_lang = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_zip = models.CharField(max_length=255, blank=True, null=True)
    html_3ds = models.CharField(max_length=255, blank=True, null=True)
    date_validate = models.DateTimeField(blank=True, null=True)
    partner_city = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sale_order",
                                   blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PortalWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    portal = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_portal")

    class Meta:
        managed = False
        db_table = 'portal_wizard'


class PortalWizardUser(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    wizard = models.ForeignKey('PortalWizard', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wizard")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=240, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    in_portal = models.NullBooleanField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'


class PosCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_category'


class PosConfig(models.Model):
    iface_big_scrollbars = models.NullBooleanField()
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal",
                                blank=True, null=True)
    iface_electronic_scale = models.NullBooleanField()
    proxy_ip = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    iface_vkeyboard = models.NullBooleanField()
    iface_print_auto = models.NullBooleanField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    cash_control = models.NullBooleanField()
    barcode_nomenclature = models.ForeignKey('BarcodeNomenclature', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_barcode_nomenclature")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    iface_scan_via_proxy = models.NullBooleanField()
    state = models.CharField(max_length=255)
    group_by = models.NullBooleanField()
    iface_invoicing = models.NullBooleanField()
    iface_display_categ_images = models.NullBooleanField()
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pricelist")
    group_pos_user = models.ForeignKey('ResGroups', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_group_pos_user", blank=True, null=True)
    iface_start_categ = models.ForeignKey('PosCategory', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_iface_start_categ", blank=True,
                                          null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    iface_print_skip_screen = models.NullBooleanField()
    stock_location = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_stock_location")
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sequence",
                                 blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tip_product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                    blank=True, null=True)
    iface_tax_included = models.NullBooleanField()
    iface_payment_terminal = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    iface_precompute_cash = models.NullBooleanField()
    iface_cashdrawer = models.NullBooleanField()
    name = models.CharField(max_length=255)
    iface_fullscreen = models.NullBooleanField()
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_picking_type", blank=True, null=True)
    receipt_footer = models.TextField(blank=True, null=True)
    receipt_header = models.TextField(blank=True, null=True)
    group_pos_manager = models.ForeignKey('ResGroups', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_group_pos_manager", blank=True,
                                          null=True)
    iface_print_via_proxy = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'pos_config'


class PosConfigJournalRel(models.Model):
    pos_config = models.ForeignKey('PosConfig', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_pos_config")
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")

    class Meta:
        managed = False
        db_table = 'pos_config_journal_rel'
        unique_together = (('pos_config', 'journal'),)


class PosConfigSettings(models.Model):
    module_pos_reprint = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    module_pos_discount = models.IntegerField(blank=True, null=True)
    module_pos_restaurant = models.IntegerField(blank=True, null=True)
    module_pos_mercury = models.IntegerField(blank=True, null=True)
    module_pos_loyalty = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_config_settings'


class PosConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_confirm'


class PosDetails(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date_end = models.DateField()
    date_start = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_details'


class PosDetailsReportUserRel(models.Model):
    user = models.ForeignKey('PosDetails', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    wizard = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wizard")

    class Meta:
        managed = False
        db_table = 'pos_details_report_user_rel'
        unique_together = (('user', 'wizard'),)


class PosDiscount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_discount'


class PosMakePayment(models.Model):
    payment_date = models.DateField()
    payment_name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_journal")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_make_payment'


class PosOpenStatement(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_open_statement'


class PosOrder(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sale_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_sale_journal", db_column='sale_journal',
                                     blank=True, null=True)
    pos_reference = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    account_move = models.ForeignKey('AccountMove', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_account_move", db_column='account_move',
                                     blank=True, null=True)
    date_order = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location",
                                 blank=True, null=True)
    nb_print = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pricelist")
    write_date = models.DateTimeField(blank=True, null=True)
    fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_fiscal_position", blank=True, null=True)
    name = models.CharField(max_length=255)
    invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_invoice",
                                blank=True, null=True)
    session = models.ForeignKey('PosSession', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_session")
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_picking",
                                blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_order'


class PosOrderLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    notice = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    order = models.ForeignKey('PosOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_order", blank=True,
                              null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_order_line'


class PosSession(models.Model):
    config = models.ForeignKey('PosConfig', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_config")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    cash_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_journal", blank=True, null=True)
    cash_register = models.ForeignKey('AccountBankStatement', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_cash_register", blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")
    login_number = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=255)
    start_at = models.DateTimeField(blank=True, null=True)
    rescue = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    stop_at = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_session'


class ProcurementGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    move_type = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_group'


class ProcurementOrder(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    date_planned = models.DateTimeField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    priority = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    rule = models.ForeignKey('ProcurementRule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_rule",
                             blank=True, null=True)
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group",
                              blank=True, null=True)
    name = models.TextField()
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location",
                                 blank=True, null=True)
    partner_dest = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_partner_dest", blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_orderpoint", blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse",
                                  blank=True, null=True)
    move_dest = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move_dest",
                                  blank=True, null=True)
    bom = models.ForeignKey('MrpBom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_bom", blank=True,
                            null=True)
    production = models.ForeignKey('MrpProduction', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_production", blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sale_line",
                                  blank=True, null=True)
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_purchase_line", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_order'


class ProcurementOrderComputeAll(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_order_compute_all'


class ProcurementOrderpointCompute(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_orderpoint_compute'


class ProcurementPropertyRel(models.Model):
    procurement = models.ForeignKey('ProcurementOrder', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_procurement")
    property = models.ForeignKey('MrpProperty', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_property")

    class Meta:
        managed = False
        db_table = 'procurement_property_rel'
        unique_together = (('procurement', 'property'),)


class ProcurementRule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    action = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group",
                              blank=True, null=True)
    group_propagation_option = models.CharField(max_length=255, blank=True, null=True)
    partner_address = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_partner_address", blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location",
                                 blank=True, null=True)
    location_src = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_location_src", blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_picking_type", blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse",
                                  blank=True, null=True)
    propagate = models.NullBooleanField()
    procure_method = models.CharField(max_length=255)
    route_sequence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route",
                              blank=True, null=True)
    propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_propagate_warehouse", blank=True,
                                            null=True)

    class Meta:
        managed = False
        db_table = 'procurement_rule'


class ProductAccessoryRel(models.Model):
    src = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_src")
    dest = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_dest")

    class Meta:
        managed = False
        db_table = 'product_accessory_rel'
        unique_together = (('src', 'dest'),)


class ProductAlternativeRel(models.Model):
    src = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_src")
    dest = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_dest")

    class Meta:
        managed = False
        db_table = 'product_alternative_rel'
        unique_together = (('src', 'dest'),)


class ProductAttribute(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute'


class ProductAttributeLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl")
    attribute = models.ForeignKey('ProductAttribute', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_attribute")
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_line'


class ProductAttributeLineProductAttributeValueRel(models.Model):
    line = models.ForeignKey('ProductAttributeLine', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_line")
    val = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_val")

    class Meta:
        managed = False
        db_table = 'product_attribute_line_product_attribute_value_rel'
        unique_together = (('line', 'val'),)


class ProductAttributePrice(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl")
    value = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_value")
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_price'


class ProductAttributeValue(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey('ProductAttribute', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_attribute")
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_value'
        unique_together = (('name', 'attribute'),)


class ProductAttributeValueProductProductRel(models.Model):
    att = models.ForeignKey('ProductAttributeValue', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_att")
    prod = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_prod")

    class Meta:
        managed = False
        db_table = 'product_attribute_value_product_product_rel'
        unique_together = (('att', 'prod'),)


class ProductCategory(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_removal_strategy", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductPackaging(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_packaging'


class ProductPriceHistory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    datetime = models.DateTimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_history'


class ProductPriceListAlone(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price_list = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_price_list", db_column='price_list')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    qty1 = models.IntegerField(blank=True, null=True)
    qty2 = models.IntegerField(blank=True, null=True)
    qty3 = models.IntegerField(blank=True, null=True)
    qty4 = models.IntegerField(blank=True, null=True)
    qty5 = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_list'


class ProductPricelist(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist'


class ProductPricelistItem(models.Model):
    fixed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sequence = models.IntegerField()
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    applied_on = models.CharField(max_length=255)
    min_quantity = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    percent_price = models.FloatField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl", blank=True, null=True)
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pricelist", blank=True, null=True)
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    compute_price = models.CharField(max_length=255, blank=True, null=True)
    base = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    categ = models.ForeignKey('ProductCategory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_categ",
                              blank=True, null=True)
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    base_pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_base_pricelist", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_item'


class ProductProduct(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    default_code = models.CharField(max_length=255, blank=True, null=True)
    name_template = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl")
    barcode = models.CharField(unique=True, max_length=255, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_product'


class ProductPublicCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_public_category'


class ProductPublicCategoryProductTemplateRel(models.Model):
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_product_template")
    product_public_category = models.ForeignKey('ProductPublicCategory', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_product_public_category")

    class Meta:
        managed = False
        db_table = 'product_public_category_product_template_rel'
        unique_together = (('product_template', 'product_public_category'),)


class ProductPutaway(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_putaway'


class ProductRating(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_rating'


class ProductRemoval(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_removal'


class ProductStyle(models.Model):
    html_class = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_style'


class ProductStyleProductTemplateRel(models.Model):
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_product_template")
    product_style = models.ForeignKey('ProductStyle', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_product_style")

    class Meta:
        managed = False
        db_table = 'product_style_product_template_rel'
        unique_together = (('product_template', 'product_style'),)


class ProductSupplierTaxesRel(models.Model):
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_prod")
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'product_supplier_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductSupplierinfo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    delay = models.IntegerField()
    write_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    min_qty = models.FloatField()
    product_code = models.CharField(max_length=255, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl", blank=True, null=True)
    name = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_name",
                             db_column='name')

    class Meta:
        managed = False
        db_table = 'product_supplierinfo'


class ProductTaxesRel(models.Model):
    prod = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_prod")
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'product_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductTemplate(models.Model):
    warranty = models.FloatField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uom")
    description_purchase = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    sale_ok = models.NullBooleanField()
    categ = models.ForeignKey('ProductCategory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_categ")
    product_manager = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_product_manager",
                                        db_column='product_manager', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    uom_po = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uom_po")
    description_sale = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    rental = models.NullBooleanField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description_picking = models.TextField(blank=True, null=True)
    sale_delay = models.FloatField(blank=True, null=True)
    tracking = models.CharField(max_length=255)
    produce_delay = models.FloatField(blank=True, null=True)
    track_service = models.CharField(max_length=255, blank=True, null=True)
    invoice_policy = models.CharField(max_length=255, blank=True, null=True)
    available_in_pos = models.NullBooleanField()
    pos_categ = models.ForeignKey('PosCategory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_pos_categ",
                                  blank=True, null=True)
    to_weight = models.NullBooleanField()
    website_description = models.TextField(blank=True, null=True)
    website_sequence = models.IntegerField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    website_published = models.NullBooleanField()
    website_size_x = models.IntegerField(blank=True, null=True)
    website_size_y = models.IntegerField(blank=True, null=True)
    purchase_method = models.CharField(max_length=255, blank=True, null=True)
    purchase_ok = models.NullBooleanField()
    event_type = models.ForeignKey('EventType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event_type",
                                   blank=True, null=True)
    event_ok = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'product_template'


class ProductUom(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    uom_type = models.CharField(max_length=255)
    category = models.ForeignKey('ProductUomCateg', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_category")

    class Meta:
        managed = False
        db_table = 'product_uom'


class ProductUomCateg(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_uom_categ'


class ProjectConfigSettings(models.Model):
    module_sale_service = models.IntegerField(blank=True, null=True)
    module_pad = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    module_project_timesheet_synchro = models.NullBooleanField()
    module_project_forecast = models.NullBooleanField()
    module_project_issue_sheet = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_rating_project = models.IntegerField(blank=True, null=True)
    generate_project_alias = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    group_time_work_estimation_tasks = models.IntegerField(blank=True, null=True)
    module_project_timesheet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_config_settings'


class ProjectProject(models.Model):
    alias_model = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_alias")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    privacy_visibility = models.CharField(max_length=255)
    label_tasks = models.CharField(max_length=255, blank=True, null=True)
    analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_analytic_account")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    date_start = models.DateField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    active = models.NullBooleanField()
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_resource_calendar", blank=True,
                                          null=True)

    class Meta:
        managed = False
        db_table = 'project_project'


class ProjectTags(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tags'


class ProjectTagsProjectTaskRel(models.Model):
    project_task = models.ForeignKey('ProjectTask', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_project_task")
    project_tags = models.ForeignKey('ProjectTags', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_project_tags")

    class Meta:
        managed = False
        db_table = 'project_tags_project_task_rel'
        unique_together = (('project_task', 'project_tags'),)


class ProjectTask(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    planned_hours = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    displayed_image = models.ForeignKey('IrAttachment', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_displayed_image", blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey('ProjectProject', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_project",
                                blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    kanban_state = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    stage = models.ForeignKey('ProjectTaskType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_stage",
                              blank=True, null=True)
    name = models.CharField(max_length=128)
    date_deadline = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    remaining_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task'


class ProjectTaskHistory(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    end_date = models.DateField(blank=True, null=True)
    task = models.ForeignKey('ProjectTask', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_task")
    type = models.ForeignKey('ProjectTaskType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_type",
                             blank=True, null=True)
    kanban_state = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    planned_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_history'


class ProjectTaskParentRel(models.Model):
    parent = models.ForeignKey('ProjectTask', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent")
    task = models.ForeignKey('ProjectTask', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_task")

    class Meta:
        managed = False
        db_table = 'project_task_parent_rel'
        unique_together = (('parent', 'task'),)


class ProjectTaskType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    legend_done = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    fold = models.NullBooleanField()
    legend_blocked = models.CharField(max_length=255, blank=True, null=True)
    legend_priority = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    legend_normal = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'project_task_type'


class ProjectTaskTypeRel(models.Model):
    type = models.ForeignKey('ProjectTaskType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_type")
    project = models.ForeignKey('ProjectProject', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_project")

    class Meta:
        managed = False
        db_table = 'project_task_type_rel'
        unique_together = (('type', 'project'),)


class PurchaseConfigSettings(models.Model):
    group_uom = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    module_stock_dropshipping = models.IntegerField(blank=True, null=True)
    group_costing_method = models.IntegerField(blank=True, null=True)
    group_advance_purchase_requisition = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    group_manage_vendor_price = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    group_product_variant = models.IntegerField(blank=True, null=True)
    module_purchase_requisition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_config_settings'


class PurchaseOrder(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    date_order = models.DateTimeField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")
    dest_address = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_dest_address", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_picking_type")
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_fiscal_position", blank=True, null=True)
    incoterm = models.ForeignKey('StockIncoterms', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_incoterm",
                                 blank=True, null=True)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_payment_term", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_ref = models.CharField(max_length=255, blank=True, null=True)
    date_approve = models.DateField(blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group",
                              blank=True, null=True)
    invoice_status = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'


class PurchaseOrderLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    qty_received = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    price_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    account_analytic = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_account_analytic", blank=True, null=True)
    order = models.ForeignKey('PurchaseOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_order")
    qty_invoiced = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    date_planned = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchase_order_line'


class RatingRating(models.Model):
    rating = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    res_model = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    res_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.ForeignKey('MailMessage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_message",
                                blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    rated_partner = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_rated_partner", blank=True, null=True)
    res_id = models.IntegerField()
    website_published = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'rating_rating'


class RegistrationEditor(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sale_order")
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration_editor'


class RegistrationEditorLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    registration = models.ForeignKey('EventRegistration', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_registration", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey('EventEvent', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_sale_order_line", blank=True, null=True)
    editor = models.ForeignKey('RegistrationEditor', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_editor",
                               blank=True, null=True)
    event_ticket = models.ForeignKey('EventEventTicket', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_event_ticket", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration_editor_line'


class RelBadgeAuthUsers(models.Model):
    gamification_badge = models.ForeignKey('GamificationBadge', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_gamification_badge")
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_res_users")

    class Meta:
        managed = False
        db_table = 'rel_badge_auth_users'
        unique_together = (('gamification_badge', 'res_users'),)


class RelModulesLangexport(models.Model):
    wiz = models.ForeignKey('BaseLanguageExport', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wiz")
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_module")

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.ForeignKey('IrActServer', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_server")
    action = models.ForeignKey('IrActServer', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_action")

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class RepairFeeLineTax(models.Model):
    repair_fee_line = models.ForeignKey('MrpRepairFee', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_repair_fee_line")
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'repair_fee_line_tax'
        unique_together = (('repair_fee_line', 'tax'),)


class RepairOperationLineTax(models.Model):
    repair_operation_line = models.ForeignKey('MrpRepairLine', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_repair_operation_line")
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tax")

    class Meta:
        managed = False
        db_table = 'repair_operation_line_tax'
        unique_together = (('repair_operation_line', 'tax'),)


class Report(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'


class ReportPaperformat(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    page_width = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    format = models.CharField(max_length=255, blank=True, null=True)
    default = models.NullBooleanField()
    header_line = models.NullBooleanField()
    header_spacing = models.IntegerField(blank=True, null=True)
    dpi = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    margin_right = models.FloatField(blank=True, null=True)
    margin_top = models.FloatField(blank=True, null=True)
    margin_left = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    margin_bottom = models.FloatField(blank=True, null=True)
    page_height = models.IntegerField(blank=True, null=True)
    orientation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_paperformat'


class ResBank(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    zip = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country",
                                db_column='country', blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    bic = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_state",
                              db_column='state', blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=255)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    rml_footer = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    rml_header = models.TextField()
    rml_paper_format = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    font = models.ForeignKey('ResFont', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_font",
                             db_column='font', blank=True, null=True)
    account_no = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    custom_footer = models.NullBooleanField()
    phone = models.CharField(max_length=64, blank=True, null=True)
    rml_header2 = models.TextField()
    rml_header3 = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    rml_header1 = models.CharField(max_length=255, blank=True, null=True)
    company_registry = models.CharField(max_length=64, blank=True, null=True)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_paperformat", blank=True, null=True)
    project_time_mode = models.ForeignKey('ProductUom', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_project_time_mode", blank=True,
                                          null=True)
    internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                                  related_name="%(app_label)s_%(class)s_internal_transit_location",
                                                  blank=True, null=True)
    propagation_minimum_delta = models.IntegerField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    anglo_saxon_accounting = models.NullBooleanField()
    fiscalyear_last_day = models.IntegerField()
    property_stock_account_input_categ = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                                           related_name="%(app_label)s_%(class)s_property_stock_account_input_categ",
                                                           blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                                         related_name="%(app_label)s_%(class)s_property_stock_valuation_account",
                                                         blank=True, null=True)
    expects_chart_of_accounts = models.NullBooleanField()
    transfer_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_transfer_account", blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                                            related_name="%(app_label)s_%(class)s_property_stock_account_output_categ",
                                                            blank=True, null=True)
    currency_exchange_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING,
                                                  related_name="%(app_label)s_%(class)s_journal", blank=True, null=True)
    period_lock_date = models.DateField(blank=True, null=True)
    paypal_account = models.CharField(max_length=128, blank=True, null=True)
    accounts_code_digits = models.IntegerField(blank=True, null=True)
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_chart_template", blank=True, null=True)
    overdue_msg = models.TextField(blank=True, null=True)
    fiscalyear_last_month = models.IntegerField()
    tax_calculation_rounding_method = models.CharField(max_length=255, blank=True, null=True)
    manufacturing_lead = models.FloatField()
    vat_check_vies = models.NullBooleanField()
    sale_note = models.TextField(blank=True, null=True)
    security_lead = models.FloatField()
    po_lead = models.FloatField()
    po_double_validation_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    po_double_validation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyUsersRel(models.Model):
    cid = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_cid",
                            db_column='cid')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user")

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_group'


class ResCountryGroupWebsitePricelistRel(models.Model):
    website_pricelist = models.ForeignKey('WebsitePricelist', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_website_pricelist")
    res_country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_res_country_group")

    class Meta:
        managed = False
        db_table = 'res_country_group_website_pricelist_rel'
        unique_together = (('website_pricelist', 'res_country_group'),)


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_res_country")
    res_country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_res_country_group")

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=3)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_state'


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    symbol = models.CharField(max_length=4, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    position = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency'


class ResCurrencyRate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.DateTimeField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency_rate'


class ResFont(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    mode = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'res_font'
        unique_together = (('family', 'name'),)


class ResGroups(models.Model):
    comment = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    share = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('IrModuleCategory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_category",
                                 blank=True, null=True)
    is_portal = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsActionRel(models.Model):
    uid = models.ForeignKey('IrActionsTodo', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uid",
                            db_column='uid')
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_gid", db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_action_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_gid", db_column='gid')
    hid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_hid", db_column='hid')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.ForeignKey('IrActReportXml', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uid",
                            db_column='uid')
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_gid", db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsUsersRel(models.Model):
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_gid", db_column='gid')
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uid", db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResLang(models.Model):
    name = models.CharField(unique=True, max_length=255)
    code = models.CharField(unique=True, max_length=16)
    date_format = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    thousands_sep = models.CharField(max_length=255, blank=True, null=True)
    translatable = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    time_format = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    decimal_point = models.CharField(max_length=255)
    active = models.NullBooleanField()
    iso_code = models.CharField(max_length=16, blank=True, null=True)
    grouping = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'res_lang'


class ResPartner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    function = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    company_type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=24, blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_title",
                              db_column='title', blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_country",
                                blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    supplier = models.NullBooleanField()
    ref = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_company = models.NullBooleanField()
    website = models.CharField(max_length=255, blank=True, null=True)
    customer = models.NullBooleanField()
    fax = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    employee = models.NullBooleanField()
    credit_limit = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    tz = models.CharField(max_length=64, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    use_parent_address = models.NullBooleanField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    birthdate = models.CharField(max_length=255, blank=True, null=True)
    vat = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_state",
                              blank=True, null=True)
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_commercial_partner", blank=True,
                                           null=True)
    notify_email = models.CharField(max_length=255)
    message_last_post = models.DateTimeField(blank=True, null=True)
    opt_out = models.NullBooleanField()
    signup_type = models.CharField(max_length=255, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    signup_token = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_website_so = models.ForeignKey('SaleOrder', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_last_website_so", blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    website_published = models.NullBooleanField()
    website_short_description = models.TextField(blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'


class ResPartnerBank(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    bank = models.ForeignKey('ResBank', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_bank", blank=True,
                             null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sanitized_acc_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    acc_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'res_partner_bank'


class ResPartnerCategory(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'res_partner_category'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_category")
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerTitle(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    shortcut = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_title'


class ResRequestLink(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    object = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_request_link'


class ResUsers(models.Model):
    active = models.NullBooleanField()
    login = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    share = models.NullBooleanField()
    write_uid = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    password_crypt = models.CharField(max_length=255, blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_alias")
    chatter_needaction_auto = models.NullBooleanField()
    sale_team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_sale_team",
                                  blank=True, null=True)
    target_sales_done = models.IntegerField(blank=True, null=True)
    target_sales_won = models.IntegerField(blank=True, null=True)
    target_sales_invoiced = models.IntegerField(blank=True, null=True)
    pos_security_pin = models.CharField(max_length=32, blank=True, null=True)
    pos_config = models.ForeignKey('PosConfig', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_pos_config",
                                   db_column='pos_config', blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_log'


class ResUsersWebTipRel(models.Model):
    web_tip = models.ForeignKey('WebTip', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_web_tip")
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_res_users")

    class Meta:
        managed = False
        db_table = 'res_users_web_tip_rel'
        unique_together = (('web_tip', 'res_users'),)


class ResourceCalendar(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    manager = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_manager",
                                db_column='manager', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar'


class ResourceCalendarAttendance(models.Model):
    dayofweek = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    date_from = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    hour_from = models.FloatField()
    hour_to = models.FloatField()
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_calendar")

    class Meta:
        managed = False
        db_table = 'resource_calendar_attendance'


class ResourceCalendarLeaves(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_resource",
                                 blank=True, null=True)
    date_from = models.DateTimeField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField()
    calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_calendar",
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_leaves'


class ResourceResource(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    time_efficiency = models.FloatField()
    code = models.CharField(max_length=16, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_calendar",
                                 blank=True, null=True)
    active = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    resource_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'resource_resource'


class RuleGroupRel(models.Model):
    rule_group = models.ForeignKey('IrRule', models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SaleAdvancePaymentInv(models.Model):
    count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    advance_payment_method = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    deposit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_deposit_account", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv'


class SaleConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    alias_domain = models.CharField(max_length=255, blank=True, null=True)
    group_use_lead = models.IntegerField(blank=True, null=True)
    module_crm_voip = models.NullBooleanField()
    module_website_sign = models.NullBooleanField()
    generate_sales_team_alias = models.NullBooleanField()
    alias_prefix = models.CharField(max_length=255, blank=True, null=True)
    deposit_product_id_setting = models.ForeignKey('ProductProduct', models.DO_NOTHING,
                                                   related_name="%(app_label)s_%(class)s_deposit_product_id_setting",
                                                   db_column='deposit_product_id_setting', blank=True, null=True)
    auto_done_setting = models.IntegerField(blank=True, null=True)
    group_display_incoterm = models.IntegerField(blank=True, null=True)
    group_pricelist_item = models.NullBooleanField()
    group_product_variant = models.IntegerField(blank=True, null=True)
    group_sale_pricelist = models.NullBooleanField()
    default_invoice_policy = models.CharField(max_length=255, blank=True, null=True)
    group_product_pricelist = models.NullBooleanField()
    module_website_portal = models.NullBooleanField()
    module_website_quote = models.IntegerField(blank=True, null=True)
    group_discount_per_so_line = models.IntegerField(blank=True, null=True)
    module_sale_margin = models.IntegerField(blank=True, null=True)
    sale_pricelist_setting = models.CharField(max_length=255)
    module_website_sale_digital = models.NullBooleanField()
    group_uom = models.IntegerField(blank=True, null=True)
    group_sale_delivery_address = models.IntegerField(blank=True, null=True)
    module_sale_contract = models.NullBooleanField()
    module_delivery = models.IntegerField(blank=True, null=True)
    group_mrp_properties = models.IntegerField(blank=True, null=True)
    group_route_so_lines = models.IntegerField(blank=True, null=True)
    default_picking_policy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_config_settings'


class SaleOrder(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_team", blank=True,
                             null=True)
    client_order_ref = models.CharField(max_length=255, blank=True, null=True)
    date_order = models.DateTimeField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    procurement_group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_procurement_group", blank=True,
                                          null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pricelist")
    project = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_project", blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    validity_date = models.DateField(blank=True, null=True)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_payment_term", blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner_invoice = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_partner_invoice")
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_fiscal_position", blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_status = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    partner_shipping = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_partner_shipping")
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_campaign",
                                 blank=True, null=True)
    opportunity = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_opportunity",
                                    blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_medium",
                               blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_source",
                               blank=True, null=True)
    picking_policy = models.CharField(max_length=255)
    incoterm = models.ForeignKey('StockIncoterms', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_incoterm",
                                 db_column='incoterm', blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse")
    payment_tx = models.ForeignKey('PaymentTransaction', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_payment_tx", blank=True, null=True)
    payment_acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_payment_acquirer", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order'


class SaleOrderLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency",
                                 blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    price_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    customer_lead = models.FloatField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    name = models.TextField()
    state = models.CharField(max_length=255, blank=True, null=True)
    order_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                      blank=True, null=True)
    order = models.ForeignKey('SaleOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_order")
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_reduce = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_delivered = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoice_status = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    salesman = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_salesman",
                                 blank=True, null=True)
    product_packaging = models.ForeignKey('ProductPackaging', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_product_packaging",
                                          db_column='product_packaging', blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route",
                              blank=True, null=True)
    event = models.ForeignKey('EventEvent', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_event", blank=True,
                              null=True)
    event_ticket = models.ForeignKey('EventEventTicket', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_event_ticket", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line'


class SaleOrderLineInvoiceRel(models.Model):
    order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_order_line")
    invoice_line = models.ForeignKey('AccountInvoiceLine', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_invoice_line")

    class Meta:
        managed = False
        db_table = 'sale_order_line_invoice_rel'
        unique_together = (('order_line', 'invoice_line'),)


class SaleOrderLinePropertyRel(models.Model):
    order = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_order")
    property = models.ForeignKey('MrpProperty', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_property")

    class Meta:
        managed = False
        db_table = 'sale_order_line_property_rel'
        unique_together = (('order', 'property'),)


class SaleOrderTagRel(models.Model):
    order = models.ForeignKey('SaleOrder', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_order")
    tag = models.ForeignKey('CrmLeadTag', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_tag")

    class Meta:
        managed = False
        db_table = 'sale_order_tag_rel'
        unique_together = (('order', 'tag'),)


class StockBackorderConfirmation(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    pick = models.ForeignKey('StockPicking', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_pick", blank=True,
                             null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation'


class StockChangeProductQty(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_product_tmpl")
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")

    class Meta:
        managed = False
        db_table = 'stock_change_product_qty'


class StockChangeStandardPrice(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    new_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_change_standard_price'


class StockConfigSettings(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    module_stock_calendar = models.IntegerField(blank=True, null=True)
    group_stock_multiple_locations = models.IntegerField(blank=True, null=True)
    module_stock_picking_wave = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    group_stock_tracking_lot = models.IntegerField(blank=True, null=True)
    group_product_variant = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    module_claim_from_delivery = models.IntegerField(blank=True, null=True)
    module_stock_barcode = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    group_stock_production_lot = models.IntegerField(blank=True, null=True)
    group_stock_tracking_owner = models.IntegerField(blank=True, null=True)
    module_delivery_usps = models.NullBooleanField()
    module_stock_dropshipping = models.IntegerField(blank=True, null=True)
    module_procurement_jit = models.IntegerField(blank=True, null=True)
    group_stock_packaging = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_delivery_fedex = models.NullBooleanField()
    decimal_precision = models.IntegerField(blank=True, null=True)
    group_uom = models.IntegerField(blank=True, null=True)
    module_delivery_ups = models.NullBooleanField()
    module_product_expiry = models.IntegerField(blank=True, null=True)
    group_stock_adv_location = models.IntegerField(blank=True, null=True)
    module_delivery_dhl = models.NullBooleanField()
    module_stock_landed_costs = models.IntegerField(blank=True, null=True)
    group_stock_inventory_valuation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_config_settings'


class StockFixedPutawayStrat(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    putaway = models.ForeignKey('ProductPutaway', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_putaway")
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    fixed_location = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_fixed_location")
    write_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_category")

    class Meta:
        managed = False
        db_table = 'stock_fixed_putaway_strat'


class StockImmediateTransfer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    pick = models.ForeignKey('StockPicking', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_pick", blank=True,
                             null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer'


class StockIncoterms(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=3)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_incoterms'


class StockInventory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)
    date = models.DateTimeField()
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_package",
                                blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    filter = models.CharField(max_length=255)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory'


class StockInventoryLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    prodlot_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    prod_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_prod_lot", blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    inventory = models.ForeignKey('StockInventory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_inventory",
                                  blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_package",
                                blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    theoretical_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom")
    product_code = models.CharField(max_length=255, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")

    class Meta:
        managed = False
        db_table = 'stock_inventory_line'


class StockLocation(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    putaway_strategy = models.ForeignKey('ProductPutaway', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_putaway_strategy", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    location = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location", blank=True,
                                 null=True)
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_removal_strategy", blank=True, null=True)
    scrap_location = models.NullBooleanField()
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    usage = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    posz = models.IntegerField(blank=True, null=True)
    posx = models.IntegerField(blank=True, null=True)
    posy = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    name = models.CharField(max_length=255)
    return_location = models.NullBooleanField()
    valuation_in_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_valuation_in_account", blank=True,
                                             null=True)
    valuation_out_account = models.ForeignKey('AccountAccount', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_valuation_out_account", blank=True,
                                              null=True)

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)


class StockLocationPath(models.Model):
    location_from = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_from")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    route_sequence = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_picking_type")
    auto = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse",
                                  blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route",
                              blank=True, null=True)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_dest")
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    propagate = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location_path'


class StockLocationRoute(models.Model):
    supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_supplier_wh", blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    warehouse_selectable = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_supplied_wh", blank=True, null=True)
    product_selectable = models.NullBooleanField()
    product_categ_selectable = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    sale_selectable = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_location_route'


class StockLocationRouteCateg(models.Model):
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route")
    categ = models.ForeignKey('ProductCategory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_categ")

    class Meta:
        managed = False
        db_table = 'stock_location_route_categ'
        unique_together = (('route', 'categ'),)


class StockLocationRouteMove(models.Model):
    move = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move")
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route")

    class Meta:
        managed = False
        db_table = 'stock_location_route_move'
        unique_together = (('move', 'route'),)


class StockLocationRouteProcurement(models.Model):
    procurement = models.ForeignKey('ProcurementOrder', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_procurement")
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route")

    class Meta:
        managed = False
        db_table = 'stock_location_route_procurement'
        unique_together = (('procurement', 'route'),)


class StockMove(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    move_dest = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move_dest",
                                  blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    price_unit = models.FloatField(blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    date = models.DateTimeField()
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    priority = models.CharField(max_length=255, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_picking_type", blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    origin_returned_move = models.ForeignKey('self', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_origin_returned_move", blank=True,
                                             null=True)
    product_packaging = models.ForeignKey('ProductPackaging', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_product_packaging",
                                          db_column='product_packaging', blank=True, null=True)
    date_expected = models.DateTimeField()
    procurement = models.ForeignKey('ProcurementOrder', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_procurement", blank=True, null=True)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse",
                                  blank=True, null=True)
    inventory = models.ForeignKey('StockInventory', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_inventory",
                                  blank=True, null=True)
    partially_available = models.NullBooleanField()
    propagate = models.NullBooleanField()
    restrict_partner = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_restrict_partner", blank=True, null=True)
    procure_method = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    restrict_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_restrict_lot", blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group",
                              blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    split_from = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_split_from",
                                   db_column='split_from', blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_picking",
                                blank=True, null=True)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_dest")
    write_date = models.DateTimeField(blank=True, null=True)
    push_rule = models.ForeignKey('StockLocationPath', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_push_rule", blank=True, null=True)
    rule = models.ForeignKey('ProcurementRule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_rule",
                             blank=True, null=True)
    consumed_for = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_consumed_for",
                                     db_column='consumed_for', blank=True, null=True)
    raw_material_production = models.ForeignKey('MrpProduction', models.DO_NOTHING,
                                                related_name="%(app_label)s_%(class)s_raw_material_production",
                                                blank=True, null=True)
    production = models.ForeignKey('MrpProduction', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_production", blank=True, null=True)
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_purchase_line", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move'


class StockMoveConsume(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    restrict_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_restrict_lot", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move_consume'


class StockMoveOperationLink(models.Model):
    reserved_quant = models.ForeignKey('StockQuant', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_reserved_quant", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    operation = models.ForeignKey('StockPackOperation', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_operation")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move")

    class Meta:
        managed = False
        db_table = 'stock_move_operation_link'


class StockMoveScrap(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product_uom",
                                    db_column='product_uom')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    restrict_lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_restrict_lot", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move_scrap'


class StockPackOperation(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    result_package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_result_package", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_package",
                                blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    owner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_owner", blank=True,
                              null=True)
    fresh_record = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product",
                                blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_uom",
                                    blank=True, null=True)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_dest")
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_picking")

    class Meta:
        managed = False
        db_table = 'stock_pack_operation'


class StockPackOperationLot(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    lot_name = models.CharField(max_length=255, blank=True, null=True)
    qty_todo = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)
    operation = models.ForeignKey('StockPackOperation', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_operation", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_pack_operation_lot'
        unique_together = (('operation', 'lot'), ('operation', 'lot_name'),)


class StockPicking(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    launch_pack_operations = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    backorder = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_backorder",
                                  blank=True, null=True)
    priority = models.CharField(max_length=255)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_picking_type")
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    move_type = models.CharField(max_length=255)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_owner", blank=True,
                              null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    min_date = models.DateTimeField(blank=True, null=True)
    printed = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    recompute_pack_op = models.NullBooleanField()
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_location_dest")
    max_date = models.DateTimeField(blank=True, null=True)
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group",
                              blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)


class StockPickingType(models.Model):
    code = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    use_create_lots = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    default_location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                              related_name="%(app_label)s_%(class)s_default_location_dest", blank=True,
                                              null=True)
    show_entire_packs = models.NullBooleanField()
    barcode_nomenclature = models.ForeignKey('BarcodeNomenclature', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_barcode_nomenclature", blank=True,
                                             null=True)
    use_existing_lots = models.NullBooleanField()
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse",
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    name = models.CharField(max_length=255)
    return_picking_type = models.ForeignKey('self', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_return_picking_type", blank=True,
                                            null=True)
    default_location_src = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                             related_name="%(app_label)s_%(class)s_default_location_src", blank=True,
                                             null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_type'


class StockProductionLot(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")

    class Meta:
        managed = False
        db_table = 'stock_production_lot'
        unique_together = (('name', 'product'),)


class StockQuant(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    propagated_from = models.ForeignKey('self', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_propagated_from", blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_package",
                                blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot",
                            blank=True, null=True)
    reservation = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_reservation",
                                    blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    owner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_owner", blank=True,
                              null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    qty = models.FloatField()
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    packaging_type = models.ForeignKey('ProductPackaging', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_packaging_type", blank=True, null=True)
    negative_move = models.ForeignKey('StockMove', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_negative_move", blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant'


class StockQuantMoveRel(models.Model):
    quant = models.ForeignKey('StockQuant', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_quant")
    move = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move")

    class Meta:
        managed = False
        db_table = 'stock_quant_move_rel'
        unique_together = (('quant', 'move'),)


class StockQuantPackage(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    packaging = models.ForeignKey('ProductPackaging', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_packaging", blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location",
                                 blank=True, null=True)
    owner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_owner", blank=True,
                              null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant_package'


class StockReturnPicking(models.Model):
    move_dest_exists = models.NullBooleanField()
    original_location = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_original_location", blank=True,
                                          null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    parent_location = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_parent_location", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location",
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_return_picking'


class StockReturnPickingLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")
    wizard = models.ForeignKey('StockReturnPicking', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wizard",
                               blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    move = models.ForeignKey('StockMove', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_move", blank=True,
                             null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'stock_return_picking_line'


class StockRouteProduct(models.Model):
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route")
    product = models.ForeignKey('ProductTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")

    class Meta:
        managed = False
        db_table = 'stock_route_product'
        unique_together = (('route', 'product'),)


class StockRouteWarehouse(models.Model):
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_route")
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse")

    class Meta:
        managed = False
        db_table = 'stock_route_warehouse'
        unique_together = (('route', 'warehouse'),)


class StockWarehouse(models.Model):
    crossdock_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_crossdock_route", blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    lot_stock = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lot_stock")
    wh_pack_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                          related_name="%(app_label)s_%(class)s_wh_pack_stock_loc", blank=True,
                                          null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    pick_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pick_type", blank=True, null=True)
    code = models.CharField(max_length=5)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    mto_pull = models.ForeignKey('ProcurementRule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_mto_pull",
                                 blank=True, null=True)
    reception_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_reception_route", blank=True, null=True)
    wh_input_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                           related_name="%(app_label)s_%(class)s_wh_input_stock_loc", blank=True,
                                           null=True)
    delivery_steps = models.CharField(max_length=255)
    default_resupply_wh = models.ForeignKey('self', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_default_resupply_wh", blank=True,
                                            null=True)
    view_location = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_view_location")
    wh_qc_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_wh_qc_stock_loc", blank=True, null=True)
    reception_steps = models.CharField(max_length=255)
    resupply_from_wh = models.NullBooleanField()
    pack_type = models.ForeignKey('StockPickingType', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pack_type", blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_wh_output_stock_loc", blank=True,
                                            null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    delivery_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_delivery_route", blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    in_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_in_type",
                                blank=True, null=True)
    out_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_out_type",
                                 blank=True, null=True)
    int_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_int_type",
                                 blank=True, null=True)
    manufacture_pull = models.ForeignKey('ProcurementRule', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_manufacture_pull", blank=True, null=True)
    manufacture_to_resupply = models.NullBooleanField()
    buy_pull = models.ForeignKey('ProcurementRule', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_buy_pull",
                                 blank=True, null=True)
    buy_to_resupply = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)


class StockWarehouseOrderpoint(models.Model):
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_location")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    lead_type = models.CharField(max_length=255)
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group",
                              blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_warehouse")
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    lead_days = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_product")

    class Meta:
        managed = False
        db_table = 'stock_warehouse_orderpoint'


class StockWhResupplyTable(models.Model):
    supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_supplied_wh")
    supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_supplier_wh")

    class Meta:
        managed = False
        db_table = 'stock_wh_resupply_table'
        unique_together = (('supplied_wh', 'supplier_wh'),)


class SurveyLabel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    question_id_2 = models.ForeignKey('SurveyQuestion', models.DO_NOTHING,
                                      related_name="%(app_label)s_%(class)s_question_id_2", db_column='question_id_2',
                                      blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    quizz_mark = models.FloatField(blank=True, null=True)
    value = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    question = models.ForeignKey('SurveyQuestion', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_question",
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_label'


class SurveyMailComposeMessage(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    no_auto_thread = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING,
                                    related_name="%(app_label)s_%(class)s_mail_server", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    notify = models.NullBooleanField()
    email_from = models.CharField(max_length=255, blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    composition_mode = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    multi_email = models.TextField(blank=True, null=True)
    is_log = models.NullBooleanField()
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent",
                               blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_subtype",
                                blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    record_name = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    use_active_domain = models.NullBooleanField()
    date_deadline = models.DateField(blank=True, null=True)
    public = models.CharField(max_length=255)
    reply_to = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_author",
                               blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_survey")
    message_type = models.CharField(max_length=255)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_template",
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_mail_compose_message'


class SurveyMailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.ForeignKey('SurveyMailComposeMessage', models.DO_NOTHING,
                               related_name="%(app_label)s_%(class)s_wizard")
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_attachment")

    class Meta:
        managed = False
        db_table = 'survey_mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class SurveyMailComposeMessageResPartnerRel(models.Model):
    wizard = models.ForeignKey('SurveyMailComposeMessage', models.DO_NOTHING,
                               related_name="%(app_label)s_%(class)s_wizard")
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partnet")

    class Meta:
        managed = False
        db_table = 'survey_mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class SurveyPage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_survey")

    class Meta:
        managed = False
        db_table = 'survey_page'


class SurveyQuestion(models.Model):
    constr_error_msg = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    matrix_subtype = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    comments_allowed = models.NullBooleanField()
    validation_min_float_value = models.FloatField(blank=True, null=True)
    constr_mandatory = models.NullBooleanField()
    column_nb = models.CharField(max_length=255, blank=True, null=True)
    validation_required = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    validation_length_max = models.IntegerField(blank=True, null=True)
    validation_length_min = models.IntegerField(blank=True, null=True)
    question = models.CharField(max_length=255)
    display_mode = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=15)
    validation_min_date = models.DateTimeField(blank=True, null=True)
    comments_message = models.CharField(max_length=255, blank=True, null=True)
    validation_email = models.NullBooleanField()
    description = models.TextField(blank=True, null=True)
    comment_count_as_answer = models.NullBooleanField()
    validation_max_float_value = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    validation_max_date = models.DateTimeField(blank=True, null=True)
    validation_error_msg = models.CharField(max_length=255, blank=True, null=True)
    page = models.ForeignKey('SurveyPage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_page")

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveyStage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    fold = models.NullBooleanField()
    closed = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_stage'


class SurveySurvey(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    thank_you_message = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    quizz_mode = models.NullBooleanField()
    users_can_go_back = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    auth_required = models.NullBooleanField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    email_template = models.ForeignKey('MailTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_email_template", blank=True, null=True)
    stage = models.ForeignKey('SurveyStage', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_stage",
                              blank=True, null=True)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'survey_survey'


class SurveyUserInput(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_partner",
                                blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    date_create = models.DateTimeField()
    email = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(unique=True, max_length=255)
    deadline = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    last_displayed_page = models.ForeignKey('SurveyPage', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_last_displayed_page", blank=True,
                                            null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_survey")
    type = models.CharField(max_length=255)
    test_entry = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'survey_user_input'


class SurveyUserInputLine(models.Model):
    value_date = models.DateTimeField(blank=True, null=True)
    value_suggested_row = models.ForeignKey('SurveyLabel', models.DO_NOTHING,
                                            related_name="%(app_label)s_%(class)s_value_suggested_row",
                                            db_column='value_suggested_row', blank=True, null=True)
    skipped = models.NullBooleanField()
    value_suggested = models.ForeignKey('SurveyLabel', models.DO_NOTHING,
                                        related_name="%(app_label)s_%(class)s_value_suggested",
                                        db_column='value_suggested', blank=True, null=True)
    answer_type = models.CharField(max_length=255, blank=True, null=True)
    value_text = models.CharField(max_length=255, blank=True, null=True)
    quizz_mark = models.FloatField(blank=True, null=True)
    user_input = models.ForeignKey('SurveyUserInput', models.DO_NOTHING,
                                   related_name="%(app_label)s_%(class)s_user_input")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    date_create = models.DateTimeField()
    value_number = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_survey",
                               blank=True, null=True)
    value_free_text = models.TextField(blank=True, null=True)
    question = models.ForeignKey('SurveyQuestion', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_question")

    class Meta:
        managed = False
        db_table = 'survey_user_input_line'


class UtmCampaign(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_campaign'


class UtmMedium(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'utm_medium'


class UtmSource(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_source'


class ValidateAccountMove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validate_account_move'


class WebEditorConverterTest(models.Model):
    binary = models.BinaryField(blank=True, null=True)
    selection = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    char = models.CharField(max_length=255, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    selection_str = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    many2one = models.ForeignKey('WebEditorConverterTestSub', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_many2one", db_column='many2one', blank=True,
                                 null=True)
    date = models.DateField(blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test'


class WebEditorConverterTestSub(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test_sub'


class WebPlanner(models.Model):
    menu = models.ForeignKey('IrUiMenu', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_menu")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    planner_application = models.CharField(max_length=255)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_view")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    progress = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    tooltip_planner = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_planner'


class WebTip(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    placement = models.CharField(max_length=255, blank=True, null=True)
    end_selector = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    end_event = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    trigger_selector = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    highlight_selector = models.CharField(max_length=255, blank=True, null=True)
    action = models.ForeignKey('IrActWindow', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_action",
                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_tip'


class Website(models.Model):
    domain = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    social_linkedin = models.CharField(max_length=255, blank=True, null=True)
    cdn_filters = models.TextField(blank=True, null=True)
    social_facebook = models.CharField(max_length=255, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    google_analytics_key = models.CharField(max_length=255, blank=True, null=True)
    default_lang = models.ForeignKey('ResLang', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_default_lang",
                                     blank=True, null=True)
    social_twitter = models.CharField(max_length=255, blank=True, null=True)
    cdn_url = models.CharField(max_length=255, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_user", blank=True,
                             null=True)
    default_lang_code = models.CharField(max_length=255, blank=True, null=True)
    social_googleplus = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company",
                                blank=True, null=True)
    social_github = models.CharField(max_length=255, blank=True, null=True)
    compress_html = models.NullBooleanField()
    social_youtube = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cdn_activated = models.NullBooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    salesteam = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_salesteam",
                                  blank=True, null=True)
    salesperson = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_salesperson",
                                    blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website'


class WebsiteConfigSettings(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    website = models.ForeignKey('Website', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_website")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_website_version = models.NullBooleanField()
    module_website_form_editor = models.NullBooleanField()
    module_delivery_usps = models.NullBooleanField()
    module_delivery_fedex = models.NullBooleanField()
    module_delivery_ups = models.NullBooleanField()
    module_sale_ebay = models.NullBooleanField()
    module_delivery_dhl = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'website_config_settings'


class WebsiteLangRel(models.Model):
    website = models.ForeignKey('Website', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_website")
    lang = models.ForeignKey('ResLang', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_lang")

    class Meta:
        managed = False
        db_table = 'website_lang_rel'
        unique_together = (('website', 'lang'),)


class WebsiteMenu(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    website = models.ForeignKey('Website', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_website",
                                blank=True, null=True)
    new_window = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_parent", blank=True,
                               null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_menu'


class WebsitePricelist(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    website = models.ForeignKey('Website', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_website")
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING,
                                  related_name="%(app_label)s_%(class)s_pricelist", blank=True, null=True)
    selectable = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'website_pricelist'


class WebsiteSeoMetadata(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    website_meta_description = models.TextField(blank=True, null=True)
    website_meta_title = models.CharField(max_length=255, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    website_meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_seo_metadata'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey('IrUiMenu', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_menu")
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'


class WizardMultiChartsAccounts(models.Model):
    only_one_chart_template = models.NullBooleanField()
    bank_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    code_digits = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    transfer_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING,
                                         related_name="%(app_label)s_%(class)s_transfer_account")
    purchase_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                     related_name="%(app_label)s_%(class)s_purchase_tax", blank=True, null=True)
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING,
                                       related_name="%(app_label)s_%(class)s_chart_template")
    complete_tax_set = models.NullBooleanField()
    sale_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING,
                                 related_name="%(app_label)s_%(class)s_sale_tax", blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_currency")
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_company")
    purchase_tax_rate = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_tax_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_multi_charts_accounts'


class WizardValuationHistory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    choose_date = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'wizard_valuation_history'


class Wkf(models.Model):
    name = models.CharField(max_length=255)
    osv = models.CharField(max_length=255)
    on_create = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf'


class WkfActivity(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    kind = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    join_mode = models.CharField(max_length=3)
    flow_stop = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    subflow = models.ForeignKey('Wkf', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_subflow", blank=True,
                                null=True)
    split_mode = models.CharField(max_length=3)
    write_date = models.DateTimeField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    wkf = models.ForeignKey('Wkf', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wkf")
    signal_send = models.CharField(max_length=255, blank=True, null=True)
    flow_start = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'wkf_activity'


class WkfInstance(models.Model):
    res_type = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    wkf = models.ForeignKey('Wkf', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_wkf", blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_instance'


class WkfTransition(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_create_uid",
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    trigger_model = models.CharField(max_length=255, blank=True, null=True)
    signal = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_write_uid",
                                  db_column='write_uid', blank=True, null=True)
    act_from = models.ForeignKey('WkfActivity', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_act_from",
                                 db_column='act_from')
    condition = models.CharField(max_length=255)
    write_date = models.DateTimeField(blank=True, null=True)
    trigger_expr_id = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_group", blank=True,
                              null=True)
    act_to = models.ForeignKey('WkfActivity', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_act_to",
                               db_column='act_to')

    class Meta:
        managed = False
        db_table = 'wkf_transition'


class WkfTriggers(models.Model):
    instance = models.ForeignKey('WkfInstance', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_instance",
                                 blank=True, null=True)
    workitem = models.ForeignKey('WkfWorkitem', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_workitem")
    model = models.CharField(max_length=255, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_triggers'


class WkfWitmTrans(models.Model):
    inst = models.ForeignKey('WkfInstance', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_inst")
    trans = models.ForeignKey('WkfTransition', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_trans")

    class Meta:
        managed = False
        db_table = 'wkf_witm_trans'
        unique_together = (('inst', 'trans'),)


class WkfWorkitem(models.Model):
    act = models.ForeignKey('WkfActivity', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_act")
    inst = models.ForeignKey('WkfInstance', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_inst")
    subflow = models.ForeignKey('WkfInstance', models.DO_NOTHING, related_name="%(app_label)s_%(class)s_subflow",
                                blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkf_workitem'
