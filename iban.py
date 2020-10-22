# coding: utf8
"""
# International Bank Account Number (IBAN) Verification

The International Bank Account Number (IBAN) is an internationally agreed system of identifying bank accounts
across national borders to facilitate the communication and processing of cross border transactions with a reduced
risk of transcription errors. It uniquely identifies the account of a customer at a financial institution.
The IBAN consists of up to 34 alphanumeric characters comprising a country code; two check digits; and a number
that includes the domestic bank account number, branch identifier, and potential routing information. The check
digits enable a check of the bank account number to confirm its integrity before submitting a transaction.

An IBAN is validated by converting it into an integer and performing a basic mod-97 operation (as described
in ISO 7064) on it. If the IBAN is valid, the remainder equals 1. The algorithm of IBAN validation
is as follows:

1. Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
2. Move the four initial characters to the end of the string
3. Replace each letter in the string with two digits, thereby expanding the string,
   where A = 10, B = 11, ..., Z = 35
4. Interpret the string as a decimal integer and compute the remainder of that number on division by 97

If the remainder is 1, the check digit test is passed and the IBAN might be valid.

Example (fictitious United Kingdom bank, sort code 12-34-56, account number 98765432):

1. IBAN: `GB82 WEST 1234 5698 7654 32` (GB for United Kingdom, length 22)
2. Rearrange: `WEST12345698765432GB82`
3. Convert to integer: `3214282912345698765432161182`
4. Compute remainder: `3214282912345698765432161182` modulo `97` = `1`

Write a function `check_iban(number)` that implements the above algorithm and returns `True` of `False`
indicating if the bank account number is correct. The function must take a full IBAN (in a string) as
its argument. This string may contain arbitrary spaces to increase legibility. These spaces must be discarded.
This function must return false if the checksum is wrong or the IBAN length is incorrect or the country code
refers to non-existing country.

Use it to verify your bank account number (please note that in Poland the country prefix `PL` is usually skipped,
so you must remember to add it).
"""

COUNTRIES = {
     'AL': ("Albania", 28),
     'AD': ("Andorra", 24),
     'AT': ("Austria", 20),
     'AZ': ("Azerbaijan", 28),
     'BH': ("Bahrain", 22),
     'BY': ("Belarus", 28),
     'BE': ("Belgium", 16),
     'BA': ("Bosnia and Herzegovina", 20),
     'BR': ("Brazil", 29),
     'BG': ("Bulgaria", 22),
     'CR': ("Costa Rica", 22),
     'HR': ("Croatia", 21),
     'CY': ("Cyprus", 28),
     'CZ': ("Czech Republic", 24),
     'DK': ("Denmark", 18),
     'DO': ("Dominican Republic", 28),
     'TL': ("East Timor", 23),
     'EG': ("Egypt", 29),
     'SV': ("El Salvador", 28),
     'EE': ("Estonia", 20),
     'FO': ("Faroe Islands", 18),
     'FI': ("Finland", 18),
     'FR': ("France", 27),
     'GE': ("Georgia", 22),
     'DE': ("Germany", 22),
     'GI': ("Gibraltar", 23),
     'GR': ("Greece", 27),
     'GL': ("Greenland", 18),
     'GT': ("Guatemala", 28),
     'HU': ("Hungary", 28),
     'IS': ("Iceland", 26),
     'IQ': ("Iraq", 23),
     'IE': ("Ireland", 22),
     'IL': ("Israel", 23),
     'IT': ("Italy", 27),
     'JO': ("Jordan", 30),
     'KZ': ("Kazakhstan", 20),
     'XK': ("Kosovo", 20),
     'KW': ("Kuwait", 30),
     'LV': ("Latvia", 21),
     'LB': ("Lebanon", 28),
     'LY': ("Libya", 25),
     'LI': ("Liechtenstein", 21),
     'LT': ("Lithuania", 20),
     'LU': ("Luxembourg", 20),
     'MK': ("North Macedonia", 19),
     'MT': ("Malta", 31),
     'MR': ("Mauritania", 27),
     'MU': ("Mauritius", 30),
     'MC': ("Monaco", 27),
     'MD': ("Moldova", 24),
     'ME': ("Montenegro", 22),
     'NL': ("Netherlands", 18),
     'NO': ("Norway", 15),
     'PK': ("Pakistan", 24),
     'PS': ("Palestinian territories", 29),
     'PL': ("Poland", 28),
     'PT': ("Portugal", 25),
     'QA': ("Qatar", 29),
     'RO': ("Romania", 24),
     'RU': ("Russia", 29),
     'LC': ("Saint Lucia", 32),
     'SM': ("San Marino", 27),
     'ST': ("São Tomé and Príncipe", 25),
     'SA': ("Saudi Arabia", 24),
     'RS': ("Serbia", 22),
     'SC': ("Seychelles", 31),
     'SK': ("Slovakia", 24),
     'SI': ("Slovenia", 19),
     'ES': ("Spain", 24),
     'SD': ("Sudan", 18),
     'SE': ("Sweden", 24),
     'CH': ("Switzerland", 21),
     'TN': ("Tunisia", 24),
     'TR': ("Turkey", 26),
     'UA': ("Ukraine", 29),
     'AE': ("United Arab Emirates", 23),
     'GB': ("United Kingdom", 22),
     'VA': ("Vatican City", 22),
     'VG': ("British Virgin Islands", 24)
}


def check_iban(iban):
     pass
