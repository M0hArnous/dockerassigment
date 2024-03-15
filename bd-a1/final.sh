#!/bin/bash
sudo ./final.sh

# Copy output files to local machine
echo "Copying files from container to local machine..." 
sudo docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv "/home/mohamed/bd-a1/service-result"
sudo docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt "/home/mohamed/bd-a1/service-result"
sudo docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt "/home/mohamed/bd-a1/service-result"
sudo docker cp bd-a1-container:/home/doc-bd-a1/vis.png "/home/mohamed/bd-a1/service-result"
sudo docker cp bd-a1-container:/home/doc-bd-a1/k.txt "/home/mohamed/bd-a1/service-result"

echo "Files copied successfully."


# Stop the container
echo "Stopping Docker container..."
docker stop bd-a1-container
echo "Container stopped."
