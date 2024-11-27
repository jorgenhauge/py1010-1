import pandas as pd

format_string = "%H:%M:%S"
data_xlsx: pd.DataFrame = pd.read_excel(
    "support_uke_24.xlsx",
    names=["u_dag", "kl_slett", "varighet", "score"],
    converters={
        "u_dag": str,
        "kl_slett": lambda ts: pd.to_datetime(ts),
        "varighet": lambda ts: pd.to_datetime(ts),
        "score": str,
    },
)
weekdays = data_xlsx["u_dag"]
t = data_xlsx["kl_slett"]
durations = data_xlsx["varighet"]

print(
    f"""Antall henvendelser: {weekdays.value_counts()}
    Antall henvendelser mellom(08:00 - 10:00): {t.between("08:00", "10:00").value_counts()},
    (10:00 - 12:00): {t.between("10:00", "12:00").value_counts()},
    (12:00 - 14:00): {t.between("12:00", "14:00").value_counts()},
    (12:00 - 14:00): {t.between("14:00", "16:00").value_counts()}
    Lengste samtaletid: {durations.max().time():"%H:%M:%S"}
    Korteste samtaletid: {durations.min().time():"%H:%M:%S"}
    Gjennomsnittlig samtaletid: {durations.mean().time():"%H:%M:%S"}
    """
)
# plt.ylabel("Antall henvendelser")
# plt.bar(counter.keys(), counter.values())
# plt.show()
