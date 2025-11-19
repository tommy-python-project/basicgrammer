
"""
threadingMixin 与 ForkingMixin
"""
import os
import socketserver
import threading


class ThreadingMixIn:
    """为服务器添加线程支持"""

    def process_request(self,request,client_address):
        """在新线程中处理请求"""
        thread = threading.Thread(
            target=self.process_request_thread,
            args=(request, client_address)
        )
        thread.daemon = self.daemon_threads
        thread.start()


class ForkingMixIn:
    """为服务器添加进程支持"""

    def process_request(self,request,client_address):
        """在新进程中处理请求"""
        pid = os.fork()
        if pid == 0:
            self.process_request(request,client_address)
            os._exit(0)
        else: # 父进程
            self.active_children.add(pid)
            self.collect_children()

# 创建支持多线程的TCP 服务器
class ThreadedTCPServer(ThreadingMixIn, socketserver.TCPServer):
    # 线程设置为守护线程
    damon_threads = True
    allow_reuse_address = True

class ForkingTCPServer(ForkingMixIn, socketserver.TCPServer):
    # 最大子进程数
    max_children = 10

# 自定义请求处理器
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        """处理客户端连接"""
        data = self.request.recv(1024).strip()
        print(f"Received: {data} from {self.client_address}")
        response = f"Echo: {data}"
        self.request.sendall(response.encode())

# 使用示例
def start_threaded_server():
    server = ThreadedTCPServer(("localhost", 9999), MyTCPHandler)
    print("Threaded server starting...")
    server.serve_forever()

if __name__ == "__main__":
    start_threaded_server()