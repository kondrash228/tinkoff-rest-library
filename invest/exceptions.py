__all__ = (
    'TinvestError',
    'TooManyRequestsError'
)


class TinvestError(Exception):
    pass


class TooManyRequestsError(TinvestError):
    pass
