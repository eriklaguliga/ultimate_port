import socket
import xlrd

def ambil_data(banyak_ip,port):
    ip_list = []
    workbook = xlrd.open_workbook('data_port.xlsx')
    worksheet = workbook.sheet_by_name('Sheet1')
    i = 1
    while(i <= banyak_ip):
        ip_list.append(worksheet.cell_value(i, 1))
        i = i + 1
    run(ip_list,port)

def report(hasil, nama_file):
    f = open(nama_file, 'w')
    for i in range(len(hasil)):
        f.write(str(hasil[i]))
        f.write("\n")
    f.close()
    print("report anda sudah dibuat")


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


def udpscan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


def Print(hasil):
    print("apakah perlu outputnya dijadikan format excel: ?")


def run(ip, port):
    ipp = []
    pport = []
    hasil_1 = []
    for i in range(len(ip)):
        try:
            print("                        ")
            hostname = socket.gethostbyaddr(ip[i])
            host_to_str = str(hostname)
            wow = host_to_str.split(",")[0]
            ipp.append(ip[i])
            ke_rep = "Scanning for ip ", ip[i], "with hostname ", wow.replace('(', '')
            hasil_1.append(ke_rep)
            print("Scanning for ip ", ip[i], "with hostname ", wow.replace('(', ''))
        except:
            print("                        ")
            print("can't find hostname value, but still scanning for ip: ", ip[i])
            b = "can't find hostname value, but still scanning for ip: ", ip[i]
            hasil_1.append(b)
        for o in range(len(port)):
            pport.append(port[o])
            if isOpen(ip[i], port[o]) == True:
                print("TCP port", port[o], ": Listening")
                hasil_2 = "TCP port", port[o], ": Listening"
                hasil_1.append(hasil_2)
            else:
                try:
                    sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    hasil = sv.connect_ex((ip[i], port[o]))
                    if (hasil == 10061):
                        print("TCP port", port[o], ": Not Listening")
                        hasil_2 = "TCP port", port[o], ": Not Listening"
                        hasil_1.append(hasil_2)

                    elif (hasil == 10060):
                        print("TCP port", port[o], ": Filtered")
                        hasil_2 = "TCP port", port[o], ": Filtered"
                        hasil_1.append(hasil_2)
                    else:
                        print("your host is unreach")
                        hasil_2 = "Unreach"
                        hasil_1.append(hasil_2)

                except:
                    print("Too many attempt, maybe your request has been block by firewall or bad ip input")
    print("                       ")
    txt = input("apakah hasil uji mau disimpan? (ya/tidak) : ")

    if (txt == "ya"):
        try:
            nama_file = input("tulikan nama file yang akan jadi report? contoh (report.txt) : ")
            report(hasil_1, nama_file)
        except:
            print("nama file harus diakhiri dengan .txt")
    elif (txt == "tidak"):
        pass
    else:
        print("error")


def run_udp(ip, port):
    for i in range(len(ip)):
        try:
            print("                        ")
            hostname = socket.gethostbyaddr(ip[i])
            host_to_str = str(hostname)
            wow = host_to_str.split(",")[0]
            print("Scanning for ip ", ip[i], "with hostname ", wow.replace('(', ''))
        except:
            print("                        ")
            print("can't find hostname value, but still scanning for ip: ", ip[i])
        for o in range(len(port)):
            if udpscan(ip[i], port[o]) == True:
                print("UDP port", port[o], ": Listening")
            else:
                try:
                    sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    hasil = sv.connect_ex((ip[i], port[o]))
                    if (hasil == 10061):
                        print("UDP port", port[o], ": Not Listening")
                    elif (hasil == 10060):
                        print("UDP port", port[o], ": Filtered")
                    else:
                        print("your host is unreach")
                except:
                    print("Too many attempt, maybe your request has been block by firewall, bad ip input")


print(
    "=========================================================================================================================================================")
print(
    "                                                                 Cek Port                                                                                ")
print(
    "=========================================================================================================================================================")
print("Port-port yang digunakan pada agent")
print(
    "1.Port 4118 (From Manager to Agent/Appliance) : Manager-to Agent/Appliance-communication. Agent/Appliance's listening port.")
print(
    "2. Port 4120 (From Agent/Appliance to Manager): The heartbeat port, used by Deep Security Agents and Appliances to communicate with the Deep Security Manager.")
print(
    "3. Port 80/443 (Outgoing): Connection to Global Web Reputation Server,Global File Reputation Server and Local File Reputation Server")
print("                                                                                            ")
print("Port-port yang digunakan pada Relay")
print("1. Port 4118 (From Manager to the Relay): Deep Security Manager sends commands to Deep Security Relay.")
print(
    "2. Port 4122 (From Manager/Agent to the Relay) : Relay listening port. Manager to Relay communication for retrieving components, and Agent/Appliance retrieve updatable components")
print("3. Port 80 and 443 (From Relay to Internet) : 	iAU Security Updates")
print("                                                                                            ")
print("Penjelsakan output port:")
print("1. Listening: Port tersebut buka dan service pada applikasi yang menggunakan port tersebut sendang jalan")
print(
    "2. Not Listening: Port tersebut buka tapi service pada applikasi yang menggunakan port tersebut sendang tidak jalan")
print("3. filtered: Port tersebut kemeungkinan diblock oleh firewall")
print("                                                                                            ")
print("                                                                                           ")
print("                                                                                                  ")
print("1. Ambil data IP dari data_port.xlsx ")
print("2. Masukan IP secara manual")

value_input = int(input("Masukkan pilihan anda:  "))
if value_input == 1:
    many_ip = (int(input("Banyak IP yg ada di file data_port:  ")))
    banyak_port = (int(input("Banyak port yang ingin di cek:  ")))
    print("                                                          ")
    port = []
    for i in range(banyak_port):
        port_ = (int(input("port :")))
        port.append(port_)
    ambil_data(many_ip,port)
elif value_input == 2:
    try:
        ip = list(input("Enter a multiple ip or single ip: ").split(","))
        print("                                                      ")
        port = list(map(int, input("Enter a multiple port or single port: ").split(",")))
        print("                                                          ")
        run(ip, port)
    except:
        print("masukkan data yang benar!")
else:
    print("masukkan input value dengan benar!")









