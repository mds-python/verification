# coding: utf8
import os

import unittest

try: import card
except: pass

try: import pesel
except: pass

try: import iban
except: pass


class TestPESEL(unittest.TestCase):

    def test_pesel_correct_20th_century(self):
        self.assertRegex(pesel.check_pesel('90090515836'), 'September 0?5, 1990')

    def test_pesel_correct_21st_century(self):
        self.assertEqual(pesel.check_pesel('01261051813'), 'June 10, 2001')

    def test_pesel_correct_19th_century(self):
        self.assertEqual(pesel.check_pesel('87832165181'), 'March 21, 1887')

    def test_pesel_incorrect(self):
        self.assertIsNone(pesel.check_pesel('90090525836'))
        self.assertIsNone(pesel.check_pesel('01261031813'))
        self.assertIsNone(pesel.check_pesel('87832165581'))

    def test_pesel_too_short(self):
        self.assertIsNone(pesel.check_pesel('123456789'))

    def test_pesels_in_file(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        infilename = os.path.join(directory, 'data.txt')
        with open(infilename, 'w') as infile:
            infile.write("90090515836\n87832165181\n01261031813\n01261051813\n123456789\n")
        pesel.check_pesel_file(infilename)
        try:
            with open(os.path.join(directory, 'data.out')) as outfile:
                answer = [line.rstrip() for line in outfile.readlines()]
            correct = ['September 0?5, 1990', 'March 21, 1887', '-', 'June 10, 2001', '-']
            for i in range(5):
                self.assertRegex(answer[i], correct[i])
        except FileNotFoundError:
            self.fail("File not found")


class TestCard(unittest.TestCase):

    def test_card_correct_16_digits(self):
        self.assertTrue(card.check_card('4929134138580797'))
        self.assertTrue(card.check_card('4152651010436721'))
        self.assertTrue(card.check_card('4539667947868665'))
        self.assertTrue(card.check_card('4024007164776170'))
        self.assertTrue(card.check_card('4485154991816266'))
        self.assertTrue(card.check_card('5443972305885927'))
        self.assertTrue(card.check_card('5114869172331548'))
        self.assertTrue(card.check_card('5578916533101687'))
        self.assertTrue(card.check_card('5406733474061897'))
        self.assertTrue(card.check_card('5419564871798376'))
        self.assertTrue(card.check_card('6011395236301055'))
        self.assertTrue(card.check_card('6011432269128210'))
        self.assertTrue(card.check_card('6011636118723985'))
        self.assertTrue(card.check_card('6011631220718007'))
        self.assertTrue(card.check_card('6011856166915099'))

    def test_card_correct_15_digits(self):
        self.assertTrue(card.check_card('370594756527911'))
        self.assertTrue(card.check_card('379451233726940'))
        self.assertTrue(card.check_card('341377872063524'))
        self.assertTrue(card.check_card('376766310514015'))
        self.assertTrue(card.check_card('375692442227519'))

    def test_card_correct_11_digits(self):
        self.assertTrue(card.check_card('79927398713'))

    def test_card_incorrect(self):
        self.assertFalse(card.check_card('79927398710'))
        self.assertFalse(card.check_card('79927398711'))
        self.assertFalse(card.check_card('79927398712'))
        self.assertFalse(card.check_card('79927398714'))
        self.assertFalse(card.check_card('79927398715'))
        self.assertFalse(card.check_card('79927398716'))
        self.assertFalse(card.check_card('79927398717'))
        self.assertFalse(card.check_card('79927398718'))
        self.assertFalse(card.check_card('79927398719'))


class TestIBAN(unittest.TestCase):

    def test_correct(self):
        self.assertTrue(iban.check_iban("AL35 2021 1109 0000 0000 0123 4567"))
        self.assertTrue(iban.check_iban("AD14 0008 0001 0012 3456 7890"))
        self.assertTrue(iban.check_iban("AT48 3200 0000 1234 5864"))
        self.assertTrue(iban.check_iban("AZ77 VTBA 0000 0000 0012 3456 7890"))
        self.assertTrue(iban.check_iban("BH02 CITI 0000 1077 1816 11"))
        self.assertTrue(iban.check_iban("BY86 AKBB 1010 0000 0029 6600 0000"))
        self.assertTrue(iban.check_iban("BE71 0961 2345 6769"))
        self.assertTrue(iban.check_iban("BA39 3385 8048 0021 1234"))
        self.assertTrue(iban.check_iban("BR15 0000 0000 0000 1093 2840814P2"))
        self.assertTrue(iban.check_iban("BG18 RZBB 9155 0123 4567 89"))
        self.assertTrue(iban.check_iban("CR23 0151 0841 0026 0123 45"))
        self.assertTrue(iban.check_iban("HR17 2360 0001 1012 3456 5"))
        self.assertTrue(iban.check_iban("CY21 0020 0195 0000 3570 0123 4567"))
        self.assertTrue(iban.check_iban("CZ55 0800 0000 0012 3456 7899"))
        self.assertTrue(iban.check_iban("DK95 2000 0123 4567 89"))
        self.assertTrue(iban.check_iban("DO22 ACAU 0000 0000 0001 2345 6789"))
        self.assertTrue(iban.check_iban("EG80 0002 0001 5678 9012 34518 0002"))
        self.assertTrue(iban.check_iban("SV43 ACAT 0000 0000 0000 0012 3123"))
        self.assertTrue(iban.check_iban("EE47 1000 0010 2014 5685"))
        self.assertTrue(iban.check_iban("FO92 6460 0123 4567 89"))
        self.assertTrue(iban.check_iban("FI14 1009 3000 1234 58"))
        self.assertTrue(iban.check_iban("FR76 3000 6000 0112 3456 78901 89"))
        self.assertTrue(iban.check_iban("GE60 NB00 0000 0123 4567 89"))
        self.assertTrue(iban.check_iban("DE75 5121 0800 1245 1261 99"))
        self.assertTrue(iban.check_iban("GI56 XAPO 0000 0123 4567 890"))
        self.assertTrue(iban.check_iban("GR96 0810 0010 0000 0123 4567 890"))
        self.assertTrue(iban.check_iban("GL89 6471 0123 4567 89"))
        self.assertTrue(iban.check_iban("GT20 AGRO 0000 0000 0012 34567 890"))
        self.assertTrue(iban.check_iban("VA59 0011 2300 0012 3456 78"))
        self.assertTrue(iban.check_iban("HU93 1160 0006 0000 0000 1234 5676"))
        self.assertTrue(iban.check_iban("IS75 0001 1212 3456 3108 962099"))
        self.assertTrue(iban.check_iban("IQ20 CBIQ 8618 0010 1010 500"))
        self.assertTrue(iban.check_iban("IE64 IRCE 9205 0112 3456 78"))
        self.assertTrue(iban.check_iban("IL17 0108 0000 0001 2612 345"))
        self.assertTrue(iban.check_iban("IT60 X054 2811 1010 0000 0123 456"))
        self.assertTrue(iban.check_iban("JO71 CBJO 0000 0000 0000 1234 5678 90"))
        self.assertTrue(iban.check_iban("KZ24 4350 0000 1234 4567"))
        self.assertTrue(iban.check_iban("XK05 1212 0123 4567 8906"))
        self.assertTrue(iban.check_iban("KW81 CBKU 0000 0000 0000 1234 5601 01"))
        self.assertTrue(iban.check_iban("LV97 HABA 0012 3456 7891 0"))
        self.assertTrue(iban.check_iban("LB92 0007 0000 0000 1231 2345 6123"))
        self.assertTrue(iban.check_iban("LY38 0210 0100 0000 1234 56789"))
        self.assertTrue(iban.check_iban("LI74 0880 6123 4567 8901 2"))
        self.assertTrue(iban.check_iban("LT60 1010 0123 4567 8901"))
        self.assertTrue(iban.check_iban("LU12 0010 0012 3456 7891"))
        self.assertTrue(iban.check_iban("MT31 MALT 0110 0000 0000 0000 0000 123"))
        self.assertTrue(iban.check_iban("MR13 0002 0001 0100 0012 3456 753"))
        self.assertTrue(iban.check_iban("MU43 BOMM 0101 1234 5678 9101 000 MUR"))
        self.assertTrue(iban.check_iban("MD21 EX00 0000 0000 0123 4567"))
        self.assertTrue(iban.check_iban("MC58 1009 6180 7901 2345 6789 085"))
        self.assertTrue(iban.check_iban("ME25 5050 0001 2345 6789 51"))
        self.assertTrue(iban.check_iban("NL02 ABNA 0123 4567 89"))
        self.assertTrue(iban.check_iban("MK07 2000 0278 5123 453"))
        self.assertTrue(iban.check_iban("NO83 3000 1234 567"))
        self.assertTrue(iban.check_iban("PK36 SCBL 0000 0011 2345 6702"))
        self.assertTrue(iban.check_iban("PS92 PALS 0000 0000 0400 1234 56702"))
        self.assertTrue(iban.check_iban("PL10 1050 0099 7603 1234 5678 9123"))
        self.assertTrue(iban.check_iban("PT50 0027 0000 0001 2345 67833"))
        self.assertTrue(iban.check_iban("QA54 QNBA 0000 0000 0000 6931 23456"))
        self.assertTrue(iban.check_iban("RO66 BACX 0000 0012 3456 7890"))
        self.assertTrue(iban.check_iban("LC14 BOSL 1234 5678 9012 3456 7890 1234"))
        self.assertTrue(iban.check_iban("SM76 P085 4009 8121 2345 6789 123"))
        self.assertTrue(iban.check_iban("ST23 0002 0000 0289 3557 1014 8"))
        self.assertTrue(iban.check_iban("SA44 2000 0001 2345 6789 1234"))
        self.assertTrue(iban.check_iban("RS35 1050 0812 3123 1231 73"))
        self.assertTrue(iban.check_iban("SC74 MCBL 0103 1234 5678 9012 3456 USD"))
        self.assertTrue(iban.check_iban("SK89 7500 0000 0000 1234 5671"))
        self.assertTrue(iban.check_iban("SI56 1920 0123 4567 892"))
        self.assertTrue(iban.check_iban("ES79 2100 0813 6101 2345 6789"))
        self.assertTrue(iban.check_iban("SD88 1112 3456 7890 12"))
        self.assertTrue(iban.check_iban("SE72 8000 0810 3400 0978 3242"))
        self.assertTrue(iban.check_iban("CH56 0483 5012 3456 7800 9"))
        self.assertTrue(iban.check_iban("TL38 0010 0123 4567 8910 106"))
        self.assertTrue(iban.check_iban("TN59 0401 8104 0049 4271 2345"))
        self.assertTrue(iban.check_iban("TR32 0010 0099 9990 1234 56789 0"))
        self.assertTrue(iban.check_iban("UA90 3052 9929 9000 4149 1234 5678 9"))
        self.assertTrue(iban.check_iban("AE46 0090 0000 0012 3456 789"))
        self.assertTrue(iban.check_iban("GB33 BUKB 2020 1555 5555 55"))
        self.assertTrue(iban.check_iban("VG07 ABVI 0000 0001 2345 6789"))

    def test_bad_length(self):
        self.assertFalse(iban.check_iban("LB33 0007 0000 0000 1231 2345"))
        self.assertFalse(iban.check_iban("LY29 0210 0100 0000 1234 5678"))
        self.assertFalse(iban.check_iban("LI86 0880 6123 4567 8901"))
        self.assertFalse(iban.check_iban("LT72 1010 0123 4567 89"))
        self.assertFalse(iban.check_iban("LU41 0010 0012 3456 7891 120"))
        self.assertFalse(iban.check_iban("MT97 MALT 0110 0000 0000 0000 123"))
        self.assertFalse(iban.check_iban("MR02 0002 0001 0100 0012 3456 7534"))
        self.assertFalse(iban.check_iban("MU77 BOMM 0101 1234 5678 9101 000 MURG"))
        self.assertFalse(iban.check_iban("MD90 EX00 0000 0000 0123 4567 1234"))
        self.assertFalse(iban.check_iban("MC58 1009 6180 7901 2345 6789 0850"))
        self.assertFalse(iban.check_iban("ME17 5050 0001 2345 6789"))
        self.assertFalse(iban.check_iban("NL34 ABNA 0123 4567 8912 00"))

    def test_bad_country(self):
        self.assertFalse(iban.check_iban("XX39 0010 0123 4567 8910"))

    def test_bad_checksum(self):
        self.assertFalse(iban.check_iban("NO35 3000 1234 567"))
        self.assertFalse(iban.check_iban("PK14 SCBL 0000 0011 2345 6702"))
        self.assertFalse(iban.check_iban("PS48 PALS 0000 0000 0400 1234 56702"))
        self.assertFalse(iban.check_iban("PL77 1050 0099 7603 1234 5678 9123"))
        self.assertFalse(iban.check_iban("PT02 0027 0000 0001 2345 67833"))
        self.assertFalse(iban.check_iban("QA86 QNBA 0000 0000 0000 6931 23456"))
        self.assertFalse(iban.check_iban("RO71 BACX 0000 0012 3456 7890"))
        self.assertFalse(iban.check_iban("LC39 BOSL 1234 5678 9012 3456 7890 1234"))
        self.assertFalse(iban.check_iban("SM15 P085 4009 8121 2345 6789 123"))
        self.assertFalse(iban.check_iban("ST18 0002 0000 0289 3557 1014 8"))
        self.assertFalse(iban.check_iban("SA23 2000 0001 2345 6789 1234"))
        self.assertFalse(iban.check_iban("RS17 1050 0812 3123 1231 73"))
        self.assertFalse(iban.check_iban("SC21 MCBL 0103 1234 5678 9012 3456 USD"))
        self.assertFalse(iban.check_iban("SK55 7500 0000 0000 1234 5671"))
        self.assertFalse(iban.check_iban("SI95 1920 0123 4567 892"))
        self.assertFalse(iban.check_iban("ES22 2100 0813 6101 2345 6789"))
        self.assertFalse(iban.check_iban("SD80 1112 3456 7890 12"))
        self.assertFalse(iban.check_iban("SE43 8000 0810 3400 0978 3242"))
        self.assertFalse(iban.check_iban("CH47 0483 5012 3456 7800 9"))
        self.assertFalse(iban.check_iban("TL92 0010 0123 4567 8910 106"))
        self.assertFalse(iban.check_iban("TN14 0401 8104 0049 4271 2345"))
        self.assertFalse(iban.check_iban("TR76 0010 0099 9990 1234 56789 0"))
        self.assertFalse(iban.check_iban("UA60 3052 9929 9000 4149 1234 5678 9"))
        self.assertFalse(iban.check_iban("AE75 0090 0000 0012 3456 789"))
        self.assertFalse(iban.check_iban("GB56 BUKB 2020 1555 5555 55"))
        self.assertFalse(iban.check_iban("VG96 ABVI 0000 0001 2345 6789"))
