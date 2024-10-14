# Defined information and details
forsikring_elbil_pr_aar, forsikring_bensinbil_pr_aar = 5000, 7500
trafikkforsikringsavgift_pr_dag = 8.38
trafikkforsikringsavgift = trafikkforsikringsavgift_pr_dag * 365

drivstoff_elbil_kwh_pr_km = 0.2
strompris_kwh = 2.00
bomavgift_elbil_pr_km = 0.1

drivstoff_bensinbil_kr_pr_km = 1.0
bomavgift_bensinbil_pr_km = 0.3

antall_kjorte_km_pr_aar = float(
    input("Skriv inn antall kilometer du kjører på et år(standardverdi: 10000):")
    or 10000
)

drivstoff_kost_elbil = (
    antall_kjorte_km_pr_aar * drivstoff_elbil_kwh_pr_km * strompris_kwh
)
bomavgift_elbil = antall_kjorte_km_pr_aar * bomavgift_elbil_pr_km


drivstoff_kost_bensinbil = antall_kjorte_km_pr_aar * drivstoff_bensinbil_kr_pr_km
bomavgift_bensinbil = antall_kjorte_km_pr_aar * bomavgift_bensinbil_pr_km


totalkost_elbil = (
    forsikring_elbil_pr_aar
    + trafikkforsikringsavgift
    + drivstoff_kost_elbil
    + bomavgift_elbil
)
totalkost_bensinbil = (
    forsikring_bensinbil_pr_aar
    + trafikkforsikringsavgift
    + drivstoff_kost_bensinbil
    + bomavgift_bensinbil
)


print(
    f"Totalkostnad(pr år) elbil: {totalkost_elbil} kr, bensinbil: {totalkost_bensinbil} kr. Differanse: {totalkost_bensinbil - totalkost_elbil} kr"
)
