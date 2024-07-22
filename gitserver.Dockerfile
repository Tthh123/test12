# Base image
FROM ubuntu:20.04

# Install Git
RUN apt-get update && apt-get install -y git

# Configure Git with your username and email
RUN git config --global user.name "TTHH" \
    && git config --global user.email "asd@gmail.com"

# Set the working directory
WORKDIR /var/www/git

# Expose port (if needed for Git server, e.g., SSH for Git)
EXPOSE 3000

# Command to keep the container running (e.g., for a Git server)
CMD ["tail", "-f", "/dev/null"]
