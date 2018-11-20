#!/bin/sh

openssl dgst -sha256 -out file-bit-49-sha256.txt -hmac "E6775C5EBE92724BB2EA725B8DC6285CD7C05A89" file-bit-49.txt
openssl dgst -sha512 -out file-bit-49-sha512.txt -hmac "E6775C5EBE92724BB2EA725B8DC6285CD7C05A89" file-bit-49.txt
openssl dgst -sha256 -out file-bit-73-sha256.txt -hmac "E6775C5EBE92724BB2EA725B8DC6285CD7C05A89" file-bit-73.txt
openssl dgst -sha512 -out file-bit-73-sha512.txt -hmac "E6775C5EBE92724BB2EA725B8DC6285CD7C05A89" file-bit-73.txt
openssl dgst -sha256 -out file-bit-113-sha256.txt -hmac "E6775C5EBE92724BB2EA725B8DC6285CD7C05A89" file-bit-113.txt
openssl dgst -sha512 -out file-bit-113-sha512.txt -hmac "E6775C5EBE92724BB2EA725B8DC6285CD7C05A89" file-bit-113.txt
