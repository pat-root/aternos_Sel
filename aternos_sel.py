from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path
import time
import os
from webserver import keep_alive

driver = webdriver.Chrome(executable_path=binary_path)

driver.get("https://aternos.org/go")

search_1 = driver.find_element_by_id("user")
search_1.send_keys("NOOBdiscordbot")
search_1.send_keys(Keys.RETURN)

search_2 = driver.find_element_by_id("password")
search_2.send_keys("")
search_2.send_keys(Keys.RETURN)

time.sleep(8)

search_3 = driver.find_element_by_xpath("/html/body/div/main/section/div/div[2]/div[1]/div[1]")
search_3.click()

time.sleep(5)

import os
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    def get_status():
        element = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[3]/div[1]/div/span[2]/span')
        print(element.text)
        i_9 = element.text
        return i_9 

    def get_players():
        x_1 = get_status()
        if(x_1=="Online"):                
            e_5 = driver.find_element_by_xpath('//*[@id="players"]')
            print(e_5.text)
            e_6 = e_5.text
            return e_6
        elif(x_1=='Offline'):
            e_5 ="0/15"              
            return e_5
            

    if message.author == client.user:
        return
    
    if message.content.startswith('--'):

        if message.content == '--get status':            
            await message.channel.send("*Retriving Server Status....*") 
            x = get_status()
            await message.channel.send('.......')
            await message.channel.send(x)
            if(x=='Online'):
                i_1 = get_players()
                if(i_1=="0/15"):
                    try:
                        await message.channel.send('*The server is online*')
                        i_5 = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[3]/div[1]/div/span[1]')
                        i_6 = i_5.text
                        await message.channel.send("**BUT THE SERVER WILL TIME OUT IN: **")
                        await message.channel.send(i_6)                
                    except Exception:
                        pass
                if(i_1!="0/15"):
                    await message.channel.send('*The server is online*') 
                    pass
                pass 

        elif message.content == '--ls':
            x_1 = get_status()
            if(x_1=="Offline"):
                await message.channel.send("*Launching Server....*")
                search_4 = driver.find_element_by_id("start")
                search_4.click()
                time.sleep(5)
                await message.channel.send('*Please wait 5 mins before issuing any other command*')
                await message.channel.send('*Please wait till we retrive queue time*')
                e_14 = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main/div/a[1]')
                e_14.click()
                time.sleep(60)

            
            
            

            x_1 = get_status()
            if(x_1=="Waiting in queue"):
                await message.channel.send('.......')
                i_5 = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[3]/div[1]/div/span[1]')
                i_6 = i_5.text
                await message.channel.send("**ESTIMATED TIME OF QUEUE IS: **")
                await message.channel.send(i_6)          
                while(x_1=="Waiting in queue"):
                    try:
                        element = driver.find_element_by_id("confirm")
                        element.click()
                        time.sleep(60)
                        x_1 = get_status()                                               
                    except Exception:                        
                        pass
            
            x_1 = get_status()
            if(x_1=="Loading ..."):
                await message.channel.send("*Please wait the server is loading this may take a few mins*")
                time.sleep(120)
                x_1 = get_status()  

            x_1 = get_status()
            if(x_1=="Starting ..."):
                await message.channel.send("*Please wait the server is starting*")
                time.sleep(120)
                x_1 = get_status()

            x_1 = get_status()
            if(x_1=="Online"):
                i_1 = get_players()
                if(i_1!="0/15"):
                    await message.channel.send("**MOFO The server is already online**")
                    pass 
                if(i_1=="0/15"):
                    await message.channel.send("*The server is now online*")
                    i_5 = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[3]/div[1]/div/span[1]')
                    i_6 = i_5.text
                    await message.channel.send("**BUT THE SERVER WILL TIME OUT IN: **")
                    await message.channel.send(i_6)
                      
            x_1 = get_status()
            if(x_1=="Saving ..."):
                await message.channel.send("**The server was recently stopped try again after some time**")

                  
           
            time.sleep(2)
            
            
     
           
        elif message.content == '--code':
            x_1 = get_status()
            if(x_1=="Online"):
                e_2 = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[1]/div/a')
                e_2.click()
                e_3 = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main')
                print(e_3.text)
                c_1 = e_3.text
                c_2 = c_1.replace('Okay',' ')
                c_3 = c_2.replace('Help',' ')
                await message.channel.send('.......')
                await message.channel.send(c_3)
                e_4 = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main/div/a[1]')
                e_4.click()               
            
            elif(x_1=="Offline"):                
                e_2 = driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[1]/div/a')
                e_2.click()
                e_3 = driver.find_element_by_xpath('//*[@id="nope"]/main/div/div/div/main')
                print(e_3.text)
                await message.channel.send('.......')
                await message.channel.send(e_3.text)

            elif(x_1=="Saving ..."):
                await message.channel.send("*The server was recently stopped try again after some time*")

            elif(x_1=="Loading ..."):
                await message.channel.send("*Please wait the server is loading when it is online try again*")

            elif(x_1=="Waiting in queue"):
                await message.channel.send("*Please wait the server is in queue*")

        elif message.content == '--players':
            await message.channel.send("*Retriving player count....*")
            x_1 = get_status()
            if(x_1=="Online"):
                i_1 = get_players()
                await message.channel.send(i_1)
                pass
            
            if(x_1=="Offline"):
               await message.channel.send("**The server is offline**")
               pass 
            

            elif(x_1=="Saving ..."):
                await message.channel.send("*The server was recently stopped try again after some time*")

            elif(x_1=="Loading ..."):
                await message.channel.send("*Please wait the server is loading when it is online try again*")

            elif(x_1=="Waiting in queue"):
                await message.channel.send("*Please wait the server is in queue*") 
           
        elif message.content == '--stop':
            await message.channel.send("*Stopping Server....*")
            x_1 = get_status()
            if(x_1=="Online"):
                i_1 = get_players()
                if(i_1!="0/15"):
                    await message.channel.send('**There are players online**')
                    await message.channel.send('**Are you sure you want to stop**')
                    await message.channel.send('**Type --yes or --no in chat**')


                if(i_1=="0/15"):
                    e_6 = driver.find_element_by_id("stop")
                    e_6.click()
                    time.sleep(10)
                    await message.channel.send("*Server has been stopped!!*")
                    pass
            
            elif(x_1=="Saving ..."):
                await message.channel.send("*The server has stopped*")

            elif(x_1=="Loading ..."):
                await message.channel.send("*Please wait the server is loading when it is online try again*")

            elif(x_1=="Waiting in queue"):
                await message.channel.send("*Please wait the server is in queue*")
            
            elif(x_1=='Offline'):
                await message.channel.send("**The server is offline try again**")              
                pass
            pass

        elif message.content == '--restart':
            await message.channel.send("*Restarting Server....*")
            x_1 = get_status()
            if(x_1=="Online"):
                e_10 = driver.find_element_by_id("restart")
                e_10.click()
                time.sleep(10)
                await message.channel.send("*Server has been restarted!!*")
                pass

            elif(x_1=="Saving ..."):
                await message.channel.send("*The server was recently stopped try again after some time*")

            elif(x_1=="Loading ..."):
                await message.channel.send("*Please wait the server is loading when it is online try again*")

            elif(x_1=="Waiting in queue"):
                await message.channel.send("*Please wait the server is in queue*")
            
            elif(x_1=='Offline'):
                await message.channel.send("**the server is offline try again**")              
                pass
            pass
        
        elif message.content == '--player list':
            await message.channel.send("*Retriving Player List....*")
            x_1 = get_status()
            if(x_1=="Online"):
                i_1 = get_players()
                if(i_1=="0/15"):
                   await message.channel.send("**The Server is Online but There are No Players On**")
                   e_20 = driver.find_element_by_xpath('//*[@id="nope"]/nav/a[1]')
                   e_20.click()
                   pass
                pass
                if(i_1!="0/15"):
                    e_7 = driver.find_element_by_xpath('//*[@id="nope"]/nav/a[5]')
                    e_7.click()
                    time.sleep(5)
                    e_8 =  driver.find_element_by_xpath('//*[@id="nope"]/main/section/div[3]/div[1]')
                    print(e_8.text)
                    i_2 = (e_8.text)
                    i_3 = i_2.replace('Online',' ')
                    i_4 = i_3.replace('Kick',' ')
                    i_5 = i_4.replace('Ban',' ')
                    await message.channel.send('.......')
                    await message.channel.send(i_5)
                    e_9 = driver.find_element_by_xpath('//*[@id="nope"]/nav/a[1]')
                    e_9.click()
                    e_30 = driver.find_element_by_xpath('//*[@id="nope"]/nav/a[1]')
                    e_30.click()
                    pass
                pass

            elif(x_1=="Saving ..."):
                await message.channel.send("*The server was recently stopped try again after some time*")

            elif(x_1=="Loading ..."):
                await message.channel.send("*Please wait the server is loading when it is online try again*")

            elif(x_1=="Waiting in queue"):
                await message.channel.send("*Please wait the server is in queue*")

            if(x_1=='Offline'):
                await message.channel.send("**The server is offline**")
                e_40 = driver.find_element_by_xpath('//*[@id="nope"]/nav/a[1]')
                e_40.click()              
                pass
            pass 

        elif message.content == '--version':
            e_16 = driver.find_element_by_id("version")
            await message.channel.send('.......')
            await message.channel.send(e_16.text)
            pass
        

        elif message.content == '--reset':
            e_9 = driver.find_element_by_xpath('//*[@id="nope"]/nav/a[1]')
            e_9.click()
            await message.channel.send('.......')
            await message.channel.send("**Reseted**")
            pass



        elif message.content == '--yes':
            e_6 = driver.find_element_by_id("stop")
            e_6.click()
            time.sleep(10)
            await message.channel.send("*Server has been stopped!!*")
            pass

        elif message.content == '--no':
            await message.channel.send("*The server is still online*")
            pass
                       

        elif message.content == '--help': 
            embed = discord.Embed(title="Help")
            embed.add_field(name="--get status", value="Gets the server status", inline=False)
            embed.add_field(name="--ls", value="Launches the server", inline=False)
            embed.add_field(name="--stop", value="Stops the server", inline=False)
            embed.add_field(name="--restart", value="restarts the server", inline=False)            
            embed.add_field(name="--players", value="Gets the number of players", inline=False)
            embed.add_field(name="--player list", value="Gets the username of all the players playing", inline=False)            
            embed.add_field(name="--code", value="Gives server IP and dynamic IP", inline=False)
            embed.add_field(name="--version", value="Gives game version", inline=False)
            embed.add_field(name="--reset", value="Goes back to the server page", inline=False)          
            embed.add_field(name="--help", value="Displays this message", inline=False)                        
            await message.channel.send(embed=embed)
            pass
        

        else:
            await message.channel.send("Unknown command, use --help to see a list of all availiable commands")
    
keep_alive()
client.run("")