import redis

class RedisTaskQueue:
    def __init__(self):
        self.redis = redis.Redis(host="localhost", port=6379, decode_responses=True)
        self.p = self.redis.pubsub()
        self.threads = []

    def depute_task(self, task_id, task_type, task_info):
        self.redis.publish(task_type, str({ "task_id": task_id, "task_info": task_info }))

    def subscribe_to_tasks(self, task_type, on_task):
        self.p.subscribe(**{task_type: on_task})
        self.threads.append(self.p.run_in_thread(0.001))

    def __del__(self):
        for thread in self.threads:
            thread.stop()
