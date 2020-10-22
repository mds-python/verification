# Verification Algorithms

## Credit Card Verification

Credit cards numbers are verified using the Luhn formula. The formula verifies a number against its included check digit, which is usually appended to a partial account number to generate the full account number. This number must pass the following test:

1. From the **rightmost** digit, which is the check digit, and moving left, double the value of every second digit. If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then add the digits of the product (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, alternatively, the same result can be found by subtracting 9 from the product (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).
2. Take the sum of all the digits.
3. If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.

Assume an example of a card number "79927398713":

| Digit index         |  10 |      9 |   8 |     7 |   6 |     5 |   4 |      3 |   2 |     1 |   0 |
|---------------------|----:|-------:|----:|------:|----:|------:|----:|-------:|----:|------:|----:|
| Card number         |   7 |    9   |   9 |   2   |   7 |   3   |   9 |    8   |   7 |   1   |   3 |
| Double every second |   7 | **18** |   9 | **4** |   7 | **6** |   9 | **16** |   7 | **2** |   3 |
| Sum digits          |   7 |    9   |   9 |   4   |   7 |   6   |   9 |    7   |   7 |   2   |   3 |

The sum of all the digits in the third row is 70, which means the card number is valid (70 module 10 is 0).

### Your task (`card.py`)

Write a function `check_card(number)` that implements the following algorithm and returns `True` of `False` indicating if the card number is correct.

Use it to verify your credit card number. You may also check the correctness of the following numbers: `79927398710`, `79927398711`, `79927398712`, `79927398713`, `79927398714`, `79927398715`, `79927398716`, `79927398717`, `79927398718`, `79927398719`.


## International Bank Account Number (IBAN) Verification

The International Bank Account Number (IBAN) is an internationally agreed system of identifying bank accounts across national borders to facilitate the communication and processing of cross border transactions with a reduced risk of transcription errors. It uniquely identifies the account of a customer at a financial institution. The IBAN consists of up to 34 alphanumeric characters comprising a country code; two check digits; and a number that includes the domestic bank account number, branch identifier, and potential routing information. The check digits enable a check of the bank account number to confirm its integrity before submitting a transaction.

An IBAN is validated by converting it into an integer and performing a basic mod-97 operation (as described in ISO 7064) on it. If the IBAN is valid, the remainder equals 1. The algorithm of IBAN validation is as follows:

1. Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
2. Move the four initial characters to the end of the string
3. Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11, ..., Z = 35
4. Interpret the string as a decimal integer and compute the remainder of that number on division by 97

If the remainder is 1, the check digit test is passed and the IBAN might be valid.

Example (fictitious United Kingdom bank, sort code 12-34-56, account number 98765432):

1. IBAN: `GB82 WEST 1234 5698 7654 32` (GB for United Kingdom, length 22)
2. Rearrange: `WEST12345698765432GB82`
3. Convert to integer: `3214282912345698765432161182`
4. Compute remainder: `3214282912345698765432161182` modulo `97` = `1`

The table below shows a list of countries using IBAN, with their country code and number of characters:

| Country                 | Chars | Code |   | Country                 | Chars | Code |
| ----------------------- | ----- | ---- | - | ----------------------- | ----- | ---- |
| Albania                 | 28    | AL   |   | Lebanon                 | 28    | LB   |
| Andorra                 | 24    | AD   |   | Libya                   | 25    | LY   |
| Austria                 | 20    | AT   |   | Liechtenstein           | 21    | LI   |
| Azerbaijan              | 28    | AZ   |   | Lithuania               | 20    | LT   |
| Bahrain                 | 22    | BH   |   | Luxembourg              | 20    | LU   |
| Belarus                 | 28    | BY   |   | North Macedonia         | 19    | MK   |
| Belgium                 | 16    | BE   |   | Malta                   | 31    | MT   |
| Bosnia and Herzegovina  | 20    | BA   |   | Mauritania              | 27    | MR   |
| Brazil                  | 29    | BR   |   | Mauritius               | 30    | MU   |
| Bulgaria                | 22    | BG   |   | Monaco                  | 27    | MC   |
| Costa Rica              | 22    | CR   |   | Moldova                 | 24    | MD   |
| Croatia                 | 21    | HR   |   | Montenegro              | 22    | ME   |
| Cyprus                  | 28    | CY   |   | Netherlands             | 18    | NL   |
| Czech Republic          | 24    | CZ   |   | Norway                  | 15    | NO   |
| Denmark                 | 18    | DK   |   | Pakistan                | 24    | PK   |
| Dominican Republic      | 28    | DO   |   | Palestinian territories | 29    | PS   |
| East Timor              | 23    | TL   |   | Poland                  | 28    | PL   |
| Egypt                   | 29    | EG   |   | Portugal                | 25    | PT   |
| El Salvador             | 28    | SV   |   | Qatar                   | 29    | QA   |
| Estonia                 | 20    | EE   |   | Romania                 | 24    | RO   |
| Faroe Islands           | 18    | FO   |   | Russia                  | 29    | RU   |
| Finland                 | 18    | FI   |   | Saint Lucia             | 32    | LC   |
| France                  | 27    | FR   |   | San Marino              | 27    | SM   |
| Georgia                 | 22    | GE   |   | São Tomé and Príncipe   | 25    | ST   |
| Germany                 | 22    | DE   |   | Saudi Arabia            | 24    | SA   |
| Gibraltar               | 23    | GI   |   | Serbia                  | 22    | RS   |
| Greece                  | 27    | GR   |   | Seychelles              | 31    | SC   |
| Greenland               | 18    | GL   |   | Slovakia                | 24    | SK   |
| Guatemala               | 28    | GT   |   | Slovenia                | 19    | SI   |
| Hungary                 | 28    | HU   |   | Spain                   | 24    | ES   |
| Iceland                 | 26    | IS   |   | Sudan                   | 18    | SD   |
| Iraq                    | 23    | IQ   |   | Sweden                  | 24    | SE   |
| Ireland                 | 22    | IE   |   | Switzerland             | 21    | CH   |
| Israel                  | 23    | IL   |   | Tunisia                 | 24    | TN   |
| Italy                   | 27    | IT   |   | Turkey                  | 26    | TR   |
| Jordan                  | 30    | JO   |   | Ukraine                 | 29    | UA   |
| Kazakhstan              | 20    | KZ   |   | United Arab Emirates    | 23    | AE   |
| Kosovo                  | 20    | XK   |   | United Kingdom          | 22    | GB   |
| Kuwait                  | 30    | KW   |   | Vatican City            | 22    | VA   |
| Latvia                  | 21    | LV   |   | British Virgin Islands  | 24    | VG   |

### Your task (`iban.py`)

Write a function `check_iban(number)` that implements the above algorithm and returns `True` of `False` indicating if the bank account number is correct. The function must take a full IBAN (in a string) as its argument. This string may contain arbitrary spaces to increase legibility. These spaces must be discarded. This function must return false if the checksum is wrong or the IBAN length is incorrect or the country coderefers to non-existing country.

Use it to verify your bank account number (please note that in Poland the country prefix `PL` is usually skipped, so you must remember to add it).


## PESEL Checksum Calculation

**PESEL** is the national identification number used in Poland since 1979.

Having a PESEL in the form of *abcdefghijk*, one can check the validity of the number by computing the following expression:

1×*a* + 3×*b* + 7×*c* + 9×*d* + 1×*e* + 3×*f* + 7×*g* + 9×*h* + 1×*i* + 3×*j*

Then the last digit of the result should be subtracted from 10. If the result of the last operation is not equal to the last digit of a given PESEL, the PESEL is incorrect. This system works reliably well for catching one-digit mistakes and digit swaps.

Checking validity of PESEL: 44051401358 (number 8, the last digit, is the check digit for this PESEL):

    1×4 + 3×4 + 7×0 + 9×5 + 1×1 + 3×4 + 7×0 + 9×1 + 1×3 + 3×5 = 101

Getting the last digit of the result (101 % 10):

101 % 10 = 1

In order to get the check digit one need to take the 10s complement of the number. It is 0 if the modulo result is 0, and it is 5 when the modulo is equal to 5, otherwise it means the modulo result has to be subtracted from 10.

10 - 1 = 9

9 is not equal to the last digit of PESEL, which is 8, so the PESEL contains errors.

### Date of birth

PESEL also a encodes birthdate. It is stored in the first six digits os the number in the form  `YYMMDDxxxxxx`, where YYMMDD is the date of birth (with century encoded in month field). The PESEL system has been designed to cover five centuries. To distinguish people born in different centuries, numbers are added to the MM field:

- for birthdates between **1900** and **1999**: no change to `MM` field is made
- for other birthdates:
  - **2000–2099**: *month* field number is increased by 20
  - **2100–2199**: *month* + 40
  - **2200–2299**: *month* + 60
  - **1800–1899**: *month* + 80

For example, a person born on *December 24, 2002* would have a PESEL number starting with `023224` and person born on *December 24, 1902* would have a PESEL number starting with `021224`.

### Your task (`pesel.py`)

1. Write a function `check_pesel` that will verify the PESEL number and the date of birth of the person identified by this number.

   The function is supposed to take the PESEL number as a text string and return:

   - None if PESEL is incorrect (either wrong checksum or too short or too long)
   - date of birth in the format `September 5, 1971` if the PESEL number is correct

2. Write the function `check_pesel_file`, which takes the file name as an argument and reads PESEL numbers from this file
   (one on each line). The function must create a file with the same name as the original file name
   with the extension changed to `.out`, containing each line of the person's date of birth, or the sign "-"
   in the case of an incorrect PESEL number.

   For example, calling `check_pesel_file("pesels.txt")` will create the file `pesels.out`. If the file `pesels.txt` contains

        90090515836
        87832165581

   This `pesels.out` will be as follows:

        September 5, 1990
        -

   It is worth considering how to use the function from the first point.
