import http.client
import os
import logging
import time

def init_logger(logfile):
    logger = logging.getLogger('call-generator')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if logfile:
        # create file handler which logs even debug messages
        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
    

def send(server = 'localhost', srv_path = '/', port=8080):
    """Send requests endlessly"""
    logger.info("Connecing to {}{}".format(server, srv_path))
    conn = http.client.HTTPConnection(server, port)
    conn.request("GET", srv_path)
    resp = conn.getresponse()
    count = 1
    t0 = time.time() # Set start time
    t1 = t0

    logger.info("Starting endless loop")
    while (200 == resp.status):
        try:
            conn.request("GET", srv_path)
            resp = conn.getresponse()
            count += 1
            if (0 == count % 1000):
                t = time.time()
                logger.info("Send {} requests with {} req/s".format(count, round(1000/(t - t1),3)))
                t1 = t
                if ( 0 == count % 10000):
                    logger.info("Send {} requests in {} seconds with an average of {} req/s".format(count, round(t - t0,3), round(count/(t - t0),3)))

        except Exception as e:
            logger.error("Caught exception {}".format(e))
            # logger.error("Get Address info error")
            break

if __name__ == "__main__":
    server = os.environ.get('SERVER') or 'localhost'
    srv_path = os.environ.get('SRV_PATH') or '/api/echo'
    port= os.environ.get('PORT') or 8080
    logfile = os.environ.get('LOGFILE') or ''
    logger = init_logger(logfile)

    try:
        send(server, srv_path)
    except KeyboardInterrupt:
        logger.info("Stopped by keyboard interrupt")
        pass