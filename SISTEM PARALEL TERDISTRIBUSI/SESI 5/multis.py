import socket
import threading
import sys


HOST = '0.0.0.0'  
PORT = 8080
clients = []  
lock = threading.Lock()  

def handle_client(client_socket):
    """Fungsi untuk menangani setiap client di thread terpisah"""
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')  
            if message:  
                print(f"[DEBUG] Pesan diterima dari client: {message} - chat_server.py:17")  
                broadcast(message, client_socket)
            else:
                print("[DEBUG] Pesan kosong diterima, menghentikan loop untuk client ini - chat_server.py:20")
                break  
    except Exception as e:
        print(f"[ERROR] Error pada client: {e} - chat_server.py:23")  
    finally:
        with lock:
            if client_socket in clients:
                clients.remove(client_socket)
                print("[DEBUG] Client dihapus dari list: - chat_server.py:28", client_socket.getpeername())
        try:
            client_socket.close()
            print("[DEBUG] Koneksi client ditutup - chat_server.py:31")
        except Exception as e:
            print(f"[ERROR] Gagal menutup socket: {e} - chat_server.py:33")

def broadcast(message, sender_socket):
    """Broadcast pesan ke semua client kecuali pengirim"""
    with lock:
        for client in clients:
            if client != sender_socket: 
                try:
                    client.send(message.encode('utf-8'))  
                    print(f"[DEBUG] Pesan '{message}' dibroadcast ke: {client.getpeername()} - chat_server.py:42")  
                except Exception as e:
                    print(f"[ERROR] Gagal broadcast ke client: {e} - chat_server.py:44")
                    if client in clients:  
                        clients.remove(client)
                        print("[DEBUG] Client bermasalah dihapus dari list - chat_server.py:47")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  
    print(f"[DEBUG] Server berjalan dan mendengarkan di port {PORT} - chat_server.py:54")
    
    while True:
        try:
            client_socket, addr = server_socket.accept()  
            print(f"[DEBUG] Client baru terhubung: {addr} - chat_server.py:59")
            with lock:
                clients.append(client_socket)  
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
        except Exception as e:
            print(f"[ERROR] Error menerima koneksi: {e} - chat_server.py:65")

if __name__ == "__main__":
    main()