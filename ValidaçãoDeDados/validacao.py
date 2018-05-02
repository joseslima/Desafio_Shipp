import re
import datetime

def mountCardsList():
    return {
        "visa": [ ["4"] , 3 ,[16,13]],
        "master": [["51","52","53", "54","55"], 3, [16]],
        "amex": [["34","37"], 4, [15] ],
        "elo": [["636368","636369","504175","636297","5067","506699"],3,[16]    ]
    }
    ##lista criada dessa forma (bandeira: restrições) caso seja adicionada a RN de identificação da bandeira de cartão.


def validateCard(number,cvc):
    cards= mountCardsList()
    for card in cards.keys():
        cardCvc, cardLen, prefixes = cards[card][1], cards[card][2], cards[card][0]
        if (len(number) in  cardLen and cardCvc == len(cvc)):
            for prefixe in prefixes:
                if (prefixe in number[: len(prefixe)]):
                    return True
            #for
    #for
    return False


def validateClients():
    telephoneList= {}
    emailList = {}
    activeClients= {}
    disableClients= {}

    file = open("clientes.csv", "r", encoding="utf-8")

    header = file.readline()

    disableClients["header"] = header
    disableClients["title"] = "Disable Clients"

    activeClients["header"]  = header
    activeClients["title"] = "Active Clients"

    clients= file.readlines()

    for cliente in clients:

        cliente = cliente.split(",")

        id, cpf,email,telephone= cliente[0],cliente[5].replace("\n",""), cliente[4], re.sub("\D","",cliente[3])

        remove = False

        if (telephone in telephoneList.keys() or email in emailList.keys()):
            remove = True

            if (telephone in telephoneList.keys()):

                if(telephoneList[telephone] != None):

                    if (telephoneList[telephone] in activeClients.keys()):
                        activeClients.pop(telephoneList[telephone])

                    disableClients[telephoneList[telephone]] = cliente
                    telephoneList[telephone] = None
            else:
                telephoneList[telephone] = id

            if (email in emailList.keys()):

                if(emailList[email] != None ):

                    if (emailList[email] in activeClients.keys()):
                        activeClients.pop(emailList[email])

                    if (emailList[email] not in disableClients.keys()):
                        disableClients[emailList[email]] = cliente

                    emailList[email] = None
            else:
                emailList[email] = id

        else:
            telephoneList[telephone] = id
            emailList[email] = id

        if not validateCpf(cpf):
            remove= True

        if (remove):
            disableClients[id] = cliente
        else:
            activeClients[id] = cliente

    file.close()

    return activeClients, disableClients


def checkValidity(validity):
    today = datetime.date.today()
    validity=validity.split("/")
    validity = datetime.date(int(validity[2]), int(validity[1]), int(validity[0]))
    return (validity>=today)



def validateCards(disableClients):
    activeCards={}
    disableCards={}
    file= open("cartoes.csv", "r", encoding="utf-8")
    header= file.readline()

    activeCards["header"] = header
    activeCards["title"]= "Active Cards"

    disableCards["header"]= header
    disableCards["title"]= "Disable Cards"

    cards= file.readlines()
    for card in cards:
        card = card.split(",")
        number, cvc, validity = card[2],card[3],card[4]
        remove= False

        if (not (validateCard(number,cvc))):
            remove = True
        if (not checkValidity(validity)):
            remove = True

        ## CASO SEJA NECESSÁRIO TORNAR INVALIDO UM CARTÃO QUE PERTENCER A UM CLIENTE INVALIDO, DESCOMENTAR TRECHO ABAIXO:

        ##idClient = card[1].replace(" ", "")
        ##if (idClient in disableClients.keys()):
         ##remove = True

        if (remove):
            disableCards[card[0]]= card
        else:
            activeCards[card[0]]= card

    file.close()
    return activeCards,disableCards


def printList(list):
    print(list["title"])
    print(list["header"])

    for i in list.keys():
        if i != "title" and i != "header":
            print (list[i])

    print("\n")




def  validateCpf(cpf):
    repeated= [
        "11111111111",
        "22222222222",
        "33333333333",
        "44444444444",
        "55555555555",
        "66666666666",
        "77777777777",
        "88888888888",
        "99999999999"
    ]
    if ((cpf in repeated) or (len(cpf) != 11)):
        return False

    #calculo
    t = 9
    while( t < 11):
        d = 0
        c = 0
        while (c < t):
            d += ((int(cpf[c])) * ((t + 1) - c))
            c+=1
        d = (  (10 * d) % 11 ) % 10
        if (int(cpf[c]) != d):
          return False

        t+=1
    return True

def main():

    try:
        activateClients, disableClients = validateClients()
        activeCards,disabledCards= validateCards(disableClients)
        list= [activateClients,disableClients,activeCards,disabledCards]

        print(len(disabledCards.keys()))

        for i in list:
           printList(i)
    except IOError:
        print("File Not Found!")


if __name__ == "__main__":
    main()