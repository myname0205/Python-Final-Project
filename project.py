import sys  

transaksiList = []
nomorTransaksiList = []
subtotalList = []

def main():
    # Ensure the file is available for writing and start the program
    OpenFile("w")
    DisplayStartingMenu()

def DisplayStartingMenu():
    # Display the main menu and handle user input
    option = input("Silahkan Pilih Menu\n1. Daftar Transaksi Penjualan\n2. Input Data Transaksi Baru\n3. Edit Data Transaksi\n4. Delete Data Transaksi\n5. Exit\nOption:")
    
    if option == "1":
        DaftarTransaksi()
    elif option == "2":
        InputTransaksi()
    elif option == "3":
        EditTransaksi()
    elif option == "4":
        DeleteTransaksi()
    elif option == "5":
        Exit()
    else:
        # Handle invalid input
        print("Input bukan salah satu opsi! Mohon pilih salah satu opsi dibawah")
        DisplayStartingMenu()
    
def DaftarTransaksi():
    # Show the list of transactions if any exist
    if len(transaksiList) == 0:
        print("Belum ada transaksi yang tercatat. Silahkan ketik '2' untuk mencatat transaksi Anda.")
        DisplayStartingMenu()
    else:
        print("\n###DAFTAR TRANSAKSI###")

        subtotalList.clear()  # Reset subtotal list for calculations

        # Loop through transactions and display each one
        for i in transaksiList:
            DisplayTransaksi(i)

        # Calculate and display total sales
        total = sum(subtotalList)
        print("Total: " + str(total))  

        input("Ketik apapun untuk balik ke menu utama")
        DisplayStartingMenu()

def DisplayTransaksi(i):
    # Display transaction details
    print("ID Transaksi: " + i["ID Transaksi"])
    print("Nomor Transaksi: " + i["Nomor Transaksi"])
    print("Nama Produk: " + i["Nama Produk"])
    print("Qty: " + i["Qty"])
    print("Harga: " + i["Harga"])
    
    # Calculate subtotal and append to subtotalList
    subtotal = float(i["Qty"]) * float(i["Harga"])
    subtotalList.append(subtotal)
    print("Subtotal: " + str(subtotal) + "\n")

def InputTransaksi():
    # Input a new transaction
    print("Silahkan input data transaksi")
    transaksiDictionary = {}

    # Input and validate ID Transaksi
    while True:
        idTransaksi = input("ID Transaksi:")
        if CheckValue(idTransaksi, not "", "ID Transaksi tidak boleh kosong!"):
            transaksiDictionary["ID Transaksi"] = idTransaksi
            break  

    # Check and add unique Nomor Transaksi
    nomorTransaksi = CheckNomorTransaksi()
    transaksiDictionary["Nomor Transaksi"] = nomorTransaksi

    # Input and validate Nama Produk
    while True:
        namaProduk = input("Nama Produk:")
        if CheckValue(namaProduk, not "", "Nama Produk tidak boleh kosong!"):
            transaksiDictionary["Nama Produk"] = namaProduk
            break  
                
    # Input and validate Qty
    while True:
        qty = input("Qty:")
        if CheckValue(qty, qty.isdigit(), "Qty harus berupa angka positif!"):
            transaksiDictionary["Qty"] = str(qty)
            break  
            
    # Input and validate Harga
    while True:
        harga = input("Harga:")
        if CheckValue(harga, harga.replace('.', '', 1).isdigit(), "Harga harus berupa angka!"):
            transaksiDictionary["Harga"] = str(harga)
            break 

    # Add transaction to the list and save to file
    transaksiList.append(transaksiDictionary.copy())
    OpenFile("a").write("ID TRANSAKSI: " + idTransaksi + "\n"
               "NOMOR TRANSAKSI: " + nomorTransaksi + "\n" 
               "NAMA PRODUK: " + namaProduk + "\n"
               "QTY: "+ qty + "\n"
               "HARGA: "+ harga + "\n")
    Repeat()

def CheckValue(var, condition, errorMessage):
    # Helper function to validate input
    if condition == True and var != "":
        return True
    else:
        print(errorMessage)
        return False

def CheckNomorTransaksi():
    # Ensure Nomor Transaksi is unique and valid
    nomorTransaksi = input("Nomor Transaksi:") 
    if nomorTransaksi in nomorTransaksiList:
        print("NOMOR TRANSAKSI SUDAH TERCATAT! Silahkan masukan Nomor Transaksi lainnya")
        return CheckNomorTransaksi()
    elif nomorTransaksi == "":
        print("Tidak terdeteksi input. Silahkan masukan Nomor Transaksi yang valid")
        return CheckNomorTransaksi()
    elif nomorTransaksi.isalpha() == True:
        print("ID harus berupa angka. Silahkan masukan Nomor Transaksi yang valid")
        return CheckNomorTransaksi()
    else:
        nomorTransaksiList.append(nomorTransaksi)
        return nomorTransaksi

