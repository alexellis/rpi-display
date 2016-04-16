FROM alexellis2/python-gpio:armv6

# This Dockerfile is for the sender.py part of the project
# it watches a PIR sensor and communicates to Redis

# Install redis.
# This could also be linked in from another container.
RUN apt-get update && \
    apt-get install redis-server && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get -qy clean all

RUN pip install redis

# Add source code
ADD *.py ./
ADD *.sh ./
RUN chmod +x *.sh

EXPOSE 6379
CMD ["/bin/bash", "./docker_start.sh"]
