import redis
import threading

class redis_controller:
    def __init__(self, key, host):
        self.key = key
        self.redisClient = redis.StrictRedis(host)
        self.subscriber = ThreadedSubscriber()
        self.subscriber.host = host

    def publish(self):
        self.redisClient.publish("sensor_data", "1")

    def set_subscriber_callback(self, callback):
        self.subscriber_callback = callback

    def increment(self):
        self.redisClient.incr(self.key)
        self.publish()

    def get(self):
        return self.redisClient.get(self.key)

    def reset(self):
        self.redisClient.delete(self.key)
        self.publish()

    def subscribe(self):
        self.subscriber.start()
        self.subscriber.callback = self.subscriber_callback

class ThreadedSubscriber(threading.Thread):
    def run(self):
        self.redisClient = redis.StrictRedis(self.host)
        self.pubsub = self.redisClient.pubsub()
        self.pubsub.subscribe("sensor_data")
        while(True):
            for m in self.pubsub.listen():
                # print m #'Recieved: {0}'.format(m['data'])
                if(self.callback != None):
                    self.callback()
