
# ProfanityBlocker Python Integration


ProfanityBlocker is a rules engine that is able to identify and block words and phrases that have been identified as containing Profane Language.

Pricing information for ProfanityBlocker can be found at: [https://www.profanity-blocker.co.uk/#pricing](https://www.profanity-blocker.co.uk/#pricing)

We have designed our Python implementation to be simple to use. Meaning that sending a request to our service to process only takes three lines of code!

    import ProfanityBlocker
    Service = ProfanityBlocker.ProfanityService(LicenceKey,EmailFilter=False, LinkFilter=False,PhoneFilter=False)
    print(Service.ParseText("Test"))

ProfanityBlocker has a range of filters that you can enable in your requests, as seen above, you can enable filtering out; E-Mail addresses, Web Links as well as Phone Numbers!
