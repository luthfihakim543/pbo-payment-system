
from datetime import datetime, timedelta

from core.base import PaymentMethod, PembayaranGagal
from core.utils import rupiah
from core.registry import register_plugin


@register_plugin("virtual_account")
class VirtualAccount(PaymentMethod):
    def __init__(
        self,
        nomor_va: str,
        batas_waktu: int = 24,
    ):
        super().__init__("Virtual Account")
        self.nomor_va = nomor_va
        self.batas_waktu = datetime.now() + timedelta(hours=batas_waktu)
        self.status = "menunggu"

    def validasi(self, jumlah: float) -> bool:
        return jumlah > 0 and datetime.now() <= self.batas_waktu

    def bayar(self, jumlah: float) -> str:
        if datetime.now() > self.batas_waktu:
            raise PembayaranGagal("Batas waktu pembayaran telah habis")

        self.status = "berhasil"
        return f"VA-{self.nomor_va}"

    def biaya_admin(self, jumlah: float) -> float:
        return 4000.0
