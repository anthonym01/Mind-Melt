import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Yorkoza {

	public static void main(String[] args) throws Exception {
		System.out.println("Yorkoza starts");
		new MyServer();

	}
}

class MyServer {

	public MyServer() {
		ThreadPoolExecutor threadPoolExecutor = (ThreadPoolExecutor)Executors.newFixedThreadPool(10);
		HttpServer server = HttpServer.create(new InetSocketAddress("localhost", 8001), 0);
		server.createContext("/test", MyHttpHandler());
		server.setExecutor(threadPoolExecutor);
		server.start();
		System.out.println(" Server started on port 8001");
	}

	public void MyHttpHandler(){

	}
}
