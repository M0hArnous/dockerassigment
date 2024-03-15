# dockerassigment

docker build -t bd-a1-image  .
docker start bd-a1-container 
docker cp load.py bd-a1-container:/home/doc-bd-a1/
docker cp eda.py bd-a1-container:/home/doc-bd-a1/
docker cp dpre.py bd-a1-container:/home/doc-bd-a1/
docker cp vis.py bd-a1-container:/home/doc-bd-a1/
docker cp model.py bd-a1-container:/home/doc-bd-a1/
docker cp final.sh bd-a1-container:/home/doc-bd-a1/
docker exec -it bd-a1-container bash \
python3 load.py economic_freedom_index2019_data.xlsx

link github : https://github.com/M0hArnous/dockerassigment

 git clone https://github.com/M0hArnous/dockerassigment.git
 git add * \
 git commit -m "docker code" \
 git push \

