from django.db import models
from django.contrib.auth.models import User


#Справочники


class Curator(models.Model):
    title = models.CharField(max_length=120)


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    curator = models.ForeignKey(Curator, on_delete=models.DO_NOTHING)


class FinanceCosts(models.Model):
    title = models.CharField(
        verbose_name="название статьи",
        max_length=100
    )


class PurchaseType(models.Model):
    title = models.CharField(max_length=200)


class ActivityForm(models.Model):
    title = models.CharField(max_length=200)


class StateASEZ(models.Model):
    title = models.CharField(max_length=200)


class NumberPZTRU(models.Model):
    title = models.CharField(max_length=200)


class ContractStatus(models.Model):
    title = models.CharField(max_length=200)


class Currency(models.Model):
    title = models.CharField(max_length=10)


class Price(models.Model):
    value = models.FloatField(verbose_name="цена")
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)


class ContractTerm(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()


class Counterpart(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reg_addr = models.CharField(max_length=255)
    UNP = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class Contract(models.Model):
    title = models.CharField(max_length=150, verbose_name="наименование договора")
    finance_cost = models.ForeignKey(
        FinanceCosts,
        on_delete=models.DO_NOTHING,
        verbose_name="статья финансирования")
    curator = models.ForeignKey(
        Curator,
        on_delete=models.DO_NOTHING,
        verbose_name="Куратор"
    )
    contract_type = models.BooleanField(
        default=True,
        verbose_name="Тип договора",
        help_text="филиал или центръ"
    )   # default fillial
    contract_mode = models.BooleanField(
        default=True,
        verbose_name="Вид договора",
        help_text="основной либо доп.согл.")   # default main
    purchase_type = models.ForeignKey(
        PurchaseType,
        verbose_name="тип закупки",
        on_delete=models.DO_NOTHING,
        help_text="вводить тип закупки которая может меняться"
    )
    activity_form = models.ForeignKey(
        ActivityForm,
        verbose_name="вид деятельности",
        on_delete=models.DO_NOTHING
    )
    stateASEZ = models.ForeignKey(
        StateASEZ,
        verbose_name="автоматизированая система эллектронных закупок",
        on_delete=models.DO_NOTHING
    )
    number_ppz = models.CharField(
        max_length=150,
        verbose_name="номер позиция плана закупок",
        null=True,
        blank=True
    )
    number_PZTRU = models.ForeignKey(
        NumberPZTRU,
        verbose_name="ПЗТРУ",
        help_text="положение о закупках товаров, работ, услуг",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    contract_status = models.ForeignKey(
        ContractStatus,
        verbose_name="статус договора",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    plan_load_date_ASEZ = models.DateField(
        verbose_name="планируемая дата загрузки в АСЭЗ",
    )
    fact_load_date_ASEZ = models.DateField(
        verbose_name="фактическая дата загрузки в АСЭЗ",
        null=True,
        blank=True
    )

    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)

    number_KGG = models.CharField(
        max_length=100,
        verbose_name="номер договора от центрального органа",
        null=True,
        blank=True
    )
    register_number_SAP = models.CharField(max_length=100)
    contract_number = models.CharField(
        max_length=100,
        verbose_name="номер договора",
        null=True,
        blank=True
    )
    plan_sign_date = models.DateField()
    fact_sign_date = models.DateField(null=True, blank=True)
    contract_term = models.ForeignKey(
        ContractTerm,
        verbose_name="период действия",
        on_delete=models.DO_NOTHING
    )
    counterpart = models.ForeignKey(Counterpart, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # TODO   contract_mode


class SumsRUR(models.Model):
    contract = models.ForeignKey(
        Contract,
        verbose_name="Контракт",
        on_delete=models.DO_NOTHING
    )
    start_max_price_ASEZ_NDS = models.ForeignKey(
        Price,
        verbose_name="начальная максимальная цена АСЭЗ с НДС рос. руб.",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    currency_rate_on_load_date_ASEZ_NDS = models.FloatField(
        verbose_name="курс валюты на дату загрузки в бел.руб.",
        null=True,
        blank=True
    )
    contract_sum_NDS_RUB = models.FloatField(
        verbose_name="сумма договора с НДС рос.руб.",
        blank=True,
        null=True
    )
    currency = models.ForeignKey(
        Currency,
        verbose_name="Валюта",
        on_delete=models.DO_NOTHING
    )
    delta_data_ASEZ = models.FloatField(
        verbose_name="отклонение от НМЦ в АСЭЗ",
        blank=True,
        null=True
    )


class SumsBYN(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.DO_NOTHING)
    year = models.DateField()
    plan_sum_SAP = models.FloatField(
        verbose_name="плановая сумма САП",
        blank=True,
        null=True
    )
    contract_sum_without_NDS_BYN = models.FloatField(
        verbose_name="сумма всего договора без НДС",
        blank=True,
        null=True
    )
    contract_sum_with_NDS_BYN = models.FloatField(
        verbose_name="сумма договора с НДС бел.руб.",
        blank=True,
        null=True
    )
    contract_total_sum_with_sub_BYN = models.FloatField(
        verbose_name='общая сумма договора всего с доп соглашениями, б.р. без ндс',
        null=True,
        blank=True,
    )
    forecast_total = models.FloatField(  # вычисляемое
        verbose_name='прогноз, всего',
        blank=True,
        null=True
    )
    economy_total = models.FloatField(
        verbose_name='Экономия по заключенному договору, всего',
        blank=True,
        null=True
    )
    fact_total = models.FloatField(  # вычисляемое
        verbose_name='факт, всего',
        blank=True,
        null=True
    )
    economy_contract_result = models.FloatField(
        verbose_name='Экономия по результатам исполенения договоров всего',
        blank=True,
        null=True
    )
    total_sum_unsigned_contracts = models.FloatField(  # вычисляемое
        verbose_name='Сумма средств по незаключенным договорам',
        blank=True,
        null=True
    )

    economy_total_absolute = models.FloatField(  # вычисляемое
        verbose_name='Абсолютная экономия по договору, всего',
        blank=True,
        null=True
    )


class Planning(models.Model):
    FinanceCosts = models.ForeignKey(
        FinanceCosts,
        verbose_name="Статья финансирования",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    curator = models.ForeignKey(
        Curator,
        verbose_name="Куратор",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    year = models.DateField(
        verbose_name="Год"
    )
    period = models.DateField(
        verbose_name="Период"
    )
    total = models.FloatField(
        verbose_name="Сумма",
        blank=True,
        null=True
    )
    currency = models.ForeignKey(
        Currency,
        verbose_name="Валюта",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )


