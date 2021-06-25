import __main__
import os
import socket
from contextdecorator import ContextDecorator
from exceptions import (
    GeneralException,
    AlreadyRunningException,
    NotAllowedException
)


class job(ContextDecorator):

    def __init__(self, allowed_hosts=None, prefix=None, pid_path=None):
        self._pid = str(os.getpid())
        self._pid_path = pid_path if pid_path else '/var/run'
        self._pid_prefix = prefix if prefix else 'cronhost'
        self._cron_id = os.path.basename(__main__.__file__)

        if not os.path.isdir(self._pid_path):
            raise GeneralException('Invalid PID file path')        

        self._pid_file = os.path.join(
            self._pid_path,
            "{}-{}.pid".format(self._pid_prefix, self._cron_id)
        )

        if allowed_hosts:
            if not self._check_hosts(allowed_hosts):
                raise NotAllowedException(
                    'This job can not be run on this host'
                )

        if os.path.exists(self._pid_file):
            raise AlreadyRunningException('Process already running. Quitting.')            

    def __enter__(self):
        try:
            f = open(self._pid_file, 'w')
        except Exception:
            raise GeneralException('Could not open PID file for write')

        f.write(self._pid)
        f.close()

    def __exit__(self, e_typ, e_val, trcbak):
        os.unlink(self._pid_file)

    @classmethod
    def _check_hosts(cls, allowed_hosts):
        if type(allowed_hosts) is not list:
            raise TypeError('Arguement must be a list: "allowed_hosts"')

        allowed_hosts = [host.lower() for host in allowed_hosts]

        sock_host = socket.gethostname().lower()
        sock_fqdn = socket.getfqdn().lower()

        if sock_host not in allowed_hosts and sock_fqdn not in allowed_hosts:
            return False

        return True
