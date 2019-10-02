class ServiceError(Exception):
    pass

class LicenceError(Exception):
    pass

class AccountError(Exception):
    pass

class RateLimited(Exception):
    pass

codeToError = {
    0: "There was an error contacting the ProfanityBlocker service. Please try again later.",
    104: "There was an error with your licence for ProfanityBlocker. Please check your licence is valid and  active and try again.",
    102: "There was an error with your account. Please try again later.",
    999: "You have sent too many requests than you have paid for in your package, you can either upgrade your package or wait."
}

CodeToException = {
    0: ServiceError,
    102: AccountError,
    104: LicenceError,
    999: RateLimited,
    103: ServiceError,
    101: ServiceError
}

def RaiseError(Code):
    raise CodeToException[Code](codeToError[Code])