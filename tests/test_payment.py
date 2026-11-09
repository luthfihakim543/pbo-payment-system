
import pytest

from core.base import PaymentMethod
from core.registry import buat_metode
from plugins import muat_semua_plugin


def test_payment_method_tidak_bisa_diinstansiasi():
    with pytest.raises(TypeError):
        PaymentMethod("uji")


def test_plugin_tidak_dikenal_memunculkan_keyerror():
    muat_semua_plugin()

    with pytest.raises(KeyError):
        buat_metode("plugin_tidak_dikenal")
