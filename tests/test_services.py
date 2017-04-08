from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
        AnsibleRunner('.molecule/ansible_inventory').get_hosts('test')


def test_command(Socket):
    assert Socket('tcp://:::8080').is_listening
    assert Socket('tcp://:::8843').is_listening