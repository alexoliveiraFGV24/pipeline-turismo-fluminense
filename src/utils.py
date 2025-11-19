import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


def DATA_FOLDER():
    return os.path.join(os.getcwd(), "data")


def dir_files(dir_path:str):
    onlyfiles = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return onlyfiles


def column_strip(df:pd.DataFrame, column:str):
    df[column] = df[column].str.strip()


def remove_lines(df:pd.DataFrame, lines:list[int]):
    df.drop(lines)


def concat_dfs(dfs:list[pd.DataFrame]):
    pd.concat(dfs, ignore_index=True)


def read_excel(file:str, sheet:int=1):
    df = pd.read_excel(file, sheet_name=sheet)
    return df


def read_csv(file:str, sep:str=","):
    df = pd.read_csv(file, sep=sep)
    return df

def plot_outcomes(outcomes: list[list], labels: list[str], x_label:str, y_label:str, title:str):
    assert len(outcomes) == len(labels)
    n = len(outcomes)
    for i in range(n):
        plt.plot(outcomes[i], label=labels[i])
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def carregar_dados(nome_arquivo):
    try:
        # Carregando o arquivo e tratando possíveis problemas de codificação e separador
        df = pd.read_csv(nome_arquivo, sep=',', encoding='utf-8')

        # Limpando nomes de colunas (removendo espaços em branco)
        df.columns = df.columns.str.strip()

        # Convertendo colunas para tipo numérico, tratando erros (coerção para NaN)
        colunas_numericas = ['Total', 'Aérea', 'Marítima', 'Ano']
        for col in colunas_numericas:
            # Tenta converter para float, forçando 'coerce' para valores não numéricos
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Removendo linhas com valores NaN essenciais (como 'Marítima')
        df.dropna(subset=['Marítima'], inplace=True)

        return df
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None
    
def carregar_dados(nome_arquivo):
    try:
        # Carregando o arquivo e tratando possíveis problemas de codificação e separador
        df = pd.read_csv(nome_arquivo, sep=',', encoding='utf-8')

        # Limpando nomes de colunas (removendo espaços em branco)
        df.columns = df.columns.str.strip()

        # Convertendo colunas para tipo numérico, tratando erros (coerção para NaN)
        colunas_numericas = ['Total', 'Aérea', 'Marítima', 'Ano']
        for col in colunas_numericas:
            # Tenta converter para float, forçando 'coerce' para valores não numéricos
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Removendo linhas com valores NaN essenciais (como 'Marítima')
        df.dropna(subset=['Marítima'], inplace=True)

        return df
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

def principais_mercados_maritimos(df, n=10, periodo_analisado='Total'):

    if periodo_analisado == 'Média Anual':
        # Agrupa por país e calcula a média anual da Marítima
        mercados = df.groupby('País')['Marítima'].mean().sort_values(ascending=False).head(n)
        titulo_eixo = 'Média Anual de Turistas Marítimos'
    else:
        # Agrupa por país e soma o total da Marítima
        mercados = df.groupby('País')['Marítima'].sum().sort_values(ascending=False).head(n)
        titulo_eixo = 'Volume Total de Turistas Marítimos (2006-2019)'

    plt.figure(figsize=(12, 7))
    sns.barplot(x=mercados.index, y=mercados.values, palette="viridis")
    plt.title(f'Principais {n} Países de Origem (Mercados Emissores) por Via Marítima')
    plt.xlabel('País de Origem')
    plt.ylabel(titulo_eixo)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    return mercados.reset_index()

def sazonalidade_maritima_anual(df):

    # Agrupa o total de turistas marítimos por Ano
    tendencia_anual = df.groupby('Ano')['Marítima'].sum()

    plt.figure(figsize=(10, 6))
    tendencia_anual.plot(kind='line', marker='o', color='royalblue')
    plt.title('Evolução Anual do Volume Total de Turistas Marítimos (2006-2019)')
    plt.xlabel('Ano')
    plt.ylabel('Total de Turistas Marítimos')
    plt.xticks(tendencia_anual.index, rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return tendencia_anual

def analise_volume_maritimo(df):
    """
    Calcula e exibe os volumes por continente e país, e identifica picos/vales.
    
    Returns:
        dict: Dicionário contendo os resultados da análise.
    """
    resultados = {}

    # 1. Maiores volumes por Continente
    volume_continente = df.groupby('Continente')['Marítima'].sum().sort_values(ascending=False)
    resultados['Continentes'] = volume_continente.head(5)

    # 2. Maiores volumes por País (Top 5)
    volume_pais = df.groupby('País')['Marítima'].sum().sort_values(ascending=False)
    resultados['Países'] = volume_pais.head(5)

    # 3. Análise de Picos e Vales (Anual) - Reutilizando a análise de sazonalidade
    tendencia_anual = df.groupby('Ano')['Marítima'].sum()
    resultados['Pico_Ano'] = tendencia_anual.idxmax()
    resultados['Vale_Ano'] = tendencia_anual.idxmin()
    resultados['Volume_Pico'] = tendencia_anual.max()
    resultados['Volume_Vale'] = tendencia_anual.min()
    return resultados
