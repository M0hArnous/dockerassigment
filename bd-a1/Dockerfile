# Use Ubuntu as the base image
FROM ubuntu

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Move the dataset file to the container
COPY economic_freedom_index2019_data.xlsx /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Open bash shell upon container startup
CMD ["bash"]
