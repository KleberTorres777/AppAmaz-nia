import pymongo
import pandas as pd

# Cria uma conexão com o banco de dados MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados e a coleção
db = client["animais"]
collection = db["animais"]

# DataFrame com os dados
df = pd.DataFrame({
    "nome_popular": ["Onça-pintada", "Tucano", "Pirarucu", "Cobra Sucuri", "Boto_cor_de_rosa",
                     "Ariranha", "Preguiça", "Tartaruga-da-amazônia", "Arara-azul", "Jacaré-açu"],
    "classe": ["Mamalia", "aves", "actinopterygii", "Reptilia", "Mammalia",
               "Mammalia", "Mammalia", "Reptilia", "Aves", "Reptilia"],
    "familia": ["felidae", "ramphastidae", "arapaimidae", "Eunectes_murinus", "Inia geoffrensis",
                "Pteronura brasiliensis", "Bradypus variegatus", "Podocnemis unifilis", "Anodorhynchus",
                "Melanosuchus niger"],
    "genero": ["panthera", "ramphastos", "arapaima", "Eunectes", "Inia",
               "Pteronura", "Bradypus", "Podocnemis", "Anodorhynchus", "Melanosuchus"],
    "especie": ["panthera_onca", "ramphastos", "arapaima_gigas", "Squamata", "Cetacea",
                "Carnivora", "Pilosa", "Testudines", "hyacinthinus", "Crocodylia"],
    "ordem": ["carnivora", "piciformes", "osteoglossiform", "Boidae", "Iniidae",
              "Mustelidae", "Bradypodidae", "Podocnemididae", "Psittaciformes", "Alligatoridae"]
})

# Converte o DataFrame para um dicionário
data_dict = df.to_dict(orient="records")

# Insere os dados no banco de dados MongoDB
collection.insert_many(data_dict)
