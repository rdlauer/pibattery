import time
import json  # optional - for debugging json payloads
import notecard
from notecard import hub
from notecard import card
from notecard import note
from periphery import I2C
import keys

# init the Notecard for cellular (more info at dev.blues.io)
productUID = keys.PRODUCT_UID
port = I2C("/dev/i2c-1")
nCard = notecard.OpenI2C(port, 0, 0)

# associate Notecard with Notehub.io project
rsp = hub.set(nCard,
              product=productUID,
              mode="periodic",
              outbound=5)
print(rsp)


def main():
    """ take a temp reading every 5 minutes and send to cloud """

    try:
        rsp = card.temp(nCard)
        print(rsp)
        temp = rsp["value"]

        # add an event/note
        rsp = note.add(nCard,
                       file="temp.qo",
                       body={"temp": temp})

        print(rsp)
    except:
        print("An exception occurred")

    time.sleep(300)


while True:
    main()