def Repeat():
    # Prompt the user to repeat or return to the menu
    repeat = input("Apakah Anda ingin menambahkan catatan lain? Y or N\n")
    if repeat == "Y" or repeat == "y":
        InputTransaksi()
    elif repeat == "N" or repeat == "n":
        DisplayStartingMenu()
    else:
        print("Mohon ketik Y atau N untuk mengindikasi pilihan Anda")
        Repeat()

def EditTransaksi():
    # Edit an existing transaction
    pilihan = input("Silahkan masukan Nomor Transaksi data yang ingin DIUBAH (Setelah di enter makan akan muncul detail transaksinya):")
    if pilihan in nomorTransaksiList:
        for transaksi in transaksiList[:]:
            if transaksi["Nomor Transaksi"] == pilihan:
                DisplayTransaksi(transaksi)            
        y = input("Apakah Anda ingin mengedit data tersebut? Y/N\n")
        if y == "Y" or y == "y":
            # Update transaction details
            while True:
                namaProdukBaru = input("Nama Produk (Baru):")
                if CheckValue(namaProdukBaru, not "", "Nama Produk tidak boleh kosong!"):
                    break
            while True:
                qtyBaru = input("Qty (Baru):")
                if CheckValue(qtyBaru, qtyBaru.isdigit(), "Qty harus berupa angka positif!"):
                    break
            while True:
                hargaBaru = input("Harga (Baru):")
                if CheckValue(hargaBaru, hargaBaru.replace('.', '', 1).isdigit(), "Harga harus berupa angka!"):
                    break
            for transaksi in transaksiList[:]:
                if transaksi["Nomor Transaksi"] == pilihan:
                    transaksi["Nama Produk"] = namaProdukBaru
                    transaksi["Qty"] = qtyBaru
                    transaksi["Harga"] = hargaBaru
            RewriteFile()  
            print("Berhasil diedit\n")
            DisplayStartingMenu()
        else:
            DisplayStartingMenu()
    else:
        print("Nomor Transaksi tidak tercatat. Mohon cek lagi input atau input data baru")
        DisplayStartingMenu()

def DeleteTransaksi():
    # Delete an existing transaction
    pilihan = input("Silahkan masukan Nomor Transaksi data yang ingin DIHAPUS (Setelah di enter makan akan muncul detail transaksinya):")
    if pilihan in nomorTransaksiList:
        for transaksi in transaksiList[:]:
            if transaksi["Nomor Transaksi"] == pilihan:
                DisplayTransaksi(transaksi)            
        y = input("Apakah Anda ingin menghapus data tersebut? Y/N\n")
        if y == "Y" or y == "y":
            for transaksi in transaksiList[:]:
                if transaksi["Nomor Transaksi"] == pilihan:
                    transaksiList.remove(transaksi)
                    nomorTransaksiList.remove(pilihan)  
            RewriteFile() 
            print("Berhasil dihapus\n")
            DisplayStartingMenu()
        else:
            DisplayStartingMenu()
    else:
        print("Nomor Transaksi tidak tercatat. Mohon cek lagi input atau input data baru")
        DisplayStartingMenu()

def Exit():
    # Close file and exit the program
    OpenFile("a").close()
    sys.exit()

def OpenFile(mode):
    # Open the file safely in the specified mode
    try:
        file = open(r"E:\data.txt", mode)
        return file
    except IOError as e:
        print(f"Terjadi kesalahan saat mengakses file: {e}")
    except FileNotFoundError as e:
        print(f"File tidak ditemukan: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan yang tidak terduga: {e}")

def RewriteFile():
    # Rewrite the file with updated transaction data
    file = OpenFile("w")
    for transaksi in transaksiList:
        file.write("ID TRANSAKSI: " + transaksi["ID Transaksi"] + "\n")
        file.write("NOMOR TRANSAKSI: " + transaksi["Nomor Transaksi"] + "\n")
        file.write("NAMA PRODUK: " + transaksi["Nama Produk"] + "\n")
        file.write("QTY: " + transaksi["Qty"] + "\n")
        file.write("HARGA: " + transaksi["Harga"] + "\n\n")

if __name__ == "__main__":
    main()
