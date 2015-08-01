from chatterbotapi import ChatterBotFactory, ChatterBotType
import subprocess
factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.CLEVERBOT)
bot2session = bot2.create_session()

s = 'Hi'
while (True):

    print 'Female> ' + s

    subprocess.call('espeak -ven-us+f2 -k20 -s135 "{0}" 2>/dev/null' .format(s),shell=True)
    s = bot2session.think(s);
    print 'Male> ' + s
    subprocess.call('espeak -ven-us+m7 -k20 -s135 "{0}" 2>/dev/null' .format(s),shell=True)

    s = bot1session.think(s);
