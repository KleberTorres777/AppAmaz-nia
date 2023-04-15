import pandas as pa




class Animal():

    REINO = "ANIMALIA"

    def __init__(self, nome_popular, classe, familia, genero, especie, ordem):
        #nome científico é formado pelo genero e a espécie.
        self.nome_popular = nome_popular
        self.classe = classe
        self.familia = familia
        self.genero = genero
        self.especie = especie
        self.ordem = ordem
        self.nome_cientifico = self.genero +" "+self.especie


    def pesquisa(self, nome_popular):
        data= pa.read_csv("dados_animais.csv")
        animal = data [data.nome_popular==nome_popular]
        return animal


    def setNomePopular(self, nome_popular):
        self.nome_popular = nome_popular

    def getNomePopular(self):
        return self.nome_popular
    
    def setClassePopular(self, classe):
        self.classe = classe

    def getClasse(self):
        return self.classe
    
    def setFamilia(self, familia):
        self.familia = familia

    def getFamilia(self):
        return self.familia
    
    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero
    
    def setEspecie(self,especie):
        self.especie = especie

    def getEspecie(self):
        return self.especie
     
    def setOrdem(self, ordem):
        self.ordem = ordem

    def getOrdem(self):
        return self.ordem




onca_pintada = Animal("Onça pintada", "Mammalia",	"Panthera onca", "Panthera", "Carnivora", "Felidae")
tucano = Animal("Tucano", "aves", "ramphastidae", "ramphastos", "ramphastos", "piciformes")
pirarucu = Animal("Pirarucu", "actinopterygii", "arapaimidae", "arapaima", "arapaima_gigas", "osteoglossiform")
cobra_sucuri = Animal ("Cobra Sucuri",	"Reptilia",	"Eunectes_murinus",	"Eunectes",	"Squamata",	"Boidae")	
boto = Animal("Boto_cor_de_rosa",	"Mammalia",	"Inia geoffrensis",	"Inia",	"Cetacea",	"Iniidae")	
ariranha = Animal("Ariranha",	"Mammalia",	"Pteronura brasiliensis", "Pteronura", "Carnivora",	"Mustelidae")	
preguiça = Animal("Preguiça",	"Mammalia",	"Bradyps variegatus", "Bradypus", "Pilosa", "Bradypodidae")
tartaruga = Animal("Tartaruga-da-amazônia", "Reptilia", "Podocnemis unifilis",	"Podocnemis", "Testudines", "Podocnemididae")	
arara_azul = Animal("Arara-azul	Aves",	"Anodorhynchus", "hyacinthinus", "Anodorhynchus", "Psittaciformes",	"Psittacidae")	
jacare_acu = Animal("Jacaré-açu", "Reptilia",	"Melanosuchus niger", "Melanosuchus", "Crocodylia", "Alligatoridae")

    
dados_animais = [onca_pintada,tucano,pirarucu,cobra_sucuri,boto,ariranha,preguiça,tartaruga,arara_azul,jacare_acu]
print(dados_animais)


 #metodo estatico
        
animais_mome_popular = Animal.nome_popular_por_nome(dados_animais, "nome popular")
animais_classe = Animal.classe_por_classe(dados_animais, "classe")
animais_familia = Animal.familia_por_familia(dados_animais, "familia")
animais_genero = Animal.genero_por_genero(dados_animais, "genero")
animais_ordem = Animal.ordem_por_ordem(dados_animais, "genero")


print("nome popular:")
for animais in animais_mome_popular:
    print(animais.nome)  

print("classe")
for animais in animais_classe:
    print(animais.classe)


print("familia")
for animais in animais_familia:
    print(animais.familia)


print("genero")
for animais in animais_genero:
    print(animais.genero) 


print("ordem")
for animais in animais_ordem:
    print(animais.ordem)
    




### TAREFA FAZER OS METODOS GET E SETTERS PARA O RESTANTE DAS VARIÁVEIS

def descrever(self):

    print("##################################################")
    print("########### CARACTÉRISTICAS DO ANINAL ############")
    print("##################################################")
    print("NOME POPULAR: "+ self.nome_popular)
    print("NOME CIENTIFICO: "+ self.nome_cientifico)
    print("CLASSE: "+ self.classe)
    print("FAMILIA: "+ self.familia)
    print("GENERO: "+ self.genero)
    print("ESPÉCIE: "+ self.especie)
    print("ORDEM: " + self.ordem)
    print("##################################################")
    print("##################################################")

        