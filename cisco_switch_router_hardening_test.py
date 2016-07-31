#!/usr/bin/python
#arguman alma

import re

import sys			#import library for input argument

print sys.argv[1]		#for debug
option = sys.argv[2]
input_file = sys.argv[1]	#assign argument to input_file variable
f = open(input_file, "r")	#open the file ..... by argument

output_file = open("SonucRaporu.txt", "w")
n=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
f = open(input_file, "r")	#open the file ..... by argument

for line in f:
	if "line con 0" in line:
		if "password" in f.next():
			output_file.write("Konsol parolasi eklenmis\n")
			n=n+1
			a=1
						
			
f = open(input_file, "r")	#open the file ..... by argument

for line2 in f:
	if "line vty" in line2:
		if "password" in f.next():
			output_file.write("Uzaktan yonetim parolasi eklenmis\n")
			n=n+1
			b=1

			
f = open(input_file, "r")	#open the file ..... by argument

for line3 in f:
	if "switchport port-security" in line3:
			output_file.write("Port security uygulanmis\n")
			c=1
if c>0:
	n=n+1
			
f = open(input_file, "r")	#open the file ..... by argument
		
if option == "switch":
	print "switch secildi"
	for line in f:
		if "banner motd" in line:
			output_file.write("Banner eklenmis\n")
			n=n+1
			d=1
		if "enable secret" in line:
			output_file.write("Enable parolasi eklenmis\n")
			n=n+1
			e=1
		if "service password-encryption" in line:
			output_file.write("Parolalar sifrelenmis\n")
			n=n+1
			f=1
		if "exec-timeout" in line:
			output_file.write("Zaman asimi uygulanmis\n")
			n=n+1
			g=1
		if "transport input ssh" in line:
			output_file.write("SSH aktif edilmis\n")
			n=n+1
			h=1
	output_file.write("\n\n")
	if a==0:
		output_file.write("Konsol parolasi eklenmemis\n")
	if b==0:
		output_file.write("Uzaktan yonetim parolasi eklenmemis\n")
	if c==0:
		output_file.write("Port security uygulanmamis\n")
	if d==0:
		output_file.write("Banner eklenmemis\n")
	if e==0:
		output_file.write("Enable parolasi eklenmemis\n")
	if f==0:
		output_file.write("Parolalar sifrelenmemis\n")
	if g==0:
		output_file.write("Zaman asimi uygulanmamis\n")
	if h==0:
		output_file.write("SSH aktif edilmemis\n")

	
	sonuc=12.5*n
	output_file.write("CIHAZ DEGERLENDIRME SONUCU:\t")
	output_file.write(repr(sonuc))

if option == "router":
	print "router secildi"
	for line in f:
		if "banner motd" in line:
			output_file.write("Banner eklenmis\n")
			n=n+1
			d=1
		if "enable secret" in line:
			output_file.write("Enable parolasi eklenmis\n")
			n=n+1
			e=1
		if "service password-encryption" in line:
			output_file.write("Parolalar sifrelenmis\n")
			n=n+1
			f=1
		if "exec-timeout" in line:
			output_file.write("Zaman asimi uygulanmis\n")
			n=n+1
			g=1
		if "transport input ssh" in line:
			output_file.write("SSH aktif edilmis\n")
			n=n+1
			h=1
		if "ntp" in line:
			output_file.write("NTP aktif edilmis\n")
			n=n+1	
			c=1
	if a==0:
		output_file.write("Konsol parolasi eklenmemis\n")
	if b==0:
		output_file.write("Uzaktan yonetim parolasi eklenmemis\n")
	if c==0:
		output_file.write("NTP aktif edilmemis\n")
	if d==0:
		output_file.write("Banner eklenmemis\n")
	if e==0:
		output_file.write("Enable parolasi eklenmemis\n")
	if f==0:
		output_file.write("Parolalar sifrelenmemis\n")
	if g==0:
		output_file.write("Zaman asimi uygulanmamis\n")
	if h==0:
		output_file.write("SSH aktif edilmemis\n")
		
	sonuc=12.5*n
	output_file.write("CIHAZ DEGERLENDIRME SONUCU:\t")
	output_file.write(repr(sonuc))

