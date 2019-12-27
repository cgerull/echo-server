import http.client

def send():
    conn = http.client.HTTPConnection("localhost", 8080)
    conn.request("GET", "/")

    resp = conn.getresponse()
    count = 1
    # print(resp.status, resp.reason, "\n", resp.read())

    while (200 == resp.status):
        conn.request("GET", "/")
        resp = conn.getresponse()
        count += 1
        if (0 == count % 1000):
            print(count)
    
if __name__ == "__main__":
    try:
        send()
    except KeyboardInterrupt:
        pass