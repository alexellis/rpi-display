FROM alexellis2/python-gpio:armv6

# Install redis.
# This could also be linked in from another container.
RUN apt-get install redis-server
RUN pip install redis

# Add source code
ADD *.py ./
ADD *.sh ./
RUN chmod +x *.sh
CMD ["/bin/bash", "./docker_start.sh"]
