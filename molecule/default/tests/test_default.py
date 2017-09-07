import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_httpd_file(host):
    f = host.file('/etc/httpd/conf/httpd.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_httpd_is_installed(host):
    httpd = host.package("httpd")
    assert httpd.is_installed
    assert httpd.version.startswith("2.4")


def test_httpd_running_and_enabled(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled
