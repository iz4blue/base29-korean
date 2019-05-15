#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import base29_korean as target


class EncodeTests(unittest.TestCase):
    def test_1자리수_결과를_encode_해본다(self):
        self.assertEqual(target.encode(0), '0')
        self.assertEqual(target.encode(1), '1')
        self.assertEqual(target.encode(9), 'A')
        self.assertEqual(target.encode(28), 'Z')

    def test_2자리수_결과를_encode_해본다(self):
        self.assertEqual(target.encode(29), '10')
        self.assertEqual(target.encode(29 + 1), '11')
        self.assertEqual(target.encode(29*14 + 14), 'GG')


    def test_3자리수_결과를_encode_해본다(self):
        self.assertEqual(target.encode(29*29), '100')
        self.assertEqual(target.encode(29*29*14 + 29*14 + 14), 'GGG')


class DecodeTests(unittest.TestCase):
    def test_1자리수를_decode_해본다(self):
        self.assertEqual(target.decode('0'), 0)
        self.assertEqual(target.decode('1'), 1)
        self.assertEqual(target.decode('A'), 9)
        self.assertEqual(target.decode('B'), 10)
        self.assertEqual(target.decode('Z'), 29 - 1)

    def test_2자리수를_decode_해본다(self):
        self.assertEqual(target.decode('10'), 29)
        self.assertEqual(target.decode('11'), 29 + 1)
        self.assertEqual(target.decode('GG'), 29*14 + 14)

    def test_3자리수를_decode_해본다(self):
        self.assertEqual(target.decode('100'), 29*29)
        self.assertEqual(target.decode('GGG'), 29*29*14 + 29*14 + 14)

    def test_5EeIiLlOoUu이_022111100VV으로_인식되는지(self):
        self.assertEqual(target.decode('5EeIiLlOoUu'), target.decode('022111100VV'))

    def test_V도_U와_같이_인식되는지(self):
        self.assertEqual(target.decode('7U'), target.decode('7V'))

    def test_5Oo도_0와_같이_인식되는지(self):
        self.assertEqual(target.decode('5'), target.decode('0'))
        self.assertEqual(target.decode('O'), target.decode('0'))
        self.assertEqual(target.decode('o'), target.decode('0'))

    def test_Ee도_2로_인식되는지(self):
        self.assertEqual(target.decode('E'), 2)
        self.assertEqual(target.decode('e'), 2)

if __name__ == '__main__':
    unittest.main()
