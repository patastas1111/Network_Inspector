import os.path
import socket
import telnetlib
import time
import configparser
import socket
conf = configparser.ConfigParser()

class guangda():
    def __init__(self, host):
        self.host = host

    def search(self, search_data):
        host_name = self.host.replace(".", "_")
        conf.read("authconf.ini")
        HOST = self.host
        password = conf.get(f'guangda', 'password').strip('"')
        password2 = "admin"
        filedir = f"tmp/guangda{host_name}.txt"
        found = False
        try:
            tn = telnetlib.Telnet(HOST)
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"en\n")
            tn.read_until(b"Password: ")
            tn.write(password2.encode('ascii') + b"\n")
            time.sleep(1)
            tn.write("show onu using".encode('ascii') + b"\n")
            # tn.write("show sla".encode('ascii') + b"\n")
            time.sleep(1)
            with open(filedir, "w") as file_write:
                pass
            while True:
                response = tn.read_very_eager().decode('utf-8', 'ignore')
                if "---MORE---" in response:
                    tn.write(" ".encode('ascii'))
                    # print(response)
                    with open(filedir, "a+") as file_write:
                        file_write.write(f"\n{response}")
                else:
                    break
                time.sleep(1)
            # print(response)
            with open(filedir, "a") as file_write:
                file_write.write(f"{response}")
            tn.write("exit".encode('ascii') + b"\n")
            time.sleep(1)
            tn.write("exit".encode('ascii') + b"\n")
            str_all = tn.read_all().decode('ascii')
            time.sleep(1)
            # print(str_all)
            with open(filedir, "a") as file_write:
                file_write.write(str_all)
            tn.close()
            time.sleep(1)
            word = search_data
            filename = filedir

            with open(filename, "r") as file:
                for line_num, line in enumerate(file):
                    if word in line:
                        #print(f"Line {line_num}: {line}")
                        print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                        found = True
            if not found:
                print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")
        except socket.gaierror:
            print("\033[1;31;40m Hostname/IP address could not be resolved. \033[1;37;40m")
        except socket.error:
            print("\033[1;31;40m Could not connect to remote server, it will use the existing data gathered \033[1;37;40m")
            time.sleep(1)
            word = search_data
            filename = filedir

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line_num, line in enumerate(file):
                        if word in line:
                            # print(f"Line {line_num}: {line}")
                            print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                            found = True
                if not found:
                    print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")
            else:
                print("\033[1;31;40m No Existing Data Detected!\033[1;37;40m")
        except EOFError:
            print("\033[1;31;40m Telnet Connection Closed Unexpectedly \033[1;37;40m")
        except OSError as e:
            print(f"\033[1;31;40m OS error:{e} \033[1;37;40m")
        except KeyboardInterrupt:
            print(" \033[1;31;40m Program Interrupted \033[1;37;40m")
    def icmp_fail(self, search_data):

        host_name = self.host.replace(".", "_")
        filedir = f"tmp/guangda{host_name}.txt"
        found = False

        time.sleep(1)
        word = search_data
        filename = filedir

        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line_num, line in enumerate(file):
                    if word in line:
                        # print(f"Line {line_num}: {line}")
                        print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                        found = True
            if not found:
                print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")

