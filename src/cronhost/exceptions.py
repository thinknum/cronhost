
class CronhostException(Exception):
    pass


class GeneralException(CronhostException):
    pass


class NotAllowedException(CronhostException):
    pass


class AlreadyRunningException(CronhostException):
    pass
