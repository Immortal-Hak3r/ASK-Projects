# Maklumat yang dimasukan oleh pengguna

jum_belian = float(input("1. Masukan jumlah belian: RM "))
kad = input("2. Adakah tempoh sah laku kad masih sah? Jawab YA atau TIDAK: ")
mata_ganjaran = int(input("3. Semak dan masukkan mata ganjaran kad anda: "))

# Tentukan tempoh sah laku kad
if kad == "YA":
    if mata_ganjaran == "0":
        exit
    elif mata_ganjaran >= 100:
        print ("\nDiskaun ialah 20%")
        bayar = jum_belian * 0.80
        print ("Jumlah yang perlu dibayar ialah RM", round(bayar,2))
    elif mata_ganjaran >= 50:
        print ("\nDiskaun ialah 15%")
        bayar = jum_belian * 0.85
        print ("Jumlah yang perlu dibayar ialah RM", round(bayar,2))
    elif mata_ganjaran <50:
        print ("\nDiskaun ialah 10%")
        bayar = jum_belian * 0.90
        print ("Jumlah yang perlu dibayar ialah RM", round(bayar,2))
    else:
        print ("\nSila semak dan masukan mata ganjaran kad anda dengan betul.")
elif kad == "TIDAK":
    exit
else:
    print ("\nTempoh sah laku kad tidak dapt ditentukan.")
