import docker
import os

#CREATE DIRECTORY
pwd = "C:/Users/karel/Desktop/DESKTOP/TradeGolem/TradeGolem"
user = 'user_0001'
golem = 'golem_0002'
userdir = os.path.join(pwd, user, golem)
try:
    os.mkdir(userdir)
except:
    print('directory already exists')
client = docker.from_env()



#CREATE SCRIPT
'''this is the dificult part m8. This is where you build a complete tradebot like this'''
scriptname = f"{golem}"
with open(f'{userdir}/{scriptname}.py', 'w') as tradebot:
    tradebot.write(f'print(\"tradebot {scriptname} running\")')
    


#CREATE DOCKERFILE
dockerfilename = scriptname+'_dockerfile'
with open(f'{userdir}/dockerfile', 'w') as golem:
    golem.write('FROM python:3.8-slim-buster\n')
    golem.write('WORKDIR /usr/src/app\n')
    golem.write('COPY . .\n')
    golem.write(f'CMD [ \"python\", \"./{scriptname}.py\" ]')
    
#RUN DOCKERFILE
client.images.build(path=f'{userdir}/', tag=f'{scriptname}')
client.containers.run(f'{scriptname}')
