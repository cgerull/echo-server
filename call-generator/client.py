import http.client
import os


def send(server = 'localhost'):
    conn = http.client.HTTPConnection(server, 8080)
    conn.request("GET", "/")

    resp = conn.getresponse()
    count = 1

    while (200 == resp.status):
        conn.request("GET", "/")
        resp = conn.getresponse()
        count += 1
        if (0 == count % 1000):
            print(count)
    
if __name__ == "__main__":
    server = os.environ.get('SERVER') or 'localhost'
    try:
        send(server)
    except KeyboardInterrupt:
        pass