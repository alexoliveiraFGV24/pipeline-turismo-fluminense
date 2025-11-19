# Pipeline de Turismo Marítimo Fluminense

# Links das bases
Dados de turismo no mundo: https://www.untourism.int/tourism-statistics/tourism-data-inbound-tourism
Dados de clima no Brasil (2006-2019): https://portal.inmet.gov.br/dadoshistoricos
Dados de turismo na cidade do Rio (2006-2019): https://www.kaggle.com/datasets/victorsoeiro/tourist-arrivals-in-rio-de-janeiro-20062019
Dados de atividade portuária no mundo: https://www.kaggle.com/datasets/arunvithyasegar/daily-port-activity-data-and-trade-estimates

# Seleção dos dados úteis da base de turismo pelo mundo
Baseado-se na consistência e na variedade dos dados, considerei pegar apenas os dados de chegada de turistas em portos fluminenses (para melhorar a inferência estatística), dados de acomodações em hotéis ou similares no Brasil (ter uma ideia de quanto representa o turismo na cidade do Rio de Janeiro no turismo brasileiro) e dados sobre empregos relacionados ao turismo marítimo (ter uma ideia de quanto representa o impacto do turimo carioca nos números empregatícios do Brasil)

# Colocando os dados de clima da cidade do Rio de Janeiro
```bash
for year in {2006..2019}; do
# Definição dos folders
folder1="<SEU_FOLDER>"
folder2="SEU_FOLDER$year"

# Pegando apenas do estado do Rio de Janeiro
ls "$folder" | grep -v "RJ" | while read f; do 
    rm -v "$folder2/$f"
done

# Pegando apenas da cidade Rio de Janeiro
ls "$folder2" | grep -Ev "MARAMBAIA|VILA MILITAR|JACAREPAGUA|FORTE DE COPACABANA" | while read f; do
    rm -v "$folder2/$f"
Done

# Salvando os arquivos
target="$folder1<SEU_FOLDER>"
mkdir -p "$target"
find "$folder2" -maxdepth 1 -type f -exec mv -v {} "$target" \;

done
```
