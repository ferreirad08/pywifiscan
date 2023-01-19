"""Tests for WifiScan."""

from pywifiscan import get_interface, scan_networks
import pytest

valid_interfaces = [
    "eth0",
    "wlan0"
]


def test_get_interface():
    iface = getInterface()
    assert isinstance(iface, str)
    assert iface in valid_interfaces


def test_scan_networks():
    iface = getInterface()
    networks = scan_networks(iface)
    assert isinstance(iface, dict)
