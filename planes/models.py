from django.db import models
from django.contrib.auth.models import User


class Curator(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    curator = models.ForeignKey(Curator, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username


class FinanceCosts(models.Model): #  A 1000      B 2000
    total = models.FloatField(verbose_name="сумма 4-x кварталов")
    title = models.CharField(
        verbose_name="название статьи",
        max_length=100
    )

    def __str__(self):
        return self.title


class Quart(models.Model): # A1-250|A2-250|A3-250|A4-250|B1-500|B2-500|B3-500|B4-500
    finance_cost = models.ForeignKey(FinanceCosts, on_delete=models.DO_NOTHING)
    total = models.FloatField(verbose_name="сумма по кварталу")
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}: {self.finance_cost.title}"


class CuratorQuartCosts(models.Model): # vadim a1 100    ser a1 100
    quart = models.ForeignKey(
        Quart,
        on_delete=models.DO_NOTHING,
        verbose_name="квартал куратора"
    )
    curator = models.ForeignKey(
        Curator,
        on_delete=models.DO_NOTHING,
        verbose_name="куратор"
    )
    total = models.FloatField(
        verbose_name="деньги выделенные данному куратору в данной статье данного квартала"
    )

    def __str__(self):
        return f"{self.curator.title} - {self.quart.title}: {self.quart.finance_cost.title}"


class PurchaseType(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ActivityForm(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class StateASEZ(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class NumberPZTRU(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ContractStatus(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Currency(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Price(models.Model):
    value = models.FloatField(verbose_name="цена")
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.value} ({self.currency.title})"


class ContractTerm(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"


class Counterpart(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reg_addr = models.CharField(max_length=255)
    UNP = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    plane_load_date_ASEZ = models.DateField(verbose_name="планируемая дата загрузки в АСЭЗ")
    fact_load_date_ASEZ = models.DateField(
        verbose_name="фактическая дата загрузки в АСЭЗ",
        null=True,
        blank=True
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
    contract_sum_NDS_RUB = models.FloatField(verbose_name="сумма договора с НДС рос.руб.")
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    delta_data_ASEZ = models.FloatField(verbose_name="отклонение от НМЦ в АСЭЗ")
    number_KGG = models.CharField(
        max_length=100,
        verbose_name="номер договора от центрального органа",
        null=True,
        blank=True
    )
    plane_sum_SAP_total = models.FloatField(verbose_name="плановая сумма САП")
    plane_sum_SAP_1 = models.FloatField(default=0, verbose_name="сумма САП 1-й квартал")
    plane_sum_SAP_2 = models.FloatField(default=0, verbose_name="сумма САП 2-й квартал")
    plane_sum_SAP_3 = models.FloatField(default=0, verbose_name="сумма САП 3-й квартал")
    plane_sum_SAP_4 = models.FloatField(default=0, verbose_name="сумма САП 4-й квартал")
    register_number_SAP = models.CharField(max_length=100)
    contract_number = models.CharField(
        max_length=100,
        verbose_name="номер договора",
        null=True,
        blank=True
    )
    plane_sign_date = models.DateField()
    fact_sign_date = models.DateField(null=True, blank=True)
    contract_term = models.ForeignKey(
        ContractTerm,
        verbose_name="период действия",
        on_delete=models.DO_NOTHING
    )
    counterpart = models.ForeignKey(Counterpart, on_delete=models.DO_NOTHING)
    contract_sum = models.FloatField(verbose_name="сумма всего договора без НДС")
    contract_sum_1 = models.FloatField(
        verbose_name="сумма 1-й квартал договора без НДС",
        null=True,
        blank=True
    )
    contract_sum_2 = models.FloatField(
        verbose_name="сумма 2-й квартал договора без НДС",
        null=True,
        blank=True
    )
    contract_sum_3 = models.FloatField(
        verbose_name="сумма 3-й квартал договора без НДС",
        null=True,
        blank=True
    )
    contract_sum_4 = models.FloatField(
        verbose_name="сумма 4-й квартал договора без НДС",
        null=True,
        blank=True
    )
    contract_sum_NDS_BYN = models.FloatField(
        verbose_name="сумма договора с НДС бел.руб.",
        blank=True,
        null=True,
    )
    contract_total_sum_with_sub_BYN = models.FloatField(
        verbose_name='общая сумма договора всего с доп соглашениями, б.р. без ндс',
        null=True,
        blank=True
    )

    forecast_total = models.FloatField( # вычисляемое
        verbose_name='прогонз, всего',
    )
    forecast_jan = models.FloatField(
        verbose_name='прогноз январь',
        default=0
    )
    forecast_feb = models.FloatField(
        verbose_name='прогноз февраль',
        default=0
    )
    forecast_mar = models.FloatField(
        verbose_name='прогноз март',
        default=0
    )
    forecast_Iq = models.FloatField( # вычисляемое
        verbose_name='прогноз 1-й квартал'
    )

    forecast_apr = models.FloatField(
        verbose_name='прогноз апрель',
        default=0
    )
    forecast_may = models.FloatField(
        verbose_name='прогноз май',
        default=0
    )
    forecast_jun = models.FloatField(
        verbose_name='прогноз июнь',
        default=0
    )
    forecast_IIq = models.FloatField( # вычисляемое
        verbose_name='прогноз 2-й квартал'
    )
    forecast_1_half = models.FloatField( # вычисляемое
        verbose_name='прогноз 1-е полугодие'
    )

    forecast_jul = models.FloatField(
        verbose_name='прогноз июль',
        default=0
    )
    forecast_aug = models.FloatField(
        verbose_name='прогноз август',
        default=0
    )
    forecast_sep = models.FloatField(
        verbose_name='прогноз сентябрь',
        default=0
    )
    forecast_IIIq = models.FloatField(  # вычисляемое
        verbose_name='прогноз 3-й квартал'
    )

    forecast_9mnth = models.FloatField(  # вычисляемое
        verbose_name='прогноз за 9 месяцев'
    )

    forecast_oct = models.FloatField(
        verbose_name='прогноз октябрь',
        default=0
    )
    forecast_nov = models.FloatField(
        verbose_name='прогноз ноябрь',
        default=0
    )
    forecast_dec = models.FloatField(
        verbose_name='прогноз декабрь',
        default=0
    )
    forecast_IVq = models.FloatField(  # вычисляемое
        verbose_name='прогноз 4-й квартал'
    )

    economy_total = models.FloatField(
        verbose_name='Экономия по заключенному договору, всего',
    )
    economy_Iq = models.FloatField(
        verbose_name='Экономия по заключенному договору за 1-й квартал',
    )
    economy_IIq = models.FloatField(
        verbose_name='Экономия по заключенному договору за 2-й квартал',
    )
    economy_IIIq = models.FloatField(
        verbose_name='Экономия по заключенному договору за 3-й квартал',
    )
    economy_IVq = models.FloatField(
        verbose_name='Экономия по заключенному договору за 4-й квартал',
    )

    fact_total = models.FloatField(  # вычисляемое
        verbose_name='факт, всего',
    )
    fact_Iq = models.FloatField(  # вычисляемое
        verbose_name='1-й квартал',
    )
    fact_jan = models.FloatField(
        verbose_name='факт январь',
        default=0
    )
    fact_feb = models.FloatField(
        verbose_name='факт февраль',
        default=0
    )
    fact_mar = models.FloatField(
        verbose_name='факт март',
        default=0
    )

    fact_IIq = models.FloatField(  # вычисляемое
        verbose_name='2-й квартал',
    )
    fact_apr = models.FloatField(
        verbose_name='факт апрель',
        default=0
    )
    fact_may = models.FloatField(
        verbose_name='факт май',
        default=0
    )
    fact_jun = models.FloatField(
        verbose_name='факт июнь',
        default=0
    )

    plane_sum_SAP_6mth = models.FloatField( # вычисляемое
        verbose_name='плановая сумма SAP за 6 месяцев'
    )

    fact_6mth = models.FloatField( # вычисляемое
        verbose_name='Факт за 6 месяцев'
    )

    fact_IIIq = models.FloatField(  # вычисляемое
        verbose_name='3-й квартал',
    )
    fact_jul = models.FloatField(
        verbose_name='факт июль',
    )
    fact_aug = models.FloatField(
        verbose_name='факт август',
        default=0
    )
    fact_sep = models.FloatField(
        verbose_name='факт сентябрь',
        default=0
    )

    plane_sum_SAP_9mth = models.FloatField(  # вычисляемое
        verbose_name='плановая сумма SAP за 9 месяцев'
    )

    fact_9mth = models.FloatField( # вычисляемое
        verbose_name='Факт за 9 месяцев'
    )

    fact_IVq = models.FloatField( # вычисляемое
        verbose_name='Факт за 4 квартал'
    )
    fact_oct = models.FloatField(
        verbose_name='факт октябрь',
        default=0
    )
    fact_10mth = models.FloatField( # вычисляемое
        verbose_name='факт 10 месяцев',
    )
    fact_nov = models.FloatField(
        verbose_name='факт ноябрь',
        default=0
    )
    fact_dec = models.FloatField(
        verbose_name='факт декабрь',
        default=0
    )

    economy_contract_result = models.FloatField(
        verbose_name='Экономия по результатам исполенения договоров всего'
    )
    economy_result_Iq = models.FloatField(
        verbose_name='Экономия по результатам исполенения договоров 1-й квартал',
        default=0
    )
    economy_result_IIq = models.FloatField(
        verbose_name='Экономия по результатам исполенения договоров 2-й квартал',
        default=0
    )
    economy_result_IIIq = models.FloatField(
        verbose_name='Экономия по результатам исполенения договоров 3-й квартал',
        default=0
    )
    economy_result_IVq = models.FloatField(
        verbose_name='Экономия по результатам исполенения договоров 4-й квартал',
        default=0
    )

    total_sum_unsigned_contracts = models.FloatField( # вычисляемое
        verbose_name='Сумма средств по незаключенным договорам'
    )

    economy_total_absolute = models.FloatField( # вычисляемое
        verbose_name='Абсолютная экономия по договору, всего'
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # TODO   contract_mode


class Planing(models.Model):
    pass
