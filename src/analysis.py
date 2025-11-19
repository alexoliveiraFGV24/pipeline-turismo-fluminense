import utils
import os
import pandas as pd

# Modificações nos dados de clima
climate_files = utils.dir_files(os.path.join(utils.DATA_FOLDER(), "dados_clima_rj"))
dfs = []
for file in climate_files:
    df = utils.read_csv(file, sep=";")
    utils.remove_lines(df, [i for i in range(8)])
    dfs.append(df)
df_concat = utils.concat_dfs(dfs)

# Modificações nos dados de turismo no Rio de Janeiro
df_turismo_rj_2006_2019 = utils.read_csv(os.path.join(utils.DATA_FOLDER(), "dados_turismo_rj", "tourists-rj-2006-2019.csv"))
utils.column_strip(df_turismo_rj_2006_2019, "País")

# Modificações nos dados de portuários
df_portuarios = utils.read_csv(os.path.join(utils.DATA_FOLDER(), "dados_portuarios", "Daily_Port_Activity_Data_and_Trade_Estimates.csv"))
df_portuarios["date"] = pd.to_datetime(df_portuarios["date"])
df_portuarios_rj = df_portuarios[df_portuarios["portname"]=="Rio de Janeiro" & df_portuarios["country"]=="Brazil"]

# Modificações nos dados de turismo
df_turismo_empregos = utils.read_excel(os.path.join(utils.DATA_FOLDER(), "dados_chegada_acomodacoes_empregos", "UN_Tourism_8_9_2_employed_persons_04_2025.xlsx"))
df_turismo_empregos_rj = df_turismo_empregos[df_turismo_empregos["GeoAreaCode"]=="Brazil"]

# Modificações nos dados de acomodações
df_turismo_acomodacoes = utils.read_excel(os.path.join(utils.DATA_FOLDER(), "dados_chegada_acomodacoes_empregos", "UN_Tourism_inbound_accommodation_10_2025.xlsx"))
df_turismo_acomodacoes_rj = df_turismo_acomodacoes[df_turismo_acomodacoes["reporter_area_label"]=="Brazil"]

if df_turismo_rj_2006_2019 is not None:
    utils.principais_mercados_maritimos(df_turismo_rj_2006_2019, n=10, periodo_analisado='Total')
    utils.sazonalidade_maritima_anual(df_turismo_rj_2006_2019)
    utils.analise_volume_maritimo(df_turismo_rj_2006_2019)