class vsol():
    def __init__(self, host):
        self.host = host

    def search(self, search_data):
        #print(search_data)
        host_name = self.host.replace(".", "_")
        conf.read("authconf.ini")
        HOST = self.host
        timeout = 10
        username = conf.get(f'vsol', 'username').strip('"')
        password = conf.get(f'vsol', 'password').strip('"')
        password2 = conf.get(f'vsol', 'password_en').strip('"')
        filedir = f"tmp/vsol{host_name}.txt"
        found = False
        try:
            tn = telnetlib.Telnet(HOST)
            tn.get_socket().settimeout(timeout)
            tn.read_until(b"Login: ")
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"en\n")
            tn.read_until(b"Password: ")
            tn.write(password2.encode('ascii') + b"\n")
            time.sleep(1)
            tn.write("configure terminal".encode('ascii') + b"\n")
            time.sleep(1)
            tn.write("show onu auth-info all".encode('ascii') + b"\n")
            # tn.write("show sla".encode('ascii') + b"\n")
            time.sleep(1)
            with open(filedir, "w") as file_write:
                pass
            while True:
                response = tn.read_very_eager().decode('utf-8', 'ignore')
                if "--More--" in response:
                    tn.write(" ".encode('ascii'))
                    #print(response)
                    with open(filedir, "a+") as file_write:
                        file_write.write(f"\n{response}")
                else:
                    break
                time.sleep(1)
            #print(response)
            with open(filedir, "a") as file_write:
                file_write.write(f"{response}")
            tn.write("exit".encode('ascii') + b"\n")
            time.sleep(1)
            tn.write("exit".encode('ascii') + b"\n")
            time.sleep(1)
            tn.write("exit".encode('ascii') + b"\n")
            str_all = tn.read_all().decode('ascii')
            time.sleep(1)
            #print(str_all)
            with open(filedir, "a") as file_write:
                file_write.write(str_all)
            tn.close()
            time.sleep(1)
            word = search_data
            filename = filedir

            with open(filename, "r") as file:
                for line_num, line in enumerate(file):
                    if word in line:
                        #print(f"Line {line_num}: {line}")
                        print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                        found = True
            if not found:
                print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")
        except socket.gaierror:
            print("\033[1;31;40m Hostname/IP address could not be resolved. \033[1;37;40m")
        except socket.error:
            print("\033[1;31;40m Could not connect to remote server, it will use the existing data gathered \033[1;37;40m")
            time.sleep(1)
            word = search_data
            filename = filedir

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line_num, line in enumerate(file):
                        if word in line:
                            # print(f"Line {line_num}: {line}")
                            print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                            found = True
                if not found:
                    print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")
            else:
                print("\033[1;31;40m No Existing Data Detected!\033[1;37;40m")
        except EOFError:
            print("\033[1;31;40m Telnet Connection Closed Unexpectedly \033[1;37;40m")
        except OSError as e:
            print(f"\033[1;31;40m OS error:{e} \033[1;37;40m")
        except KeyboardInterrupt:
            print(" \033[1;31;40m Program Interrupted \033[1;37;40m")
    def icmp_fail(self, search_data):

        host_name = self.host.replace(".", "_")
        filedir = f"tmp/guangda{host_name}.txt"
        found = False

        time.sleep(1)
        word = search_data
        filename = filedir

        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line_num, line in enumerate(file):
                    if word in line:
                        # print(f"Line {line_num}: {line}")
                        print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                        found = True
            if not found:
                print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")


class richerlink():
    def __init__(self, host):
        self.host = host

    def search(self, search_data):
        #print(search_data)
        host_name = self.host.replace(".", "_")
        conf.read("authconf.ini")
        HOST = self.host
        timeout = 10
        username = conf.get(f'richerlink', 'username').strip('"')
        password = conf.get(f'richerlink', 'password').strip('"')
        password2 = conf.get(f'richerlink', 'password_en').strip('"')
        filedir = f"tmp/richerlink{host_name}.txt"
        found = False
        try:
            tn = telnetlib.Telnet(HOST)
            tn.get_socket().settimeout(timeout)

            tn.read_until(b"Username:")
            tn.write(username.encode('ascii') + b"\n")

            tn.read_until(b"Password:")
            tn.write(password.encode('ascii') + b"\n")

            tn.write(b"en\n")
            tn.read_until(b"Password:")
            tn.write(password2.encode('ascii') + b"\n")
            time.sleep(1)

            tn.write("show mac-address-table".encode('ascii') + b"\n")
            time.sleep(1)
            with open(filedir, "w") as file_write:
                pass
            while True:
                response = tn.read_very_eager().decode('utf-8', 'ignore')
                if "--More--" in response:
                    tn.write(" ".encode('ascii'))
                    #print(response)
                    with open(filedir, "a+") as file_write:
                        file_write.write(f"\n{response}")
                else:
                    break
                time.sleep(1)
            #print(response)
            with open(filedir, "a") as file_write:
                file_write.write(f"{response}")
            tn.write("exit".encode('ascii') + b"\n")
            time.sleep(1)
            str_all = tn.read_all().decode('ascii')
            time.sleep(1)
            #print(str_all)
            with open(filedir, "a") as file_write:
                file_write.write(str_all)
            tn.close()
            time.sleep(1)
            word = search_data
            filename = filedir

            with open(filename, "r") as file:
                for line_num, line in enumerate(file):
                    if word in line:
                        #print(f"Line {line_num}: {line}")
                        print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                        found = True
            if not found:
                print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")
        except socket.gaierror:
            print("\033[1;31;40m Hostname/IP address could not be resolved. \033[1;37;40m")
        except socket.error:
            print("\033[1;31;40m Could not connect to remote server, it will use the existing data gathered \033[1;37;40m")
            time.sleep(1)
            word = search_data
            filename = filedir

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line_num, line in enumerate(file):
                        if word in line:
                            print(f" '-> \033[1;33;40m {line} \033[1;37;40m")
                            found = True
                if not found:
                    print(" '-> \033[1;32;40m Cannot found on this olt \033[1;37;40m")
            else:
                print("\033[1;31;40m No Existing Data Detected!\033[1;37;40m")
        except EOFError:
            print("\033[1;31;40m Telnet Connection Closed Unexpectedly \033[1;37;40m")
        except OSError as e:
            print(f"\033[1;31;40m OS error:{e} \033[1;37;40m")
        except KeyboardInterrupt:
            print(" \033[1;31;40m Program Interrupted \033[1;37;40m")
