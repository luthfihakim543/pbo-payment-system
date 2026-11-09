from core.protocols import Notifier
from core.notifiers import TelegramNotifier
from core.processor import PaymentProcessor
from core.registry import buat_metode
from plugins import muat_semua_plugin

muat_semua_plugin()

# 1. Buktikan bahwa isinstance() bernilai True meskipun tanpa pewarisan
telegram = TelegramNotifier()
print("Apakah TelegramNotifier memenuhi Notifier?", isinstance(telegram, Notifier))

# 2. Uji pakai langsung ke PaymentProcessor
pemroses = PaymentProcessor(telegram)
metode = buat_metode("transfer", saldo=500_000, bank="BCA")
pemroses.checkout(metode, 100_000, pelanggan="mahasiswa@utr.ac.id")