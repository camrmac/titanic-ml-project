import pandas as pd 
import numpy as np

def analyze_titanic():  
    # Análise básica do dataset Titanic
    print("🚢 Analisador Titanic Containerizado")
    print("=" * 40)
    
    # ler dados (caminho correto dentro do container)
    data = pd.read_csv('data/train.csv')
    
    # transformar dados em dataframe
    df = pd.DataFrame(data)
    
    #exibir dados
    print(f"Dataset shape: {df.shape}")
    print(f"Survival rate: {df['Survived'].mean():.2%}")
    print("\n📊 Primeiras 5 linhas:")
    print(df.head())
    print("\n📈 Estatísticas por classe:")
    print(df.groupby('Pclass')['Survived'].mean())
    print("\nAnálise concluída com sucesso! ✅")

if __name__ == "__main__":
    analyze_titanic()